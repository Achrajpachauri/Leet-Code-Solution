class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        res = address.split('.')

        return '[.]'.join(res)


