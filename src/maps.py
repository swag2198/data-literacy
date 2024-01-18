"""
A helper file that contains dictionaries for mapping various attributes to their corresponding labels.
Also contains some useful constants that hold important column names.

"""

PERSONTYPE = 'PRPERTYP'
SEX = 'PESEX'
AGE = 'PRTAGE'
STATECODE = 'GESTFIPS'
SOCIALMEDIA = 'PESOCIAL'
TEXTING = 'PETEXTIM'
EMAIL = 'PEEMAIL'

StatesMap = {1: 'AL',
             30: 'MT',
             2: 'AK',
             31: 'NE',
             4: 'AZ',
             32: 'NV',
             5: 'AR',
             33: 'NH',
             6: 'CA',
             34: 'NJ',
             8: 'CO',
             35: 'NM',
             9: 'CT',
             36: 'NY',
             10: 'DE',
             37: 'NC',
             11: 'DC',
             38: 'ND',
             12: 'FL',
             39: 'OH',
             13: 'GA',
             40: 'OK',
             15: 'HI',
             41: 'OR',
             16: 'ID',
             42: 'PA',
             17: 'IL',
             44: 'RI',
             18: 'IN',
             45: 'SC',
             19: 'IA',
             46: 'SD',
             20: 'KS',
             47: 'TN',
             21: 'KY',
             48: 'TX',
             22: 'LA',
             49: 'UT',
             23: 'ME',
             50: 'VT',
             24: 'MD',
             51: 'VA',
             25: 'MA',
             53: 'WA',
             26: 'MI',
             54: 'WV',
             27: 'MN',
             55: 'WI',
             28: 'MS',
             56: 'WY',
             29: 'MO'}

RegionsMap = {'AK': 'West',
              'HI': 'West',
              'WA': 'West',
              'OR': 'West',
              'CA': 'West',
              'NV': 'West',
              'ID': 'West',
              'MT': 'West',
              'UT': 'West',
              'AZ': 'West',
              'CO': 'West',
              'WY': 'West',
              'NM': 'West',
              'ND': 'Midwest',
              'SD': 'Midwest',
              'NE': 'Midwest',
              'KS': 'Midwest',
              'MN': 'Midwest',
              'IA': 'Midwest',
              'MO': 'Midwest',
              'WI': 'Midwest',
              'IL': 'Midwest',
              'IN': 'Midwest',
              'MI': 'Midwest',
              'OH': 'Midwest',
              'TX': 'South',
              'OK': 'South',
              'AR': 'South',
              'LA': 'South',
              'MS': 'South',
              'AL': 'South',
              'TN': 'South',
              'KY': 'South',
              'WV': 'South',
              'VA': 'South',
              'MD': 'South',
              'DE': 'South',
              'DC': 'South',
              'NC': 'South',
              'SC': 'South',
              'GA': 'South',
              'FL': 'South',
              'PA': 'Northeast',
              'NJ': 'Northeast',
              'NY': 'Northeast',
              'CT': 'Northeast',
              'RI': 'Northeast',
              'MA': 'Northeast',
              'NH': 'Northeast',
              'VT': 'Northeast',
              'ME': 'Northeast'}


EducDTMap = {31 : "Less than 1st grade",
             32 : "1st-4th grade",
             33 : "5th-6th grade",
             34 : "7th-8th grade",
             35 : "9th grade",
             36 : "10th grade",
             37 : "11th grade",
             38 : "12th grade-no diploma",
             39 : "HS graduate, GED",
             40 : "Some college but no degree",
             41 : "Associate degree-occupational/vocational",
             42 : "Associate degree-academic program",
             43 : "Bachelor's degree",
             44 : "Master's degree",
             45 : "Professional school",
             46 : "Doctorate"}


AsianMap = {1: 'Asian Indian', 2: 'Chinese', 3: 'Filipino', 4: 'Japanese', 
            5: 'Korean', 6: 'Vietnamese', 7: 'Other'}

educ = {'LTHS': [31, 32, 33, 34, 35, 36, 37, 38], 
        'HS': [39],
        'SC': [40, 41, 42],
        'COLL': [43],
        'ADV': [44, 45, 46]}

race = {'White': [1], 
        'Black': [2, 6, 10, 11, 12, 16, 17, 18, 22, 23], 
        'Asian': [4, 5, 8, 9, 13, 14, 15, 19, 20, 21, 24], 
        'Other': [3, 7, 25, 26]}

hisp = [1, 2, 3, 4, 5, 6, 7, 8]

# Industry group of first job - Consistent industry groups for first job: Construction and mining (also includes agriculture and the like), Manufacturing, Trade, transportation, and utilties, Finance and business services (also includes Information and the like), Leisure and hospitality, and Public administration. 
ind = {'Construction and mining': [1, 2, 3],
        'Finance and business services': [7, 8, 9, 12],
        'Manufacturing': [4],
        'Trade, transportation, and utilities': [5, 6],
        'Education and health': [10],
        'Leisure and hospitality': [11],
        'Public administration': [13],
        'Armed forces': [14]}

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



