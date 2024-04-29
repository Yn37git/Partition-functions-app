import streamlit as st


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
            if (i+k)<=t:
                try:
                    p[i+k]+=(j*l) #main step of adding powers and multiplying coefficients
                except:
                    p[i+k]=(j*l)
    return p


@st.cache_data
def C_l_regular(n,l,s=100):
    '''outputs (fl/f1)^n = ((q^l;q^l)_\infty / (q;q)_\infty)^n restricted till q^s term'''
    
    p={0:1}
    for i in range(1,s+1):
        
        if i%l != 0:
            for j in range(0,n):
                p=qmul(p,qf1(s,i),s)
    
    return p

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




# dictionary to list 

def to_list(q):
    ''' outputs values of dictionary in ordered list'''
    ll=[q[i] for i in range(len(q))]
    return ll



st.set_page_config(page_title="Colored l-regular partitions of n",page_icon=":waving_white_flag:")
st.sidebar.header(('Colored $l$-regular partitions of n'))

st.markdown('## $s$ Colored $l$-regular partitions of n = $c_l^s(n)$ ')
st.sidebar.write('$c_l^s(n)$ is the $s$ Colored $l$-regular partition function that outputs the number of $s$ Colored $l$ regular partitions a non-negative integer can be partitioned into.')
st.markdown('which can be represented as :')
st.latex(r'C_l^s(q) = \displaystyle \sum_{n=0}^\infty c_l^s(n) q^n = \frac {(q^l;q^l)_\infty^s} {(q;q)_\infty^s} = \frac {f_l^s} {f_1^s}')
st.markdown('where $f_s=(q^s;q^s)_\infty = \displaystyle \prod_{n=1}^\infty (1-q^{ns})$')

s=st.number_input('Input value for $s \quad$ i.e. for $c_l^s$', min_value=1, max_value=3000, step=1, value=2 , disabled=False)
l=st.number_input('Input value for $l \quad$ i.e. for $c_l$', min_value=1, max_value=3000, step=1, value=2 , disabled=False)
n=st.number_input('Input value for $n \quad$ i.e. for $c_l^s(n)$', min_value=1, max_value=3000, step=1, value=100 , disabled=False)



if st.button('q series values'):
    clreg_p= C_l_regular(s,l,n)
    l_p=to_list(clreg_p)
   
    c=st.text_area(label='',value=l_p)
    
if st.button('q series representation'):
    clreg_p= C_l_regular(s,l,n)
    clreg_s=qprint(clreg_p)
    d=st.text_area(label='',value=clreg_s)
