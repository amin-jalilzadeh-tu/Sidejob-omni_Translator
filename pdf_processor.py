import base64
import requests
from PyPDF2 import PdfReader
from PIL import Image
import io
import fitz  # PyMuPDF

def create_message(content: str, role: str) -> dict:
    return {"content": content, "role": role}

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_response(messages, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": messages,
        "max_tokens": 4000
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

def process_pdf(uploaded_file, api_key, output_tex_file):
    reader = PdfReader(uploaded_file)
    num_of_pages = len(reader.pages)

    user_prompt_template = """
    I have a PDF document in Dutch that includes text, tables, and images across multiple pages. 
    I need assistance with several tasks for each page of the document. 
    First, translate all the text from Dutch to English. 
    For any images that depict tables, interpret and extract the data, then represent this data as an editable text table in English. 
    Additionally, provide descriptions and relevant interpretations for other images within the document. If not possible to make them as a table, **Fig: [bold interpretation of the image]** instead of leaving a placeholder for these images/figures. 
    If a figure image was as a table and you replicated it as a table, you should NOT write a placeholder for that image.
    This will ensure that both the textual and visual content are fully accessible and usable in English.
    Also, I want you to just directly go respond, and you don't need, for example, to say that this is translated.
    We need to replicate each page.
    Finally, everything needs to be written in LaTeX format, i.e., if it is a section write as a section if it is a table write as a table.

    PS. Document class article, usepackage graphicx begin document, and end are all already defined and you shouldn't write them
    text: {text}
    """

    # Open the PDF with PyMuPDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Collect all LaTeX content to save in one file
    latex_content = ""

    # Add LaTeX preamble at the beginning
    latex_content += """
    \\documentclass{article}
    \\usepackage{geometry}
    \\usepackage{array}
    \\usepackage{graphicx}
    \\usepackage{color}

    \\begin{document}
    """

    # Iterate through each page of the PDF
    for page_num in range(num_of_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        
        # Extract images using PyMuPDF
        images = []
        pdf_page = doc.load_page(page_num)
        image_list = pdf_page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image_path = f"temp_image_{page_num}_{img_index}.png"
            image.save(image_path)
            images.append(image_path)
        
        system_message = create_message(
            "I have a PDF document in Dutch that includes text, tables, and images across multiple pages. I need assistance with several tasks for each page of the document. First, translate all the text from Dutch to English. For any images that depict tables, interpret and extract the data, then represent this data as an editable text table in English. Additionally, provide descriptions and relevant interpretations for other images within the document. If not possible to make them as a table and leave a placeholder for these images/figures, instead, **Fig: [bold interpretation of the image]**. If a figure image was as a table and you replicated it as a table, you should NOT write a placeholder for that image. This will ensure that both the textual and visual content are fully accessible and usable in English. Also, I want you to just directly respond, and you don't need for example to say that this is translated. We need to replicate each page. Finally, everything needs to be written in latex format, i mean if it is section write as section if it is table write as table. ps. document class article, usepackage graphicx begin document, end are all already defined and you shouldn't not write them ",
            "system"
        )

            
        user_message = create_message(content=user_prompt_template.format(text=text), role="user")

        messages = [system_message, user_message]

        # Include images in the request
        for image_path in images:
            image_data = encode_image(image_path)
            image_message = {
                "role": "user",
                "content": f"data:image/jpeg;base64,{image_data}"
            }
            messages.append(image_message)

        try:
            # Get response from GPT-4o
            response = get_response(messages, api_key)
            if 'choices' in response and response['choices']:
                translated_content = response['choices'][0]['message']['content']
                latex_content += f"% Page {page_num + 1} Content START\n"
                latex_content += translated_content
                latex_content += f"\n% Page {page_num + 1} Content END\n\n"
            else:
                raise Exception(f"Error processing page {page_num + 1}: {response}")
        except Exception as e:
            print(f"Error processing page {page_num + 1}: {e}")
            latex_content += f"% Page {page_num + 1} skipped due to error.\n"



    # Add LaTeX ending
    latex_content += "\\end{document}"

    # Save the LaTeX content to a file
    with open(output_tex_file, "w", encoding="utf-8") as f:
        f.write(latex_content)
