from bs4 import BeautifulSoup
import requests
import pandas as pd

link = 'https://verbos-irregulares-ingles.com/'
parser = 'lxml'
html_table = 'table'
table_id = 'verbs-table'
table_headers = 'th'
table_rows = 'tr'
table_data = 'td'

def scraper(link,parser,html_table,table_id,table_headers,table_rows,table_data):
    page = requests.get(link).text
    if page == None:
        print('page not found')
    soup = BeautifulSoup(page, parser)
    if soup == None:
        print("soup couldn't be parsed")

    # Obtain information from tag <table>
    table = soup.find(html_table,id=table_id)
    if table == None:
        print("table not found")
    
    # Obtain every title of columns with tag <th>
    headers = []
    for i in table.find_all(table_headers):
        title = i.text
        headers.append(title)
    
    headers[0] = 'Infinitivo'
    headers[1] = 'Pasado simple'
    headers[2] = 'Participio pasado'
    headers[3] = 'Traduccion'
    # Create a dataframe
    mydata = pd.DataFrame(columns = headers)

    # Create a for loop to fill mydata
    for j in table.find_all(table_rows)[1:]:
        row_data = j.find_all(table_data)
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row
    
    # Drop and clearing unnecessary rows
    # mydata.drop(mydata.index[0:7], inplace=True)
    # mydata.drop(mydata.index[222:229], inplace=True)
    # mydata.reset_index(inplace=True, drop=True)
    # Drop “#” column
    mydata.drop(columns=mydata.columns[-1], 
                axis=1, 
                inplace=True)
    print(headers)

    # Export data to CSV
    mydata.to_csv(f'{table_id}.csv',sep=';', index=False)  
    

if __name__ == '__main__':
    scraper(link,parser,html_table,table_id,table_headers,table_rows,table_data)

