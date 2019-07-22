# Federal Contracts & Campaign Contributions Before & After Citizens United

Mod 3 Project @ The Flatiron School 
Team members: Joey Goodman and Phoebe Wong

## Executive summary:

The goal of this project is to present preliminary findings on a unique data set we constructed that matches federal contractor data and campaign contribution data.

![alt text](https://github.com/yontartu/citizens-united/blob/master/img/award_vs_pac_soft.gif) 


## Contents

- [Introduction](#Introduction)
    - [Problem statement](#Problem-statement)
    - [Dataset](#Dataset)
- [Analysis](#Analysis)
    - [Data cleaning](#Data-cleaning)
    - [Exploratory data analysis](#Exploratory-data-analysis)

## Introduction

### Problem statement

Our goal is to identify the effects of political spending on federal contract awards before and after the Supreme Court’s decisions in Citizens United and SpeechNow vs FEC.

### Data set

The main dataset of this project has two main sources. 

Federal contractor data is downloaded from:
[USASpending.gov](https://www.usaspending.gov/#/download_center/award_data_archive)(from 2008-2018)

Campaign contribution data is scrapped from:
[OpenSecrets.org](https://www.opensecrets.org/orgs/methodology.php)

## Analysis

### Data cleaning

We merged the datasets with some novel techniques and created multiple unique features for this analysis. For explanations on the methodology, see Mod3_Project_JG_PW.ipynb 

### Exploratory data analysis

We seek to answer 3 main questions in this project: 
1. Have federal contractors made more campaign donations since Citizens United?
2. Do federal contractors w/ PAC donations receive more contract awards?
3. Do federal contractors donate a larger share to Democrats than non-contractors?
4. Do federal contractors make the same amount of campaign contributions as non-contractors?