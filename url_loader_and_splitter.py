from typing import List
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.url_selenium import SeleniumURLLoader

import streamlit as st

main_placeholder = st.empty()


def load_data_from_urls(urls: List[str]):
    try:
        main_placeholder.text("Loading data from urls...")
        loader = SeleniumURLLoader(urls=urls)
        data = loader.load()
    except Exception as e:
        main_placeholder.text(
            "Error loading data from urls. Please try again.")
    return data


def get_info_from_url(url: str):
    try:
        response = requests.get(url)
    except:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    text = md(text)

    return text


def url_splitter(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, separators=[
                                              "\n\n", "\n", ".", "!", "?", ",", " ", "", "|"], chunk_overlap=10)
    chunks = splitter.create_documents(data)
    return chunks
