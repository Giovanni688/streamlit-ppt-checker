# Streamlit PowerPoint Checker

This project is a Streamlit web application that allows users to upload PowerPoint files and automatically checks the factual accuracy of the content within the slides. 

## Project Structure

```
streamlit-ppt-checker
├── src
│   ├── app.py              # Main entry point of the Streamlit application
│   ├── utils
│   │   ├── ppt_parser.py   # Functions for parsing PowerPoint files
│   │   └── fact_checker.py  # Functions for checking factual accuracy using the Conversation API
├── requirements.txt        # Lists the dependencies required for the project
└── README.md               # Documentation for the project
```

## Installation

To run this application, you need to have Python installed on your machine. You can then install the required packages using pip. 

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-ppt-checker
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload your PowerPoint file and wait for the application to process the slides.

4. The application will display the factual accuracy results for the content within the slides.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.