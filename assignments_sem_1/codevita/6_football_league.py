"""Q6 Football League 

Football League Table Statement : All major football leagues have big league tables. 
Whenever a new match is played, the league table is updated to show the current 
rankings (based on Scores, Goals For (GF), Goals Against (GA)). Given the results of a 
few matches among teams, write a program to print all the names of the teams in 
ascending order (Leader at the top and Laggard at the bottom) based on their rankings. 

Rules: A win results in 2 points, a draw results in 1 point and a loss is worth 0 points. 
The team with the most goals in a match wins the match. Goal Difference (GD) is 
calculated as Goals For (GF) Goals Against (GA). Teams can play a maximum of two 
matches against each other Home and Away matches respectively. 

The ranking is decided as follows: Team with maximum points is ranked 1 and minimum 
points is placed last Ties are broken as follows Teams with same points are ranked 
according to Goal Difference(GD). 
If Goal Difference(GD) is the same, the team with higher Goals For is ranked ahead 
If GF is same, the teams should be at the same rank but they should be printed in case
insensitive alphabetic according to the team names. More than 2 matches of same 
teams, should be considered as Invalid Input. 
A team can't play matches against itself, hence if team names are same for a given 
match, it should be considered Invalid Input 

Input Format: First line of input will contain number of teams (N) Second line contains 
names of the teams (Na) delimited by a whitespace character Third line contains 
number of matches (M) for which results are available Next M lines contain a match 
information tuple {T1 T2 S1 S2}, where tuple is comprised of the following information 
• T1 Name of the first team 
• T2 Name of the second team 
• S1 Goals scored by the first team 
• S2 Goals scored by the second team 

Output Format: Team names in order of their rankings, one team per line OR Print 
“Invalid Input” where appropriate. 

Constraints: 0< N <=10,000 0<=S1,S2
"""
n=5
Na=['Spain','England','France','Italy','Germany']
m=[('Spain','England',3,0),('England','France',1,1),('Spain','France',0,2)]
s = {}

for i in Na:
    s[i]=[0,0,0] 

for t1,t2,s1,s2 in m:
    s[t1][1]+=s1
    s[t1][2]+=s2
    s[t2][1]+=s2
    s[t2][2]+=s1
    if s1>s2:
        s[t1][0]+=2
    elif s2>s1:
        s[t2][0]+=2
    else:
        s[t1][0]+=1
        s[t2][0]+=1
print(s)
# for i in s.values():


