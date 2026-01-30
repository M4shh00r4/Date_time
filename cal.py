import calendar

oct_cal = calendar.month(3000,10)
print(oct_cal)

year_cal = calendar.calendar(2030)
print(year_cal)

html_cal = calendar.HTMLCalendar()
oct_html = html_cal.formatmonth(2026,10)
print(oct_html)