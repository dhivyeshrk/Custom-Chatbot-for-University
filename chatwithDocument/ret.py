import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
import os
from langchain.embeddings import SentenceTransformerEmbeddings
import platform
from langchain.document_loaders import DirectoryLoader
import numpy as np

os.environ['OPENAI_API_KEY'] = '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'

def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents

def split_docs(documents, chunk_size=100, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

directory = r'C:\Users\DELL\DataspellProjects\Chatbot_Test_2\ChatWithDocument\Similar_check_TextFiles'

