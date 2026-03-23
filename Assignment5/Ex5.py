def remove_odd(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


nums = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd(nums)

print("Original list:", nums)
print("Without odd numbers:", new_list)