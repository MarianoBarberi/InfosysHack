import streamlit as st

def ask():
    st.title("Is my transaction fraudulent?")
    data = st.text_input("This is a simple example of a machine learning model that predicts whether a transaction is fraudulent.")

    if st.button("Predict"):
        if data:
            # Placeholder for the machine learning model
            output = "False"
            st.write(f"The model predicts: {output}")

            st.success("The transaction is not fraudulent.")
        else:
            st.error("Please provide some data.")