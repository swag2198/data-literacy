<h1 align="center">Cautious Clicks: Analyzing the Perceived Risks on the Web</h1>

This repository is associated with the _Data Literacy_ course project, submitted to [Prof. Dr. Philipp Hennig](https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/methoden-des-maschinellen-lernens/personen/philipp-hennig/) at the Univerity of Tübingen for WS 23/24. We also 
thank Tobias Weber (PhD student) for his helpful inputs and guidance throughout this project.

## Abstract

In this report, we study 
the public perception of technology related risks (e.g., fear while expressing opinions on a controversial issue) 
and try to understand the factors that make people sensitive to certain kinds of _risks_. We 
analyse the Internet Supplement from CPS 
Survey and focus on questions on internet usage, concerns, and 
online behaviours which, to the best 
of our knowledge, is previously unexplored. Our contributions include identifying and categorizing features that are deemed important for the risk-perception. The results uncover the interesting insight that over time people are warming up to the convenience of using internet for automated tasks such as banking/online shopping, but growing increasingly cautious of social interactions such as sharing opinions.

## Downloading data
Download the csv file from `https://www.census.gov/data/datasets/time-series/demo/cps/cps-supp_cps-repwgt/cps-computer.html` to get the 2021 version of the CPS Computer 
and Internet supplement dataset. Also the corresponding csv files for 2015, 2017, 2019 and 2021 can also be found in NTIA Internet Use Survey Datasets store: 
`https://www.ntia.gov/page/download-ntia-internet-use-survey-datasets`.


## Repository structure
- `/dat` contains the dataset documentation
- `/exp` contains our methods, experiments, and analysis in separate notebooks
- `/res` stores plots and csv files output as results
- `/src` has attribute definitions, data stratification criteria, and our annotated labels for the coded features
- `/streamlit` contains files related to the [streamlit application](https://datalitproject1.streamlit.app/)
- `streamlit_app.py` file contains the streamlit code hosted on the steamlit public cloud.

## Reproducibility
- Figure 2 (geographic distribution of cyber crime in the US): [notebook](https://github.com/swag2198/data-literacy/blob/main/exp/Statewise_distribution.ipynb)
- Figure 5 (overall trends in risk-perceptions for various activities): [notebook](https://github.com/swag2198/data-literacy/blob/main/exp/Time_series_data.ipynb)
- Figures 1 and 3 (bar plot showing risk perceptions in overall population, and when grouped under different income levels): [notebook](https://github.com/swag2198/data-literacy/blob/main/exp/exp_AssociationBetweenVariables.ipynb)
- Figures 4 and 6 (categorisation of important features into different buckets and their evolution over time): [notebook](https://github.com/swag2198/data-literacy/blob/main/exp/XGB_feature_importance.ipynb)
- Table 1 (chi-square testing): [notebook](https://github.com/swag2198/data-literacy/blob/main/exp/exp_AssociationBetweenVariables.ipynb)


## Contacts
If you find any issues or have any questions on our analysis, please feel free to raise an issue! 

