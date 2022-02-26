#!/usr/bin/env python
# coding: utf-8

# In[27]:


def exprapID(base, num, mod):
    acu=1
    binary=format(num,"b")
    i=0
    exp=0
    while i<len(binary):
        exp*=2
        acu=(acu**2)%mod
        if binary[i]=="1":
            acu=(acu*base)%mod
            exp+=1
        i+=1
    return acu


# In[31]:


def TestLucas(n,L):
    a=2
    i=0
    while a<n:     
        bool=True
        if exprapID(2, n-1,n)!=1:
            return False
        else:
            while i<len(L):
                if exprapID(2,int((n-1)/L[i]),n)==1:
                    bool=False
                i+=1
        if bool==True:
            return True
    return False

