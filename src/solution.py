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

def lru(k, m):
    cache = deque()
    cacheSize = len(cache)
    cacheMiss = 0

    for i in m:

        if i in cache:
            # Hit
            cache.remove(i)
            cache.append(i)

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

def optff(k, requests):
    occurences = {}
    for i, current in enumerate(requests):
        if current not in occurences:
            occurences[current] = deque()
        occurences[current].append(i)

    cache = set()
    cacheMisses = 0
    for i, current in enumerate(requests):
        occurences[current].popleft()

        # Hit
        if current in cache:
            continue

        # Miss
        cacheMisses = cacheMisses + 1

        if len(cache) < k:
            cache.add(current)
            continue

        evictItem = None
        furthestUse = -1
        for item in cache:
            futureQueue = occurences.get(item)
            if not futureQueue or len(futureQueue) == 0:
                evictItem = item
                break
            followingUseIndex = futureQueue[0]
            if followingUseIndex > furthestUse:
                furthestUse = followingUseIndex
                evictItem = item
        cache.remove(evictItem)
        cache.add(current)

    return cacheMisses

def main():
    if len(sys.argv) < 2:
        print("Type the following to use: python3 src/solution.py tests/inputFile.")
        exit(1)

    inputFile = sys.argv[1]

    try:
        with open(inputFile, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
    except FileNotFoundError:
        print("File not found.")
        exit(1)

    if not lines:
        print("Empty input file")
        exit(1)

    k, m = map(int, lines[0].split())
    requests = list(map(int, lines[1].split()))

    print(f"FIFO  : {fifo(k, requests)}")
    print(f"LRU   : {lru(k, requests)}")
    print(f"OPTFF : {optff(k, requests)}")

if __name__ == "__main__":
    main()
