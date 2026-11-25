"""Điểm vào của ứng dụng. Chạy:  streamlit run app.py"""

import streamlit as st

from stockly.main import main
from stockly.ui.logo import mo_logo

# st.set_page_config phải là lệnh Streamlit đầu tiên của mỗi lần chạy.
st.set_page_config(page_title='Stockly - Quản lý kho hàng', page_icon=mo_logo() or '', layout='wide')

main()
