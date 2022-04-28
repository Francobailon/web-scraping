from bs4 import BeautifulSoup
import requests
import docx

link = "https://subslikescript.com/movie/Titanic-120338"
html_box = 'article'
box_class = 'main-article'
html_tittle = 'h1'
html_content = 'div'
content_class = 'full-script'

def scraper(link,html_box,box_class,html_tittle,html_content,content_class):
    result = requests.get(link)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find(html_box,class_=box_class)
    tittle = box.find(html_tittle).get_text()
    transcript = box.find(html_content, class_ = content_class).get_text(strip=True,separator=' ')

    mydoc = docx.Document()
    mydoc.add_paragraph(transcript)
    mydoc.save(f"{tittle}.docx")

    return {'message': 'word file created succesfully'}

if __name__ == '__main__':
    scraper(link,html_box,box_class,html_tittle,html_content,content_class)