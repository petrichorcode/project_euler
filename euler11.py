from math import copysign

data = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
product_check = []
show_messages = True

def debug(msg,indent=0):
    if show_messages:
        print(' '*indent,msg)

def multiply_adjacent(row_start, col_start):
    global proceed
    actions = [
        { 'name': 'left'  ,'row_inc':  0 ,'col_inc':  3, 'diag':False },
        { 'name': 'right' ,'row_inc':  0 ,'col_inc': -3, 'diag':False },
        { 'name': 'down'  ,'row_inc':  3 ,'col_inc':  0, 'diag':False },
        { 'name': 'up'    ,'row_inc': -3 ,'col_inc':  0, 'diag':False },
        { 'name': 'lrtd'  ,'row_inc':  3 ,'col_inc':  3, 'diag':True }, #Left to Right, Top down
        { 'name': 'lrbu'  ,'row_inc': -3 ,'col_inc':  3, 'diag':True }, #Left to Right, Bottom up
        { 'name': 'rltd'  ,'row_inc':  3 ,'col_inc': -3, 'diag':True }, #Right to Left, Top down
        { 'name': 'rlbu'  ,'row_inc': -3 ,'col_inc': -3, 'diag':True }  #Right to Left, Bottom up
    ]
    for a in actions:
        product = 1
        row_inc, col_inc, is_diagonal, direction = a['row_inc'], a['col_inc'], a['diag'], a['name']
        debug({'direction':direction, 'row_start':row_start, 'col_start':col_start},5)
        
        row = row_start
        row_terminate = (row_start + row_inc)
        debug([(row + row_inc) < len(data), row, row_inc, len(data)],15)
        if row_terminate < len(data):
            while row != row_terminate:
                col = col_start
                debug([(col + col_inc) < len(data[row]), col, col_inc, len(data[row])],20)
                col_terminate = (col_start + col_inc)
                if col_terminate < len(data[row]):
                    loop_once = False
                    while col != col_terminate or loop_once is False:
                        loop_once = True
                        try:
                            debug({'row':row, 'col':col, 'number':data[row][col], 'action':a},8)
                            product *= data[row][col]
                        except IndexError:
                            debug([row,col,'out of bounds'])
                            product = 0 
                        #increment or decrement the counter depending on the direction 
                        col += int(copysign(1,col_inc))
                        #if the direction is diagonal adjust the row count at the same time as the column
                        if is_diagonal: row += int(copysign(1,row_inc))
                        #Reset the row override 
                row += int(copysign(1,row_inc))
                if row != row_terminate: proceed = True
                #ignore invalid or tiny products
                if product > 1:
                    #record the product and where it started
                    product_check.append({ 
                        'direction': a['name'], 
                        'row_index': row_start,
                        'column_index': col_start,
                        'starting_number': data[row_start][col_start],
                        'product': product
                    })

#iterates through all possible starting points for all directions
row_index = 10
while row_index < 11: #len(data):
    col_index = 10
    debug(['Row loop:',row_index,len(data)],1)
    while col_index < 11: #len(data[row_index]):
        debug(['Column loop:',col_index,len(data[row_index])],2)
        multiply_adjacent(row_index,col_index)
        col_index += 1
    row_index += 1

#Return max product, starting point, and direction
max_product = max(i['product'] for i in product_check)
for i in product_check:
    if i['product'] == max_product:
        print('')
        print('The max product of any 4 adjacent numbers in any direction is:')
        print(i)