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
# Start at zero just as a choice
notify = ng.push(0)
assert not notify

# First price is between lo and hi
notify = ng.push(45)
assert not notify

# A value greater than hi is pushed, generate a notif
notify = ng.push(55)
assert notify

# This value is bigger than hi, but we just generated a notif so don't do it again
# Note: we also probably will want an "all time high" notification, but here
#       i'm just thinking about crossing the hi threshold
notify = ng.push(60)
assert not notify

# Push a value below hi, but above the lo threshold
notify = ng.push(45)
assert not notify

# Push a value above hi, but no notif bc we haven't passed below lo
notify = ng.push(55)
assert not notify

# Pass below lo, no notif
notify = ng.push(30)
assert not notify

# pass the hi threshold after the lo threshold was crossed, generate a notif
notify = ng.push(55)
assert notify



