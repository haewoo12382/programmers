# def solution(numbers):
#     answer = []    
#     passCnt = 0
#     for i in range(len(numbers)):                            
#         for j in range(i,len(numbers)):                 
#             if len(numbers)-1 > j:               
#                 if numbers[i] < numbers[j+1] :
#                     answer.append(numbers[j+1])                                            
#                     break
#                 else:
#                     passCnt += 1
#             else:
#                 answer.append(-1)    
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for ind, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(ind)
    return answer
solution([9, 1, 5, 3, 6, 2])  

