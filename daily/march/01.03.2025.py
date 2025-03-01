class Solution:
    def applyOperations(nums):
        for i in range(len(nums)):
            if i!=len(nums)-1:
                n,m=nums[i],nums[i+1]
                if n==m:
                    nums[i]=n*2
                    nums[i+1]=0
        res=[]
        for i in nums:
            if i!=0:
                res.append(i)
        res+=[0]*(len(nums)-len(res))
        return res
    print(applyOperations([1,2,2,1,1,0]))