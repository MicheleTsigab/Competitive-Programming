class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        3 2 1
          
        
        """
        i = len(arr) - 2
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                break
        else:
            return arr
        
        for j in range(len(arr)-1,i,-1):
            if arr[j] < arr[i] and arr[j] != arr[j-1]:
                break
        arr[j],arr[i] = arr[i],arr[j]
        return arr