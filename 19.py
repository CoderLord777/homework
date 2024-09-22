def f(k,h):
    if k>=202: return h%2==0
    if h==0: return 0
    xod = [f(k+1,h-1),f(k+4,h-1),f(k*3,h-1)]
    return any (xod) if (h-1)%2==0 else all (xod)
print(min (w for w in range (1,202) if f(w,2)))
print ([w for w in range (1,202) if f(w,3)>f(w,1)])
print(min (w for w in range (1,202) if f(w,4)>f(w,2)))
