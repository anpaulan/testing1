handle = ('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008')
line = handle.split()
time = line[5]
time = time.split(':')
hour = time[0]
print(hour)
