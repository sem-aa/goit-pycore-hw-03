import re
from datetime import datetime, timedelta
from random import sample

# Task 1
def get_days_from_today(date: str) -> int:
    try:
        today = datetime.today()
        date = datetime.strptime(date, '%Y-%m-%d')
        return (today - date).days
    except ValueError:
        print('Invalid date format')
        return 'Invalid date format'
    except Exception as e:
        print(e)
        return None

print("get_days_from_today", get_days_from_today('2025-02-22'))

# Task2
def get_numbers_ticket(min, max, quantity):
    return sorted(sample(range(min, max), quantity))

print("get_numbers_ticket", get_numbers_ticket(1, 49, 5))

# Task 3
def normalize_phone(phone_number):
    pattern = r"[^\d+]"
    phone = re.sub(pattern, '', phone_number)
    
    if not phone.startswith('+'):
        if phone.startswith('38'):
            phone = f'+{phone}'
        else:
            phone = f'+38{phone}'
    
    return phone

print('normalize_phone', normalize_phone("38050 111 22 11   "))

# Task 4
def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()
    current_year = today.year
    
    for item in users:
        date = datetime.strptime(item["birthday"], '%Y.%m.%d').date()
        date_this_year = date.replace(year=current_year)
        
        # Checks if the birthday was this year
        if date_this_year < today:
            date_this_year = date.replace(year=current_year + 1)

        diff_days = (date_this_year - today).days  

        if diff_days <= 7:

            # Checks if the birthday fell on a weekend.
            if date_this_year.weekday() in [5,6]:
                numDays = 2 if date_this_year.weekday() == 5 else 1
                date_this_year += timedelta(days=numDays)
                print("date_this_year", date_this_year)

            upcoming_birthdays.append({"name": item['name'], "congratulation_date": date_this_year.strftime("%Y.%m.%d") })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Alice Brown", "birthday": "2000.02.26"}, 
    {"name": "Jane Smith", "birthday": "1990.02.27"},
    {"name": "Bob Johnson", "birthday": "1995.02.28"}, 
    {"name": "Bob Johnson", "birthday": "1995.03.01"}, 
    {"name": "Bob Johnson", "birthday": "1995.03.02"}, 
]


print("get_upcoming_birthdays", get_upcoming_birthdays(users)) 
