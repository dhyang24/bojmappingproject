a,b,c,d,s = int(input()),int(input()),int(input()),int(input()),int(input())
byron = (s//(a+b))*(a-b) + (s%(a+b) if  s%(a+b) <= a else a-(s%(a+b)-a))
nikky = (s//(c+d))*(c-d) + (s%(c+d) if  s%(c+d) <= c else c-(s%(c+d)-c))
print("Byron" if byron < nikky else ("Nikky" if nikky < byron else "Tied"))