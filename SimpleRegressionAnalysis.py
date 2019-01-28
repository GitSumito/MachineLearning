#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# ベクトルの定義


# In[3]:


x = np.array([1,2,3])


# In[4]:


x


# In[5]:


y = np.array([2,3.9,6.1])


# In[6]:


y


# In[7]:


## データの中心化


# In[8]:


# 平均の算出


# In[9]:


x.mean()


# In[10]:


y.mean()


# In[11]:


# 中心化


# In[12]:


xc = x -x.mean()


# In[13]:


xc


# In[16]:


yc = y - y.mean()


# In[17]:


yc


# In[18]:


## パラメータaの計算


# In[19]:


# 要素ごとの掛け算（要素積）


# In[20]:


xx = xc * xc


# In[21]:


xx


# In[22]:


xy = xc * yc


# In[24]:


xy


# In[25]:


xx.sum()


# In[26]:


xy.sum()


# In[27]:


a = xy.sum()/xx.sum()


# In[28]:


a


# In[ ]:




