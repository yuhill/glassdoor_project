from glassdoor_analysis.data_cleaner import example


def test_example():
    assert [2, 3, 4] == example([1, 2, 3])
