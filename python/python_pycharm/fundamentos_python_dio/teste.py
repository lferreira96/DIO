qte = int(input())

while (qte>0):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")
    qte -=1