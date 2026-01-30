from datetime import date, datetime
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birthday = date(2012, 10, 30)
print(f"Age: {calculate_age(birthday)}")

def days_until_event(event_date):
    today = date.today()
    return (event_date - today).days

my_birthday = date(2026, 10, 30)
print(f"Days until my birthday: {days_until_event(my_birthday)}")