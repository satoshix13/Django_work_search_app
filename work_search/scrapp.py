import requests
from bs4 import BeautifulSoup
import codecs

url = 'https://www.work.ua/jobs-kyiv-python'

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    job_list = []
    errors = []
    url = 'https://www.work.ua'
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('div', class_="card card-hover card-visited wordwrap job-link")
    for job in jobs:
        title = job.find('a').get('title')
        link = job.find('a').get('href')
        final_link = url+link
        company = 'no name'
        content = job.find('p', class_='overflow text-muted add-top-sm add-bottom').text.strip().replace('\n','')
        logo = job.find('img')
        if logo:
            company = job.find('img').get('alt')

        job_list.append({'title':title,'url':final_link,'description':content,
                         'company':company})


    h = codecs.open('work.txt','w','utf-8')
    h.write(str(job_list))
    h.close()



get_data(get_html(url))