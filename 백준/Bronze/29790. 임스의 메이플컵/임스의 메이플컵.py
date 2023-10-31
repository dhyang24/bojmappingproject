q,w,e = map(int,input().split())
if (w >= 8000 or e >= 260) and q >= 1000:
    print("Very Good")
elif q >= 1000:
    print("Good")
else:
    print("Bad")