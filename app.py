## App: LinguaCraft - Advanced NLP App with Streamlit
# Author: Omayma Chattat
# Source: [Github](https://github.com/omaymaprojects)
# Credits: Streamlit Team, HuggingFace, spaCy, TextRank


import streamlit as st
import spacy
from googletrans import Translator
from transformers import pipeline
from summa import keywords

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function for Language Translation
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function for Keyword Extraction
def extract_keywords(text):
    key_phrases = keywords.keywords(text, words=5, split=True)
    return key_phrases

# Function for POS Tagging
def pos_tagger(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

# Function for Text Generation
def generate_text(prompt):
    generator = pipeline("text-generation", model="gpt2")
    generated_text = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return generated_text

# Main function for the Streamlit app
def main():
    """ Advanced NLP App with Streamlit """

    # App Title
    st.title("LinguaCraft with Streamlit")
    st.subheader("Explore Advanced Natural Language Processing Capabilities")

    # Language Translation
    if st.checkbox("Translate Text"):
        st.subheader("Translate Your Text")

        text = st.text_area("Enter Text", "Type here...")
        target_language = st.text_input("Target Language (e.g., 'fr' for French, 'es' for Spanish)", "fr")
        
        if st.button("Translate"):
            translation = translate_text(text, target_language)
            st.success(f"Translation: {translation}")

    # Keyword Extraction
    if st.checkbox("Extract Keywords"):
        st.subheader("Extract Keywords from Your Text")

        text = st.text_area("Enter Text", "Type here...")
        
        if st.button("Extract"):
            key_phrases = extract_keywords(text)
            st.write("Keywords:", ', '.join(key_phrases))

    # POS Tagging
    if st.checkbox("Show POS Tagging"):
        st.subheader("Part-of-Speech Tagging")

        text = st.text_area("Enter Text", "Type here...")
        
        if st.button("Analyze"):
            pos_tags = pos_tagger(text)
            st.json(pos_tags)

    # Text Generation
    if st.checkbox("Generate Text"):
        st.subheader("Generate Text from a Prompt")

        prompt = st.text_area("Enter Prompt", "Type here...")
        
        if st.button("Generate"):
            generated_text = generate_text(prompt)
            st.write("Generated Text:", generated_text)

    # About the App
    st.sidebar.subheader("About App")
    st.sidebar.text("LinguaCraft App with Streamlit")
    st.sidebar.info("This app demonstrates advanced NLP functionalities.")

    st.sidebar.subheader("By")
    st.sidebar.text("Omayma Chattat")
    st.sidebar.text("AI Enthusiast and Developer")

if __name__ == '__main__':
    main()