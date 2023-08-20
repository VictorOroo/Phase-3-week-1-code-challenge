# Phase-3-week-1-code-challenge

# Phase 3 Week 1(Toy Problems)
#### Created By Victor Oroo on August 20 2023

## Description

- This read me will help you use my python codes to perform the following tasks :


1. Challenge 1: Converting 12-hour time to 24-hour time
   Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") 

   You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

  

   Notes
   By convention, noon is 12:00 pm, and midnight is 12:00 am.

   On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.

 2. Challenge 2: Two numbers are positive.
    
    It has a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

    Examples:
    (2, 4, -3) == True

    (-4, 6, 8) == True

    (4, -6, 9) == True

    (-4, 6, 0) == False

    (4, 6, 10) == False

    (-14, -3, -4) == False 


  3.  Challenge 3: Consonant value
    Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

    Examples;
    For the word "zodiacs", solve("zodiacs") = 26

    For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

    -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

    For the word "strength", solve("strength") = 57.

    The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.


    ## Setup Requirements

- Git
- Github
- Visiual studio Code

## Technologies Used

The following have been used on this project:

- Python 3

## Project Setup
Clone my repository in y(git clone git@github.com:VictorOroo/Phase-3-week-1-code-challenge.git)
follow the following to run the codes for each challenge:
1. Challenge 1 (Convert 12-Hour Time to 24-Hour Time)
- open Challenge-1.py in visual studio code.
- make changes by adding a 12 hour time format in the print() e.g print(convert_12hr_to_24hr("08:30:00"))
- open terminal and  run python3 Challenge-1.py

2. Challenge 2 (Count Exactly Two Positive Numbers)
- open Challenge-2.py in visual studio code.
- make changes by adding three intergers in the print() e.g print(intchecker(3, -2, -3))   
- open terminal and  run python3 Challenge-2.py

3. 

## Support and contact details 🙂

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: victor.oroo@student.moringaschool.com

## License

Copyright (c) 2022 Victor Oroo.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files , to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.