#partition of n

import streamlit as st

# Partition function list
@st.cache_data
def p(n):
    '''partition function that generates partitions and returns a list of them till n (input) using eulers algoritm'''
    
    pat=[1,1,2,3,5,7,11]
    n=int(n)
    if n<0  :
        return pat[1] 
    elif n<7:
        return pat[0:n+1]
    else:
        pt=pat
        for j in range (7,n+1):
            P=0
            
            for i in range (1,j+1):
                k1=int((i*(3*i+1))/2)
                k2=int((i*(3*i-1))/2)
                if j-k1<0 and j-k2 <0:
                    break
                elif j-k1<0 :
                    P+=((-1)**(i+1))*(pt[j-k2])
                elif j-k2<0 :
                    P+=((-1)**(i+1))*(pt[j-k1])
                else:
                    P+=((-1)**(i+1))*(pt[j-k1]+pt[j-k2]) # eulers formula iteration

            pt.append(P)
        return pt 




# q-series generation 

# =============================================================================
# def qf1(n,m=1):
#     ''' outputs a dictionary in which we concider its keys as 'q' raised to power and 
#     values is the respective coefficient = 1 as (LaTeX): (q^m;q^m)_\infty = \Pi_{i=1}^\infty (1-q^{m i})'''
#     
#     n=n//m
#     return {m*i:1 for i in range(n+1)}
# 
# 
# 
# 
# # q-series multiplication
# 
# def qmul(a,b,t=100):
#     ''' we define qmul as multiplication of two dictionaries in a way to replicate multiplication in q series'''
#     p={}
#     
#     for i,j in a.items():
#         for k,l in b.items():
#             if (i+k)<=t:
#                 try:
#                     p[i+k]+=(j*l) #main step of adding powers and multiplying coefficients
#                 except:
#                     p[i+k]=(j*l)
#     return p
# 
# 
# 
# 
# # 1/f1 p(n)q^n generator
# 
# def f_1(s):
#     '''outputs 1/f1 = 1/(q;q)_\infty restricted till q^s term'''
#     
#     p={0:1}
#     for i in range(1,s+1):
#     
#         p=qmul(p,qf1(s,i),s)
# 
#     return p
# 
# 
# 
# 
# # l-regular partition function generator
# 
# def f_l_regular(l,s=100):
#     '''outputs fl/f1 = (q^l;q^l)_\infty / (q;q)_\infty restricted till q^s term'''
#     
#     p={0:1}
#     for i in range(1,s+1):
#         
#         if i%l != 0:
#             p=qmul(p,qf1(s,i),s)
#     
#     return p
# 
# 
# 
# 
# # (l,m)-regular partition function generator
# 
# def f_lm_regular(l,m,s=100):
#     '''outputs fl fm /f1 flm = (q^l;q^l)_\infty (q^m;q^m)_\infty / (q;q)_\infty (q^{lm};q^{lm})_\infty restricted till q^s term'''
#     
#     p={0:1}
#     
#     for i in range(1,s+1):
#         
#         if i%l != 0 and i%m !=0 :
#             p=qmul(p,qf1(s,i),s)
#     
#     return p
# 
# 
# 
# 
# # n colored partitions i.e. 1/f1^n i.e. C_n(m)q^m generator
# 
# def C_f_1(n,s):
#     '''outputs 1/f1^n = 1/(q;q)_\infty^n restricted till q^s term'''
#     
#     p={0:1}
#     for i in range(1,s+1):
#         
#         for j in range(0,n):
#             p=qmul(p,qf1(s,i),s)
# 
#     return p
# 
# 
# 
# 
# # n colored l-regular partition function generator
# 
# def C_l_regular(n,l,s=100):
#     '''outputs (fl/f1)^n = ((q^l;q^l)_\infty / (q;q)_\infty)^n restricted till q^s term'''
#     
#     p={0:1}
#     for i in range(1,s+1):
#         
#         if i%l != 0:
#             for j in range(0,n):
#                 p=qmul(p,qf1(s,i),s)
#     
#     return p
# 
# 
# 
# 
# #2 colour (l,m) - regular partition function generator
# 
# def C_lm_regular(n,l,m,s=100):
#     '''outputs (fl fm /f1 flm)^n = ((q^l;q^l)_\infty (q^m;q^m)_\infty / (q;q)_\infty (q^{lm};q^{lm})_\infty)^n restricted till q^s term for co-prime m and l'''
#     
#     p={0:1}
#     
#     for i in range(1,s+1):
#         
#         if i%l != 0 and i%m !=0 :
#             for j in range(0,n):
#                 p=qmul(p,qf1(s,i),s) 
#             
#     return p
# =============================================================================




def outsci(stat,n): # converts number to scientific (10^n) form
    st=str(stat)
    m=len(st)
    stt=''
    if m>n:
        for i in range(n):
                try:
                    stt=stt+st[i]
                except:
                    stt+='0'
        at=m-n
        return f' {stt} \\times 10^{ {at} } '
    else:
        return f' {st} ' 




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




# dictionary to list 

def to_list(q):
    ''' outputs values of dictionary in ordered list'''
    ll=[q[i] for i in range(len(q))]
    return ll




def str_to_list(a): #coverts string to a numerical list
    lll=a[1:-1]
    lll=lll.split(',')
    lll=[ int(j) for i,j in enumerate(lll)]
    return lll

def list_to_str(a): # converts a list to comma saperated string
    s=''
    s+=str(a[0])
    for i in a[1:] :
        s=s+','+str(i)
    return s

def str_brk(a,m): #breaks string to desired length and adds \n 
    l=len(a)
    div=l//m
    rem=l%m
    ll=[]
    for i in range(div):
        try:
            ds=a[i*m:(i+1)*m]
            ll.append(ds)
        except:
            ds=a[i*m:(i*m)+rem]
            ll.append(ds)
    b=' \n '.join(ll)
    return b


# list mod function

# =============================================================================
# def filter_mod(a,b,c,d,e):
#     ''' collapses list a to ci+d for i variable indexes and filters it with [..]mod b = e to give exceptions'''
#     try:
#         a=str_to_list(a)
#         l=[]
#         tt=0
#         i=0
#             
#         while tt<=len(a) :
#             tt=c*i+d
#             if tt<len(a) :
#                 l.append(a[tt])
#             i+=1
#             
#         res=list(filter(lambda x : (x%b)-e ,l))
#             
#         if len(res)==0:
#             t=f'No exceptions found for list[{c}n+{d}] mod {b} = {e} '
#             
#         else:
#             lmn=[]
#             for i,j in enumerate(res):
#                 k=a.index(j)
#                 lmn.append(k)
#             t= f'Exceptions for list[{c}n+{d}] mod {b} = {e} they are list{lmn} = {res}'
#     except:
#         t = 'input a proper list with numerical values (eg format: [2,4,8])'
#     return t
# =============================================================================







st.set_page_config(page_title="Partitions of n",page_icon=":signal_strength:")
st.sidebar.header((' Partitions of n '))

st.markdown('# Partition of n = p(n) ')
st.sidebar.write('$p(n)$ is the partition function that outputs the number of partitions a non-negative integer can be partitioned into.')
st.markdown('which can be represented as :')
st.latex(r'P(q) = \displaystyle \sum_{n=0}^\infty p(n) q^n = \frac {1} {(q;q)_\infty} = \frac {1} {f_1}')
st.markdown('where $f_1=(q^1;q^1)_\infty = \displaystyle \prod_{n=1}^\infty (1-q^n)$')


n=st.number_input('Input value for $n \quad$ i.e. $p(n=)$', min_value=0, max_value=None, value=1000 , disabled=False)

    
btn=st.button('   =   ' )

# =============================================================================
# @st.cache_data
# def partition_val(n):
#     return effparti(n)
# =============================================================================

if btn :
    p=p(n)
    p_n=p[-1]
    k_sci=outsci(p_n,7)
    w=f' p({n}) \quad = \quad {k_sci} '
    a=st.latex(w) 
    
if st.button('precisely ='):
    p=p(n)
    p_n=p[-1]
        
    w1=f' p({n})  =  {p_n} '
    b=st.write(w1)
    
        
if st.button('q series values'):
    p=p(n)
    p_n=p[-1]
    c=st.text_area(label='',value=p)
  
if st.button('q series representation'):
    p=p(n)
    p_n=p[-1]
    q_s=qprint(p)
    d=st.text_area(label='',value=q_s)




