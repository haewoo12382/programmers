def solution(players, m, k):
    server = 1    
    serverAddTime=[]
    serverInfo = {}
    total = 0
    for i in range(len(players)):
        upCnt = 0        
        if i in serverAddTime:        
            serverAddTime.remove(i)            
            server = server - serverInfo[i]          
        if players[i] >= int(m*server):
            serverAddTime.append(i+k)                 
            print(server)
            cnt = int((players[i]-int(m*(server-1)))/m)
            upCnt = cnt
            serverInfo[i+k] = upCnt
            total += upCnt
            server += cnt
            
        
        print(i, players[i] , server-1 , upCnt)
            
        
    answer = total
    print(answer)
    return answer