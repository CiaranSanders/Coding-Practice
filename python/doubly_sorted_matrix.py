# Ciaran Sanders
# May 27, 2021
# given a key k, find k in a doubly sorted matrix

test_matrix_1 = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7],
]

test_matrix_2 = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
]

test_matrix_3 = [
    [1],
]

test_matrix_4 = [
    [1, 4, 8, 10],
    [5, 10, 20, 34],
    [12, 14, 22, 35],
    [100, 101, 102, 105],
]

def find_key(m, k):
    """
    algorithm for finding key k in the doubly sorted matrix m
    :return: a tuple (x,y) for the index of the key k, else None if k is not in m
    """
    h = len(m)
    w = len(m[0])

    def go_up(x, y):
        x -= 1
        return check_index(x, y)

    def go_right(x, y):
        y += 1
        return check_index(x, y)

    def check_index(x, y):
        if x < 0 or y > w-1:
            return None
        if k == m[x][y]:
            return (x, y)
        elif k > m[x][y]:
            return go_right(x, y) 
        elif k < m[x][y]:
            return go_up(x, y) 

    x, y = h-1, 0 
    return check_index(x, y)


if __name__ == '__main__':
    print('searching...')
    index = find_key(test_matrix_1, 5)
    print(index)
    print('searching...')
    index = find_key(test_matrix_3, 5)
    print(index)
    print('searching...')
    index = find_key(test_matrix_4, 20)
    print(index)

