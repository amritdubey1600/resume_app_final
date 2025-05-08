import streamlit as st
import base64

def set_styles(jpg_file):
    with open(jpg_file, "rb") as f:
        base64_img = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #fff;
    }}

    textarea {{
        background-color: rgb(19, 23, 32) !important; 
        border: 1px solid #444 !important;
        border-radius: 6px !important;
        color: #fff !important;
    }}

    .stTextArea label {{
        color: #fff !important;
    }}

    .stTextArea div[data-testid="InputInstructions"]{{
        color: #fff !important;
    }}

    .stFileUploader label, .stFileUploader small{{
        color: #fff !important;
    }}

    .stFileUploader button[data-testid="stBaseButton-secondary"]{{
        background-color: rgb(38, 39, 48) !important;
        color: #fff !important;
    }}

    .stFileUploader section[data-testid="stFileUploaderDropzone"]{{
        background-color: rgb(19, 23, 32) !important;
        color: #fff !important;
    }}

    .stButton > button:disabled {{
        background: rgb(19, 23, 32) !important;
        color: #666666 !important;
        cursor: not-allowed;
    }}

    .stButton > button {{
        background: rgb(19, 23, 32);
        color: white;
    }}

    .stMarkdown div[data-testid="stMarkdownContainer"] > p > code{{
        background: rgb(19, 23, 32);
    }}

     hr {{
        background-color: #fff !important;
    }}

    section[data-testid="stSidebar"] {{
        background-color: #121212 !important;  
        color: white; 
    }}
    
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5,
    section[data-testid="stSidebar"] h6,
    div[data-testid="stSidebarCollapseButton"],
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span, .stRadio p{{
        color: white !important;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
