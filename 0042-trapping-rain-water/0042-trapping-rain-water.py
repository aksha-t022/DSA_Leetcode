class Solution:
    def trap(self, h: List[int]) -> int:
        size=len(h)
        leftmax=[0]*size
        rightmax=[0]*size

        leftmax[0]=h[0]
        rightmax[size-1]=h[size-1]
        for index in range(1,size):
            leftmax[index]=max(leftmax[index-1],h[index])

        for index in range(size-2,-1,-1):
            rightmax[index]=max(rightmax[index+1],h[index])
        ans=0
        for index in range(size):
                ans +=min(leftmax[index],rightmax[index])-h[index]
        return ans