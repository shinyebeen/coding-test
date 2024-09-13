def solution(tickets):
    # tickets 정렬
    tickets.sort(key=lambda x : (x[0], x[1]))
    
    def DFS(t, path):
        
        if len(t) == 0:
            return path
        
        now = path[-1]
        valid_idx = -1
        
        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break
        
        if valid_idx == -1:
            return []
        
        while t[valid_idx][0] == now:
            nxt_path = DFS(t[:valid_idx] + t[valid_idx+1:], path + [t[valid_idx][1]])
            
            if nxt_path != []:
                return nxt_path
        
            valid_idx += 1
        
        return []

    return DFS(tickets, ["ICN"]) 
        