import streamlit as st

@st.cache_data
def str_to_list(a): #coverts string to a numerical list
    lll=a[1:-1]
    lll=lll.split(',')
    lll=[ int(j) for i,j in enumerate(lll)]
    return lll


@st.cache_data
def filter_mod(a,b,c,d,e):
    ''' collapses list a to ci+d for i variable indexes and filters it with [..]mod b = e to give exceptions'''
    try:
        a=str_to_list(a)
        l=[]
        tt=0
        i=0
            
        while tt<=len(a) :
            tt=c*i+d
            if tt<len(a) :
                l.append(a[tt])
            i+=1
            
        res=list(filter(lambda x : (x%b)-e ,l))
            
        if len(res)==0:
            t=f'No exceptions found for list[{c}n+{d}] mod {b} = {e} '
            st.balloons()
            st.success(t)
            
        else:
            lmn=[]
            for i,j in enumerate(res):
                k=a.index(j)
                lmn.append(k)
            t= f'Exceptions for list[{c}n+{d}] mod {b} = {e} they are list{lmn} = {res}'
            st.error(t)
    except:
        
        t = 'input a proper list with numerical values (eg format: [2,4,8])'
        st.warning(t)



st.set_page_config(page_title="Mod check",page_icon=":notebook:")
st.sidebar.header(('Mod check'))

st.write(r'## Check for $a \; mod \; b \equiv e$ for $\; c\;i+d \;$ indices ($i$ variable) of a list $a$')
st.write(r'input a list $a$ (copy any list from "q series values" output) and integers $b,c,d,e$ as for above operations')

a=st.text_area(label='input $a \quad$ list $a$ (copy any list from "q series values" output)')
b = st.number_input('Input value for $b \quad$ i.e. for $\pmod b$', min_value=1, max_value=3000, step=1, value=2 , disabled=False)
c = st.number_input('Input value for $c \quad$ i.e. for $c\;i+d$', min_value=0, max_value=3000, step=1, value=2 , disabled=False)
d = st.number_input('Input value for $d \quad$ i.e. for $c\;i+d$', min_value=0, max_value=3000, step=1, value=2 , disabled=False)
e =st.number_input('Input value for $e \quad$ i.e. for $\pmod b = e$', min_value=0, max_value=3000, step=1, value=0 , disabled=False)

if st.button('Check'):
    filter_mod(a,b,c,d,e)
