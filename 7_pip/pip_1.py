numbers = [-3, 5, -10, 9, -5]
numbers.sort(key=lambda x:(x<0, x))
print(numbers)