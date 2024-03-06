import streamlit as st
import joblib
import pandas as pd
import os
import datetime

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

# Initialize session state
# List of keys to initialize
keys_to_initialize = ['customerId','gender','Contract','partner','dependent','tenure','phoneService','internetService','onlineSecurity','onlineBackup','deviceProtection','techSupport','streamingTv','streamingMovies']

# Initialize session state
for key in keys_to_initialize:
    if key not in st.session_state:
        st.session_state[key] = None

# Initialize 'prediction' key
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None

# Initialize 'probability' key
if 'probability' not in st.session_state:
    st.session_state['probability'] = None

# Make prediction using the selected model
def prediction(form_data, pipeline, encoder):
    customerId = st.session_state['customerId']
    gender = st.session_state['gender']
    Contract = st.session_state['Contract']
    partner= st.session_state['partner']
    dependent = st.session_state['dependent']
    tenure = st.session_state['tenure']
    phoneService = st.session_state['phoneService']
    internetService = st.session_state['internetService']
    onlineSecurity = st.session_state['onlineSecurity']
    onlineBackup = st.session_state['onlineBackup']
    deviceProtection = st.session_state['deviceProtection']
    techSupport= st.session_state['techSupport']
    streamingTv = st.session_state['streamingTv']
    streamingMovies = st.session_state['streamingMovies']
    PaperlessBilling = st.session_state['PaperlessBilling']
    PaymentMethod = st.session_state['PaymentMethod']
    MonthlyCharges = st.session_state['MonthlyCharges']
    TotalCharges = st.session_state['TotalCharges']
    SeniorCitizen = st.session_state['SeniorCitizen']
    Churn = st.session_state['Churn']






    
    columns = ['customerId','gender','Contract','partner','dependent','tenure','phoneService','internetService','onlineSecurity','onlineBackup','deviceProtection','techSupport','streamingTv','streamingMovies','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges','SeniorCitizen','Churn']

    data = [[customerId,gender,Contract,partner,dependent,tenure,phoneService,internetService,onlineSecurity,onlineBackup,deviceProtection,techSupport,streamingTv,streamingMovies,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,SeniorCitizen,Churn]]

    ## creating a DataFrame
    df = pd.DataFrame(data, columns=columns)

    df['prediction time'] = datetime.date.today()
    df['model used'] = st.session_state['selected_model']

    df.to_csv("D:\\Azubi LP4\\Prediction-Attrition-App\\data\\history.csv", mode='a', header=not os.path.exists("D:\\Azubi LP4\\Prediction-Attrition-App\\data\\history.csv"), index=False)
   
    pred = pipeline.predict(df)
    pred = int(pred[0])
    prediction = encoder.inverse_transform([pred])

    probability = pipeline.predict_proba(df)

    ##updating state
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability

    return prediction, probability

def start_form():
    pipeline, encoder = select_model()
    with st.form('input-feature'):
        column1, column2, column3 = st.columns(3)

        with column1:
            st.write('### Personal info')
            st.text_input('Enter customer ID', key='customerId')
            st.selectbox('Gender', options=['Male', 'Female'], key='gender')
            st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='contract')
            st.selectbox('Do you have a partner', options=['Yes', 'No'], key='partner')
            st.selectbox('Are you a SeniorCitizen', options=['Yes', 'No'], key='SeniorCitizen')
            st.selectbox('Do you have Dependents', options=['Yes', 'No'], key='dependent')
            st.number_input('Customer term (tenure)', min_value=0, max_value=72, key='tenure')

        with column2:
            st.write('### Services offered')
            st.selectbox('Are you subscribed to a Phone Service', options=['Yes', 'No'], key='phoneService')
            st.selectbox('Do you have Multiple Lines', options=['No', 'No phone service', 'Yes'], key='multipleLines')
            st.selectbox('Which internet Service do you use', options=['DSL', 'Fiber optic', 'No'], key='internetService')
            st.selectbox('Do you have Online Security', options=['No', 'Yes', 'No internet service'], key='onlineSecurity')
            st.selectbox('Do you have Online Backup', options=['No', 'Yes', 'No internet service'], key='onlineBackup')
            st.selectbox('Do you have Device Protection', options=['No', 'Yes', 'No internet service'], key='deviceProtection')

        with column3:
            st.write('### Additional Services')
            st.selectbox('Are you subscribed to Tech Support', options=['No', 'Yes', 'No internet service'], key='techSupport')
            st.selectbox('Are you subscribed to Streaming TV', options=['No', 'Yes', 'No internet service'], key='streamingTv')
            st.selectbox('Are you subscribed to Streaming Movies', options=['No', 'Yes', 'No internet service'], key='streamingMovies')
            st.selectbox('Are you happy with our paperless billing', options=['No', 'Yes', 'No PaperlessBilling'], key='PaperlessBilling')
            st.selectbox('Are you satisfied with our Payment method', options=['No', 'Yes', 'No PaymentMethod'], key='PaymentMethod')
            st.number_input('Monthly Charges', min_value=0.0, key='MonthlyCharges')
            st.number_input('Total Charges', min_value=0.0, key='TotalCharges')
            st.number_input('Churn', min_value=0.0, key='Churn')

        form_data = st.form_submit_button('Submit')
        if form_data:
            prediction(form_data, pipeline, encoder)

if __name__ == "__main__":
    start_form()


prediction = st.session_state['prediction']
probability = st.session_state['probability']


if not prediction:
    st.markdown('*###Prediction*')
elif prediction == 'Yes':
    probability_of_yes = probability[0][1]*100
    st.markdown(f"probability of churnig is{round(probability_of_yes,2)}%")
else:
    probability_of_no = probability[0][0]*100
    st.markdown(f"probability of not churnig is{round(probability_of_yes,2)}%")   
st.write(st.session_state)