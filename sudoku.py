'''
COMP 1405 - Fall 2020
Assignment #3

Name: Quynh Vo
ID: 101203972
Comments: set default filename in this program is 'puzzle1.csv'
'''

from typing import List
#------------------------------------------------------------------#
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            row = [int(val) for val in line.split(",")]
            puzzle.append( row )
    return puzzle

#------------------------------------------------------------------#
#------------------------------------------------------------------#

def puzzle_to_string(puzzle):
    '''
    Print puzzle in sudoku format
        puzzle_to_string(puzzle:list[list[int]]) ->
    '''
    for row_index in range(len(puzzle)):    # each row index in puzzle
        tmp = []
        for el_index in range(len(puzzle[row_index])):  # for each element in each row
            temp = str(puzzle[row_index][el_index])   
            if el_index == 2 or el_index == 5:
                a = temp + ' |'     # | after 3 numbers
                tmp.append(a)       # append a to empty list when index = 2 or 5 
            else:
                tmp.append(temp)    # append str el into empty list if index isn't 2 or 5
        for i in range(len(tmp)):
            if tmp[i] == '0':
                tmp[i] = ' '
            if tmp[i] == '0 |':
                tmp[i] = '  |'
        print(" ".join(tmp))        

        if row_index == 2 or row_index == 5:    # print the dividing symbols for every 3 row
            print('------+-------+-------')
        

def check_rows(puzzle : List[List[int]] ) -> List[int]:
    '''
    Check if each row in puzzle is invalid
    Return list of invalid index of rows 
        check_rows(puzzle : list[list[int]] ) -> list[int]
    '''
    temp = []
    for row in puzzle:
        dic = {}
        if row :   # if len(row) != 0
            for el in row:
                # check row if digits in 0-9
                if (0 <= el <= 9) == False:    
                    invalid_index = puzzle.index(row)
                    #print(invalid_index)
                    temp.append(invalid_index)
                    break
                # check if digit is duplicated.
                if el in dic:
                    if el != 0:
                        temp.append(puzzle.index(row))
                        break
                else:
                    dic[el] = 1
    return temp
            


def check_columns(puzzle : List[List[int]] ) -> List[int]:
    '''
    Check if each column in puzzle is invalid
    Return list of invalid index of columns 
        check_columns(puzzle : list[list[int]] ) -> list[int]
    '''
    temp = []
    # take each column -> make a new list
    for i in range(len(puzzle)):
        column = []
        for row in puzzle:
            column.append(row[i])
        #print(column)

        ########################### check for column
        
        dic = {}
        if column :   # if len(col) != 0
            for el in column:
                # check row if digits in 0-9
                if (0 <= el <= 9) == False:    
                    temp.append(i)
                    break
                # check if digit is duplicated.
                if el in dic:
                    if el != 0:
                        temp.append(i)
                        break
                else:
                    dic[el] = 1
    return temp

def check_subgrids(puzzle : List[List[int]] ) -> List[int]:
    '''
    Check if each subgrid in puzzle is invalid
    Return list of invalid index of subgrids 
        check_subgrids(puzzle : list[list[int]] ) -> list[int]
    '''
    temp = []
    # identify 1 subgrid
    for sub_row_index in range(0,3):    
        for sub_col_index in range(0,3): 
            subgrids = []
            # for 1 subrow and 1 subcol will have 1 subgrid inchuding 9 numbers 
            for row_index in range(3 * sub_row_index, 3 * sub_row_index + 3):            # find row index in the puzzle but just take 3 rows
                for col_index in range(3 * sub_col_index, 3 * sub_col_index + 3):        # find col index in the puzzle but just take 3 columns
                    subgrids.append(puzzle[row_index][col_index])                        # take each col in 1 row 
            

    ###################################################### check for subgrid

            dic = {}
            if subgrids :   # if len(row) != 0
                for el in subgrids:
                    # check each number in 1 subgrid if digits in 0-9
                    if (0 <= el <= 9) == False:    
                        temp.append(3* sub_row_index + sub_col_index)
                        break
                    # check if digit is duplicated. 
                    if el in dic: 
                        if el != 0:
                            temp.append(3* sub_row_index + sub_col_index)
                            break
                    else:
                        dic[el] = 1   # in each key (el), set value of each key = 1 to count 
    return temp

#------------------------------------------------------------------#
#------------------------------------------------------------------#



#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions

def main():        
    filename = 'puzzle1.csv'  
    puzzle = load_puzzle(filename)
    puzzle_to_string(puzzle)
    rows = check_rows(puzzle)
    print(rows)
    columns = check_columns(puzzle)
    print(columns)
    subgrids = check_subgrids(puzzle)
    print(subgrids)



#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()