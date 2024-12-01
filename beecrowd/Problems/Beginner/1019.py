# Time Conversion

n = int(input())

hours = minutes = seconds = 0

while n >= 3600:
    n -= 3600
    hours += 1

while n >= 60:
    n -= 60
    minutes += 1

while n >= 1:
    n -= 1
    seconds += 1

print(f'{hours}:{minutes}:{seconds}')