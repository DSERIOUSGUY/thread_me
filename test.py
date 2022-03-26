from thread_lib import matrix_threaded_for


def print_test(temp_matrix):
    data = temp_matrix[0]
    i = temp_matrix[1]
    j = temp_matrix[2]

    print(data,i,j)
    print(data[i][j])


test = [[1,2],[3,4]]

print(test)

matrix_threaded_for(print_test,test)
