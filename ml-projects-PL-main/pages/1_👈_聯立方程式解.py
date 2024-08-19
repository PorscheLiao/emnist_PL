# streamlit run web_solve.py

# 若出現錯誤：TypeError: Descriptors cannot not be created directly. 可執行下列指令：
# Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# streamlit user guide
# https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets

import streamlit as st
from sympy.solvers import solve
from sympy import symbols
from sympy.core import sympify

x, y, z = symbols('x y z')

exp1 = st.text_area('請輸入聯立方程式：', 'x+y=5\nx-y=1')


    
if st.button('求解'):
    list1 = exp1.split('\n')
    list2=[]

    for i in list1:
   
        i=i.replace("=","-(")+")"
        list2.append(i)
   
            
    ans = solve(list2)
    print('結果:', ans[x],ans[y])
    st.write('結果:\nx=', ans[x],'y=',ans[y])
