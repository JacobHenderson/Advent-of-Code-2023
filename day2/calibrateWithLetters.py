## JacobHenderson
## Advent of Code 2023 - https://adventofcode.com/2023/day/1

'''
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.

What is the sum of all of the calibration values?
 
'''

# EX)
# two1nine - 29
# eightwothree - 83
# abcone2threexyz - 13
# xtwone3four - 24
# 4nineeightseven2 - 42
# zoneight234 - 14
# 7pqrstsixteen - 76

import re # Regex Cheatsheet, my dearest - https://www.dataquest.io/blog/regex-cheatsheet/

def calibrate(txt):

    with open(txt) as input:

        sum = 0
        nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        numb = '|'.join(nums)


        for value in input:
            print('===')
            regexD1 = r'[1-9]'
            regexD2 = r'([1-9])(?!.*[1-9])'
            # regexL1 = r'(?:{one|two|three|four|five|six|seven|eight|nine})'
            # regexL2 = r'(?:{one|two|three|four|five|six|seven|eight|nine})(?!.*{one|two|three|four|five|six|seven|eight|nine})'
            regexL1 = r'(?:{})'
            regexL2 = r'(?:{})(?!.*{})'

            indices = []
            digits = []

            # Find values & indices of first/last digit 0-9
            valueD1 = re.search(regexD1, value).group()
            valueD2 = re.search(regexD2, value).group()
            print(f'Value: {value}')
            print(f'valueD1: {valueD1}')
            print(f'valueD2: {valueD2}')
            print(f'd1 index: {value.find(valueD1)}')
            print(f'd2 index: {value.find(valueD2)}')
            indices.append(value.find(valueD1))
            indices.append(value.find(valueD2))


            # Find indices of first/last digit written out

            valueL1 = re.search(regexL1.format(numb, numb), value)
            valueL2 = re.search(regexL2.format(numb, numb), value)

            if valueL1 != None:
                print(f'valueL1: {valueL1.group()}')
                print(f'L1 index: {value.find(valueL1.group())}')
                indices.append(value.find(valueL1.group()))
            else:
                print('999')
                indices.append(999999999)
                

            if valueL2 != None:
                print(f'valueL2: {valueL2.group()}')
                print(f'L2 index: {value.find(valueL2.group())}')
                indices.append(value.find(valueL2.group()))
            else:
                print('-1')
                indices.append(-1)


            
   #         print(f'valueL2: {valueL2}')
   #         
   #         


            # 1st digit num appears before the 1st written number
            if indices[0] < indices[2]:
                print(f'valueD1: {valueD1}')
                digits.append(valueD1)
            else: # 1st written number is first
                valueL1 = txtToInt(valueL1)
                print(f'valueD2: {valueL2}')
                digits.append(valueL1)

            if indices[1] > indices[3]:
                digits.append(valueD2)
            else: 
                valueL2 = txtToInt(valueL2)
                digits.append(valueL2)

            # Join the digits into a two-digit number, and add to total
            print(f'Digits: {digits}')
            print(f'Digits Added: {int("".join(digits))}')
            print('---')
            sum += int(''.join(digits))
            # Find first and last digits
    
    print(sum)

def txtToInt(value):
    if value == 'one':
        return '1'
    elif value == 'two':
        return '2'
    elif value == 'three':
        return '3'
    elif value == 'four':
        return '4'
    elif value == 'five':
        return '5'
    elif value == 'six':
        return '6'
    elif value == 'seven':
        return '7'
    elif value == 'eight':
        return '8'
    else:
        return '9'

calibrate('input.txt')
