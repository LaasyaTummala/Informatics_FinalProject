import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
st.set_page_config(page_title="No-Show Prediction", page_icon="🩺")
# Load data
df = pd.read_csv("PatientData.csv")

# Feature engineering
features = ['Age','Scholarship', 'Hypertension', 'Diabetes', 'Alcoholism', 'Handicap']
X = df[features] 
y = df['NoShow']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training 
model = RandomForestClassifier(random_state=95)
model.fit(X_train, y_train)  

# Streamlit app
st.markdown('''
         # Medical Appointment No-Show Prediction
         '''.strip(), unsafe_allow_html=True)
st.write("""
         This app predicts whether a patient will show up for their medical appointment...
         """)
# Layout
with st.container():
     col1, col2 = st.columns(2)
     with col1:
         st.header("Patient Data")
         with st.form(key='form'):
             # Input widgets 
           
            age = st.slider("Age", 0, 120, 25)
            scholarship = st.checkbox("Scholarship") 
            hypertension = st.checkbox("Hypertension")
            diabetes = st.checkbox("Diabetes")       
            alcoholism = st.checkbox("Alcoholism")
            handicap = st.select_slider("Handicap", options=[0,1])
            submit_button = st.form_submit_button(label='Predict')
             
     with col2:
         st.image("appointment.jpeg")
         
 # Divide sections                 
st.markdown("---")
left, right = st.columns(2)

with left:
   st.subheader("Prediction Results")
   
   if submit_button:
       
    user_input = pd.DataFrame(
        {
            'Age': [age], 
            'Scholarship': [scholarship], 
            'Hypertension': [hypertension],
            'Diabetes': [diabetes],
            'Alcoholism': [alcoholism],
            'Handicap': [handicap]
        }
    )

    with st.spinner("Making prediction..."):
        prediction = model.predict(user_input)

   
    if prediction[0] == 'No':
        st.success("The patient is likely to show up for the appointment", icon="👍")
    else:   
        st.error("The patient is unlikely to show up for the appointment", icon="⚠️")
            
   
  


