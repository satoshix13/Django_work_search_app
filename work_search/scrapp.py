import requests
from bs4 import BeautifulSoup
import codecs


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }




def rabota(url):
    job_list = []
    errors = []
    r = requests.get(url)
    domain = 'https://rabota.ua/'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        new_jobs = soup.find('div', class_='f-vacancylist-newnotfound')
        if not new_jobs:
            table = soup.find('table', id='ctl00_content_ctl00_gridList')
            if table:
                trs = table.find_all('tr')
                for tr in trs:
                    div = tr.find('div', class_='card-body')
                    if div:
                        title = div.find('p', class_="card-title").find('a').get('title')
                        link = div.find('p', class_="card-title").find('a').get('href')
                        final_link = domain+link
                        company = 'no name'
                        content = div.find('div', class_='card-description').text.strip().replace('\n','')
                        logo = tr.find('img')
                        if logo:
                            company = div.find('img').get('alt').replace('Все вакансии компании ','')


                        job_list.append({'title':title,'url':final_link,'description':content,
                                         'company':company})


            else:
                errors.append({'url':url,'title':'Table does not exists'})
        else:
            error.append({'url':url,'title':'Page is empty'})
    else:
        errors.append({'url':url,'title':'Page do not respond'})

    return job_list,errors





def work(url):
    job_list = []
    errors = []
    r = requests.get(url)
    domain = 'https://www.work.ua'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        main_div = soup.find('div', id='pjax-job-list')
        if main_div:
            jobs = soup.find_all('div', class_="card card-hover card-visited wordwrap job-link")
            for job in jobs:
                title = job.find('a').get('title')
                link = job.find('a').get('href')
                final_link = domain+link
                company = 'no name'
                content = job.find('p', class_='overflow text-muted add-top-sm add-bottom').text.strip().replace('\n','')
                logo = job.find('img')
                if logo:
                    company = job.find('img').get('alt')

                job_list.append({'title':title,'url':final_link,'description':content,
                                 'company':company})


        else:
            errors.append({'url':url,'title':'Div does not exists'})
    else:
        errors.append({'url':url,'title':'Page do not respond'})

    return job_list,errors

# def dou(url):
#     job_list = []
#     errors = []
#     r = requests.get(url)
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.text, 'lxml')
#         main_div = soup.find('div', id='vacancyListId')
#         if main_div:
#             jobs = soup.find_all('li', class_="l-vacancy")
#             for job in jobs:
#                 title = job.find('div', class_='title')
#                 link = title.a['href']
#                 company = 'no name'
#                 content = job.find('div', class_='sh-info').text
#                 a = title.find('a', class_='company')
#                 if a:
#                     company = a.text
#
#                 job_list.append({'title':title,'url':link,'description':content,
#                                  'company':company})
#                 print(title)


    #     else:
    #         errors.append({'url':url,'title':'Div does not exists'})
    # else:
    #     errors.append({'url':url,'title':'Page do not respond'})
    #
    # return job_list,errors


def djinni(url):
    job_list = []
    errors = []
    domain = "https://djinni.co"
    r = requests.get(url,headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        main_ul = soup.find('ul', class_='list-unstyled list-jobs')
        if main_ul:
            jobs = main_ul.find_all('li', class_="list-jobs__item")
            for job in jobs:
                title = job.find('div', class_='list-jobs__title').text.strip()
                link = job.find('div', class_='list-jobs__title').find('a').get('href')

                company = 'no name'
                content = job.find('div', class_='list-jobs__description').find('p').text
                comp = job.find('div', class_='list-jobs__details__info')
                if comp:
                    company = comp.text.replace('\n','')

                job_list.append({'title':title,'url':domain+link,'description':content,
                                 'company':company})



        else:
            errors.append({'url':url,'title':'Div does not exists'})
    else:
        errors.append({'url':url,'title':'Page do not respond'})

    return job_list,errors



# djinni('https://djinni.co/jobs/?title_only=True&primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2')



if __name__ == '__main__':
    url = 'https://djinni.co/jobs/?title_only=True&primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2'
    job_list,errors = djinni(url)
    # url = "https://www.work.ua/jobs-kyiv-python"
    # job_list,errors = work(url)
    h = codecs.open('work.txt','w','utf-8')
    h.write(str(job_list))
    h.close()



