import streamlit as st
import requests




st.title("Customer Churn Prediction Demo")


Age=st.number_input("Age",18,70,key="Age")             
Gender=st.selectbox("Gender",["Male","female"])          
Tenure =st.number_input("Tenure",1,60,key="tenure")       
Usage_Frequency=st.number_input("Usage_Frequency",1,30,key="Usage_frequency")    
Support_Calls=st.number_input("Support_Calls",0,10,key="Support_Calls")  
Payment_Delay=st.number_input("Payment_Delay",0,30,key="Payment_Delay")   
Subscription_Type =st.selectbox("Subscription type",["basic","premium","standard"])  
Contract_Length=st.selectbox("contract length",["Monthly","quarterly","Annual"])  
Total_Spend=st.number_input("Total spend",100,1000,key="Total_Spend")  
Last_Interaction=st.number_input("last interaction",1,30,key="Last_Interaction")  

with st.spinner(text="predicting churn.......",width="content"):
    if st.button("predict"):
    
        payload={       
    "Age": Age,              
    "Gender": Gender,         
    "Tenure": Tenure,
    "Usage_Frequency" : Usage_Frequency,  
    "Support_Calls" : Support_Calls,
    "Payment_Delay"  : Payment_Delay,
    "Subscription_Type" : Subscription_Type,
    "Contract_Length" : Contract_Length,
    "Total_Spend"  : Total_Spend,
    "Last_Interaction" : Last_Interaction
 
    }
        res=requests.post("http://localhost:8000/predict",json=payload)
        st.write("Status code:", res.status_code)
        try:
            st.json(res.json())
        except Exception as e:
            st.write("Response is not JSON:")
            st.text(res.text)
       
