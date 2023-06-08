
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

st.title('predict salary of the new employee')

with open('decsiontree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the pre-trained StandardScaler object
with open('standard_scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


def predict_solubility(inputs, model, scaler):
    # Convert input dictionary to pandas dataframe
    # print(inputs)
    df = pd.DataFrame([inputs])
    for col in df.columns:
        df[col] = float(df[col])
    # print(df)

    value = scaler.transform(df.head(1).values)
    # Make predictions using the pre-trained random forest model

    prediction = model.predict(value)
    # print(prediction)
    return prediction

    # if prediction == 1:
    #     return "You have to consult with the Doctor"
    # elif prediction == 0:
    #     return "You seems fine"
    # else:
    #     return "Unpredictable"



# Define input fields
inputs = {}
inputs['age'] = st.text_input('AGE')
inputs['healthy_eating'] = st.text_input('healthy_eating')
inputs['active_lifestyle'] = st.text_input('active_lifestyle')
inputs['Gender'] = st.text_input('Gender')



# Add a button to trigger predictions
if st.button('predict salary of the new employee'):
    prediction = predict_solubility(inputs, model, scaler)
    st.success(f'Prediction --> {prediction}')
