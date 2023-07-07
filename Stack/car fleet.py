class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair =[[p,s] for p,s in zip(position,speed)] # pair if position and speed in list
        
        stack=[]
        
        for p,s in sorted(pair)[::-1]: # reverse sorted array posed on position
            stack.append((target-p)/s) # append time to stack
            if len(stack)>=2 and stack[-1]<=stack[-2]: # check if they collide
                stack.pop() # pop the car behind in line as that car will adjust its speed according to
                # car in front
            
        return len(stack)
        
        
x=Solution()
print(x.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))