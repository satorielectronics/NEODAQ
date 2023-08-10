class NotificationGenerator:
    def __init__(self):
        print("hi there")

    def setLimits(self, lo, hi):
        self.lo = lo
        self.hi = hi

    def push(self, price):
        return False


ng = NotificationGenerator()

ng.setLimits(40,50)
result = ng.push(0)
if not result:
    print("fail")
