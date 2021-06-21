import pandas as pd
import numpy as np
import seaborn as sns
 

#Function to convert the date format for consistency purposes
def date_year(date):
    from datetime import datetime
    first_clean = date.replace("-", "/")
    second_clean = datetime.strptime(first_clean, "%m/%d/%Y")
    return second_clean.year

#Function to clean the valuation column in order to remove the $ sign and convert to float
def clean_valuation(valuation):
    return float(valuation.replace("$", ""))

#Function to convert the company names to lower case
def lower_case(x):
    return x.lower()

#Function to scrap the corresponding url and obtain the total funding value
def obtain_funding(u):
    response = requests.get(u)
    soup = BeautifulSoup(response.text, 'html.parser')
    company_funding = (soup.find_all(name="span", class_="tooltip-target")[0].text)
    return company_funding

#Function to normalize the total funding obtained from web scraping
def funding_normalizer(x):
    if "b" in x:
        y = x.replace("b", "")
        if "€" not in y:
            return("Not available")
        else:
            z = y.replace("€", "")
            return float(z)*1000
    elif "m" in x:
        y = x.replace("€", "")
        z = y.replace("m", "")
        return float(z)
    elif "k" in x:
        y = x.replace("€", "")
        z = y.replace("k", "")
        return float(z)/1000
    else:
        return("Not available")