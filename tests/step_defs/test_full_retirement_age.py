from pytest_bdd import parsers, given, then, scenario
import re

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

@scenario("../features/full_retirement_age.feature", "User looks for retirement age and retirement date")
def test_add():
    pass    # Whatever is in here gets executed after all of the scenario steps


# Given Steps

@given(parsers.parse("year_of_birth is entered as {yob:d} and month_of_birth is entered as {mob:d}"), target_fixture="setup")
def setup2(yob, mob):
    return dict(year_of_birth=int(yob), month_of_birth=int(mob))
    # return [year_of_birth, month_of_birth]       # year_of_birth, month_of_birth


@then(parsers.parse("the program displays Your full retirement age is {retirement_age:d} and {retirement_month:d} months"))
def correct_retirement_age(setup2, retirement_age, retirement_month):
    assert find_retirement_age(setup2[0]) == [retirement_age, retirement_month]
    return find_retirement_age(setup2[0])

@then(parsers.parse("the program displays {future_month:d} of {future_year:d}"))
def correct_retirement_age(setup2, correct_retirement_age, future_month, future_year):
    assert calculate_retirement_date(setup2[0], setup2[1], correct_retirement_age) == [future_year, future_month]



