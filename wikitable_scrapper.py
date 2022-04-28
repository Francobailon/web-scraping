from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'
parser = 'html.parser'
html_table = 'table'
table_id = 'wikitable'

def scraper(link,parser,html_table,table_id):
    page = requests.get(link).text
    if page == None:
        print('page not found')
    soup = BeautifulSoup(page, parser)
    if soup == None:
        print("soup couldn't be parsed")

    # Obtain information from tag <table>
    table = soup.find(html_table,{"class":table_id})  
    df=pd.read_html(str(table))

    # convert list to dataframe
    df=pd.DataFrame(df[0])
    
    # drop the unwanted columns
    data = df.drop(["Rank", "Population(2001)"], axis=1)

    # rename columns for ease
    data = data.rename(columns={"State or union territory": "State","Population(2011)[3]": "Population"})

    # Export data to CSV
    df.to_csv(f'{table_id}.csv',sep=';', index=False)  
    

if __name__ == '__main__':
    scraper(link,parser,html_table,table_id)