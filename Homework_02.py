def isLeap(year):
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return isLeapYear


# test for leap year
print(isLeap(2000))
print(isLeap(2400))

# test for not leap year
print(isLeap(2100))
print(isLeap(2300))
print(isLeap(1800))