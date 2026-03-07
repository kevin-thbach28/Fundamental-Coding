def remove_odds(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


def main():
    original = [1, 2, 3, 4, 5, 6, 7, 8]
    new_list = remove_odds(original)

    print("Original list:", original)
    print("Without odd numbers:", new_list)


main()