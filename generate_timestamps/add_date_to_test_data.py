import csv
import datetime, time
import random
import calendar
import holidays

rows = []
csvfile = '../original_data/test.csv'
training_data = list()
holidays = holidays.UnitedStates()

with open(csvfile, 'r') as original:
    reader = csv.reader(original)
    cnt = 1
    for row in reader:
        if cnt == 1:
            row.append("YEAR")
            row.append("MONTH")
            row.append("DAY")
            row.append("DAY_OF_WEEK")
            row.append("HOUR")
            row.append("MINUTE")
            row.append("IS_HOLIDAY")
        else:
            year = random.randint(2010, 2011)
            month = random.randint(1, 12)
            date_range = calendar.monthrange(year, month)[1]
            day = random.randint(1, date_range)
            is_weekday = datetime.date(year, month, day).weekday()
            is_holiday = datetime.date(year, month, day) in holidays
            hour = random.randint(0, 24)

            if is_holiday == True:
                is_holiday = 1
            else:
                is_holiday = 0

            row.append(year)
            row.append(month)
            row.append(day)
            row.append(is_weekday)
            row.append(hour)
            row.append(random.randint(0, 59))
            row.append(is_holiday)
        rows.append(row)
        cnt += 1;


    output = csv.writer(open('../generated_data/testing_with_dates.csv', 'w'), delimiter=',')
    output.writerows(rows)
