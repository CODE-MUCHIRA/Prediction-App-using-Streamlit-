import streamlit as st
import pandas as pd

def show_history():
    st.title("Historical Data")

    # Read the historical data from the CSV file
    try:
        history_df = pd.read_csv("D:\Azubi LP4\Prediction-Attrition-App\data\history.csv")
    except FileNotFoundError:
        st.error("Could not find the historical data file.")
        return
    except pd.errors.ParserError:
        st.error("Error parsing the historical data. Please ensure the file format is correct.")
        return

    # Display the historical data
    st.write(history_df)

if __name__ == "__main__":
    show_history()