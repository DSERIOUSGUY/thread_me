from thread_lib import matrix_threaded_rows_for
from multiprocessing import Queue


def print_test(temp_matrix):
    data = temp_matrix[0]

    if(len(temp_matrix)>2):
        args = temp_matrix[1]
        print(args)

    i = temp_matrix[-1]

    print(data[i])


test = [[1,2],[3,4,5]]

print(test)


matrix_threaded_rows_for(print_test,test,["hi"])
