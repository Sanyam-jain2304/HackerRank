# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for i in range(0, N):
    S = input()
    print(S[0::2]+" " +S[1::2])
