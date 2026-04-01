numbers = [2, 5, 8, 6, 3, 2, 9]

even_list = []
odd_list = []

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
        even_sum += num
    else:
        odd_list.append(num)
        odd_sum += num

print("Even numbers:", even_list)
print("Sum of even numbers:", even_sum)

print("Odd numbers:", odd_list)
print("Sum of odd numbers:", odd_sum)
