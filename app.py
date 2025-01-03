
import streamlit as st
import pandas as pd

st.write('# dokdox view chart')


view = [2,3,4]
view
st.bar_chart(view)
view = pd.Series(view)
view