import streamlit as st

from ml_app import run_ml_app

def main():
    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Welcome to homepage - Edit')
    elif choice == 'Machine Learning':
        st.subheader('Welcome to Prediction Page')
        run_ml_app()

if __name__ == '__main__':
    main()

