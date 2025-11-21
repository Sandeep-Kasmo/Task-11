import pandas as pd #type:ignore

def transform_data(dataframe):
    
    dataframe['start_date']=pd.to_datetime(dataframe['start_date'],format='mixed',errors='coerce')
    dataframe['end_date']=pd.to_datetime(dataframe['end_date'],format='mixed',errors='coerce')
    dataframe['project_manager']=dataframe['project_manager'].astype(str).str.strip().str.title()
    dataframe['status']=dataframe['status'].astype(str).str.strip().str.title()
    dataframe['project_id']=dataframe['project_id'].astype(str).str.upper()
    dataframe['technologies']=dataframe['technologies'].apply(lambda x:','.join(x) if isinstance(x,list) else x)
    dataframe['location']=dataframe['location'].astype(str).str.strip()
    dataframe['domain']=dataframe['domain'].astype(str).str.strip()
    dataframe['client']=dataframe['client'].astype(str).str.strip()
    dataframe['project_name']=dataframe['project_name'].astype(str).str.strip()
    dataframe=dataframe.drop_duplicates().reset_index(drop=True)
    return dataframe
