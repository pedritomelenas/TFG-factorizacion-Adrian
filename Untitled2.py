#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import numpy as np
import random


# In[4]:


def  trialdiv(n):
    L=[]
    if n<0:
        n=math.fabs(n)
        L.append(-1)
    m=math.ceil(math.sqrt(math.fabs(n)))
    for i in  range (2,m+1):
        while n%i==0  and n!=1:
            L.append(i)
            n=n/i
    if n==1:
        return L
    else:
        L.append(int(n))
        return L 


# In[5]:


def Bsmooth(n,B):
    smooth=True
    L=trialdiv(n)
    i=0
    while smooth==True and i<len(L):
        if L[i] not in B:
            smooth=False
        i+=1
    return smooth


# In[6]:


def exp(n,B):
    L=trialdiv(n)
    E = []
    i=0
    while len(L)>0 and i<len(B):
        a=L[0]
        if a==B[i]:
            j=0
            count=0
            while j<len(L):
                if L[j]==a:
                    count+=1
                    L.pop(j)
                    j=0
                else:
                    j+=1
            E.append(count%2)
            i+=1
        else:
            i+=1
            E.append(0)
    while len(E)<len(B):
        E.append(0)
    return E        


# In[7]:


def iszero(n):
    bool=True
    L=exp(n,[2,3,5,7])
    i=0
    while bool==True and i<len(L):
        if L[i]==1:
            bool=False
        i+=1
    return bool


# In[8]:


def isprime(n):
    prime=True
    i=2
    while i<=math.sqrt(n) and prime==True:
        if n%i==0:
            prime=False
        i+=1
    return prime


# In[9]:


def basef (n,M):
    B=[-1,2]
    i=3
    while i<=M:
        if int((n**int((i-1)/2))%i)==1 and isprime(i)==True:  #criterio de Euler
            B.append(i)
        i+=1
    return B


# In[1]:


def QS(n,M1,M2):
    z=0
    w=0
    Base=basef(n,M2) #generamos la base de factores
    S=[math.ceil(math.sqrt(n))]
    #Generación de la lista S
    for i in range(1,M1):
        S.append(math.ceil(math.sqrt(n))+i)
        S.append(math.ceil(math.sqrt(n))-i)
    B = []
    Z = []
    W=[]
    i=0
    #Búsqueda de números lisos para nuestra base de factores
    while i<len(S) and len(Base)>=len(Z):
        z=S[i]
        w=z**2-n 
        if Bsmooth(w,Base):
            Z.append(z)
            W.append(w) 
            B.append(exp(w,Base)) #aqui tendríamos la matriz de exponentes
        i+=1
