class TimeDuration:
    def __init__(self, hours, minutes):
        self.total_minutes = hours * 60 + minutes
        self.hours = self.total_minutes // 60
        self.minutes = self.total_minutes % 60

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"
    
    def __repr__(self):
        return f"TimeDuration({self.hours}, {self.minutes})"
    
    def __add__(self, other):
        if isinstance(other, TimeDuration):
           return  TimeDuration(0, self.total_minutes + other.total_minutes)
        elif isinstance(other, (int, float)):
            return TimeDuration(0, self.total_minutes + other)
        return NotImplemented
            
    def __eq__(self, other):
        if not isinstance(other, TimeDuration):
            return NotImplemented
        return self.total_minutes == other.total_minutes
    
    def __bool__(self):
        return self.total_minutes > 0
        
t1 = TimeDuration(1, 45)
t2 = TimeDuration(0, 30)
t3 = TimeDuration(2, 15)

print(str(t1))
print(repr(t1))
print(t1 + t2)
print(t1 + 20)
print((t1 + t2) == t3)
print(bool(TimeDuration(0, 0)))
