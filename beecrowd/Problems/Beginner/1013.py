a, b, c = map(int, input().split())

greatest_ab = (a + b + abs(a - b)) // 2

greatest = (greatest_ab + c + abs(greatest_ab - c)) // 2

print(f"{greatest} eh o maior")