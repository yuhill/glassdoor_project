import requests
import bs4
import time
from pprint import pprint


def download_website(page_url):
    s = requests.session()
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0'}
    s.get("https://www.glassdoor.com", headers=headers)
    parsed_boeing = bs4.BeautifulSoup(s.get(page_url, headers=headers).text, 'html.parser')
    return parsed_boeing


# download_website("https://www.glassdoor.com/Salary/Boeing-Salaries-E102.htm")
def get_salary_table(page):
    salaries_html = page.find_all('div', class_="salaryChartModule")[0]
    return salaries_html


def find_titles_and_salaries(table):
    list_of_salary_divs = table.find_all('div', class_="meanPay alignRt")
    salary_list = []
    for salary_div in list_of_salary_divs:
        salary_text = salary_div.get_text()
        salary_list.append(salary_text)
    list_of_title_divs = table.find_all('a', class_="noMargVert jobTitle")
    title_list = []
    for title_div in list_of_title_divs:
        title_text = title_div.get_text()
        title_list.append(title_text)
    return list(zip(title_list, salary_list))


def extract_salaries(page_url):
    webpage = download_website(page_url)
    salary_table = get_salary_table(webpage)
    salries_and_titles = find_titles_and_salaries(salary_table)
    return salries_and_titles


def add_company_to_salary_info(titles_and_salaries, company_name):
    result = []
    for title, salary in titles_and_salaries:
        result.append((company_name, title, salary))
    return result


if __name__ == '__main__':
    list_urls = ["https://www.glassdoor.com/Salary/Boeing-Salaries-E102.htm",
                 "https://www.glassdoor.com/Salary/Airbus-Salaries-E3059.htm"]
    companies = list()
    for page in list_urls:
        titles_and_salaries = find_titles_and_salaries(download_website(page))
        company_name = page.split('-')[0].split('/')[-1]
        companies += add_company_to_salary_info(titles_and_salaries, company_name)
        time.sleep(1)
    pprint(companies)
