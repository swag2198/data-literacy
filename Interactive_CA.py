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

import sys 



# In[8]:


from src import maps


pd.set_option('display.max_columns', 100)
# plt.style.use('ggplot')


import tueplots
from tueplots import bundles

# this provides the color palette of Uni Tuebingen
from tueplots.constants.color import rgb
# e.g. as rgb.tue_blue, rgb.tue_red, etc.




# In[18]:


year = '2021'
CSV_FILE_PATH = 'https://www2.census.gov/programs-surveys/cps/datasets/2021/supp/nov21pub.csv'


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

CONCERNS_LABELS_FOR_PLOTS = {
    'HEPSCON1': 'Identity\ntheft',
    'HEPSCON2': 'Financial\nfraud',
    'HEPSCON3': 'Data\ncollection\nby online services',
    'HEPSCON4': 'Data\ncollection\nby government',
    'HEPSCON5': 'Credentials\nloss',
    'HEPSCON6': 'Harassment',
    'HEPSCON8': 'Other\nconcerns'
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

ACTIVITY_LABELS_FOR_PLOTS = {
    'HEPSPRE1': 'Financial\ntransactions\nonline',
    'HEPSPRE2': 'Buying goods\nor services\nonline',
    'HEPSPRE3': 'Posting\nphotos/status\nupdates',
    'HEPSPRE4': 'Opinion on\ncontroversial\nissues',
    'HEPSPRE5': 'Using web\nsearch\nengines'
 
}

CONCERNS = list(CONCERNS_MAP.keys())
ACTIVITIES = list(ACTIVITIES_MAP.keys())



DROP_COLUMNS = [
    'FILLER',  # all rows have NaN values for some reason
]


# In[20]:

@st.cache_resource
def download_dataset():
    df21 = pd.read_csv(CSV_FILE_PATH)
    df21 = df21[(df21[AGE] >= 10) * (df21[SEX] != -1)]
    df21 = df21.drop(DROP_COLUMNS, axis=1)
    return df21

df21 = download_dataset()

columns = features = df21.columns.to_list()


# In[21]:


query_string1 = ' or '.join([f'{item} == 1' for item in [f'HEPSCON{i}' for i in [1,2,3,4,5,6,8]]]) #concerns
query_string2 = ' or '.join([f'{item} == 1' for item in [f'HEPSPRE{i}' for i in [1,2,3,4,5]]])     #activities



cybercrime = df21.query('HEPSCYBA != -1')[[CYBERCRIME, SEX]]
count_sex = cybercrime.value_counts().reset_index()

def crime_plot():
    xpos = ['YES', 'NO']
    male_yn = [count_sex.query('PESEX == 1 and HEPSCYBA == 1')['count'].iloc[0],
            count_sex.query('PESEX == 1 and HEPSCYBA == 2')['count'].iloc[0]
            ]
    female_yn = [count_sex.query('PESEX == 2 and HEPSCYBA == 1')['count'].iloc[0],
            count_sex.query('PESEX == 2 and HEPSCYBA == 2')['count'].iloc[0]
            ]

    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False),
                        **tueplots.axes.lines()
                        }):
        
        fig, ax = plt.subplots()
        b = ax.bar(xpos, male_yn, color=rgb.tue_blue, ec="black", width=0.65, label="Males")
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center")
        
        b = ax.bar(xpos, female_yn, bottom=male_yn, color=rgb.tue_red, ec="black", width=0.65, label= "Females")
        ax.bar_label(b, padding=0, color = 'w', fontsize = 'small', label_type="center")
        
        total = np.array(male_yn) + np.array(female_yn)
        for i, p in enumerate(total):
            ax.text(xpos[i], total[i]+1500, f"{total[i]}", ha='center', fontsize='small')
        
        
        ax.grid(True, color = "lightgrey", ls = ":")
        ax.set_xlabel("Affected by an online security breach,\nidentity theft, or a similar crime?")
        ax.legend(loc = 'upper left', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.set_ylabel("Number of responders")
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)

        return fig



sort_dict = lambda x: dict(sorted(x.items(), key=lambda item: -item[1]))

concerns_size = sort_dict({concern: df21.query(f'{concern} == 1').shape[0] for concern in CONCERNS})
activities_size = sort_dict({activity: df21.query(f'{activity} == 1').shape[0] for activity in ACTIVITIES})

def distribution_concerns():
    # xpos = np.arange(len(activities_size))
    xpos = concerns_size.keys()
    xpos = [CONCERNS_LABELS_FOR_PLOTS[item] for item in xpos]
    counts_concern = list(concerns_size.values())

    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        b = ax.bar(xpos, counts_concern, color=rgb.tue_blue, ec="black", width=0.69)#, label="Responded Yes")
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center")
        
        pcts = np.array(counts_concern) / df21.shape[0]
        for i, p in enumerate(pcts):
            ax.text(xpos[i], counts_concern[i]+500, f"{p*100:.2f}%", ha='center', fontsize='small')
        
        ax.grid(True, color = "lightgrey", ls = ":")
        ax.set_xlabel("Prevalent digital concerns in the US population")
        # ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.set_ylabel("Number of\nyes responders")
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        
        return fig
    
def distribution_activities():
    # xpos = np.arange(len(activities_size))
    xpos = activities_size.keys()
    xpos = [ACTIVITY_LABELS_FOR_PLOTS[item] for item in xpos]
    counts_concern = list(activities_size.values())

    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        b = ax.bar(xpos, counts_concern, color=rgb.tue_blue, ec="black", width=0.65)#, label="Responded Yes")
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center")
        
        b1 = ax.bar([xpos[3]], [counts_concern[3]], color=rgb.tue_violet, ec='black', width=0.65)
        ax.bar_label(b1, padding=0, color='w', fontsize='small', label_type="center")
        
        b1 = ax.bar([xpos[0]], [counts_concern[0]], color=rgb.tue_lightblue, ec='black', width=0.65)
        ax.bar_label(b1, padding=0, color='w', fontsize='small', label_type="center")
        
        pcts = np.array(counts_concern) / df21.shape[0]
        for i, p in enumerate(pcts):
            ax.text(xpos[i], counts_concern[i]+250, f"{p*100:.2f}%", ha='center', fontsize='small')
        
        ax.grid(True, color = "lightgrey", ls = ":")
        ax.set_xlabel("Online activities that people hesitate to do")
        # ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.set_ylabel("Number of\nyes responders")
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        plt.savefig(f"../res/figures/activity_distribution_{year}.pdf")

        return fig
    





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


# In[38]:


def fourBars(selected_options,divide_by,graph_labels):

    #selected_options = [index values of the concerns/activities]
    #divide_by = [key, group],eg:['HRINCOME',income_groups]
    #graph_labels = [legend of bar1....n, Title of the plot]

        # call
    res_act, sample_sizes_act = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=ACTIVITIES)
    
    res_con, sample_sizes_con = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=CONCERNS)
    


    xpos = list(res_act.keys())
    X = np.arange(len(xpos))

    problem_list = []

    for option in selected_options:

        if option <=4:
            fins = np.array([res_act[key][option] for key in xpos])
            fins = np.around(fins,4)
            fins_no = [round(res_act[key][option]*sample_sizes_act[key][option]) for key in xpos]
            problem_list.append(fins)
        
        else:
            fins = np.array([res_con[key][option-5] for key in xpos])
            fins = np.around(fins,4)
            fins_no = [round(res_con[key][option-5]*sample_sizes_con[key][option-5]) for key in xpos]
            problem_list.append(fins)

    # X, xpos, opin


    with plt.rc_context({**bundles.icml2022(column='full', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()

        #colors for the bars:
        colors = [rgb.tue_lightblue, rgb.tue_violet, rgb.tue_lightgreen]
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        # Add grid and axis labels
        ax.grid(True, color = "lightgrey", ls = ":")
        
        # We specify the width of the bar
        width = 1.0/(len(selected_options)+1)
        current_width = 0

        bars_list = []

        for i in range(len(problem_list)):
            bars_list.append(
                ax.bar(
                X+current_width, 
                problem_list[i], 
                ec = "black", 
                lw = .75,
                color = colors[i],
                zorder = 3, 
                width = width,
                label = graph_labels[i],
                )
            )
            current_width += width
            ax.bar_label(bars_list[-1], padding=0, color = 'w', fontsize=10, label_type="center", rotation=90)

        
        # Adjust ticks
        xticks_ = ax.xaxis.set_ticks(
            ticks = X + (width/(2))*(len(selected_options)-1), #DONE
            labels = xpos,
            rotation = 15,
            fontsize=8
        )

        ax.set_xlabel(graph_labels[-1], fontsize=10)
        ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none',)
        ax.legend(
            ncol = 2, 
            loc = "upper right", 
            framealpha=1.0, facecolor='white', edgecolor='none',
            fontsize=10,
            bbox_to_anchor = (0.95, 1.2),
            # frameon = False
        )

        ax.set_ylabel("Probability of responding yes\ngiven a person belongs\nto a certain group", fontsize=10)

        return fig
# In[48]:



attribute_to_group = {

    "Income :moneybag:" : ['HEFAMINC', income_groups, 'Income groups in the population'],
    "Education :female-student:" : ['PEEDUCA', education_groups, 'Education levels in the population'],
    "Age :man-boy:" : ['PRTAGE', age_groups, 'Age groups in the population'],
    
}

activity_index= {
    'Financial transactions' : 0,
    'Online shopping' : 1,
    'Posting photos, status updates' : 2,
    'Expressing controversial opinions' : 3,
    'Searching on google, yahoo, bing' : 4,
    'Identity theft' : 5, #0
    'Credit card fraud': 6, #1
    'Data tracking': 7, #2
    'Govt. data collection': 8, #3
    'Losing digital credentials': 9, #4
    'Cyber harrassment': 10, #5

}



def generate_graph(selected_options, stratify_by):

  
    selected_indices = []
    divide_by = attribute_to_group[stratify_by]



    for option in selected_options:
        selected_indices.append(activity_index[option])

    



    
    #CODE: divide_by, graph_label
        #CODE: Handle Concerns in function: fourBars
    
    st.pyplot(fourBars(selected_indices,divide_by=divide_by,graph_labels=selected_options+[divide_by[-1]]))  

    
   


# In[49]:


# Streamlit app
def main():
    
    

    options = st.multiselect(
    'Select online concerns and activities to show:',
    ['Financial transactions', 'Online shopping', 'Posting photos, status updates', 
     'Expressing controversial opinions','Searching on google, yahoo, bing',
     'Identity theft','Credit card fraud', 'Data tracking','Govt. data collection',
     'Losing digital credentials','Cyber harrassment',],
     max_selections=3)
    
    with st.sidebar:
    
        stratify_by = st.radio(
        "Stratify by:",
        ["Income :moneybag:", "Education :female-student:", "Age :man-boy:"],
        
        )

    if len(options)!=0 and stratify_by!=None:
        generate_graph(options, stratify_by)

    else:
        pass
    

if __name__ == '__main__':
    main()


# In[ ]:




