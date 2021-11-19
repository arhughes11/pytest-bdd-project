
def main(year_of_birth, month_of_birth):
    normal_retirement_age = find_retirement_age(year_of_birth)
    output_retirement_age_results(normal_retirement_age)
    year, months = calculate_retirement_date(year_of_birth, month_of_birth, normal_retirement_age)
    output_retirement_date_results(year, months)

def output_retirement_age_results(normal_retirement_age):
    print('Your full retirement age is ' + str(normal_retirement_age[0]) + ' and ' + \
          str(normal_retirement_age[1]) + ' months. ')


def output_retirement_date_results(year, months):
    print('This will be in ' + month_switch(months) + ' of ' + str(year))

def find_retirement_age(year_of_birth):
    if year_of_birth <= 1937 and year_of_birth >= 1900:
        return [65, 0]
    elif year_of_birth < 1943:
        return year_switch(year_of_birth)
    elif year_of_birth < 1955:
        return [66, 0]
    elif year_of_birth < 1960:
        return year_switch(year_of_birth)
    else:
        return [67, 0]


def year_switch(year_of_birth):
    switch = {
        1938: [65, 2],
        1939: [65, 4],
        1940: [65, 6],
        1941: [65, 8],
        1942: [65, 10],
        1955: [66, 2],
        1956: [66, 4],
        1957: [66, 6],
        1958: [66, 8],
        1959: [66, 10]
    }
    return switch.get(year_of_birth)


def month_switch(int_month):
    switch = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    return switch.get(int_month)

def calculate_retirement_date(year_of_birth, month_of_birth, normal_retirement_age):
    months = month_of_birth + normal_retirement_age[1]
    year = year_of_birth + normal_retirement_age[0]

    if months > 12:

        months = months % 12
        year += 1
    return [year, months]

main(1900, 4)