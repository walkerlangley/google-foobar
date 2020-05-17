def solution(x,y):
    if len(x) > len(y):
        longest = sorted(x, key=lambda x: int(x))
        shortest = sorted(y, key=lambda x: int(x))
    else:
        longest = sorted(y)
        shortest = sorted(x)
    for i, x in enumerate(longest):
        yval = shortest[i]
        if yval == x:
            continue
        else:
            print('ID: ', x)
            break


solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
solution({13, 5, 6, 2, 5}, {5, 2, 5, 13})
solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50})
solution(['13', 5, 6, 2, 5], [5, 2, 5, 13])
