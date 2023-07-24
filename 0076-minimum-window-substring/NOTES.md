# Algorithm
​
* so the intuitive approach is to use hashmap and while adding each character check if all the character in hashmap of t is in s
* if all the characters are in hashmap then just update result based on the length of result
​
# Optimal
1. Map all the character of t in countT hashmap
2. set the need count to the length of countT hashmap and have count to zero
3. now for each characters in s just add them into the hashmap (window[c]) amd consider them in the window length
4. now check if the character exist in hashmap of t and has same value as s , then just update the have count
5. now untill the have count is equal to need
* just check if the window length (r-l) is less than result lenght and update result accordingly
* decrement hashmap of s left pointer value ( window[s[l]] ) and change have value if changes apply to it
* increment left pointer
6. return result