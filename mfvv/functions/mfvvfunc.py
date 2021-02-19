from datetime import date

def calculate_age(birth_date):
    today = date.today()
    y = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        y -= 1
    return y


if __name__ == '__main__':
    print(calculate_age(date(1965, 9, 27)))
