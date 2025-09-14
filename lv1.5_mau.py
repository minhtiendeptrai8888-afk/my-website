import streamlit as st

st.title("Demo Code và Toán")

st.code("""
import math

def tinh_can_bac_hai(x):
    return math.sqrt(x)

print(tinh_can_bac_hai(16))
""", language="python")

st.latex(r"E = mc^2")

st.latex(r"\frac{a}{b} = x")

st.latex(r"\sqrt{16} = 4")