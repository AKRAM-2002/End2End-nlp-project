#We import the core packages
import streamlit as st


#EDA packages
import pandas as pd
import numpy as np

#Utils
import joblib

def main():
    st.title("Emotion Classifier App")
    menu = ["Home","Monitor","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home-Emotion In Text")

        with st.form(key="emotion_clf_form"):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label="Submit")

    elif choice == "Monitor":
        st.subheader("Monitor App")


    else: 
        st.subheader("About")


if __name__ == '__main__':
    main()