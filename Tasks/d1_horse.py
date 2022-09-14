def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    table = [[0 for i in range(shape[1])] for i in range(shape[0])]
    table[start_point[0]][start_point[1]] = 1

    def path_rec(i, j):
        if 0 <= i <= shape[0] - 1 and 0 <= j <= shape[1] - 1:
            if table[i][j]:
                return table[i][j]
            table[i][j] = sum((path_rec(i + 1, j - 2),
                               path_rec(i - 1, j - 2),
                               path_rec(i - 2, j - 1),
                               path_rec(i - 2, j + 1)
                              ))
            return table[i][j]


        return 0
    return path_rec(*point)