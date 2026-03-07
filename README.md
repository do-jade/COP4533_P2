COP4533 Programming Assignment 2

Team Members:
Dohyun Lee (UFID: 92659157)
Charan Sriram (UFID: 73870076)

Project Structure

Written Portion:

Question 1:

Question 2:
- In theory just thinking about the scenario, there should be a sequence that has less misses than LRU or FIFO. This would mean the sequence needs to make these two throw out something that will be needed very soon. To keep it simple I did a sequence of 4 items, and found that 2, 4, 6, 8, 2, 4, 6, 8 is a valid squence that proves my point. FIFO and LRU both have 8 misses, while OPTFF has only 5.


data: Contains test file inputs for written component portion
src: Contains the solution code for the coding component portion
tests: Contains one input and one expected output file
written: Contains pdf file answers for written component

How to run:
Enter command below to test existing input file:
python3 src/solution.py tests/input.txt

Replace tests/input.txt with own file if wish. 
