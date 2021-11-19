from pytest_bdd import parsers, given, then, scenario

import sys
sys.path.insert(0, '/Users/andrewhughes/Desktop/full_retirement_age')
from full_retirement_age import find_retirement_age, calculate_retirement_date



EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'year_of_birth': int,
    'month_of_birth': int,
    'retirement_age': int,
    'retirement_month': int,
    'future_year': int,
    'future_month': int,
}

@scenario('../features/full_retirement_age.feature', 'User looks for retirement age and retirement date')
def test_add():
    pass    # Whatever is in here gets executed after all of the scenario steps

# Fixtures
# @pytest.fixture():


# Given Steps

@given(parsers.parse('year_of_birth is entered as {year_of_birth:d}', \
       target_fixture='setup'))
@given(parsers.parse('month_of_birth is entered as {month_of_birth:d}', \
       target_fixture='setup'))
def setup(birth_year, month_of_birth):
    return find_retirement_age(year_of_birth=birth_year, month_of_birth=month_of_birth)


@then(parsers.parse('the program displays Your full retirement age is {retirement_age:d}' \
                      'and {retirement_month:d} months.'))
def correct_retirement_age(setup, retirement_age, retirement_month):
    assert setup[0] == retirement_age
    assert setup[1] == retirement_month
    return [retirement_age, retirement_month]

@then(parsers.parse('This will be in {future_month:d} of {future_year:d}'))
def future_retirement_date(correct_retirement_age, year_of_birth, month_of_birth, future_month, future_year):
    assert calculate_retirement_date(year_of_birth, month_of_birth,
            correct_retirement_age) == [future_year, future_month]


