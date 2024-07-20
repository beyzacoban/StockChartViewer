import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
from io import BytesIO

symbol = st.sidebar.text_input('Stock Symbol', value='ASELS')

st.title(symbol + ' Stock Chart')

start_date = st.sidebar.date_input('Start Date', value=datetime(2020, 1, 1))
end_date = st.sidebar.date_input('End Date', value=datetime.now())

df = yf.download(symbol + '.IS', start=start_date, end=end_date)

st.subheader('Stock Symbol Input') 
st.line_chart(df['Close'])

st.subheader('Stock Data')
st.write(df)

st.subheader('Download Data')
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=True, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

excel_data = to_excel(df)
st.download_button(label='Download as Excel', data=excel_data, file_name=f'{symbol}_data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') 
