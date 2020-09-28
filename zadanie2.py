seconds = int(input('Enter seconds'))
minutes = 0
hours = 0

while seconds >= 3600:
    hours += 1
    seconds -= 3600
while seconds >= 60:
    minutes += 1
    seconds -= 60

print(f"{hours}:{minutes}:{seconds}")
