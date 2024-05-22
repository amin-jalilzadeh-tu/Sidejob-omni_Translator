import streamlit as st
from pdf_processor import process_pdf  # Import the function from the second file

# Streamlit UI
st.title('PDF Translator and Processor')
st.write('Upload a PDF file to translate and process it into a LaTeX document.')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
api_key = st.text_input("Enter your API Key", type="password")
output_tex_file = st.text_input("Enter the output path for the LaTeX file", value="translated_document.tex")

if st.button('Process PDF'):
    if uploaded_file is not None and api_key:
        st.write("Processing the PDF...")
        
        try:
            process_pdf(uploaded_file, api_key, output_tex_file)
            st.success(f"LaTeX document saved as {output_tex_file}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload a PDF file and enter your API Key.")
