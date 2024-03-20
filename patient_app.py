import joblib 
import streamlit as st



def set_bg_hack_url():    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-vector/hospital-clinic-building-with-ambulance-car-truck_107791-2645.jpg?w=1380&t=st=1710933594~exp=1710934194~hmac=8323997c87c733edab33dadf0caca560985903445cc1b1e2c8d936e5cbc944d8");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()


model=joblib.load(open('/content/patient_care.pkl','rb'))
scaler=joblib.load(open('/content/mscaler.pkl','rb'))




st.title('Patient Care Classification')
HA=st.number_input('HAEMATOCRIT:')
HAE=st.number_input('HAEMOGLOBINS:')
ER=st.number_input('ERYTHROCYTE:')
LE=st.number_input('LEUCOCYTE:')
TH=st.number_input('THROMBOCYTE:')
MCH=st.number_input('MCH:')
MCHC=st.number_input('MCHC:')
MCV=st.number_input('MCV:')
AGE=st.number_input('AGE:')
SEX=st.number_input('SEX:')

k=scaler.transform([[HA,HAE,ER,LE,TH,MCH,MCHC,MCV,AGE,SEX]])

if st.button('PREDICT'):
  pred=model.predict(k)

  patient_prediction={1:'Hospitalization', 0:'Home Care'}
  prediction_label=patient_prediction.get(pred[0],'unknown')

  st.markdown(
      f'<p style="font-size:20px; background-color:#333333; color:#ffffff; padding:10px;">'
      f'Predicted Care : {prediction_label}'
      '</p>',
      unsafe_allow_html=True
  )

