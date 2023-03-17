#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date


# In[11]:


# Carregando dados da base fornecida

base_Geral = pd.read_csv("walmart.csv")
recursos = pd.read_csv("features.csv")
envio_amostras = pd.read_csv("sampleSubmission.csv")
lojas = pd.read_csv("stores.csv")
tem_feriado = pd.read_csv("test.csv")
fat_departamento = pd.read_csv("train.csv")


# In[ ]:


# Exibição de todos as bases, com suas respectivas informações e dados estatísticos


# In[12]:


display(base_Geral)


# In[13]:


base_Geral.info()


# In[14]:


base_Geral.describe()


# In[15]:


display(recursos)


# In[17]:


recursos.info()


# In[18]:


recursos.describe()


# In[19]:


display(envio_amostras)


# In[20]:


envio_amostras.info()


# In[21]:


display(lojas)


# In[22]:


lojas.info()


# In[66]:


lojas.describe().transpose()


# In[23]:


lojas.shape


# In[24]:


display(tem_feriado)


# In[25]:


tem_feriado.info()


# In[26]:


display(fat_departamento)


# In[27]:


fat_departamento.info()


# In[28]:


fat_departamento.describe()


# In[29]:


# Mesclando os conjuntos de dados similares entre as bases

geral = fat_departamento.merge(lojas, 'left').merge(recursos, 'left')
geral.head()


# In[30]:


# Descrição Geral pós mesclagem

geral.describe().transpose()


# In[31]:


# Faturamento por loja

fat_por_loja = geral[["Store", "Weekly_Sales"]].groupby("Store").sum()
display(fat_por_loja)


# In[32]:


# Faturamento por departamento

fat_por_departamento = geral[["Store", "Dept", "Date", "IsHoliday", "Weekly_Sales"]].groupby(["Store", "Dept", "Date", "IsHoliday"]).sum()
display(fat_por_departamento)


# In[33]:


# Faturamento nos dias de feriado

fat_feriado = base_Geral.loc[base_Geral['Holiday_Flag'] == 1]
display(fat_feriado)


# In[49]:


fat_feriado.to_excel('fat_feriado.xlsx')


# In[55]:


fat_feriado.plot(kind='bar', subplots=True, layout=(3,3), figsize=(80,40), sharey=True)


# In[37]:


fat_Nao_feriado = base_Geral.loc[base_Geral['Holiday_Flag'] == 0]
display(fat_Nao_feriado)


# In[65]:


fat_Nao_feriado.plot(kind='bar', subplots=True, layout=(3,3), figsize=(80,40), sharey=True)


# In[ ]:


# Faturamento em dias sem feriado


# In[ ]:


fat_Nao_feriado.to_excel('fat_Nao_feriado.xlsx')


# In[39]:


geral[['Date', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']].plot(x='Date', subplots=True, figsize=(15,15))

plt.show()


# In[40]:


# Correlação entre os recursos

sns.heatmap(recursos.corr())


# In[41]:


# Correlação entre os dados gerais
sns.heatmap(geral.corr())


# In[42]:


# Vendas Médias por Loja

vendas_semanais = geral['Weekly_Sales'].groupby(geral['Store']).mean()
plt.figure(figsize=(20,8))
sns.barplot(vendas_semanais.index, vendas_semanais.values, palette='dark')
plt.grid()
plt.title('Média de vendas - por loja', fontsize=18)
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Loja', fontsize=16)
plt.show()


# In[43]:


# Vendas Médias por Departamento

vendas_porDepartamento = geral['Weekly_Sales'].groupby(geral['Dept']).mean()
plt.figure(figsize=(20,8))
sns.barplot(vendas_porDepartamento.index, vendas_porDepartamento.values, palette='dark')
plt.grid()
plt.title('Média de vendas - por Departamento', fontsize=18)
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Departamento', fontsize=16)
plt.show()


# In[44]:


# Vendas Médias por Data

vendas_porData = geral['Weekly_Sales'].groupby(geral['Date']).mean()
plt.figure(figsize=(20,8))
sns.barplot(vendas_porData.index, vendas_porData.values, palette='dark')
plt.grid()
plt.title('Média de vendas - por Data', fontsize=18)
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Data', fontsize=16)
plt.show()


# In[45]:


# Vendas Médias por Categoria da Loja

vendas_porCatLoja = geral['Weekly_Sales'].groupby(geral['Type']).mean()
plt.figure(figsize=(20,8))
sns.barplot(vendas_porCatLoja.index, vendas_porCatLoja.values, palette='dark')
plt.grid()
plt.title('Média de vendas - por Categoria de Loja', fontsize=18)
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Categoria', fontsize=16)
plt.show()


# In[46]:


# Agrupando de vendas por data

vendas_Data = geral.groupby('Date')['Weekly_Sales'].sum()
display(vendas_Data)


# In[47]:


# Faturamento nos dias de feriado

media_Fat_Feriado = geral[['Date', 'Store', 'Dept', 'Weekly_Sales']]
display(media_Fat_Feriado)


# In[48]:


FatFeriado = media_Fat_Feriado['Weekly_Sales'].groupby(media_Fat_Feriado['Date']).mean()
plt.figure(figsize=(20,8))
sns.barplot(FatFeriado.index, FatFeriado.values, palette='dark')
plt.grid()
plt.title('Média de vendas - por Data', fontsize=18)
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Data', fontsize=16)
plt.show()


# In[ ]:




