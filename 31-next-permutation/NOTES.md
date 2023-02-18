Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
Find the largest index l > k such that nums[k] < nums[l]. so start from end
Swap nums[k] and nums[l].
Reverse the sub-array nums[k + 1:].