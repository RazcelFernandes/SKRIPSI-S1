import streamlit as st

def set_background():
    st.markdown("""
    <style>

   [data-testid="stAppViewContainer"]{
    background: #111827;
}

    [data-testid="stHeader"]{
        background: rgba(0,0,0,0);
    }

    [data-testid="stToolbar"]{
        right: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)