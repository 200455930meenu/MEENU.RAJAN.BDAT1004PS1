#!/usr/bin/env python
# coding: utf-8

# In[4]:


#question3a
def inside(x,y,x1,y1,x2,y2):
    if(x>x1 and x<x2 and y>y1 and y<y2):
        return True
    else:
        return False
    
    


# In[5]:


inside(1,1,0,0,2,3)


# In[9]:


inside(-1,-1,0,0,2,3)


# In[8]:


#question3b
inside(1,1,0.3,0.5,1.1,0.7)


# In[10]:


inside(1,1,0.5,0.2,1.1,2)


# In[ ]:


#by checking both set of points it's clear that (1,1) does not lies inside(0.3,0.5)an(1.1,0.7)

