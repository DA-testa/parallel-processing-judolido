# python3
import heapq

def parallel_processing(n, m, D):
    output = []
    thread = [(0,i)for i in range(n)]
    heapq.heapify(thread)
    
    for i in range(m):
        time, index = heapq.heappop(thread)
        output.append((index,time))
        heapq.heappush(thread, (time+D[i], index))
        
        
    return output

def main():
    
    n, m = map(int, input().split())
    
    D = list(map(int, input().split()))
    
    assert 1<=n<=10**5
    assert 1<=m<=10**5
    assert len(D) == m
    assert all(0<=ti<=10**9 for ti in D)

    result = parallel_processing(n,m,D)
    
    for index, bgTm in result:
        print(index, bgTm)



if __name__ == "__main__":
    main()
