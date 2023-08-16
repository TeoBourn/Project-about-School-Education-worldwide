from Project import dEur
from matplotlib import pyplot as plt
import streamlit as st
import seaborn as sb

st.write('---')
st.write(f'Εξετάστηκαν δεδομένα για συνολικά {len(dEur)} χώρες της Ευρώπης.')

sb.set_style('dark')

left_col1, right_col1 = st.columns(2)

t=1
k=0
while k<len(dEur):
    l1=[]
    l2=[]
    fig, ax = plt.subplots()
    ax.set_xlabel('year')
    ax.set_ylabel('Average Years of School Education')
    ax.set_title('Average years of education in Europe')
    ax.grid(True)
    for j in range(k, k + 5):
        length = len(dEur) - k
        if length<2:
            for i in range(0,length):
                k+=1
                l = ax.plot(dEur[j]['years'], dEur[j]['edu'], linewidth=1)
                l1.append(l[0])
                l2.append(dEur[j]['name'])
        else:
            k+=1
            l = ax.plot(dEur[j]['years'], dEur[j]['edu'], linewidth=1)
            l1.append(l[0])
            l2.append(dEur[j]['name'])



    plt.legend(l1, l2, loc=2);
    t+=1
    if t%2:
        with right_col1:
            st.pyplot(fig)
    else:
        with left_col1:
            st.pyplot(fig)


