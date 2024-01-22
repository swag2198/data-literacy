#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os, re, json, requests
import PyPDF2
import urllib.request
from bs4 import BeautifulSoup
from scipy import stats


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import sys; sys.path.append('../')  # to import src


# In[8]:


from src import maps

pd.set_option('display.max_columns', 100)
# plt.style.use('ggplot')


# In[17]:


DATA_DIR = os.path.join('..', 'dat')


# In[18]:


year = '2021'
CSV_FILE_PATH = os.path.join(DATA_DIR, os.path.join(year, f'nov{year[2:]}pub.csv'))


# In[19]:


PERSONTYPE = 'PRPERTYP'
SEX = 'PESEX'
AGE = 'PRTAGE'
STATECODE = 'GESTFIPS'
SOCIALMEDIA = 'PESOCIAL'
TEXTING = 'PETEXTIM'
EMAIL = 'PEEMAIL'

# During the past year, (have you/has any member of your household) been affected by an
# online security breach, identity theft, or a similar crime?
CYBERCRIME='HEPSCYBA'


#what concerns (you/members of this household) the most when it comes to online privacy and security risks?
CONCERNS_MAP = {
    'HEPSCON1': 'Identity theft',
    'HEPSCON2': 'Credit card or banking fraud',
    'HEPSCON3': 'Data collection or tracking by online services',
    'HEPSCON4': 'Data collection or tracking by government',
    'HEPSCON5': 'Loss of control over personal data such as email or social network profiles',
    'HEPSCON6': 'Threats to personal safety, such as online harassment, stalking, or cyberbullying',
    'HEPSCON8': 'Other concerns'
}

# During the past year, have concerns about privacy or security STOPPED (you/anyone in this household)
# from doing any of these activities online
ACTIVITIES_MAP = {
    'HEPSPRE1': 'Conducting financial transactions such as banking, investing, or paying bills online?',
    'HEPSPRE2': 'Buying goods or services online?',
    'HEPSPRE3': 'Posting photos, status updates, or other information on social networks?',
    'HEPSPRE4': 'Expressing an opinion on a controversial or political issue on a blog or social network, or in a forum, email or any other venue?',
    'HEPSPRE5': 'Searching for information using a platform such as Google Search, Yahoo Search, Microsoft Bing, or another web search engine?'
}

CONCERNS = list(CONCERNS_MAP.keys())
ACTIVITIES = list(ACTIVITIES_MAP.keys())


DROP_COLUMNS = [
    'FILLER',  # all rows have NaN values for some reason
]


# In[20]:

@st.cache_resource
def process_dataframe():
    df21 = pd.read_csv(CSV_FILE_PATH)
    df21 = df21[(df21[AGE] >= 10) * (df21[SEX] != -1)]
    df21 = df21.drop(DROP_COLUMNS, axis=1)
    return df21

df21 = process_dataframe()

columns = features = df21.columns.to_list()


# In[21]:


query_string1 = ' or '.join([f'{item} == 1' for item in [f'HEPSCON{i}' for i in [1,2,3,4,5,6,8]]]) #concerns
query_string2 = ' or '.join([f'{item} == 1' for item in [f'HEPSPRE{i}' for i in [1,2,3,4,5]]])     #activities


# In[37]:


columnsmapa= {
    'HEPSPRE1': 'Financial transactions',
    'HEPSPRE2': 'Online shopping',
    'HEPSPRE3': 'Posting photos, status updates',
    'HEPSPRE4': 'Expressing controversial opinions',
    'HEPSPRE5': 'Searching on google, yahoo, bing'
}

columnsmapc = {
    'HEPSCON1': 'Identity theft',
    'HEPSCON2': 'Credit card fraus',
    'HEPSCON3': 'Data tracking',
    'HEPSCON4': 'Govt. data collection',
    'HEPSCON5': 'Losing digital credentials',
    'HEPSCON6': 'Cyber harrassment',
    'HEPSCON8': 'Other'
}

# poverty guidelines: https://aspe.hhs.gov/2021-poverty-guidelines
income_groups = {
    "below 35k": [1,2,3,4,5,6,7,8,9],
    "35k-60k": [10,11,12], #13],
    "60k-100k": [13, 14],
    "100k-150k": [15],
    "above 150k": [16]
}

age_groups = {
    '10-18':    [10, 18],
    '18-25':    [18, 25],
    '26-35':    [26, 35],
    '36-45':    [36, 45],
    '46-55':    [46, 55],
    '56-65':    [56, 65],
    '66+':      [66, 120],
}

education_groups = maps.educ  # education_educationid_mapping
industry_groups = maps.ind    # industry_jobid_mapping


# In[38]:


def stratified_proportions(df,
                           stratify_by,      # age, income, education or job industry
                           categories_dict,  # mapping of age groups etc. as shown above
                           target_variables, # list of concerns/activities
                          ):
    
    # for each group, stores the probability of responding "YES" for each target variable
    stratified_output_count_normalized = {}
    sample_sizes = {}
    
    
    v = stratify_by
    for groupname, groupids in categories_dict.items():
        if v != 'PRTAGE':
            query_string = ' or '.join([f'{v} == {gid}' for gid in groupids])
        else:
            query_string = f'{v} >= {groupids[0]} and {v} <= {groupids[1]}'
        # print(groupname)
        _df = df.query(query_string)[target_variables]
        
        props = []  # props[i] = proportion for target variable i
        sample_size = []
        for tv in target_variables:
            # Take 1 target variable and find the proportion of people who responded as 1 (yes)
            _df1 = _df[[tv]]
            _df1 = _df1[_df1[tv] != -1]  # remove the -1 responses (only keep 1 or 2)
#             print(f'total #samples in this group for {tv} (Yes/No) = {_df1.shape[0]}')
#             print(f'yes: {_df1.value_counts()[1]}, no: {_df1.value_counts()[2]}; proportion: {_df1.value_counts(normalize=True)[1]:.4f}')
            props.append(_df1.value_counts(normalize=True)[1])
            sample_size.append(_df1.shape[0])
        
        stratified_output_count_normalized[groupname] = props
        sample_sizes[groupname] = sample_size
        
    return stratified_output_count_normalized, sample_sizes

# In[48]:


activities_graph_functions = {
    'People affected by cyber crime' : 'HEPSCYBA',
    'What people hesitate to do stratified by annual income levels' : 'HEFAMINC',
    'What people hesitate to do stratified by education groups' : 'PEEDUCA',
    'What people hesitate to do stratified by age' : 'PRTAGE'
    
}

concerns_graph_functions = {
    'What are people concerned about stratified by annual income levels' : 'HEFAMINC',
    'What are people concerned about stratified by education groups' : 'PEEDUCA',
    'What are people concerned about stratified by age' : 'PRTAGE'
}

attribute_to_group = {
    'PEEDUCA' : education_groups,
    'HEFAMINC' : income_groups,
    'PRTAGE' : age_groups
    
}

activities_graph_functions = {
    'People affected by cyber crime' : 'HEPSCYBA',
    'What people hesitate to do stratified by annual income levels' : 'HEFAMINC',
    'What people hesitate to do stratified by education groups' : 'PEEDUCA',
    'What people hesitate to do stratified by age' : 'PRTAGE'
    
}

concerns_graph_functions = {
    'What are people concerned about stratified by annual income levels' : 'HEFAMINC',
    'What are people concerned about stratified by education groups' : 'PEEDUCA',
    'What are people concerned about stratified by age' : 'PRTAGE'
}

attribute_to_group = {
    'PEEDUCA' : education_groups,
    'HEFAMINC' : income_groups,
    'PRTAGE' : age_groups
    
}


def generate_graph(selected_option):
    
    if selected_option in activities_graph_functions or selected_option in concerns_graph_functions:
        
        if selected_option == 'People affected by cyber crime' : 
    
            df21.query('HEPSCYBA != -1')[CYBERCRIME].value_counts().plot(kind='bar')
            st.pyplot(plt)
            
        else :
            
            if selected_option in activities_graph_functions:
            
                attribute = activities_graph_functions[selected_option]
                target_var = ACTIVITIES
                column_names = {
                    0: 'financial transactions',
                    1: 'online shopping',
                    2: 'posting photos, status updates',
                    3: 'expressing controversial opinions',
                    4: 'searching on google, yahoo, bing'
                }
            
            else:
                
                attribute = concerns_graph_functions[selected_option]
                target_var = CONCERNS
                column_names = {
                    0: 'Identity theft',
                    1: 'Credit card or banking fraud',
                    2: 'Data collection or tracking by online services',
                    3: 'Data collection or tracking by government',
                    4: 'Loss of control over personal data',
                    5: 'Online threats/cyberbullying',
                    6: 'Other concerns',
                }
                
            #Common code here:
            attribute_group = attribute_to_group[attribute]
            res, sample_sizes = stratified_proportions(df21, stratify_by=attribute,
                                         categories_dict=attribute_group,
                                         target_variables=target_var)

            df = pd.DataFrame.from_dict(res, orient='index')
            df = df.rename(columns= column_names)



            # Plot the DataFrame
            ax = df.plot(kind='bar')
            ax.set_title(selected_option, color='black')
            ax.legend(bbox_to_anchor=(1.0, 1.0))
            ax.plot()
            
            st.pyplot(plt)
            
        
        
    else:
        st.error("Invalid option")
            
    


# In[49]:


# Streamlit app
def main():
    
    
    # Sidebar options
    sidebar_option = st.sidebar.selectbox("Select an option:", ['Concerns', 'Activities'])
    
    if sidebar_option == 'Activities' : 
        st.title('Online Activities')
        # Dropdown for selecting activities
        selected_option = st.selectbox('Select an option:', list(activities_graph_functions.keys()))
        # Generate and display the graph based on the selected option
        generate_graph(selected_option)
        
        
    elif sidebar_option == 'Concerns' : 
        st.title('Online Concerns')
        # Dropdown for selecting activities
        selected_option = st.selectbox('Select an option:', list(concerns_graph_functions.keys()))    
        # Generate and display the graph based on the selected option
        generate_graph(selected_option)
        
    
    else:
        st.error("Invalid option")

if __name__ == '__main__':
    main()


# In[ ]:




