from decimal import Decimal

from glassdoor_analysis.data_cleaner import normalize_salaries


def test_normalize_salaries():
    start_data = [
        ('Intern - Hourly', '$23.92 hourly'),
        ('Financial Analyst ', '$62,164 per year'),
        ('Senior Software Engineer ', 'About $83k - $119k'),
        #('Project Manager/Computer and Info Systems Manager ', 'About $88k - $95k'),
        #('SVT Engineer II - Hourly', 'About $33 - $35 hourly'),

    ]

    expected_restult = [
        ('Intern - Hourly', 49753.600000000006),
        ('Financial Analyst ', 62164),
        (),
        #(),
        #(),
    ]
    assert normalize_salaries(start_data) == expected_restult