# 881. Boats to Save People
# List = [1,2], limit =3
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        right  = len(people)-1
        left = 0
        boat = 0

        while(left<=right):
            if left!=right and people[left]+people[right]<=limit:
                left+=1
            
            right-=1
            boat+=1
        
        return boat