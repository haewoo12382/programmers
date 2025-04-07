def solution(arr):
    answer = [10]

    for idx, num in enumerate(arr):        
        if num != answer[-1]:
            answer.append(num)
        
    answer.remove(10)    
    return answer

solution([1,1,3,3,0,1,1])