# Colored partition

import streamlit as st

# q-series generation 

def qf1(n,m=1):
    ''' outputs a dictionary in which we concider its keys as 'q' raised to power and 
    values is the respective coefficient = 1 as (LaTeX): (q^m;q^m)_\infty = \Pi_{i=1}^\infty (1-q^{m i})'''
    
    n=n//m
    return {m*i:1 for i in range(n+1)}




# q-series multiplication

def qmul(a,b,t=100):
    ''' we define qmul as multiplication of two dictionaries in a way to replicate multiplication in q series'''
    p={}
    
    for i,j in a.items():
        for k,l in b.items():
            if (i+k)<=t: # stop for >= q^t
                try:
                    p[i+k]+=(j*l) #main step of adding powers and multiplying coefficients
                except:
                    p[i+k]=(j*l)
    return p





# superscript output function

def supspt(n):
    '''outputs superscripts of the int input with help of UniCode'''
    
    ss={'0':'\u2070','1':'\u00b9','2':'\u00b2','3':'\u00b3','4':'\u2074',
        '5':'\u2075','6':'\u2076','7':'\u2077','8':'\u2078','9':'\u2079'}
    
    st=str(int(n))
    sd=''
    
    for i in st:
        sd+=ss[i]
        
    return f'{sd}'




# print q-series from Dictionary

def qprint(a):
    ''' outputs q series representations from raw dictionary'''
    d=''
    if len(a)>0:
        d=str(a[0])
        coef=''
        
        for i in range(1,len(a)):
            
            coef=' + '+str(a[i])+' q'+supspt(i)
            d+=coef
        
    return d

@st.cache_data
def c_s(s,n):
    '''outputs 1/f1^s = 1/(q;q)_\infty^s restricted till q^n term'''
    
    p={0:1}
    for i in range(1,n+1): # cycle through (q^i;q^i)
        
        for j in range(0,s): # cycle through (q^i;q^i)^j s times 
            p=qmul(p,qf1(n,i),n)

    return p

# dictionary to list 

def to_list(q):
    ''' outputs values of dictionary in ordered list'''
    ll=[q[i] for i in range(len(q))]
    return ll


# =============================================================================
# =============================================================================


st.set_page_config(page_title="Color partitions of n",page_icon=":abacus:")
st.sidebar.header(('Color partitions of n'))

st.markdown('## Color partitions of n of color s = $c_s(n)$ ')
st.sidebar.write('$c_s(n)$ is the colored partition function that outputs the number of s colored partitions a non-negative integer can be partitioned into.')
st.markdown('which can be represented as :')
st.latex(r'C_s(q) = \displaystyle \sum_{n=0}^\infty c_s(n) q^n = \frac {1} {(q;q)_\infty^s} = \frac {1} {f_1^s}')
st.markdown('where $f_s=(q^s;q^s)_\infty = \displaystyle \prod_{n=1}^\infty (1-q^{ns})$')


s=st.number_input('Input value for $s \quad$ i.e. for $c_s$', min_value=1, max_value=3000, step=1, value=2 , disabled=False)
n=st.number_input('Input value for $n \quad$ i.e. for $c_s(n)$', min_value=1, max_value=3000, step=1, value=100 , disabled=False)



if st.button('q series values'):
   
    c_p=c_s(s,n)
    l_p=to_list(c_p)
   
    c=st.text_area(label='',value=l_p)
    
if st.button('q series representation'):
    c_p=c_s(s,n)
    
    q_s=qprint(c_p)
    d=st.text_area(label='',value=q_s)
