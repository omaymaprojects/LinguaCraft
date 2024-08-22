LinguaCraft
LinguaCraft is an advanced Natural Language Processing (NLP) web application built using Streamlit. This app provides several powerful NLP functionalities such as language translation, keyword extraction, part-of-speech (POS) tagging, and text generation, all in a user-friendly interface.

Features
Language Translation: Translate text from one language to another using Google Translate.
Keyword Extraction: Extract key phrases from text using the TextRank algorithm.
Part-of-Speech Tagging: Analyze the grammatical structure of text and identify parts of speech (e.g., nouns, verbs, adjectives).
Text Generation: Generate coherent text based on a given prompt using the GPT-2 model.
Installation
To run this project locally, follow these steps:

Clone the repository:

```
git clone https://github.com/omaymaprojects/LinguaCraft.git
cd LinguaCraft
```
Create and activate a virtual environment:

On Windows:

```
python -m venv venv
venv\Scripts\activate 
```
On macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```
Install the required dependencies:

```
pip install -r requirements.txt
```
Download the spaCy language model:

```
python -m spacy download en_core_web_sm
```
Run the app:

```
streamlit run app.py
```
Usage
Translate Text: Enter your text and select the target language for translation.
Extract Keywords: Analyze your text to extract the most relevant keywords.
POS Tagging: Identify the grammatical parts of speech in your text.
Generate Text: Input a prompt and generate coherent text based on GPT-2.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Streamlit team for providing an easy-to-use framework for building web apps.
Hugging Face for the amazing NLP models.
The spaCy team for their powerful NLP library.
Author
Omayma Chattat - AI Enthusiast and Data Scientist.