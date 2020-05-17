def solution(l):
    n = len(l)
    for i in range(n):
        done = True
        for j in range(n - i - 1):
            # Compare the first digit
            cf = l[j].split('.')[0] if "." in l[j] else l[j]
            nf = l[j+1].split('.')[0] if "." in l[j+1] else l[j+1]
            # if the next item is less than the current, swap
            if int(nf) < int(cf):
                l[j], l[j+1] = l[j+1], l[j]
                done = False
            if int(nf) == int(cf):
                # The firs items are the same, so move on to the 2nd decimal
                cs = l[j].split('.')[1] if "." in l[j] else -1
                ns = l[j+1].split('.')[1] if "." in l[j+1] else -1
                if int(ns) < int(cs):
                    l[j], l[j+1] = l[j+1], l[j]
                    done = False
                if int(ns) == int(cs):
                    # The second items are the same, so move on to the 3rd decimal
                    ct = l[j].split('.')[2] if len(l[j].split('.')) == 3 else -1
                    nt = l[j+1].split('.')[2] if len(l[j+1].split('.')) == 3 else -1
                    if int(nt) < int(ct):
                        l[j], l[j+1] = l[j+1], l[j]
                        done = False

        if done:
            break
    print(l)
    return l
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# 0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0
solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
# 1.0,1.0.2,1.0.12,1.1.2,1.3.3
