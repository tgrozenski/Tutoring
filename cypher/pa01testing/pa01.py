import os, sys

# 1 2 3 4 5
# 1 2 3 4 5 
# 1 2 3 4 5

# input the testing files that contain uppercase letters 

# command line argument ???

# distinguish between uppercase and lowercase 

# https://simple.m.wikipedia.org/wiki/File:ASCII-Table-wide.svg

# python3 filename

# bash pa01test.sh pa01.py

# help(parse_file)

# python3 --version -checks the version of python you have downloaded
def parse_file(file) -> list:
    """
    reads only the upper and lowercase letters in the input file 
    into an char array of size 10,000, storing only 
    the appropriate lowercase letters in the character array.
    Lets think through what this function should do here in the docstring

    Input: File 
    Output: returns a list of characters that are uppercase
    Examples: 
    """
    # List list = new List()
    # emptyArr = []
    # emptyArr.append('t')
    # emptyArr.append('y')
    # emptyArr.append('l')
    # print(emptyArr[0:3])

    lowercase_letters = []

    for line in file:
        # any logic in here is line by line of the file
        for char in line:
            if (ord(char) <= 90 and ord(char) >= 65):
                ## this character is uppercase
                pass
            elif (ord(char) <= 122 and ord(char) >= 97):
                # this character is lowercase, the variable char is lowercase
                lowercase_letters.append(char)
                
    #if conditional to check if is uppercase
    return lowercase_letters 


def parse_key(file):
    """
    Lets think through what this function should do here in the docstring
    This function parses the matrix given as a key. We want to write the key into memory as a matrix 
    list. Using whitespace to separate characters.
    """
    #nested for loop to go character by character
    # store the first number as size 
    # create empty matrix list 
    matrix = []
    for line in file:
        # any logic in here is line by line of the file
        subList: list = line.split()
        # adding the new split list into the matrix
        if(len(subList) > 1):
            matrix.append(subList)
    return matrix


def produce_cypher():
    """
    Lets think through what this function should do here in the docstring
    """
    pass


def main():
    # we are getting the command line argument variables
    # command_line_arg1: str = sys.argv[0]
    command_line_arg2: str = sys.argv[1]
    file = open(f"{command_line_arg2}", "r")
    # lowerCaseLetters: list = parse_file(file)
    matrix = parse_key(file)
    print(matrix)    
    ## grab 
    dimensions = 4
    for row in range(dimensions):
        for column in range(dimensions):
            print(matrix[row][column], end=" ")

    # print(lowerCaseLetters)

    # command_line_arg3: str = sys.argv[2]
    # # print(command_line_arg1, command_line_arg2)

    # file = open(f"{command_line_arg2}", "r")
    # for line in file:
    #     # any logic in here is line by line of the file
    #     for char in line:
    #         if (ord(char) <= 90 and ord(char) >= 65):
    #             os.system(f"echo {char}")
                # this character is uppercase
            # elif (ord(char) <=)
        
        # any logic in here is character by character 


    # file2 = open(f"pa01testing/{command_line_arg3}", "r")
    # for line in file2:
    #     print(line)

    # for line in file:
    #     print(line)

    # use make matrix function
    # some function that reads the key
    # txt = "welcome to the jungle"
    # x = txt.split()
    # print(x)

    # matrix = make_matrix(10, 10)
    # for row in range(10):
    #     for column in range(10):
    #         print(matrix[row][column], end=" ")
    #     print()


def make_matrix(c: int, r: int):
    Row = r
    Column = c
    # outer lists 
    matrix = []

    #[1,2,3], 
    #[4,5,6], 
    #[7,8,9]

    # A for loop for row entries
    for row in range(Row):    
        # each inner lists
        a = []
        num: int = 0
        # A for loop for column entries
        for column in range(Column):   
            a.append(num)
            num+=1
        matrix.append(a)
    return matrix


if (__name__ == main()):
    main()