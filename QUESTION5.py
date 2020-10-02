#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bloodCount():
    f1=open('bloodtype.txt','r+')
    for i in range (f1): 
        
    int a=f1.count('A')
        print('There is'+' '+a+' '+'patients of blood type A')
    int  b=f1.count('B')
        print('There is'+' '+b+' '+'patients of blood type B')
    int  c=f1.count('AB')
        print('There is'+' '+c+' '+'patients of blood type AB')
    int  d=f1.count('O')
        print('There is'+' '+d+' '+'patients of blood type O')
    int  e=f1.count('OO')
        print('There is'+' '+e+' '+'patients of blood type OO')
                   

        


# In[ ]:




