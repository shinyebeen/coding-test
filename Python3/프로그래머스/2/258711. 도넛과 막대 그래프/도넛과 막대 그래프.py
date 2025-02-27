# 생성된 정점 : 나가는 간선의 수가 2 이상, 들어오는 간선의 수 0
# 막대모양 그래프 : 나가는 간선의 수 0, 들어오는 간선의 수 1
# 8자모양 그래프 : 나가는 간선의 수 2, 들어오는 간선의 수도 2
# 도넛모양 그래프 : 생성된 정점의 나가는 간선의 수에서 막대모양 그래프와 8자모양 그래프의 개수를 뺌 


def solution(edges):
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]
                
            edge_counts[a][0] += 1 # a는 n번 노드에서 나가는 간선
            edge_counts[b][1] += 1 # b는 n번 노드로 들어오는 간선
        return edge_counts
    
    def check_answer(edge_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edge_counts.items():
            # 생성된 정점 확인
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            
            # 막대모양 그래프 확인
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            
            # 8자모양 그래프 확인
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
            
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3]) # 생성된 정점의 나가는 간선 개수에서 8자, 막대 그래프 수 빼기
        
        return answer

    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)
    
    return answer