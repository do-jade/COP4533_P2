COP4533 Programming Assignment 2

Team Members:
Dohyun Lee (UFID: 92659157)
Charan Sriram (UFID: 73870076)

Project Structure

data: Contains test file inputs for written component portion  
src: Contains the solution code for the coding component portion  
tests: Contains one input and one expected output file  
written: Contains pdf file answers for written component  

How to run:
Enter PYTHON command below to test existing input file:
python3 src/solution.py tests/input.txt

Replace tests/input.txt with own file if wish. 

Written Portion:  
**Question 1:**  
- Look at written/question1.pdf for a slightly better formatted answer. We included it here though for continuity and as you requested they all be in the README  
Input File | k | m | FIFO | LRU | OPTFF  
waQ1T1.txt | 4 | 60 | 60 | 60 | 18  
waQ1T2.txt | 5 | 55 | 42 | 38 | 25  
waQ1T3.txt | 3 | 50 | 46 | 46 | 35  

Does OPTFF have the fewest misses?
- Yes, based on the three test inputs,
OPTFF has the fewest misses among FIFO, LRU, OPTFF.
This difference is most evident in waQ1T1 that uses
a cyclic pattern of five items with a k size of 4.

How does FIFO compare to LRU?
- Files 1 and 3 are tied, but waQ1T2 is where LRU slightly
outperforms FIFO because items 1, 2, and 3 appears more
repeatedly throughout the sequence than the other items.
LRU will hold on to more recently accessed items, so they
stay protected from eviction than FIFO, where the recency
of the item appearing does not affect the eviction.

**Question 2:**  
- In theory just thinking about the scenario, there should be a sequence that has less misses than LRU or FIFO. This would mean the sequence needs to make these two throw out something that will be needed very soon. To keep it simple I did a sequence of 4 items, and found that 2, 4, 6, 8, 2, 4, 6, 8 is a valid sequence that proves my point. FIFO and LRU both have 8 misses, while OPTFF has only 5.

**Question 3:**  
- Okay to prove OPTFF is Optimal, I will do a proof by contradiction. So lets say then that OPTFF is not optimal. This means there is another offline algorithm labeled A that has a lower number of misses than OPTFF for a fixed sequence. Lets look at the earliest situation where OPTFF now has more misses than A in the fixed sequence. At this request, OPTFF will miss while A gets a cache hit. This means that the requested page would have to not be in the OPTFF cache, but present in A's cache. However, this cannot happen in a fixed sequence as OPTFF will always choose to evict the page furthest from use and since we are looking at the first point in the sequence where this happens, the two algorithms would have had to have the same number of misses. For this to actually occur, earlier OPTFF would have had to evict a page, lets call it x, and A would have had to keep x and evict a different page, lets call it y. Since OPTFF evict the furthest page from use, the next use of x must be at least as late as the next use of y. Since y is needed no later than x, A would have to have a miss on y before or at the same time as OPTFF misses on x, meaning they cannot have the same number of misses before this point. This contradicts being the earliest point of eviction where A becomes better, and as such shows there is no offline Algorithm A that exists. Thus OPTFF is optimal.
