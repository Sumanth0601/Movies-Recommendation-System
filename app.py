import streamlit as st

st.title("Movie Recommender System")
option = st.selectbox('Select the movie which you like?',
                      ('Email','Home phone','Mobile phone'))