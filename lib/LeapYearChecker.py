class LeapYearChecker:
    def __init__(self, fullYear):
        self.year = fullYear
    
    def isLeapYear(self):
        return self.year % 400 == 0 or self.year % 4 == 0 and not self.year % 100 == 0