class Solution:
    def clearDigits(s: str) -> str:
        s=list(s)
        c=0
        for i in range(len(s)):
            n=s[i-c]
            if n.isdigit():
                if i!=0:
                    del s[i-1-c]
                    c+=1
                    del s[i-c]
                    c+=1
        return "".join(s)

