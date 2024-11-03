from datetime import datetime, timedelta

def get_upcoming_birthdays(user_dict):
        """
        The function should determine list of people whose birthdays are in next 7 days including the current day.
        If the birthday falls on a weekend, the date of the greeting is moved to the following Monday.
        """
        current_date = datetime.today().date()
        
        # Find users whose birthdays are within the next 7 days
        upcoming_birthdays = []
        for username, user in self.data.items():
            # Create birthday for the current year
            if user.birthday:
                current_year_birthday = user.birthday.value.replace(year=current_date.year)
                
                # If the birthday has already passed, skip to next year
                if current_year_birthday < current_date:
                    current_year_birthday = current_year_birthday.replace(year=current_date.year + 1)

                difference = (current_year_birthday - current_date).days

                # Check if the birthday is within the next 7 days
                if 0 <= difference <= 7:
                    # Check if the birthday falls on a weekend (Saturday or Sunday)
                    if current_year_birthday.weekday() in [5, 6]:  # Saturday or Sunday
                        # Move to next Monday
                        next_monday = current_year_birthday + timedelta(days=(7 - current_year_birthday.weekday()))
                        upcoming_birthdays.append({'name': username, 'congratulation_date': str(next_monday)})
                    else:
                        upcoming_birthdays.append({'name': username, 'congratulation_date': str(current_year_birthday)})

        return upcoming_birthdays
