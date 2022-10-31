#!/usr/bin/env python
# coding: utf-8

# In[1]:



from google_trans_new import google_translator
import streamlit as st
translator = google_translator()
st.title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt='fr')
st.write(translate)


# In[ ]:




