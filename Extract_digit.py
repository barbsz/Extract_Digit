def reverse_and_space(num):
    reversed_str = str(num)[::-1]
    spaced_str = ' '.join(reversed_str)
    return spaced_str


number = 7536
result = reverse_and_space(number)
print(result)
