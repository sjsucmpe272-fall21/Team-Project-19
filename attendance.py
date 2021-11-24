import pandas as pd
from datetime import datetime

def mark_attendance(name):
    df_temp = pd.read_excel("temp.xlsx")
    if name not in list(df_temp.Name):
        temp = [name, datetime.now()]
        a_series = pd.Series(temp, index = df_temp.columns)
        df_temp = df_temp.append(a_series, ignore_index=True)
        df_temp.to_excel("temp.xlsx", index=False)
        return True
    return False