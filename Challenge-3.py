def extract_consonants(input_text):
    consonants = []

    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_text:
        if char.isalpha() and char.lower() not in vowels:
            consonants.append(char)
    return consonants

print(extract_consonants("hello"))