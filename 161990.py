def solution(wallpaper):
    startX = 50
    startY = 50
    endX = 0
    endY = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                print(i, j)
                if i < startX:
                    startX = i
                if j < startY:
                    startY = j
                if i > endX:
                    endX = i
                if j > endY:
                    endY = j
    answer = []
    answer.append(startX)
    answer.append(startY)
    answer.append(endX+1)
    answer.append(endY+1)
    print(answer)
    return answer

solution(["..", "#."])