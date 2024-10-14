n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = (start+end) // 2
        current = array[0]
        count = 1

        # 1 2 3 4 * * * 8 9
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid

        else:
            end = mid - 1 

start = 1
end = house[-1] - house[0]
answer = 0

binary_search(house, start, end)
print(answer)