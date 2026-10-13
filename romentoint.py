s = input("enter a roman numeral:")

value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
t = 0
for i in range(len(s)):
    if i+1 < len(s) and value[s[i]] < value[s[i+1]]:

        t -= value[s[i]]
    else:
        t += value[s[i]]
print(t)                 
