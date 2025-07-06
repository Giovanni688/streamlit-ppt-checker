import streamlit as st
from utils.ppt_parser import parse_file
from utils.fact_checker import process_and_check_facts
from utils.fact_checker import estimate_api_cost

def main():
    st.title("PowerPoint and PDF Factual Accuracy Checker")
    
    uploaded_file = st.file_uploader("Upload a PowerPoint or PDF file", type=["ppt", "pptx", "pdf"])
    
    if uploaded_file is not None:
        # Parse the file to extract text
        slides_text = parse_file(uploaded_file)
        
        if slides_text:
            st.subheader("Extracted Text:")
            for i, text in enumerate(slides_text):
                st.write(f"Slide/Page {i + 1}: {text}")
            
            estimated_cost = estimate_api_cost(slides_text)
            st.write(f"Estimated API cost: ${estimated_cost:.6f}")

            # Check factual accuracy of the extracted text
            if st.button("Check Factual Accuracy"):
                st.subheader("Processing and Filtering Objective Statements...")
                results = process_and_check_facts(slides_text)
                
                st.subheader("Factual Accuracy Results:")
                for statement, result in results.items():
                    st.write(f"Statement: {statement}")
                    st.write(f"Result: {result}")
        else:
            st.warning("No text found in the uploaded file.")

if __name__ == "__main__":
    main()