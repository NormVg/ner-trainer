import streamlit as st
st.title('The Fury')
st.text('ONLINE')
print("starting")
import spacy
print("imported")
nlp_ner = spacy.load("model-best")
print("modal loded")
def NER(text):
    ent_text = []
    ent_lable = []
    doc = nlp_ner(text)
    for ent in doc.ents:
        ent_text.append(ent.text)
        ent_lable.append(ent.label_)
    if "SONG-NAME" == ent_lable[0]:
        ent_text = str(ent_text[0]).replace("songs","")
        ent_text = ent_text.replace("song","")
        ent_text = ent_text.replace("of","")
        ent_text = ent_text.replace("musics","")
        ent_text = ent_text.replace("music","")
        return ent_text
    elif "MOVIE-NAME" == ent_lable[0]:
        ent_text = str(ent_text[0]).replace("movies","")
        ent_text = ent_text.replace("movie","")
        ent_text = ent_text.replace("of","")
        ent_text = ent_text.replace("film","")
        
        return ent_text
    else:
        return "000"
    
data = NER("play thala anjum song")
st.text(data)
