import sys
import os

"""
Your program should open the input text files, 
1. echo the processed input to the screen, 
2. make the necessary calculations, 
3. and then output the checksum to the console (terminal) screen in the format described below.

The input file specified as the first command line argument, will consist of 
the valid 8 bit ASCII characters normally associated with the average text file. 
This includes punctuation, numbers, special characters, and whitespace.

1. Collect the command line input arguments and print them to the console. 
Remember to remove or comment out this test code when running the testing scripts.
2. Read the file and print it out to the console.
3. Adjust the out put to print 80 characters per line.
4. Calculate the 8 bit checksum. Remember that the checksum is a running total with no overflow.
5. Resolve the calculations and padding for both 16 and 32 bit checksums.    
    
"""
# create a throw error message function 
# hex(255)
def throw_error(msg: str) -> None:
    ...

def calculate_checksum(size: int):
    """
    Divide input into uniform words (e.g., 2 byte blocks) of the checksum size

    Add all the words as unsigned binary numbers, discarding any overflow bits

    Interpret the result as a two’s complement number

    Use the negation of the result as the checksum value

    Append the checksum value to the end of the input

    >>> calculate_checksum()
    1
    >>> calculate_checksum("hello")
    output

    """
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

    num: int = 0xB37F19
    num: str = 'B37F19'
    num = num.lower()
    bin
    print(num)
    binary_str = ''

    for digit in num:
        print(hex_dict[digit])
        binary_str += hex_dict[digit]


    digit1 = hex_dict[num[0]]
    digit2 = hex_dict[num[1]]
    print(digit1, digit2)

    sum = bin(int(digit1, 2) + int(digit2, 2))
    print(bin(int(digit1, 16) + int(digit2, 16)))
    print(sum)
    print(int(sum, 2))

    # twos compliment
    # 1110 -> 0001 + 1 = 0010

    # 1110 
    # 0010
    # 10000
    # # size = 8
    # # div: num / size
    # print()

    return 0
    

def validate_check_sum_size(file: str):
    """
    Divide into words and add them up in same manner, including the checksum
    If result is not a word full of zeroes, then a change has occurred
    NOTE: a single-bit error will be detected, but likelihood of 2 errors in the
    same column being undetected is 1/n, where n = #bits in word.
    """
    ...

def format_checksum():
    """

    printf("%2d bit checksum is %8lx for all %4d chars\n", checkSumSize, checksum, characterCnt);


    """
    ...


# Input the required file name and the checksum size as command line parameters
def main():

    # file_name = sys.argv[1]
    # checksum_size = sys.argv[2]

    sys.stderr.write("This is an error message \n")

    # file = open(f"{file_name}", "r") 

    # s = 'The quick brown fox jumps over the lazy dog.'.encode('utf-8')
    # print(s.hex())

    os.system("echo Print this to the screen")
    calculate_checksum(8)

if(__name__ == "__main__"):
    main()