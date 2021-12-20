# from sudoku import *
from sudoku import load_puzzle, puzzle_to_string, check_rows, check_columns, check_subgrids 

def main():
    '''
    Import the file that the user input in
    Take the user's digit which is indicate through the format row, column, digit
    Allow user to play
    Print   if the puzzle was solved or not,
            how many numbers the user entered in total,
            how many numbers the user entered that were invalid.

    '''
    file_name = input('Enter your file name stores the Sudoku game: ')
    puzzle = load_puzzle(file_name)
    print('Current grid')

    count = 0
    count_zero = 0
    # create sets to save the input digits that are invalid
    count_invalid_row = set()
    count_invalid_col = set()
    count_invalid_sub = set()
    
    puzzle_to_string(puzzle)
    flag = True # don't allow user to input again when the puzzle is valid
    flag2 = True # if the user inputs quit
    
    while(flag):
        text = input("Enter move row/col/number(quit to exit): ")
        count += 1   # count the total of inputs
        # when the user inputs quit
        if text == 'quit':
            print('Game has ended.')
            print('Puzzle is NOT completed.')
            print('You entered ' + str(count-1) + ' numbers in total')  #don't count quit
            flag2 = False
            break
    
        if ' ' in text:    # to see if there are any spaces between the inputs and remove the spaces
            text = text.replace(' ', '')
        text_list = text.split(',') 
        row, col, digit = text_list[0], text_list[1], text_list[2]  

        if digit == '0':   # count the number of time the user removes an existing digit
            count_zero += 1
        
        original_digit = puzzle[int(row)][int(col)]  # 
        puzzle[int(row)][int(col)] = int(digit)  # take the user's input to play game
         
        
        # check rows, columns and subgrids to see if the puzzle is valid
        invalid_row_list = check_rows(puzzle)
        invalid_col_list = check_columns(puzzle)
        invalid_sub_list = check_subgrids(puzzle)
        if invalid_row_list != []:
            count_invalid_row.update(invalid_row_list)   # if invalid row list has invalid indexes, update row invalid set 
        elif invalid_col_list != []:
            count_invalid_col.update(invalid_col_list)   # if invalid column list has invalid indexes, update column invalid set
        elif invalid_sub_list != []:
            count_invalid_sub.update(invalid_sub_list)   # if invalid subgrid list has invalid indexes, update subgrid invalid set


        # check if the input digit valid or not
        flag_printPuzzle = True
        if invalid_row_list != [] or invalid_col_list != [] or invalid_sub_list != []:
            flag_printPuzzle = False
            print('That is invalid.')
            puzzle[int(row)][int(col)] = original_digit
            # print(count_invalid_row)
            # print(count_invalid_col)
            # print(count_invalid_sub)

        # if the digit is not invalid -> print the puzzle out
        if flag_printPuzzle == True:
            puzzle_to_string(puzzle)
        
        # no more input when the puzzle is correct
        if len(invalid_row_list) == 0 and len(invalid_col_list) == 0 and len(invalid_sub_list) == 0:
            flag = False   
        
        # if the puzzle still has 0, continue to play
        for line in puzzle:
            if 0 in line:
                flag = True 

    # if the user doesn't input quit and the puzzle is correct    
    if flag2 == True:
        print('The game has ended.')
        print('Puzzle is complete.')
        print('You entered ' + str(count) + ' numbers in total')   
    count_invalid = len(count_invalid_col) + len(count_invalid_row) + len(count_invalid_sub)
    print('You entered ' + str(count_invalid) + ' invalid number')   # if the user doesn't quit, count invalid times
                             

if __name__ == "__main__":
    main()