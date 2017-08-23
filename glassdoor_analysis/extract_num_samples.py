import requests
import bs4
import time
from pprint import pprint

from glassdoor_analysis.data_cleaner import normalize_salaries


def download_website(page_url):
    s = requests.session()
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0'}
    s.get("https://www.glassdoor.com", headers=headers)
    parsed_boeing = bs4.BeautifulSoup(s.get(page_url, headers=headers).text, 'html.parser')
    return parsed_boeing


def get_salary_samples(page):
    """
    This function takes in all the html code of the page
    extract the number of samples from each page
    """
    pass


if __name__ == '__main__':
    list_urls = ["https://www.glassdoor.com/Salary/Boeing-Salaries-E102.htm",
                 "https://www.glassdoor.com/Salary/Airbus-Salaries-E3059.htm",
                 "https://www.glassdoor.com/Salary/Airbus-Salaries-E3059_P2.htm",
                 "https://www.glassdoor.com/Salary/Airbus-Salaries-E3059_P3.htm",
                 "https://www.glassdoor.com/Salary/Airbus-Salaries-E3059_P4.htm",]
    companies = list()
    for page in list_urls:
        companies += get_salary_samples(download_website(page))
        time.sleep(1)
    pprint(companies)
