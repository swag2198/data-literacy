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

sys.path.append('../')

#sys.path.append('../')  # to import src

# In[8]:


from src import maps


pd.set_option('display.max_columns', 100)
# plt.style.use('ggplot')


import tueplots
from tueplots import bundles

# this provides the color palette of Uni Tuebingen
from tueplots.constants.color import rgb
# e.g. as rgb.tue_blue, rgb.tue_red, etc.


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

def finTrans_contrOpinion(divide_by,graph_label):

        # call
    res, sample_sizes = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=ACTIVITIES)

    xpos = list(res.keys())
    X = np.arange(len(xpos))

    fins = np.array([res[key][0] for key in xpos])
    fins = np.around(fins,4)
    fins_no = [round(res[key][0]*sample_sizes[key][0]) for key in xpos]

    opin = np.array([res[key][3] for key in xpos])
    opin = np.around(opin,4)

    opin_no = [round(res[key][3]*sample_sizes[key][3]) for key in xpos]

    # X, xpos, opin


    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        # Add grid and axis labels
        ax.grid(True, color = "lightgrey", ls = ":")
        
        # We specify the width of the bar
        width = 0.35
        
        # Fouls conceded
        b = ax.bar(
            X, 
            fins, 
            ec = "black", 
            lw = .75,
            color = rgb.tue_lightblue, 
            zorder = 3, 
            width = width,
            label = "financial transactions"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)

        b = ax.bar(
            X + width, 
            opin, 
            ec = "black", 
            lw = .75, 
            color = rgb.tue_violet, 
            zorder = 3, 
            width = width,
            label = "controversial opinions"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)
        
        
        # Adjust ticks
        xticks_ = ax.xaxis.set_ticks(
            ticks = X + width/2,
            labels = xpos,
            rotation = 15
        )
        
        ax.set_xlabel(graph_label)
        ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.legend(
            ncol = 2, 
            loc = "upper right", 
            framealpha=1.0, facecolor='white', edgecolor='none',
            
            bbox_to_anchor = (0.95, 1.2),
            # frameon = False
        )
        ax.set_ylabel("Probability of responding yes\ngiven a person belongs\nto a certain group")
        
        # plt.savefig(f"../res/figures/income_bar_{year}.pdf")
        return fig
    
def onlineShop_postingPics(divide_by,graph_label):
        # call
    res, sample_sizes = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=ACTIVITIES)

    xpos = list(res.keys())
    X = np.arange(len(xpos))

    online_shopping = np.array([res[key][1] for key in xpos])
    online_shopping = np.around(online_shopping,4)
    online_shopping_no = [round(res[key][1]*sample_sizes[key][1]) for key in xpos]

    post_photo = np.array([res[key][2] for key in xpos])
    post_photo = np.around(post_photo,4)

    post_photo_no = [round(res[key][2]*sample_sizes[key][2]) for key in xpos]

    # X, xpos, post_photo


    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        # Add grid and axis labels
        ax.grid(True, color = "lightgrey", ls = ":")
        
        # We specify the width of the bar
        width = 0.35
        
        # Fouls conceded
        b = ax.bar(
            X, 
            online_shopping, 
            ec = "black", 
            lw = .75,
            color = rgb.tue_lightblue, 
            zorder = 3, 
            width = width,
            label = "Online shpping"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)

        b = ax.bar(
            X + width, 
            post_photo, 
            ec = "black", 
            lw = .75, 
            color = rgb.tue_violet, 
            zorder = 3, 
            width = width,
            label = "Posting photos"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)
        
        
        # Adjust ticks
        xticks_ = ax.xaxis.set_ticks(
            ticks = X + width/2,
            labels = xpos,
            rotation = 15
        )
        
        ax.set_xlabel(graph_label)
        ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.legend(
            ncol = 2, 
            loc = "upper right", 
            framealpha=1.0, facecolor='white', edgecolor='none',
            
            bbox_to_anchor = (0.95, 1.2),
            # frameon = False
        )
        ax.set_ylabel("Probability of responding yes\ngiven a person belongs\nto a certain group")
        
        # plt.savefig(f"../res/figures/income_bar_{year}.pdf")
        return fig
    
def dataTr_govtColl(divide_by,graph_label):
        # call
    res, sample_sizes = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=CONCERNS)

    xpos = list(res.keys())
    X = np.arange(len(xpos))

    data_tracking = np.array([res[key][2] for key in xpos])
    data_tracking = np.around(data_tracking,4)
    data_tracking_no = [round(res[key][2]*sample_sizes[key][2]) for key in xpos]

    gov_data = np.array([res[key][3] for key in xpos])
    gov_data = np.around(gov_data,4)

    gov_data_no = [round(res[key][3]*sample_sizes[key][3]) for key in xpos]

    # X, xpos, gov_data


    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        # Add grid and axis labels
        ax.grid(True, color = "lightgrey", ls = ":")
        
        # We specify the width of the bar
        width = 0.35
        
        # Fouls conceded
        b = ax.bar(
            X, 
            data_tracking, 
            ec = "black", 
            lw = .75,
            color = rgb.tue_lightblue, 
            zorder = 3, 
            width = width,
            label = "Data tracking"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)

        b = ax.bar(
            X + width, 
            gov_data, 
            ec = "black", 
            lw = .75, 
            color = rgb.tue_violet, 
            zorder = 3, 
            width = width,
            label = "Govt. data collection"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)
        
        
        # Adjust ticks
        xticks_ = ax.xaxis.set_ticks(
            ticks = X + width/2,
            labels = xpos,
            rotation = 15
        )
        
        ax.set_xlabel(graph_label)
        ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.legend(
            ncol = 2, 
            loc = "upper right", 
            framealpha=1.0, facecolor='white', edgecolor='none',
            
            bbox_to_anchor = (0.95, 1.2),
            # frameon = False
        )
        ax.set_ylabel("Probability of responding yes\ngiven a person belongs\nto a certain group")
        
        # plt.savefig(f"../res/figures/income_bar_{year}.pdf")
        return fig
    
def idTheft_cyberHarr(divide_by,graph_label):
        # call
    res, sample_sizes = stratified_proportions(df21, stratify_by=divide_by[0],
                                categories_dict=divide_by[1],
                                target_variables=CONCERNS)

    xpos = list(res.keys())
    X = np.arange(len(xpos))

    identity_theft = np.array([res[key][0] for key in xpos])
    identity_theft = np.around(identity_theft,3)
    identity_theft_no = [round(res[key][0]*sample_sizes[key][0]) for key in xpos]

    cyber_harras = np.array([res[key][5] for key in xpos])
    cyber_harras = np.around(cyber_harras,3)

    cyber_harras_no = [round(res[key][5]*sample_sizes[key][5]) for key in xpos]

    # X, xpos, cyber_harras


    with plt.rc_context({**bundles.icml2022(column='half', nrows=1, ncols=1, usetex=False), **tueplots.axes.lines()}):
        fig, ax = plt.subplots()
        
        # Add spines
        ax.spines["top"].set(visible = False)
        ax.spines["right"].set(visible = False)
        
        # Add grid and axis labels
        ax.grid(True, color = "lightgrey", ls = ":")
        
        # We specify the width of the bar
        width = 0.35
        
        # Fouls conceded
        b = ax.bar(
            X, 
            identity_theft, 
            ec = "black", 
            lw = .75,
            color = rgb.tue_lightblue, 
            zorder = 3, 
            width = width,
            label = "Identity theft"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)

        b = ax.bar(
            X + width, 
            cyber_harras, 
            ec = "black", 
            lw = .75, 
            color = rgb.tue_violet, 
            zorder = 3, 
            width = width,
            label = "Cyber harrassment"
        )
        ax.bar_label(b, padding=0, color = 'w', fontsize='small', label_type="center", rotation=90)
        
        
        # Adjust ticks
        xticks_ = ax.xaxis.set_ticks(
            ticks = X + width/2,
            labels = xpos,
            rotation = 15
        )
        
        ax.set_xlabel(graph_label)
        ax.legend(loc = 'upper right', framealpha=1.0, facecolor='white', edgecolor='none')
        ax.legend(
            ncol = 2, 
            loc = "upper right", 
            framealpha=1.0, facecolor='white', edgecolor='none',
            
            bbox_to_anchor = (0.95, 1.2),
            # frameon = False
        )
        ax.set_ylabel("Probability of responding yes\ngiven a person belongs\nto a certain group")
        
        # plt.savefig(f"../res/figures/income_bar_{year}.pdf")
        return fig
# In[48]:


activities_graph_functions = {
    'People affected by cyber crime' : 'HEPSCYBA',
    'Finanical transactions and Controversial opinions: Annual income levels' : 'HEFAMINC',
    'Finanical transactions and Controversial opinions: Education groups' : 'PEEDUCA',
    'Finanical transactions and Controversial opinions: Age' : 'PRTAGE',
    'Online shopping and Posting photos: Annual income levels' : 'HEFAMINC',
    'Online shopping and Posting photos: Education groups' : 'PEEDUCA',
    'Online shopping and Posting photos: Age' : 'PRTAGE'
}

concerns_graph_functions = {
    'Data tracking and Govt. data collection: Annual income levels' : 'HEFAMINC',
    'Data tracking and Govt. data collection: Education groups' : 'PEEDUCA',
    'Data tracking and Govt. data collection: Age groups' : 'PRTAGE',
    'Identity theft and Cyber harrassment: Annual income levels' :  'HEFAMINC',
    'Identity theft and Cyber harrassment: Education groups' : 'PEEDUCA',
    'Identity theft and Cyber harrassment: Age groups' : 'PRTAGE',
}

attribute_to_group = {
    'PEEDUCA' : education_groups,
    'HEFAMINC' : income_groups,
    'PRTAGE' : age_groups
    
}


def generate_graph(selected_option):
    
    if selected_option in activities_graph_functions or selected_option in concerns_graph_functions:
        
        if selected_option == 'People affected by cyber crime' : 
            
            
            st.pyplot(crime_plot())
            
        elif selected_option == 'Finanical transactions and Controversial opinions: Annual income levels':
            divide_by = ['HEFAMINC', income_groups]
            graph_label='Income groups in the population'
            st.pyplot(finTrans_contrOpinion(divide_by,graph_label))

        elif selected_option == 'Finanical transactions and Controversial opinions: Education groups':
            divide_by = ['PEEDUCA', education_groups]
            graph_label='Education levels in the population'
            st.pyplot(finTrans_contrOpinion(divide_by,graph_label))

        elif selected_option == 'Finanical transactions and Controversial opinions: Age':
            divide_by = ['PRTAGE', age_groups]
            graph_label='Age groups in the population'
            st.pyplot(finTrans_contrOpinion(divide_by,graph_label))

        elif selected_option == 'Online shopping and Posting photos: Annual income levels':
            divide_by = ['HEFAMINC', income_groups]
            graph_label='Income groups in the population'
            st.pyplot(onlineShop_postingPics(divide_by,graph_label))

        elif selected_option == 'Online shopping and Posting photos: Education groups':
            divide_by = ['PEEDUCA', education_groups]
            graph_label='Education levels in the population'
            st.pyplot(onlineShop_postingPics(divide_by,graph_label))

        elif selected_option == 'Online shopping and Posting photos: Age':
            divide_by = ['PRTAGE', age_groups]
            graph_label='Age groups in the population'
            st.pyplot(onlineShop_postingPics(divide_by,graph_label))

        elif selected_option == 'Data tracking and Govt. data collection: Annual income levels':
            divide_by = ['HEFAMINC', income_groups]
            graph_label='Income groups in the population'
            st.pyplot(dataTr_govtColl(divide_by,graph_label))

        elif selected_option == 'Data tracking and Govt. data collection: Education groups':
            divide_by = ['PEEDUCA', education_groups]
            graph_label='Education levels in the population'
            st.pyplot(dataTr_govtColl(divide_by,graph_label))

        elif selected_option == 'Data tracking and Govt. data collection: Age groups':
            divide_by = ['PRTAGE', age_groups]
            graph_label='Age groups in the population'
            st.pyplot(dataTr_govtColl(divide_by,graph_label))

        elif selected_option == 'Identity theft and Cyber harrassment: Annual income levels':
            divide_by = ['HEFAMINC', income_groups]
            graph_label='Income groups in the population'
            st.pyplot(idTheft_cyberHarr(divide_by,graph_label))

        elif selected_option == 'Identity theft and Cyber harrassment: Education groups':
            divide_by = ['PEEDUCA', education_groups]
            graph_label='Education levels in the population'
            st.pyplot(idTheft_cyberHarr(divide_by,graph_label))
    
        elif selected_option == 'Identity theft and Cyber harrassment: Age groups':
            divide_by = ['PRTAGE', age_groups]
            graph_label='Age groups in the population'
            st.pyplot(idTheft_cyberHarr(divide_by,graph_label))

        else:
            st.write("Invalid")
            
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




