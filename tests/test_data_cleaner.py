from decimal import Decimal

from glassdoor_analysis.data_cleaner import normalize_salaries, salary_to_number, handle_vauge_salaries


def test_handle_vauge_salaries():
    assert handle_vauge_salaries('About $83k - $119k'.split()) == 119000
    assert handle_vauge_salaries('About $33 - $35 hourly'.split()) == 72800

def test_salary_to_number():
    assert salary_to_number('$23.92 hourly') == 49753.600000000006
    assert salary_to_number('$62,164 per year') == 62164
    assert salary_to_number('About $83k - $119k') == 119000

def test_normalize_salaries():
    start_data = [
        ('Intern - Hourly', '$23.92 hourly'),
        ('Financial Analyst ', '$62,164 per year'),
        ('Senior Software Engineer ', 'About $83k - $119k'),
        #('Senior Software Engineer ', 'Around $83k - $119k'), # fake
        #('Financial Analyst ', '$62,164 per minute'), # fake
        #('Financial Analyst ', '$62,164.47'), # fake
    ]

    expected_restult = [
        ('Intern - Hourly', 49753.600000000006),
        ('Financial Analyst ', 62164),
        ('Senior Software Engineer ', 119000),
        #('Senior Software Engineer ', 119000), # fake
        #('Financial Analyst ', 7758067200),  # fake
        #('Financial Analyst ', 62164.47) #fake
    ]
    assert normalize_salaries(start_data) == expected_restult