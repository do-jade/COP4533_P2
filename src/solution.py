import sys
from collections import deque

def fifo(k, m):
    cache = deque()
    cacheSize = len(cache)
    cacheMiss = 0

    for i in m:

        if i in cache:
            # Hit
            continue

        else:
            # Miss
            if cacheSize < k:
                cache.append(i)
                cacheSize += 1
                cacheMiss += 1

            else:
                cache.popleft()
                cache.append(i)
                cacheMiss += 1
        
    return cacheMiss


k = 3
m = [1, 2, 3, 4, 1, 2, 5, 1]

print(fifo(k, m))