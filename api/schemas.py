from pydantic import BaseModel

class CustomerInput(BaseModel):       
    Age: int              
    Gender: str           
    Tenure : int      
    Usage_Frequency : int   
    Support_Calls : int
    Payment_Delay  : int
    Subscription_Type : str
    Contract_Length : str
    Total_Spend  : int
    Last_Interaction : int
