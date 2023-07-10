class TimeMap:

    def __init__(self):
        self.ts={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        new_data={
            "value":value,
            "timestamp":timestamp
        }
        if self.ts and self.ts[key]:
            self.ts[key].append(new_data)
        else:
            self.ts[key]=[new_data]     

    def get(self, key: str, timestamp: int) -> str:
        
        min=0 # setting minimum gap 
        l,r=0,len(self.ts[key])-1
        while(l<=r):
            mid=(l+r)//2
            min_gap=abs(self.ts[key][min]['timestamp']-timestamp)
            new_min_gap=abs(self.ts[key][mid]['timestamp']-timestamp)
            if new_min_gap<=min_gap:
                min=mid
                l=mid+1
            else:
                r=mid-1
        return self.ts[key][min]['value']