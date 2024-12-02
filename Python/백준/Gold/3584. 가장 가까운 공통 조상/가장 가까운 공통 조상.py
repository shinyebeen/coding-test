T = int(input())
for _ in range(T):
    n = int(input())
    parent = [0] * (n+1)
    for _ in range(n-1):
        i, j = map(int, input().split())
        parent[j] = i 
    
    a, b = map(int, input().split())
    a_parent, b_parent = [0, a], [0, b] 
        # a 또는 b가 루트노드일 수 있으므로 앞에 0 추가
        # 0이 없으면 자기자신 이전 값을 비교하려고 할 때 에러가 날 수 있음

    # a와 b 각각의 최상위 부모 노드를 a, b에 저장
    while parent[a]:
        a_parent.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b = parent[b]

    i = 1
    while a_parent[-i] == b_parent[-i]:
        i += 1

    print(a_parent[-i + 1])