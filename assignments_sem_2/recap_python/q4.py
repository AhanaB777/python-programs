"""Given two strings s and t, return true if they are equal when both are typed into empty text 
editors. '#' means a backspace character. 
Note that after backspacing an empty text, the text will continue empty. 
 Example 1: 
Input: s = "ab#c", t = "ad#c" 
Output: true 
Explanation: Both s and t become "ac" """

s="ab#c"
new_s=""
t="ad#c"
new_t=""
for i in range(len(s)):
    if s[i]=='#':
        new_s=s[:i-1]+s[i+1:]
        break

for i in range(len(t)):
    if t[i]=='#':
        new_t=t[:i-1]+t[i+1:]
        break

if new_s==new_t:
    print("True")
else:
    print("false")