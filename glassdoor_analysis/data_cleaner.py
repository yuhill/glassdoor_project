from decimal import Decimal, ROUND_DOWN

HRS_PR_WK = 40
WKS_PR_YR = 52

def normalize_salaries(input_salaries):
    salary_data = list()
    for line in input_salaries:
        title, salary = line
        salary_split = salary.split()
        first_element = salary_split[0][1:].replace(',','')
        if salary_split[1] == 'hourly':
            yearly_salary = float(first_element) * HRS_PR_WK * WKS_PR_YR
            salary_data.append(
                (title, yearly_salary)
            )
        else:
            salary_data.append(
                (title, float(first_element)))
    return salary_data
