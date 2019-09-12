for _ in range(int(input())):
    N,K= map(int,input().split())
    if (N%K==0):
        cand1= [N/K]*K
        cand2= [0]*K
        num= N
        while num>0:
            for i in range(K):
                cand2[i]= cand2[i]+K
                num=num-K
        if cand1==cand2:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")