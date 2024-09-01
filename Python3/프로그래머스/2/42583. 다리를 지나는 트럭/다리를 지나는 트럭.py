from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    answer = 0
    bridge_weight = 0
    
    while len(truck_weights) > 0:
        
        bridge_weight -= bridge.popleft()
        
        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
            
        else:
            bridge.append(0)
                
        answer += 1
    
    answer += bridge_length
    
    return answer