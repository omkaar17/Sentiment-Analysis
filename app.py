import streamlit as st
import sidebar
import textPage
import imdbReviewsPage
import imagePage


page = sidebar.show()

if page=="Text":
    textPage.renderPage()
elif page=="IMDb movie reviews":
    imdbReviewsPage.renderPage()
elif page=="Image":
    imagePage.renderPage()
