class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] == 0:
                pass
            else:
                
                for j in range(i+1,len(batteryPercentages)):
                    if batteryPercentages[j] > 0:
                         batteryPercentages[j] = batteryPercentages[j] - 1

                   
                
                c = c + 1
        
        return c