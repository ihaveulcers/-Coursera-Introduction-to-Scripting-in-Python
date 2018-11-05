import calendar
import datetime

#input int y = year,  m = month
#return number of days

def days_in_month (y,m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return int(31)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return int(30)
    elif calendar.isleap(y) is True:
        return int(29)
    else:
        return int(28)


# check input validity

def valid_date (y, m, d):
    days = days_in_month(y,m)
    if(datetime.MINYEAR <= y <= datetime.MAXYEAR):
        if (m >=1 and m <=12):
            if (d >=1 and d <=days):
                return True
            else:
                return False
        return False
    return False

print('test date 2018-11-06 is :', valid_date(2018,11,6))


# find the number of days between two periods
# returns 0 if invalid date

def days_between(y1, m1, d1, y2, m2, d2):
    if valid_date(y1, m1, d1) is False or valid_date(y2, m2, d1) is False:
        return 0
    elif datetime.date(y1,m1,d1) > datetime.date(y2,m2,d2):
        return 0
    else:
        return (datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).days

print('test 2018-11-01 to 2018-11-06 is :', days_between(2018,11,1,2018,11,6))


#find the age in days
# returns 0 if invalid

def age_in_days(y,m,d):
    if valid_date(y,m,d) is False:
        return 0
    elif datetime.date.today() < datetime.date(y,m,d):
        return 0
    else:
        return (datetime.date.today() - datetime.date(y,m,d)).days


print('test birthday 2018-11-02 is :',age_in_days(2018,11,2))
