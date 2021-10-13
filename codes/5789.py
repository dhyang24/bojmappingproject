for _ in range(int(input())):
    a = input()
    print("Do-it" if a[len(a)//2-1] == a[len(a)//2] else "Do-it-Not")
