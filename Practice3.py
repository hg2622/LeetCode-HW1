class Solution(object):
    def maxArea(self, height):
        a=0
        b=len(height)-1
        record=0
        while (b>a):
            if (abs(b-a)* min(height[b],height[a]))>record:
                record=abs(b-a)* min(height[b],height[a])
            if (height[b]>height[a]):
                a+=1
            else:
                b-=1
        
        return record