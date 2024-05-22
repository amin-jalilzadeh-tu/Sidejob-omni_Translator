# Sidejob-omni_Translotor


The script utilizes GPT-4o's vision capabilities to translate and convert PDF files into LaTeX format, offering a distinct advantage over traditional methods that require text extraction. By processing each page as an image, it interprets both text and graphical data, translating content into English and recreating tables from visuals. This method bypasses common issues associated with text extraction, ensuring accurate replication of the original document's layout and content in LaTeX format. Textual content is directly converted into LaTeX, while placeholders are inserted for non-table images. The output is ready for immediate use in platforms like Overleaf, making the original PDF's content fully editable and accessible.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/amin-jalilzadeh-tu/Sidejob-omni_Translotor.git
    cd Sidejob-omni_Translotor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

4. Open your web browser and go to `http://localhost:8501`.

5. Upload a PDF file, enter your OpenAI API key (you can get it from [OpenAI Platform](https://platform.openai.com/usage)), specify the output path for the LaTeX file, and click "Process PDF".

6. The LaTeX file will be generated at the specified location. The output is ready to be used in Overleaf, and your file will be translated with tables generated and replicated from the PDF file.

## Project Structure

- `streamlit_app.py`: Contains the Streamlit UI code.
- `pdf_processor.py`: Contains the PDF processing and translation logic.
- `requirements.txt`: Lists the required Python packages.

## Contributing

Contributions are welcome! 

