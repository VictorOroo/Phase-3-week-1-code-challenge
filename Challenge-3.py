def highest_consonant_value(input_str):
    vowels = set('aeiou')
    max_value = 0
    current_value = 0

    for char in input_str:
        if char.isalpha() and char.lower() not in vowels:
            current_value = max(0,current_value + ord(char) - ord('a') + 1)
            max_value = max(max_value, current_value)
        else:
             current_value = 0

    return max_value  

max_value = highest_consonant_value("strength")
print(max_value)

          