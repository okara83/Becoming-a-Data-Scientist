"""
Day Number of Year
Each year has 365 or 366 days. Given a string date representing a Gregorian calendar date formatted as month/day/year, return the day-number of the year.

Examples
day_of_year("11/16/2020") ➞ 321

day_of_year("1/9/2019") ➞ 9

day_of_year("3/1/2004") ➞ 61

day_of_year("12/31/2000") ➞ 366
Notes
All input strings in tests are valid dates.
"""

def day_of_year(date):
    
    a=date.split("/")
    month, day, year = int(a[0]), int(a[1]), int(a[2])
    if month == 1 : return day
    dict_month={"1":"31", "2":"28", "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31","9":"30", "10":"31","11":"30","12":"31"  }
    dict_month_leap={"1":"31", "2":"29", "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31","9":"30", "10":"31","11":"30","12":"31"  }
    b, c = [], []
    for i in dict_month.values():
        b.append(int(i))
    for i in dict_month_leap.values():
        c.append(int(i))               
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: lst_month = c       
            else: lst_month = b        
        else: lst_month = c        
    else:lst_month = b                  
    d = sum(lst_month[0:(month-1)])
    
    return  (d + day)

#day_of_year("11/16/2020") #➞ 321
#day_of_year("1/9/2019") #➞ 9
#day_of_year("3/1/2004") #➞ 61
day_of_year("12/31/2000") #➞ 366