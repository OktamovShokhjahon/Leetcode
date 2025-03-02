class Solution:
    def mergeArrays(nums1, nums2):
        ids={}
        q=[]
        for i in nums1:
            if i[0] not in ids:
                ids[i[0]]=0
                q.append(i[0])
        for i in nums2:
            if i[0] not in ids:
                ids[i[0]]=0
                q.append(i[0])
        for i in nums1:
            ids[i[0]]=ids[i[0]]+i[1]
        for i in nums2:
            ids[i[0]]=ids[i[0]]+i[1]
        q.sort()
        res=[]
        for i in q:
            res.append([i, ids[i]])
        return res
    print(mergeArrays([[1,2],[2,3],[4,5]],  [[1,4],[3,2],[4,1]]))