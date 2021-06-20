# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.

#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.

#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)


def task_19():
    numSundays = 0
    dayOfWeek = 1
    monthlyDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for year in range(1901, 2001):
        if isLeap(year) == True:
            monthlyDays[1] += 1
        for month in monthlyDays:
            for days in range(1, month + 1):
                dayOfWeek += 1
                if dayOfWeek == 7:
                    if days == 1:
                        numSundays += 1
                    dayOfWeek = 0
        if isLeap(year) == True:
            monthlyDays[1] -= 1

    return numSundays

def isLeap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    print(task_19())
    #answer is 171
