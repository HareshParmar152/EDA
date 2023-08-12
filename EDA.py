#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv("C:/Users/hares/Downloads/drive-download-20220817T202742Z-001/application_data.csv")


# In[4]:


df.shape


# In[5]:


temp= df.describe()


# In[6]:


Nul_col = df.isnull().sum()


# In[7]:


Nul_filter = Nul_col[Nul_col >1]


# In[8]:


temp = Nul_col * 100 / 307511


# In[9]:


temp


# In[10]:


df = df[~df.AMT_ANNUITY.isnull()]


# In[11]:


df.isnull().sum()


# In[12]:


df = df[~df.AMT_GOODS_PRICE.isnull()]


# In[13]:


df.isnull().sum()


# In[14]:


df = df[~df.NAME_TYPE_SUITE.isnull()]


# In[15]:


df.isnull().sum()


# In[16]:


df = df[~df.EXT_SOURCE_2.isnull()]


# In[17]:


df.isnull().sum()


# In[18]:


df = df[~df.OBS_30_CNT_SOCIAL_CIRCLE.isnull()]
df = df[~df.DEF_30_CNT_SOCIAL_CIRCLE.isnull()]
df = df[~df.OBS_60_CNT_SOCIAL_CIRCLE.isnull()]
df = df[~df.DEF_60_CNT_SOCIAL_CIRCLE.isnull()]


# In[19]:


df.isnull().sum()


# In[20]:


df1 = df.copy()


# In[21]:


df.shape


# In[22]:


Nul_col = df.isnull().sum()
temp = Nul_col * 100 / 304531
temp


# In[23]:


df = df1.copy()


# In[24]:


N_col = temp[temp > 35]


# In[25]:


col = df.columns


# In[26]:


test = Nul_col * 100 / 304531


# In[27]:


test[test > 32]


# In[28]:


l = []
for i in col:
    Nl = df[i].isnull().sum()
    Nl = Nl * 100 / 304531
    if Nl > 45:
        l.append(i)
        


# In[29]:


df.drop(columns=l,inplace=True)


# In[30]:


l


# In[31]:


df.isnull().sum()


# In[32]:


df.shape


# In[33]:


208259 * 100 / 304531


# In[34]:


i


# In[35]:


df1.AMT_REQ_CREDIT_BUREAU_YEAR.isnull().sum()


# In[36]:


N_col = df.isnull().sum()


# In[37]:


N_col[N_col > 1]


# In[38]:


df.OCCUPATION_TYPE.value_counts(normalize=True)


# In[39]:


OCCUPATION = df.OCCUPATION_TYPE.mode()[0]


# In[40]:


df.OCCUPATION_TYPE.fillna(OCCUPATION,inplace=True)


# In[41]:


N_col = df.isnull().sum()
N_col[N_col > 1]


# In[42]:


EXT_SOURCE = df.EXT_SOURCE_3.mean()


# In[43]:


df.EXT_SOURCE_3.fillna(EXT_SOURCE,inplace=True)


# In[44]:


N_col = df.isnull().sum()
N_col[N_col > 1]


# In[45]:


df.AMT_REQ_CREDIT_BUREAU_HOUR.describe()


# In[46]:


df.AMT_REQ_CREDIT_BUREAU_DAY.describe()


# In[47]:


df.AMT_REQ_CREDIT_BUREAU_WEEK.describe()


# In[48]:


df.AMT_REQ_CREDIT_BUREAU_QRT.describe()


# In[49]:


df.AMT_REQ_CREDIT_BUREAU_YEAR.describe()


# In[50]:


df.drop(columns=['AMT_REQ_CREDIT_BUREAU_HOUR','AMT_REQ_CREDIT_BUREAU_DAY',
                 'AMT_REQ_CREDIT_BUREAU_WEEK','AMT_REQ_CREDIT_BUREAU_MON','AMT_REQ_CREDIT_BUREAU_QRT'],inplace=True)


# In[51]:


AMT_Year = df.AMT_REQ_CREDIT_BUREAU_YEAR.mean()


# In[52]:


df.AMT_REQ_CREDIT_BUREAU_YEAR.fillna(AMT_Year,inplace=True)


# In[53]:


df.isnull().sum()


# In[54]:


col = df.columns


# In[55]:


df[i].dtypes


# In[56]:


temp = df.OCCUPATION_TYPE.dtypes


# In[57]:


print(temp)


# In[58]:


ob = []
num = []
num_group = []
for i in col:
    
    if df[i].dtypes == "object":
        ob.append(i)
    elif len(df[i].unique()) < 5:
        num_group.append(i)
    else:
        num.append(i)
    


# In[59]:


for i in range(len(num)):
    plt.figure(figsize=(7,5))
    plt.boxplot(df[num[i]])
    plt.title(num[i])
    plt.show()


# In[60]:


df.CNT_CHILDREN.describe()#Will Drop


# In[61]:


df.AMT_INCOME_TOTAL.describe()


# In[62]:


df[df.AMT_INCOME_TOTAL > 10000000]


# In[63]:


df[df.AMT_INCOME_TOTAL > 10000000]


# In[64]:


df.shape


# In[65]:


df = df[~(df.AMT_INCOME_TOTAL > 40000000)]


# In[66]:


plt.boxplot(df.AMT_INCOME_TOTAL)
plt.show()


# In[67]:


df[df.AMT_INCOME_TOTAL > 4000000]


# In[68]:


df.shape


# In[69]:


df = df[~(df.AMT_INCOME_TOTAL > 4000000)]


# In[70]:


df


# In[71]:


plt.boxplot(df.AMT_INCOME_TOTAL)
plt.show()


# In[72]:


df[df.AMT_INCOME_TOTAL > 2400000]


# In[73]:


df = df[~(df.AMT_INCOME_TOTAL > 2400000)]


# In[74]:


df.shape


# In[75]:


plt.boxplot(df.AMT_INCOME_TOTAL)
plt.show()


# In[76]:


df[df.AMT_ANNUITY > 250000]


# In[77]:


df[df.REGION_POPULATION_RELATIVE == 0.072508]


# In[78]:


df.REGION_POPULATION_RELATIVE.value_counts()


# In[79]:


df.DAYS_EMPLOYED = abs(df.DAYS_EMPLOYED)


# In[80]:


df.DAYS_EMPLOYED.describe()


# In[81]:


df[df.DAYS_EMPLOYED > 18250]


# In[82]:


df.DAYS_EMPLOYED.value_counts()


# In[83]:


plt.boxplot(df.DAYS_EMPLOYED == 365243)
plt.show()


# In[84]:


df.isnull().sum()


# In[85]:


df.shape


# In[86]:


249678  * 100 / 304511


# In[87]:


temp = df[df.DAYS_EMPLOYED < 18250]


# In[88]:


#df2 = df.copy()


# In[89]:


df[num] = abs(df[num])


# In[90]:


df


# In[91]:


df.DAYS_EMPLOYED.describe()


# In[92]:


#df[df.DAYS_EMPLOYED != 365243].mean()


# In[93]:


#df.DAYS_EMPLOYED == 365243


# In[94]:


sns.boxplot(df.DAYS_EMPLOYED)
plt.show()


# In[95]:


df.DAYS_EMPLOYED.replace(365243,2385.949395,inplace=True)


# In[96]:


sns.boxplot(df.DAYS_EMPLOYED)
plt.show()


# In[97]:


df.DAYS_EMPLOYED.describe()


# In[98]:


sns.boxplot(df.DAYS_REGISTRATION)
plt.show()


# In[99]:


df.DAYS_REGISTRATION.describe()


# In[100]:


df[df.DAYS_REGISTRATION > 20672]


# In[101]:


df.CNT_FAM_MEMBERS.describe()


# In[102]:


df[df.CNT_FAM_MEMBERS <10]


# In[103]:


df[df.CNT_FAM_MEMBERS < 5]


# In[104]:


sns.boxplot(df.CNT_FAM_MEMBERS)
plt.show()


# In[105]:


df[df.CNT_FAM_MEMBERS > 5]


# In[106]:


df = df[~(df.CNT_FAM_MEMBERS > 4.5)]


# In[107]:


sns.boxplot(df.CNT_FAM_MEMBERS)
plt.show()


# In[108]:


df.CNT_FAM_MEMBERS.describe()


# In[109]:


sns.boxplot(df.CNT_FAM_MEMBERS)
plt.show()


# In[110]:


sns.boxplot(df.HOUR_APPR_PROCESS_START)
plt.show()


# In[111]:


df.HOUR_APPR_PROCESS_START.describe()


# In[112]:


sns.boxplot(df.EXT_SOURCE_3)


# In[113]:


df.EXT_SOURCE_3.describe()


# In[114]:


df.OBS_30_CNT_SOCIAL_CIRCLE.describe()


# In[115]:


df.drop(columns="OBS_30_CNT_SOCIAL_CIRCLE",inplace=True)


# In[116]:


df.DEF_30_CNT_SOCIAL_CIRCLE.describe()


# In[117]:


df.drop(columns="DEF_30_CNT_SOCIAL_CIRCLE",inplace=True)


# In[118]:


df.OBS_60_CNT_SOCIAL_CIRCLE.describe()


# In[119]:


df.drop(columns="OBS_60_CNT_SOCIAL_CIRCLE",inplace=True)


# In[120]:


df.DEF_60_CNT_SOCIAL_CIRCLE.describe()


# In[121]:


df.drop(columns="DEF_60_CNT_SOCIAL_CIRCLE",inplace=True)


# In[122]:


df.DAYS_LAST_PHONE_CHANGE.describe()


# In[123]:


sns.boxplot(df.DAYS_LAST_PHONE_CHANGE)


# In[124]:


df.AMT_REQ_CREDIT_BUREAU_YEAR.describe()


# In[125]:


sns.boxplot(df.AMT_REQ_CREDIT_BUREAU_YEAR)


# In[126]:


df[df.AMT_REQ_CREDIT_BUREAU_YEAR > 19]


# In[127]:


df.shape


# In[128]:


df.isnull().sum()


# # New data load

# In[129]:


df_prevours = pd.read_csv("C:/Users/hares/Downloads/drive-download-20220817T202742Z-001/previous_application.csv")


# In[130]:


df_prevours.isnull().sum()


# In[131]:


df_prevours.shape


# In[132]:


Nul_col = df_prevours.isnull().sum()


# In[133]:


temp = Nul_col * 100 / 1670214


# In[134]:


Nul_filter = Nul_col[Nul_col >1]


# In[135]:


temp = Nul_filter * 100 / 1670214


# In[136]:


temp


# In[137]:


temp[temp >40]


# In[138]:


df_prevours.drop(columns=["AMT_DOWN_PAYMENT","RATE_DOWN_PAYMENT","RATE_INTEREST_PRIMARY","RATE_INTEREST_PRIVILEGED",
                         "NAME_TYPE_SUITE","DAYS_FIRST_DRAWING","DAYS_FIRST_DUE","DAYS_LAST_DUE_1ST_VERSION","DAYS_LAST_DUE",
                         "DAYS_TERMINATION","NFLAG_INSURED_ON_APPROVAL"],inplace=True)


# In[139]:


df_prevours.isnull().sum()


# In[140]:


temp[temp <40]


# In[141]:


df_prevours = df_prevours[~(df_prevours.AMT_CREDIT.isnull())]


# In[142]:


df_prevours[df_prevours.AMT_CREDIT.isnull()]


# In[143]:


df_prevours.isnull().sum()


# In[144]:


temp[temp <40]


# In[145]:


df_prevours.AMT_ANNUITY.isnull().sum()


# In[146]:


df_prevours.shape


# In[147]:


mean_test = df_prevours[~(df_prevours.AMT_ANNUITY.isnull())]


# In[148]:


NA_fill = mean_test.AMT_ANNUITY.mean()


# In[149]:


df_prevours.AMT_ANNUITY.describe()


# In[150]:


df_prevours.AMT_ANNUITY.fillna(NA_fill,inplace=True)


# In[151]:


df_prevours.AMT_ANNUITY.describe()


# In[152]:


df_prevours.AMT_ANNUITY.isnull().sum()


# In[153]:


df_prevours.AMT_GOODS_PRICE.isnull().sum()


# In[154]:


NA_fill = mean_test.AMT_GOODS_PRICE.mean()


# In[155]:


df_prevours.AMT_GOODS_PRICE.fillna(NA_fill,inplace=True)


# In[156]:


df_prevours.AMT_GOODS_PRICE.isnull().sum()


# In[157]:


df_prevours.CNT_PAYMENT.isnull().sum()


# In[158]:


NA_fill = mean_test.CNT_PAYMENT.mean()


# In[159]:


df_prevours.CNT_PAYMENT.fillna(NA_fill,inplace=True)


# In[160]:


df_prevours.CNT_PAYMENT.isnull().sum()


# In[162]:


NA_fill = mean_test.PRODUCT_COMBINATION.mode()[0]


# In[163]:


df_prevours.PRODUCT_COMBINATION.fillna(NA_fill,inplace=True)


# In[164]:


df_prevours.isnull().sum()


# In[165]:


col_pr = df_prevours.columns


# In[166]:


col_pr


# In[167]:


ob_pr = []
num_pr = []
num_group_pr = []
for i in col_pr:
    
    if df_prevours[i].dtypes == "object":
        ob_pr.append(i)
    elif len(df_prevours[i].unique()) < 5:
        num_group_pr.append(i)
    else:
        num_pr.append(i)


# In[168]:


num_pr


# In[169]:


df_prevours[num_pr] =  abs(df_prevours[num_pr])


# In[170]:


round(df_prevours[num_pr[2:]].describe(),2)


# In[171]:


for i in range(len(num_pr)):
    plt.figure(figsize=(7,5))
    plt.boxplot(df_prevours[num_pr[i]])
    plt.title(num_pr[i])
    plt.show()


# In[172]:


df_prevours[df_prevours.AMT_ANNUITY > 240000]


# In[173]:


df_prevours = df_prevours[~(df_prevours.AMT_ANNUITY > 350000)]


# In[174]:


sns.boxplot(df_prevours.AMT_ANNUITY)
plt.show()


# In[175]:


df_prevours[df_prevours.AMT_APPLICATION > 5000000]


# In[176]:


df_prevours = df_prevours[~(df_prevours.AMT_APPLICATION > 5000000)]


# In[177]:


sns.boxplot(df_prevours.AMT_APPLICATION)
plt.show()


# In[178]:


df_prevours[df_prevours.AMT_CREDIT > 4000000]


# In[179]:


df_prevours = df_prevours[~(df_prevours.AMT_CREDIT > 4000000)]


# In[180]:


sns.boxplot(df_prevours.AMT_CREDIT)
plt.show()


# In[181]:


df_prevours[df_prevours.AMT_GOODS_PRICE > 4000000]


# In[182]:


df_prevours = df_prevours[~(df_prevours.AMT_GOODS_PRICE > 4000000)]


# In[183]:


sns.boxplot(df_prevours.AMT_GOODS_PRICE)
plt.show()


# In[184]:


sns.boxplot(df_prevours.SELLERPLACE_AREA)
plt.show()


# In[185]:


round(df_prevours.SELLERPLACE_AREA.describe(),2)


# In[186]:


df_prevours[df_prevours.SELLERPLACE_AREA > 400000]


# In[187]:


df_prevours = df_prevours[~(df_prevours.SELLERPLACE_AREA > 400000)]


# In[188]:


sns.boxplot(df_prevours.SELLERPLACE_AREA)
plt.show()


# In[189]:


df_prevours[df_prevours.SELLERPLACE_AREA > 100000]


# In[190]:


df_prevours = df_prevours[~(df_prevours.SELLERPLACE_AREA > 100000)]


# In[191]:


sns.boxplot(df_prevours.SELLERPLACE_AREA)
plt.show()


# In[192]:


df_prevours[df_prevours.SELLERPLACE_AREA > 60000]


# In[193]:


df_prevours = df_prevours[~(df_prevours.SELLERPLACE_AREA > 60000)]


# In[194]:


sns.boxplot(df_prevours.SELLERPLACE_AREA)
plt.show()


# In[195]:


round(df_prevours.CNT_PAYMENT.describe(),2)


# In[196]:


df_prevours[df_prevours.CNT_PAYMENT > 80]


# In[197]:


df_prevours = df_prevours[~(df_prevours.CNT_PAYMENT > 80)]


# In[198]:


sns.boxplot(df_prevours.CNT_PAYMENT)
plt.show()


# In[199]:


num_group_pr


# In[200]:


num_group


# In[201]:


num


# In[202]:


col = df.columns
ob = []
num = []
num_group = []
for i in col:
    if df[i].dtypes == "object":
        ob.append(i)
    elif len(df[i].unique()) < 5:
        num_group.append(i)
    else:
        num.append(i)


# In[203]:


df[num_group]


# In[204]:


df1.TARGET.value_counts()


# In[205]:


col_pr = df_prevours.columns
ob_pr = []
num_pr = []
num_group_pr = []
for i in col_pr:
    
    if df_prevours[i].dtypes == "object":
        ob_pr.append(i)
    elif len(df_prevours[i].unique()) < 5:
        num_group_pr.append(i)
    else:
        num_pr.append(i)


# In[226]:


num


# In[229]:


df.TARGET.value_counts(normalize=True).plot.barh()
plt.show()


# In[230]:


for i in range(len(num_group)):
    plt.figure(figsize=(7,5))
    df[num_group[i]].value_counts(normalize=True).plot.barh()
    plt.title(num_group[i])
    plt.show()


# In[231]:


df.CNT_CHILDREN.value_counts(normalize=True)


# In[232]:


df.FLAG_MOBIL.value_counts(normalize=True)


# In[233]:


for i in range(len(num_group)):
    print(df[num_group[i]].value_counts(normalize=True))
    


# In[236]:


df.drop(columns=["CNT_CHILDREN","FLAG_MOBIL","FLAG_WORK_PHONE","FLAG_PHONE","REGION_RATING_CLIENT_W_CITY",
                 "REG_REGION_NOT_LIVE_REGION","REG_REGION_NOT_WORK_REGION","LIVE_REGION_NOT_WORK_REGION",
                "REG_CITY_NOT_WORK_CITY","LIVE_CITY_NOT_WORK_CITY","FLAG_DOCUMENT_3","FLAG_DOCUMENT_4",
                "FLAG_DOCUMENT_5","FLAG_DOCUMENT_6","FLAG_DOCUMENT_7","FLAG_DOCUMENT_8","FLAG_DOCUMENT_9",
                "FLAG_DOCUMENT_10","FLAG_DOCUMENT_11","FLAG_DOCUMENT_12","FLAG_DOCUMENT_13","FLAG_DOCUMENT_14",
                 "FLAG_DOCUMENT_15","FLAG_DOCUMENT_16","FLAG_DOCUMENT_17","FLAG_DOCUMENT_18","FLAG_DOCUMENT_19",
                "FLAG_DOCUMENT_20","FLAG_DOCUMENT_21"],inplace=True)


# In[237]:


df.head(10)


# In[240]:


for i in range(len(ob)):
    plt.figure(figsize=(7,5))
    df[ob[i]].value_counts(normalize=True).plot.barh()
    plt.title(ob[i])
    plt.show()


# In[241]:


num_group_pr


# In[242]:


df_prevours.NFLAG_LAST_APPL_IN_DAY.value_counts(normalize=True).plot.barh()


# In[243]:


df_prevours.NFLAG_LAST_APPL_IN_DAY.value_counts(normalize=True)


# In[244]:


for i in range(len(ob_pr)):
    plt.figure(figsize=(7,5))
    df_prevours[ob_pr[i]].value_counts(normalize=True).plot.barh()
    plt.title(ob_pr[i])
    plt.show()


# In[245]:


for i in range(len(ob)):
    plt.figure(figsize=(7,5))
    df[ob[i]].value_counts(normalize=True).plot.barh()
    plt.title(ob[i])
    plt.show()


# In[246]:


df[df.CODE_GENDER == "XNA"]


# In[247]:


df = df[~(df.CODE_GENDER == "XNA")]


# In[248]:


df[df.CODE_GENDER == "XNA"]


# In[249]:


df_prevours[df_prevours.NAME_CONTRACT_TYPE == "XNA"]


# In[250]:


df_prevours = df_prevours[~(df_prevours.NAME_CONTRACT_TYPE == "XNA")]


# In[251]:


df = df[~(df.CODE_GENDER == "XNA")]


# In[252]:


df_prevours.NAME_CONTRACT_TYPE.value_counts(normalize=True)


# In[253]:


df_prevours.NAME_PAYMENT_TYPE.value_counts(normalize=True)


# In[254]:


df_prevours.CODE_REJECT_REASON.value_counts(normalize=True)


# In[255]:


df_prevours = df_prevours[~(df_prevours.CODE_REJECT_REASON == "XNA")]


# In[256]:


df_prevours.NAME_CLIENT_TYPE.value_counts(normalize=True)


# In[257]:


df_prevours = df_prevours[~(df_prevours.NAME_CLIENT_TYPE == "XNA")]


# In[258]:


round(df_prevours.NAME_GOODS_CATEGORY.value_counts(normalize=True),2)


# In[259]:


df_prevours.drop(columns="NAME_GOODS_CATEGORY",inplace=True)


# In[260]:


round(df_prevours.NAME_PORTFOLIO.value_counts(normalize=True),2)


# In[261]:


df_prevours.drop(columns="NAME_PRODUCT_TYPE",inplace=True)


# In[262]:


round(df_prevours.NAME_SELLER_INDUSTRY.value_counts(normalize=True),2)


# In[263]:


df_prevours.drop(columns="NAME_SELLER_INDUSTRY",inplace=True)


# In[264]:


round(df_prevours.NAME_YIELD_GROUP.value_counts(normalize=True),2)


# In[265]:


df[num]


# In[266]:


sns.scatterplot(df.AMT_ANNUITY,df.AMT_REQ_CREDIT_BUREAU_YEAR)
plt.show()# There no 


# In[267]:


sns.scatterplot(df.AMT_ANNUITY,df.AMT_CREDIT)
plt.show()


# In[268]:


sns.scatterplot(df.AMT_ANNUITY,df.AMT_GOODS_PRICE)
plt.show()


# In[269]:


df["BIRTH_YEAR"] = round(df.DAYS_BIRTH/365,0)


# In[270]:


df.BIRTH_YEAR


# In[271]:


sns.scatterplot(df.AMT_INCOME_TOTAL,df.BIRTH_YEAR)
plt.show()


# In[272]:


sns.pairplot(data=df,vars=["AMT_ANNUITY","AMT_CREDIT"])
plt.show()


# In[273]:


df[["AMT_INCOME_TOTAL","AMT_CREDIT","AMT_ANNUITY","AMT_GOODS_PRICE","REGION_POPULATION_RELATIVE","EXT_SOURCE_3","AMT_REQ_CREDIT_BUREAU_YEAR","BIRTH_YEAR"]].corr()


# In[274]:


sns.scatterplot(df.AMT_CREDIT,df.AMT_GOODS_PRICE)
plt.show()


# In[275]:


sns.heatmap(df[["AMT_INCOME_TOTAL","AMT_CREDIT","AMT_ANNUITY","AMT_GOODS_PRICE","REGION_POPULATION_RELATIVE","EXT_SOURCE_3",
                "AMT_REQ_CREDIT_BUREAU_YEAR","BIRTH_YEAR"]].corr(),annot=True,cmap="Reds")
plt.show()


# In[277]:


df.groupby("CODE_GENDER")["TARGET"].mean()


# In[296]:


df.groupby("NAME_EDUCATION_TYPE")["TARGET"].mean().plot.barh()
plt.title("Education & Default\n")
plt.show()


# In[300]:


df.groupby("NAME_INCOME_TYPE")["TARGET"].mean().plot.barh()
plt.title("INCOME_TYPE Vs Default \n")
plt.show()


# In[302]:


df.groupby("OCCUPATION_TYPE")["TARGET"].mean().plot.barh()
plt.title("OCCUPATION Vs Default \n")
plt.show()


# In[305]:


df.groupby("NAME_HOUSING_TYPE")["TARGET"].mean().plot.barh()
plt.title("House Type Vs Default \n")
plt.show()


# In[282]:


df.groupby("NAME_EDUCATION_TYPE")["TARGET"].mean().plot.bar()
plt.show()


# In[283]:


df.groupby("NAME_TYPE_SUITE")["TARGET"].mean().plot.bar()
plt.show()


# In[285]:


df["BIRTH_YEAR"] = round(df.DAYS_BIRTH/365,0)


# In[286]:


df.BIRTH_YEAR = df.BIRTH_YEAR.astype(int)


# In[287]:


df["Age_Group"] = pd.cut(df.BIRTH_YEAR,[0,20,30,40,50,60,9999],labels = ["<20","20-30","30-40","40-50","50-60","60+"])


# In[288]:


df.BIRTH_YEAR.describe()


# In[306]:


df.groupby("Age_Group")["TARGET"].mean().plot.barh()
plt.title("Age Groups Vs Default \n")
plt.show()


# In[ ]:




