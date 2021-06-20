from PIL import Image
import numpy as np


def clip(data):
    if data > 255:
        return 255
    elif data < 0:
        return 0
    else:
        return data


def maskSum(mask):
    if sum(sum(i) for i in mask) <= 0:
        return 1
    else:
        return sum(sum(i) for i in mask)


def borderFill(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 and j == 0:
                arr[i][j] = arr[i + 1][j + 1]
            elif i == 0 and j == len(arr[i])-1:
                arr[i][j] = arr[i + 1][j - 1]
            elif i == len(arr)-1 and j == 0:
                arr[i][j] = arr[i - 1][j + 1]
            elif i == len(arr)-1 and len(arr[i])-1:
                arr[i][j] = arr[i - 1][j - 1]
            elif i == 0:
                arr[i][j] = arr[i + 1][j]
            elif j == 0:
                arr[i][j] = arr[i][j + 1]
            elif j == len(arr[i])-1:
                arr[i][j] = arr[i][j - 1]
            elif i == len(arr)-1:
                arr[i][j] = arr[i - 1][j]
    return arr


def konvolusi(arr, mask):
    data = np.zeros(arr.shape, dtype='u1')
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            try:
                data[i][j] = [(clip((
                    arr[i - 1, j - 1][x] * mask[0][0] +
                    arr[i - 1, j + 1][x] * mask[0][2] +
                    arr[i - 1, j][x] * mask[0][1] +
                    arr[i, j - 1][x] * mask[1][0] +
                    arr[i, j][x] * mask[1][1] +
                    arr[i, j + 1][x] * mask[1][2] +
                    arr[i + 1, j - 1][x] * mask[2][0] +
                    arr[i + 1, j][x] * mask[2][1] +
                    arr[i + 1, j + 1][x] * mask[2][2]
                ) / maskSum(mask))) for x in range(3)]

            except:
                data[i][j] = clip((
                    arr[i - 1, j - 1] * mask[0][0] +
                    arr[i - 1, j + 1] * mask[0][1] +
                    arr[i - 1, j] * mask[0][2] +
                    arr[i, j - 1] * mask[1][0] +
                    arr[i, j] * mask[1][1] +
                    arr[i, j + 1] * mask[1][2] +
                    arr[i + 1, j - 1] * mask[2][0] +
                    arr[i + 1, j] * mask[2][1] +
                    arr[i + 1, j + 1] * mask[2][2]
                ) / maskSum(mask))

    return data


unweighted = [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]]

gaussian = [[7, 9, 7],
            [9, 7, 9],
            [7, 9, 7]]

sharper = [[0, -1, 0],
           [-1, 5, -1],
           [0, -1, 0]]

intensified_sharper = [[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]]


