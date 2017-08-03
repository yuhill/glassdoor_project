import re

import requests
import bs4
import pandas as pd

boeing_url = "https://www.glassdoor.com/Salary/Boeing-Salaries-E102.htm"
cisco_url = "https://www.glassdoor.com/Salary/Cisco-Systems-Salaries-E1425.htm"


def get_salary_chart(salary_url):
    """
    Retrieves the HTML from the glassdoor url and returns the "salaryChartModule" element
    from the page. Only works if the page is a glassdoor salary page
    """
    s = requests.session()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0'}
    s.get("https://www.glassdoor.com", headers=headers)
    parsed_boeing = bs4.BeautifulSoup(
        s.get(salary_url, headers=headers).text,
        'html.parser'
    )
    return parsed_boeing.find_all('div', class_="salaryChartModule")[0]


def salary_string_to_float(salary_string):
    """
    Converts a string like "$154,711 per year" or "$23.92 hourly" to their numeric
    form 154771 and 23.92 respectively
    """
    salary_string = salary_string.strip()
    truncated_salary_string = salary_string[salary_string.find("$")+1 : salary_string.find(" ")]
    return float(truncated_salary_string.replace(",", ""))


def get_titles_and_salaries_from_glassdoor(glassdoor_url):
    """
    Grabs the data from glassdoor and extracts the titles and salary information
    Returns a pandas data frame with a titles and salaries
    Result will be sorted by the numeric form of the salary
    """
    salary_chart = get_salary_chart(glassdoor_url)
    salaries = [s.get_text() for s in salary_chart.find_all('div', class_="meanPay alignRt")]
    titles = [s.get_text() for s in salary_chart.find_all('a', class_="noMargVert jobTitle")]
    return sorted((list(zip(titles, salaries))), key=lambda x: salary_string_to_float(x[1]), reverse=True)


def add_company_to_salaries(company_name, salary_tuples):
    return [(company_name, title, salary) for title, salary in salary_tuples]


def main():
    cisco_salaries = get_titles_and_salaries_from_glassdoor(cisco_url)
    boeing_salaries = get_titles_and_salaries_from_glassdoor(boeing_url)

    print(pd.DataFrame(
        add_company_to_salaries("cisco", cisco_salaries) + add_company_to_salaries("boeing", boeing_salaries),
        columns=["Company", "Title", "Salary"]
    ))

if __name__ == '__main__':
    main()
