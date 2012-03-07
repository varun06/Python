#Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

#define a procedure, how_many_days,
#that takes as input a number
#representing a month, and outputs
#the number of days in that month.

#how_many_days(1) => 31
#how_many_days(9) => 30
def how_many_days(month):
    days = days_in_month[month-1]
    return days
    
print how_many_days(1)
print how_many_days(9)
print how_many_days(12)
    
