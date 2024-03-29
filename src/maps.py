"""
A helper file that contains dictionaries for mapping various attributes to their corresponding labels.
Also contains some useful constants that hold important column names.

"""

from tueplots.constants.color import rgb

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

ACTIVITIES_MAP_SHORT = {
    'HEPSPRE1': 'Financial transactions',
    'HEPSPRE2': 'E-commerce',
    'HEPSPRE3': 'Posting photos / other information on social networks?',
    'HEPSPRE4': 'Expressing an opinion',
    'HEPSPRE5': 'Searching for information using a platform such as Google Search, Yahoo Search, Microsoft Bing, or another web search engine?'
}

feat_dict = {
    
    'HEPSPRE1' : 
    
    {
        'HENOHM8' : 'Safety',
        'PUBUSCK2' : 'Work', # Family business realted
        'PULAYCK1' : 'Work', #NOTE: Some work related thing, layoff related (I checked similar prefixes)
        'PEDWLKO' : 'Work', # Did you look for work in the last 12 months
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'PEPDEMP2' : 'Work', # Usually paid employees?
        'HUBUSL3' : 'Work', #Have a business or a farm
        'HEEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'HEHOMTE3' : 'Digital access', #Using internet via dial-up?
        'PELAYDUR' : 'Work', #Layoff period
        'HENOTV3' : 'Financial', #No subscription to TV channels service, why? -> Can't afford it
        'HEHNETST' : 'Financial', # Temporarily lose internet access due to non-payment
        'HETRADTV' : 'Digital access', #Cable TV/Satellite TV
        'HXTVBOX' : 'Digital access', #Smart TV/Game system (XBOX, etc)
        'PXMPHONE' : 'Digital access', #Who uses a cellular phone or smartphone?
        'PXMLR' : 'Work', #Major Labor Force Recode
        'HEDEVSTA' : 'Digital access', #How often is internet inaccessible?
        'PXNETCK2' : 'Digital access', #Who uses internet from any location, for any purpose.
        'HENOTV10' : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        'PXWEARAB' : 'Digital access', #Who uses a wearable Internet-connected device such as a smart watch or glasses?
    
    },
    
    'HEPSPRE2':
    {
        'HEHOMTE3' : 'Digital access', #Using internet via dial-up?
        'HEPRINOH' : 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'HXTENURE' : 'House', #Owned or rented house
        'HXHNETQL' : 'Digital access', #Access the Internet from their homes, other than a mobile data plan.
        'HXPSCON1' : 'Safety', #Identity theft concern
        'PXERNPER' : 'Work', #Periodicity of earnings
        'PUDWCK5' : 'Work', #Passive job seekers
        'HENOTV11' : 'Digital access', #Do dot subscibe to TV due to poor quality
        'HEEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'PXLKM1' : 'Work', #What all have you done to find work in the last 4 weeks?
        'PXHSPNON': 'Demographic', #Hispanic?
        'HEINSCHL' : 'Digital access', #Use internet at school?
        'HENOTV8' : 'Digital access' , #Do dot subscibe to TV due not having a TV or broken TV
        'HEDEVSTA' : 'Digital access', #How often is internet inaccessible?
        'HXINWORK' : 'Digital access', #Use internet at work?
        'HENOHM3' : 'Financial', #Don't use intenet at home? ->Not worth the cost
        'PXINSCHL' : 'Digital access', #Use internet at school(again-> Look HEINSCHL)
        'PXNETCK2' : 'Digital access', #Who uses internet from any location, for any purpose.
        'PRHERNAL': 'Financial', # HOURLY EARNINGS
        
    },
    
    'HEPSPRE3' : 
    {
        
        'HXEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'PREXPLF' : 'Work', #EXPERIENCED LABOR FORCE EMPLOYMENT
        'HXPRINOH' : 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'HXTENURE' : 'House', #Owned or rented house
        'HENOHM5' : 'Digital access', #Do not use the internet at home? ->No computing device, or device inadequate or broken
        'PRDTCOW2' : 'Work', #DETAILED CLASS OF WORKER RECODE - JOB 2
        'PXDWLKO' : 'Work', #Did you look for work at any time in the last 12 months?
        'HEHOMTE3' : 'Digital access', #Using internet via dial-up?
        'HEPRINOH' : 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'HXHNETQL' : 'Digital access', #Access the Internet from their homes, other than a mobile data plan.
        'PXINOTHR' : 'Digital access', #Who uses internet at other places not covered in the survey
        'HENOHM4' : 'Digital access', #Dont use internet at home -> Can use it elsewhere
        'HXLOPRCE' : 'Financial', #At what price would you buy home internet service
        'HXINHOME' : 'Digital access', #Use internet at home?
        'BUSL1' : 'Financial', #
        'PXMPHONE' : 'Digital access', #Who uses a cellular phone or smartphone?
        'HEINSCHL' : 'Digital access', #Use internet at school?
        'HEDEVSTA' : 'Digital access', #How often is internet inaccessible?
        'PXINELHO': 'Digital access', # Who uses the Internet at someone else's home? 
        'HUBUSL2'  : 'Financial', # Have a business or a farm
        
    },

    'HEPSPRE4': {
        "PXMLR"    : 'Work', #Major Labor Force Recode
        "HENOHM10" : 'Online activities', # reason for not using internet at home - some other reason
        "HXPRINOH" : 'Online activities', # reason for not using internet at home - most important reason
        "HXNOHM1"  : 'Online activities', # # reason for not using internet at home - don't need it
        "HEPSCYBA" : 'Safety', #Affected by online security breach?
        "PRSJMJ"   : 'Work', # single job or multiple jobs
        "PTNMEMP2" : 'Work', # NOTE: Can also be financial # number of paid employees.
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        "PEDWLKWK" : 'Work', # since you left your job, have you looked for work?
        "HENOTV10" : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        "PXLKLL2O" : 'Work', # Did you lose your job or quit, or was it temporary?
        "PXEGOVTS" : 'Online activities', # use of internet for accessing govt services like regestering to vote, paying taxes, etc.
        "HENOTV7"  : 'Digital access', # Do dot subscibe to TV since not available in area
        "HENOTV5"  : 'Digital access', # Do dot subscibe to TV since can watch at another location
        "HXINOTHR" : 'Digital access', # use internet at some other location
        "PXIO2ICD" : 'Work', # industry code of job 2
        "HENOHM7"  : 'Safety', # Do not use internet at home -> privacy or cybersecurity concerns
        "HEMEDREC" : 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        "PXERNHRY" : 'Financial', # hourly/non-hourly earnings
        "PXDISREM" : 'Disability', 
    },

    'HEPSPRE5' : {
        'HENOHM6'  : 'Digital access', # Do not use internet at home -> 
        'PXIO2ICD' : 'Work', # industry code of job 2
        'PELKAVL'  : 'Work', # LAST WEEK, COULD YOU HAVE STARTED A JOB IF ONE HAD BEEN OFFERED? 
        'PXERN'    : 'Financial', # weekly overtime earnings
        'HXINELHO' : 'Digital access', # Who uses the Internet at someone else's home? 
        'HXLOPRCE' : 'Financial', #At what price would you buy home internet service
        'PELAYLK'  : 'Work', # even though you are to be called back to work, have you been looking for work?
        'HXEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'PXDISEYE' : 'Disability', # is blind or difficulty seeing even when wearing glasses
        'HEPRINOH' : 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'HENOTV9'  : 'Digital access', # moving or in process of moving
        'HEPSCYBA' : 'Safety', # Affected by online security breach?
        'PULAYCK2' : 'Work', # dependent layoff
        'PXDISREM' : 'Disability', # any disability condition
        'PRDTCOW2' : 'Work', # DETAILED CLASS OF WORKER RECODE - JOB 2
        'HUBUSL2'  : 'Financial', # Have a business or a farm
        'HXPSPRE1' : 'Safety', # Privacy concerns
        'PUJHCK5'  : 'Work', # NILF - passive job seekers
        'PXINHOME' : 'Digital access', # Use internet at home?
        'PXINSCHL' : 'Digital access', # Use internet at school(again-> Look HEINSCHL)
    },

    'HEPSCON1' : {
        'HEPSCYBA' : 'Safety', # Affected by online security breach?
        "HENOHM7"  : 'Safety', # Do not use internet at home -> privacy or cybersecurity concerns
        'HEPREVTV' : 'Digital access', #Subscription to cable tv/satellite tv
        'HENOHM3' : 'Financial', #Don't use intenet at home? ->Not worth the cost
        'PXDISPHY' : 'Disability', #HAVE SERIOUS DIFFICULTY WALKING OR CLIMBING STAIRS?
        'HENOTV9'  : 'Digital access', # moving or in process of moving
        "HEMEDREC" : 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        'HENOTV4' : 'Financial', #do not subscribe to a service providing access to TV channels-> Not worth the cost
        'HENOHM1' : 'Digital access', #do not use the Internet at home->Don't need it or not interested
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HEPRINOH' : 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'PXINLICO' : 'Digital access', #Who uses the Internet at a library,community center, park, or other public place?
        'HENOTV6' : 'Digital access', #Do no subsribe to TV service-> Can watch using an antenna.
        'HEHOMTE3' : 'Digital access', #Using internet via dial-up?
        'PXINELHO': 'Digital access', # Who uses the Internet at someone else's home? 
        'HEINTRAV' : 'Digital access', #use the Internet while traveling between places?
        'HXPREVTV' : 'Digital access', #Subscription to cable tv/satellite tv
        'HENOHM6'  : 'Digital access', # Do not use internet at home -> No computing device, or device inadequate or broken
        'HXLOPRCE' : 'Financial', #At what price would you buy home internet service
        'PEERNUOT' : 'Work', #Do you usually receive overtime pay, tips or commisions?
    }, 
    
    'HEPSCON2':{
        'HEPSCYBA' : 'Safety', # Affected by online security breach?
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        "PXDISREM" : 'Disability',
        'PXERN' : 'Work', #Weekly overtime amount
        'PXJHWANT' : 'Work', #DO YOU INTEND TO LOOK FOR WORK DURING THE NEXT 12 MONTHS?
        'PXHRUSL1' : 'Work', #HOW MANY HOURS PER WEEK DO YOU USUALLY WORK AT YOUR MAIN JOB?
        'HEEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'PXHRUSLT' : 'Work', #Working hours per week
        'PXDISPHY' : 'Disability', #HAVE SERIOUS DIFFICULTY WALKING OR CLIMBING STAIRS?
        "HEMEDREC" : 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        'HEPREVTV' : 'Digital access', #Subscription to cable tv/satellite tv
        'PRHERNAL': 'Financial', # HOURLY EARNINGS
        'PXPUBLISH' : 'Online activities', #Posted online in the past 6 months
        'PREMP' : 'Work', #Employed persons
        'HUBUSL2'  : 'Financial', # Have a business or a farm
        'HEINTRAV' : 'Digital access', #use the Internet while traveling between places?
        'HENOTV4' : 'Financial', #do not subscribe to a service providing access to TV channels-> Not worth the cost
        'PXMPHONE' : 'Digital access', #Who uses a cellular phone or smartphone?
        'HXDEVSTA' : 'Digital access', #How often is the internet inaccessible?
        'PXLAPTOP' : 'Digital access', #Use a laptop?
    },
    
    'HEPSCON3': {
        'PXMLR' : 'Work', #Major Labor Force Recode
        'HUBUSL3' : 'Financial', # Have a business or a farm
        'PULAYCK3' : 'Work',
        'HENOHM3' : 'Financial', #Don't use intenet at home? ->Not worth the cost
        'HENOHM5' : 'Digital access', #Do not use the internet at home? ->No computing device, or device inadequate or broken
        'HENOTV8' : 'Digital access' , #Do dot subscibe to TV due not having a TV or broken TV
        'HENOTV10' : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'HXMEDINF' : 'Online activities', #Research health info online
        "PXDISREM" : 'Disability', 
        'PUJHCK2' : 'Work',
        "HEMEDREC" : 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        'PEPDEMP2' : 'Work',
        'PRDTIND2' : 'Work', #Industry code
        'PRUNEDUR' : 'Work', #Duration of unemployment for layoff
        'HEINOTHR' : 'Digital access', #use the Internet at some other location we haven't covered yet?
        'PXINLICO' : 'Digital access', #Who uses the Internet at a library,community center, park, or other public place?
        'HENOTV4' : 'Financial', #do not subscribe to a service providing access to TV channels-> Not worth the cost   
        'HEINTRAV': 'Digital access', #use the Internet while traveling between places?'
    },
    
    'HEPSCON4': {
        'HXTENURE' : 'House', #Owned or rented house
        'HUBUSL4' : 'Financial', #Have a business or a farm
        'HXDEVSTA' : 'Digital access', #How often is the internet inaccessible?
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'HUBUSL3' : 'Financial', #Have a business or a farm
        'PXINHOME' : 'Digital access', # Use internet at home?
        'PXINOTHR' : 'Digital access', #Who uses internet at other places not covered in the survey
        'PXNETCK2' : 'Digital access', #Who uses internet from any location, for any purpose.
        'HENOHM1' : 'Digital access', #do not use the Internet at home->Don't need it or not interested
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HXWEARAB' : 'Digital access', #Use a wearable smart device?
        'PXHSPNON': 'Demographic', #Hispanic?
        'PUHRCK5' : 'Work',
        'HENOTV4' : 'Financial', #do not subscribe to a service providing access to TV channels-> Not worth the cost
        'PELKFTO' : 'Work', #Jobseeker status
        'PELKLL1O' : 'Work', #What were you doing before you started looking for work
        'HENOTV11' : 'Digital access', #Do dot subscibe to TV due to poor quality
        'HXMPHONE' : 'Digital access', #Use a smartphone?
        "HENOTV5"  : 'Digital access', # Do dot subscibe to TV since can watch at another location
        'HENOTV10' : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
    },

    'HEPSCON5': {
        'HENOHM5' : 'Digital access', #Do not use the internet at home? ->No computing device, or device inadequate or broken
        'HXNOHM1' : 'Digital access', # # reason for not using internet at home - don't need it
        'HXEVRHOM': 'Digital access', #Ever used the Internet from home?
        'PRCITFLG': 'Demographic', #CITIZENSHIP ALLOCATION FLAG
        'HEMEDINF': 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HXTENURE': 'House', #Owned or rented house
        'HEPSCYBA': 'Safety', #Affected by online security breach?
        'HENOTV7' : 'Digital access', # Do dot subscibe to TV since not available in area
        'PXJHWANT': 'Work', #DO YOU INTEND TO LOOK FOR WORK DURING THE NEXT 12 MONTHS?
        'PULAYCK3': 'Work', #something layoff related
        'PXGAMING': 'Online activities', # What about playing video games online, whether on a smartphone, console, PC, or any other computing device
        'HXPRINOH': 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
        'HENOTV10': 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        'HEMEDREC': 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        'HUBUSL3' : 'Financial', # Have a business or a farm
        'HXTELAVL': 'Digital access', #iS THERE A TELEPHONE ELSEWHERE O
        'PXERNUOT': 'Work', #Do you usually receive overtime pay, tips or commisions?
        'HENOTV11': 'Digital access', #Do dot subscibe to TV due to poor quality
        'HEHMINT1': 'Digital access', # In addition to your household's mobile 1067-1068 Internet service or data plan, we are  interested in whether your household  also uses any other type of Internet  service when at home
        'PXDESKTP': 'Digital access', # Who uses a desktop computer?
    },

    'HEPSCON6':{
        'HENOHM5' : 'Digital access', #Do not use the internet at home? ->No computing device, or device inadequate or broken
        'HUBUSL3' : 'Financial', # Have a business or a farm
        'PXNETCK2': 'Digital access', #Who uses internet from any location, for any purpose.
        'HXTENURE': 'House', #Owned or rented house
        'HENOTV10': 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        'HENOHM1' : 'Digital access', #do not use the Internet at home->Don't need it or not interested
        'HEPSCYBA': 'Safety', # Affected by online security breach?
        'PXPAR2'  : 'Demographic', # LINE NUMBER OF FIRST PARENT (ALWAYS THE FATHER, IF PRESENT. WILL BE A FEMALE IF THE PARENTS ARE SAME SEX.)
        'HEEVRHOM': 'Digital access', # (Have you/Has anyone in this household) ever used the Internet from home?
        'HEINSCHL': 'Digital access', #Use internet at school?
        'HEMEDINF': 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HXMEDREC': 'Online activities',# What about accessing health records or health  insurance records online.
        'HXMPHONE': 'Digital access', #Use a smartphone?
        'PXINOTHR': 'Digital access', #Who uses internet at other places not covered in the survey
        'PUHRCK12': 'Work', 
        'HEDEVSTA': 'Digital access', #How often is internet inaccessible?
        'HENOTV6' : 'Digital access', #Do no subsribe to TV service-> Can watch using an antenna.
        'HEHNETQL': 'Digital access', #does internet connection at home fill your needs.
        'HEHNETST': 'Financial',  # Temporarily lose internet access due to non-payment
        'HXPRINOH': 'Online activities', #Of the reasons you just listed for not going online at home, which (do you/does your household) consider to be the most important?
    },
   
    'HEPSCON8': {
        "HUBUSL3": "Financial", # see above
        "PUJHCK2": "Work", # see above
        "HEHOMTE3": "Digital access", # see above
        "HENOTV9": "Digital access", # see above
        "PXLAPTOP": "Digital access", # see above
        "HXWEARAB": "Digital access", # see above
        "HXINELHO": "Digital access", # see above
        "HXHNETQL": "Digital access", # see above
        "PXWEARAB": "Digital access", # see above
        'HXHOMTE1': "Digital access",
        'PTOT'    : 'Financial', #  WEEKLY OVERTIME AMOUNT - TOP CODE 
        'PUDWCK2' : 'Disability', # SCREEN FOR DISABLED
        'PRUNTYPE': 'Work',  # REASON FOR UNEMPLOYMENT  
        'PEAFWHN4': 'Work', # WHEN DID YOU SERVE?
        'HENOTV12': 'Digital access', #Do no subsribe to TV service
        'HXDESKTP': 'Digital access', # use a desktop computer
        'HXHNETST': 'Financial',
        'PXESRVCS': 'Work', # What about offering (your/his/her) own  services for sale via the Internet?
        'PXDW4WK' : 'Work', # DID YOU DO ANY OF THIS WORK DURING    355 - 356       THE LAST 4 WEEKS?
        'PXNATVTY': 'Demographic', # COUNTRY OF BIRTH
    }
}

feat_dict_yearwise = {
    '2015': {
         'HENOHM5'           :  'Digital access' ,#Do not use the internet at home? ->No computing device, or device inadequate or broken
         'HECBULLY'          :  'Safety'         ,#During the past year (have you/has any member of your household) experienced online harassment, stalking, or cyber-bullying? 1-yes, 2-no
         'HECYBA'            :  'Safety'         ,#During the past year, (have you/has any 1105-1106 member of your household) been affected by an online security breach, identity theft,or a similar crime?  
         'HEINCAFE'          :  'Digital access' ,#(Do you/Doesanyone in this household use the Internetwhile at a coffee shop or other business that offers Internet access?
         'PEIO2ICD'          :  'Work'           ,#INDUSTRY CODE FOR SECOND JOB, 0 Min value, 9999 Max Value
         'HEINTRAV'          :  'Digital access' ,#What about while traveling between places? 991-992(Do you/Does anyone in this household) use the Internet while traveling between places?1- Yes, 2- No
         'PXINUSYR'          :  'Demographic'    ,#ALLOCATION FLAG for PRINUSYR : IMMIGRANT'S YEAR OF ENTRY
         'PXMLR'             :  'Work'           ,#PXMLR is allocation flag for PEMLR (Major Labor Force Recode) This classification is available for each civilian 15 years old.1 EMPLOYED-AT WORK2 EMPLOYED-ABSENT etc.
         'HEDESKTP'          :  'Digital access' ,#(Do you/Does anyone in this household, including you,) use a desktop computer?
         'HHWGT83'           :  'House'          ,#Replicate weight variable for household characteristics
         'HEINSCHL'          :  'Digital access' ,#(Do you/Does anyone in this household) use the Internet at school? 
         'HHWGT21'           :  'House'          ,#Replicate weight variable for household characteristics
         'GTCSA'             :  'Demographic'    ,#GTCSA 3 Consolidated Statistical Area (CSA) FIPS CODE(SEE GEOGRAPHIC ATTACHMENT 000 NOT IDENTIFIED OR NONMETROPOLITAN, 104 MIN VALUE,548 MAX VALUE
         'HHWGT121'          :  'House'          ,#Replicate weight variable for household characteristics
         'HHWGT107'          :  'House'          ,#Replicate weight variable for household characteristics
         'HHWGT94'           :  'House'          ,#Replicate weight variable for household characteristics
         'HEHOMSU3'          :  'Digital access' ,#at home, do you connect to the Internet using: Internet service provided for an entireapartment building, condominium,etc?
         'HEINOTHR'          :  'Digital access' ,#(Do you/Does anyone in this household) use the Internet at some other location we haven't covered yet?
         'PXJHWKO'           :  'Work'           ,#ALLOCATION FLAG for PEJHWKO 2 HAVE YOU WORKED AT A JOB OR BUSINESS AT ANY TIME DURING THE PAST 12 MONTHS?
         'PXDISEYE'          :  'Disability'     ,#ALLOCATION FLAG forPEDISEYE  IS…BLIND OR DOES…HAVE SERIOUS DIFFICULTY SEEING EVEN WHENWEARING GLASSES?    
         'HHWGT122'          :  'House'          ,#Replicate weight variable for household characteristics
         'HEHOMTE4'          :  'Digital access' ,#At home, (do you/does anyone in this household) access the Internet using:Dial-up service?
         'HHWGT92'           :  'House'          ,#Replicate weight variable for household characteristics
         'HEHOMSU4'          :  'Digital access' ,#When going online at home, do you connect to the Internet using:Publicly-available Internet service provided at no charge?
        },

    '2017': {
        'HEPSCYBA' : 'Safety', #Affected by online security breach?
        'HENOTV11' : 'Digital access', #Do dot subscibe to TV due to poor quality'
        'HENOTV10' : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        'HEMEDINF' : 'Online activities', # Do you use the internet to get information about health or medical topics?
        'PXLKM1' : 'Work', #What all have you done to find work in the last 4 weeks?
        'PUNLFCK1' : 'Work', #Not in labor force(flag)
        'HEINCAFE' : 'Digital access', #Used internet at a coffee shop
        'HECBULLY' : 'Safety', #During the past year have you experienced online harassment, stalking, or cyber-bullying?
        'HEEVRHOM' : 'Digital access', #Ever used the Internet from home?
        'PRNLFSCH' : 'Work', #In school or not in school
        'PESCHLVL' : 'Work', #Enrolled in a school or college as part-time/full-time
        'PULAY' : 'Work', #Last week were you on a layoff from a job?
        'HETRADTV' : 'Digital access', #Cable TV/Satellite TV
        'HENOTV9' : 'Digital access', # moving or in process of moving
        'HEMPHONE' : 'Digital access', #Use a smartphone that connects to the internet
        'HHWGT53' : 'House', #Replicate weight variable for household characteristics
        'HEHOMTE4' : 'Digital access', #Access the internet using some other service not covered by the survey
        'HENOOU7' : 'Safety', #do not use the Internet outside the home-> Online privacy or cybersecurity concerns
        'HEHMINT1' : 'Digital access', # In addition to your household's mobile Internet service or data plan, we are  interested in whether your household  also uses any other type of Internet  service when at home
        'HENOTV1' : 'Digital access' #Not subscribed to TV because using internet based video services instead
    },

    '2019': {
        'HUBUSL4' : 'Financial', #Have a business or a farm
        'HENOOU9' : 'Digital access', # no internet because moved from previous internet location
        'HEPSCYBA': 'Safety', #Affected by online security breach?
        'HECBULLY': 'Safety', #During the past year have you experienced online harassment, stalking, or cyber-bullying?
        'HENOOU5' : 'Financial', # No internet due to no computer device, or inadequate or broken
        'HENOTV5' : 'Digital access', # Do dot subscibe to TV since can watch at another location
        'HEMEDINF': 'Online activities', # Do you use the internet to get information about health or medical topics?
        'HEINOTHR': 'Digital access' ,#(Do you/Does anyone in this household) use the Internet at some other location we haven't covered yet?
        'HENOHM7' : 'Safety', # Do not use internet at home -> privacy or cybersecurity concerns
        'HEHOMTE4': 'Digital access', #Access the internet using some other service not covered by the survey
        'HENOTV10': 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        'HENOTV3' : 'Financial', #No subscription to TV channels service, why? -> Can't afford it
        'HEINLICO': 'Digital access', # in library or community center, park, public place
        'HENOTV12': 'Digital access', #Do no subsribe to TV service
        'HUBUSL1' : 'Work', # have business or farm?
        'HENOTV6' : 'Digital access', #Do no subsribe to TV service-> Can watch using an antenna.
        'HENOHM1' : 'Digital access', #do not use the Internet at home->Don't need it or not interested
        'HENOHM10': 'Online activities', # reason for not using internet at home - some other reason
        'PXLNMOM' : 'Demographic', # Line number of mother
        'HEPECOMP': 'Digital access', # Any providers near you who offer fast internet connectivity
    },

    '2021': {
        "PXMLR"    : 'Work', #Major Labor Force Recode
        "HENOHM10" : 'Online activities', # reason for not using internet at home - some other reason
        "HXPRINOH" : 'Online activities', # reason for not using internet at home - most important reason
        "HXNOHM1"  : 'Online activities', # # reason for not using internet at home - don't need it
        "HEPSCYBA" : 'Safety', #Affected by online security breach?
        "PRSJMJ"   : 'Work', # single job or multiple jobs
        "PTNMEMP2" : 'Work', # NOTE: Can also be financial # number of paid employees.
        "HEMEDINF" : 'Online activities', # Do you use the internet to get information about health or medical topics?
        "PEDWLKWK" : 'Work', # since you left your job, have you looked for work?
        "HENOTV10" : 'Digital access', #Do dot subscibe to TV due to poor customer servcie.
        "PXLKLL2O" : 'Work', # Did you lose your job or quit, or was it temporary?
        "PXEGOVTS" : 'Online activities', # use of internet for accessing govt services like regestering to vote, paying taxes, etc.
        "HENOTV7"  : 'Digital access', # Do dot subscibe to TV since not available in area
        "HENOTV5"  : 'Digital access', # Do dot subscibe to TV since can watch at another location
        "HXINOTHR" : 'Digital access', # use internet at some other location
        "PXIO2ICD" : 'Work', # industry code of job 2
        "HENOHM7"  : 'Safety', # Do not use internet at home -> privacy or cybersecurity concerns
        "HEMEDREC" : 'Online activities', # Do you use the internet to get information about health (/insurance) records?
        "PXERNHRY" : 'Financial', # hourly/non-hourly earnings
        "PXDISREM" : 'Disability', 
    },
}

# Re-categorize the variables into broader categories using this map.
category_category_new_mapping = {
'Digital access' : {"Digital access"}, # To split
'Online activities': {"Online activities"},
"Wealth related":{"Financial", "Work", "House"}, # Wealth-related
"Safety": {"Safety"}, #
"Personal Characteristics":{"Demographic", "Disability"} # Personal characteristics (Demography, disability)
}

for variables in feat_dict:
    for col in feat_dict[variables]:
        for category in category_category_new_mapping:
            if feat_dict[variables][col] in category_category_new_mapping[category]:
                feat_dict[variables][col] = category

for variables in feat_dict_yearwise:
    for col in feat_dict_yearwise[variables]:
        for category in category_category_new_mapping:
            if feat_dict_yearwise[variables][col] in category_category_new_mapping[category]:
                feat_dict_yearwise[variables][col] = category