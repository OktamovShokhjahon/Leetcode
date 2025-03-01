class Solution:
    def longestMonotonicSubarray(nums):
        a=[]
        b=[]
        c=1
        for i in range(len(nums)):
            if i != 0:
                n,m=nums[i-1],nums[i]
                if n>m:
                    c+=1
                else:
                    if c>1:
                        a.append(c)
                        c=1
        a.append(c)
        k=1
        for i in range(len(nums)):
            if i != 0:
                n,m=nums[i-1],nums[i]
                if n<m:
                    k+=1
                else:
                    if k>1:
                        b.append(k)
                        k=1
        b.append(k)
        if len(a)==0 and len(b)==0:
            return 1
        if len(a)==0:
            return max(b)
        if len(b)==0:
            return max(a)
        return max(max(a),max(b))
    print(longestMonotonicSubarray([3,2,1]))