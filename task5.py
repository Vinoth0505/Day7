class Time:
    """This is sample class"""
    hours=0
    minutes=0
    seconds=0
t=Time()#Creates an instance of class
t.hours=1
t.minutes=20
t.seconds=30

def print_time(t):
    print('%.2d:%.2d:%2d'%(t.hours,t.minutes,t.seconds))
print_time(t)