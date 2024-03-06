
import streamlit as st
import joblib

# Load the trained models
@st.cache_resource(show_spinner='models loading')
def load_Gradient_pipeline():
    pipeline = joblib.load("D:\\Azubi LP4\\Prediction-Attrition-App\\models\\Gradient_pipeline.joblib")
    return pipeline

@st.cache_resource(show_spinner='models loading')
def load_Naives_pipeline():
    pipeline = joblib.load("D:\\Azubi LP4\\Prediction-Attrition-App\\models\\Naives_pipeline.joblib")
    return pipeline

def select_model():
    col1, col2 = st.columns(2)

    with col1:
        selected_model = st.selectbox("Select a model", options=["Gradient boosting", "Naives bayes"], key="selected_model")
        
    if selected_model == "Gradient boosting":
        pipeline = load_Gradient_pipeline()
    else:
        pipeline = load_Naives_pipeline()

    encoder = joblib.load("D:\\Azubi LP4\\Prediction-Attrition-App\\models\\encoder.joblib")

    return pipeline, encoder  

def prediction(form_data, pipeline, encoder):
    # Extract features from the form data and preprocess them
    # Make prediction using the selected model
    pass  # Placeholder for actual prediction code

def start_form():
    pipeline, encoder = select_model()
    with st.form('input-feature'):
        column1, column2, column3 = st.columns(3)

        with column1:
            st.write('### Personal info')
            st.text_input('Enter customer ID', key='customer_id')
            st.selectbox('Gender', options=['Male', 'Female'], key='gender')
            st.selectbox('Are you a Senior Citizen', options=['Yes', 'No'], key='senior_citizen')
            st.selectbox('Do you have a partner', options=['Yes', 'No'], key='partner')
            st.selectbox('Do you have Dependents', options=['Yes', 'No'], key='dependent')
            st.number_input('Customer term (tenure)', min_value=0, max_value=72, key='tenure')

        with column2:
            st.write('### Services offered')
            st.selectbox('Are you subscribed to a Phone Service', options=['Yes', 'No'], key='phone_service')
            st.selectbox('Do you have Multiple Lines', options=['No', 'No phone service', 'Yes'], key='multiple_lines')
            st.selectbox('Which internet Service do you use', options=['DSL', 'Fiber optic', 'No'], key='internet_service')
            st.selectbox('Do you have Online Security', options=['No', 'Yes', 'No internet service'], key='online_security')
            st.selectbox('Do you have Online Backup', options=['No', 'Yes', 'No internet service'], key='online_backup')
            st.selectbox('Do you have Device Protection', options=['No', 'Yes', 'No internet service'], key='device_protection')

        with column3:
            st.write('### Additional Services')
            st.selectbox('Are you subscribed to Tech Support', options=['No', 'Yes', 'No internet service'], key='tech_support')
            st.selectbox('Are you subscribed to Streaming TV', options=['No', 'Yes', 'No internet service'], key='streaming_tv')
            st.selectbox('Are you subscribed to Streaming Movies', options=['No', 'Yes', 'No internet service'], key='streaming_movies')

        form_data = st.form_submit_button('Submit')
        if form_data:
            prediction(form_data, pipeline, encoder)

if __name__ == "__main__":
    start_form()