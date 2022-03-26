import threading
from time import sleep

timeout = 0.05

def simple_threaded_for(func, args_list):

    global timeout

    #for each iteration, launch a thread
    threads_array = []
    reps = len(args_list)

    for i in range(reps):
        t = threading.Thread(target=func, args=(args_list[i],))
        t.start()
        threads_array.append(t)

    #wait for each thread to complete
    for i in range(reps):
        threads_array[i].join()
        if(threads_array[i].is_alive):
            sleep(timeout)

    return 0


def matrix_threaded_for(func, matrix):

    global timeout

    #for each iteration, launch a thread
    threads_array = []

    reps_y = len(matrix)

    for i in range(reps_y):
        reps_x = len(matrix[i])
        for j in range(reps_x):
            args_list = (matrix,i,j)
            t = threading.Thread(target=func, args=(args_list,))
            t.start()
            threads_array.append(t)

    #wait for each thread to complete
    for i in range(len(threads_array)):
        threads_array[i].join()
        if(threads_array[i].is_alive):
            sleep(timeout)

    return 0
