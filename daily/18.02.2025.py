class Solution:
    def smallestNumber(pattern: str):
        n=['0']*len(pattern)
        for i in range(len(pattern)):
            if pattern[i]=='I':
                if i-1!=len(pattern):
                    n[i]=str(int(n[i-1])+1)
                    n[i+1]=str(int(n[i])+1)
            else:
                if i-1!=len(pattern):
                    n[i]=str(int(n[i-1])-1)
                    n[i+1]=str(int(n[i])-1)
        return n
    print(smallestNumber('IIIDIDDD'))