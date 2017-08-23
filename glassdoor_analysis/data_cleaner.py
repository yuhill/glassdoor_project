from decimal import Decimal, ROUND_DOWN

HRS_PR_WK = 40
WKS_PR_YR = 52

def handle_vauge_salaries(salary_split):
    """
    This handles salaries that contain about and a range like
    "About $83k to 119k"
    salary_split is a list of strings like such ["About, "83k", "to" "119k"]
    """
    if 'hourly' in salary_split:
        return float(salary_split[-2][1:]) * HRS_PR_WK * WKS_PR_YR
    else:
        return float(salary_split[-1][1:-1]) * 1000


def salary_to_number(salary):
    salary_split = salary.split()
    if salary_split[1] == 'hourly':
        first_element = salary_split[0][1:].replace(',', '')
        yearly_salary = float(first_element) * HRS_PR_WK * WKS_PR_YR
        return yearly_salary
    elif salary_split[1] == 'per':
        first_element = salary_split[0][1:].replace(',', '')
        return(float(first_element))
    elif salary_split[0] == 'About':
        return (handle_vauge_salaries(salary_split))
    else:
        last_element = salary_split[1][1:].replace('k', '')
        return (float(last_element))

def normalize_salaries(input_salaries):
    salary_data = list()
    for line in input_salaries:
        title, salary = line
        salary = salary_to_number(salary)
        salary_data.append((title, salary))
    return salary_data
