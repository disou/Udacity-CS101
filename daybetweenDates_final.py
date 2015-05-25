__author__ = 'Dis'

# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def daysOfMonth(month, year):
    if isLeapYear(year) and month == 2:
        days_of_month = 29
    elif not isLeapYear(year) and month == 2:
        days_of_month = 28
    else:
        days_of_month = 31 - (month - 1) % 7 % 2
    return days_of_month


def nextDay(year, month, day):
    """ Full Version. Leap Year is taken into account
    >>> nextDay(2000, 12, 31)
    (2001, 1, 1)
    >>> nextDay(2001, 12, 31)
    (2002, 1, 1)

    - November has 30 days:

    >>> nextDay(2000, 12, 30)
    (2000, 12, 31)
    >>> nextDay(2001, 11, 30)
    (2001, 12, 1)

    - In a normal year, February has 28 days:

    >>> nextDay(2001, 02, 28)
    (2001, 3, 1)

    - In a Leap Year, February has 29 days:

    >>> nextDay(2000, 02, 28)
    (2000, 2, 29)
    >>> nextDay(2000, 02, 29)
    (2000, 3, 1)
    """
    if day < daysOfMonth(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def isLeapYear(year):
    """Decide whether the provided year is leap or not
    >>> print isLeapYear(2000)
    True
    >>> print isLeapYear(2400)
    True
    >>> print isLeapYear(2016)
    True
    >>> print isLeapYear(1800)
    False
    >>> print isLeapYear(2015)
    False
    """
    if not year % 4 and year % 100 or not year % 400:
        return True
    return False

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    assert daysOfMonth(12, 2012) == 31
    assert daysOfMonth(12, 2010) == 31
    assert daysOfMonth(11, 2010) == 30
    assert daysOfMonth(7, 2015) == 31
    assert daysOfMonth(8, 2015) == 31
    assert daysOfMonth(2, 2015) == 28
    assert daysOfMonth(2, 2016) == 29

    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
