s = "011101"
max_v = 0
count_zero = 0
count_ones = s.count("1")

# print(count_ones)

for i in range(len(s)-1):
    count_zero+= s[i]=="0"
    count_ones-= s[i]=="1"
    
    max_v = max(max_v,count_ones+count_zero)
    
    
print(max_v) 