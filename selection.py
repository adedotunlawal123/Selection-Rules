def valid_l(l,n):
    return l >= 0 and l < n

def valid_m(m,l):
    return m >= -l and m <= l

Nmax = 20
for n2 in range(1,Nmax+1):
    for n1 in range(1,n2):
        num = 0
        for l2 in range(0,n2):
            for m2 in range(-l2,l2+1):
                # the l1 = l2-1 transition
                if valid_l(l2-1,n1):
                    l1 = l2-1
                    if valid_m(m2-1,l1): 
                        num+=1
                    if valid_m(m2,l1):
                        num+=1
                    if valid_m(m2+1,l1):
                        num+=1
                # the l1 = l2+1 transition
                if valid_l(l2+1,n1):
                    l1 = l2+1
                    if valid_m(m2-1,l1):
                        num+=1
                    if valid_m(m2,l1):
                        num+=1
                    if valid_m(m2+1,l1):
                        num+=1

        dE = 13.6*(1.0/n1/n1 - 1.0/n2/n2)

        lam = 1240.0/dE

        if lam >= 380.0 and lam <= 750.0:
            vflag="v"
        else:
            vflag=""
        print("{:2} -> {:2}{:1}  {:10} {:20.12f} {:20.12f}".format(n2,n1,vflag,num,dE,lam))

