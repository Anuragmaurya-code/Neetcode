# Algorithm
#### Bruteforce
Its a sliding window problem the intuitve approach is to just set the window of length k and find max value and then keep doing that for  every window
​
Time complexity=k*(n-k)
​
#### Optimal
​
we will use queue data structure that keeps only the largest element on its 0th index
1. for every element in the nums just put the elements index in the queue based on its value to its appropriate position
2. now check if the biggest element in queue is in the bound of the window (l<q[0]) else just pop
3. if the window is of appropriate length i.e the initial window is set the just append to output the biggest queue value and increment left pointer
4. increment right pointer
5. return output list
​