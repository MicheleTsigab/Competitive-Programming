class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed[0]==0 and (0==len(flowerbed) - 1 or flowerbed[1]==0):
            #print('here')
            flowerbed[0]=1
            n-=1
        for i in range(1,len(flowerbed)):
            if flowerbed[i]==flowerbed[i-1]==0 and (i==len(flowerbed)-1 or (i < len(flowerbed) -1 and flowerbed[i+1]==0)):
                flowerbed[i]=1
                n-=1
        return n<=0
                