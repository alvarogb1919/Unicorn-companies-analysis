# Unicorn-companies-analysis

![Startups image](https://news.america-digital.com/wp-content/uploads/2020/10/Top-ten-Startups-m%C3%A1s-valiosas-de-Latinoam%C3%A9rica-en-2020.jpg)

### Welcome to my second Ironhack project! The focus area of the analysis presented below is unicorn startups, this term basically refers to startups that are able to reach at least a $1bn valuation. Let's talk about the depths of the project:

## Scope of the project
The dataset used comes from Kaggle and it provided a list of 708 global unicorn startups providing the following information for each of them: 1) Company name, 2) Valuation, 3) Date they became unicorn / reached the $1bn valuation, 4) Country of origin, 5) City, 6) Industry, and 7) Investors.

With this initial dataset already several interesting analysis could've been performed, however the goal of the project was to find a decent dataset and enrich it via API calls or web scraping. In my case, I enriched the dataset via web scraping. Let's talk about the scraping process.

## Web scraping
The website from which I fed the startup database is DealRoom (https://dealroom.co/). This is a great website for my purpose as it provided the total number of funding ronds undergone by each startup, and most importantly the total funding received, which is exactly the data I wanted to include. I wanted to include this specific data point for each as I was curious about the relationship between the total valuation of a startup and the total funding it has received (apart from some further interesting analysis) If you want to know the answer please feel free to dive into the Jupyter Notebook called "Unicorns analysis and visualization" - the answer might surprise you! (or at least I was surpised ;))

## Analysis rationale
If you are curious about the unicorn startups and have decided to explore the "Unicorns analysis and visualization" let me provide a simple but clear map of the file. The file is structured in 7 different sections. In each section a specific analysis is performed. Specifically the order is the following:

- Analysis 1.0: Which countries have nested the most unicorn companies? and which cities?
- Analysis 2.0: In which sectors have unicorn startups succeeded the most?
- Analysis 3.0: How has the rate of unicorn startups changed? How many startups reached the $1bn valuation milestone each year since 2007
- Analysis 4.0: Based on the results of the previous analysis: How those valuation moves depending on the year in which the startup became a unicorn?
- Analysis 5.0: How does valuation and funding change by sector and by country?
- Analysis 6.0: Does more funding lead to higher valuations?
- Analysis 7.0: Who were the smart or lucky funds who invested in startups before they converted to unicorns?

Overall I hope that after going through the analysis performed you are able to grasp in more detail the dynamics of the current unicorn startups in terms of trending sectors, countries, cities, and how relevant or not the total funding received is when determining a total valuation

## Sources and libraries used
- Pandas - https://pandas.pydata.org/
- Seaborn - https://seaborn.pydata.org/#
- Matplotlib - https://matplotlib.org/
- Datetime - https://docs.python.org/3/library/datetime.html
- Requests - https://docs.python-requests.org/en/master/
- BeautifulSoup - https://www.crummy.com/software/BeautifulSoup/
- Kaggle(for inital dataset) - https://www.kaggle.com/
- DealRoom (mentioned above for web scraping) - https://dealroom.co/

## Files structure
- "Data" folder containing the initial dataset downloaded (unicorns) and the clean version after data handling and web scraping applied (Cleaned_unicorns)
- "src" folder with a python file (functions_clean.py): files with functions used in the "Unicorns cleaning_called_functions" jupyter notebook. Please look at the "Unicorns cleaning simple" notebook instead to see the whole cleaning process as I experienced some unfortunate problems with the other file
- "Unicorns analysis and visualization" notebook where you will be able to see the previously mentioned analysis alongside some written straigth and concise conclusions
# That's all! Thank you for your interest :)