class Solution:
    def addMinimum(self, word: str) -> int:
        word_ptr = 0
        target = 'abc' * len(word)
        tar_ptr = 0
        count = 0
        
        while word_ptr < len(word):
                            
            if word[word_ptr]!= target[tar_ptr]:
                tar_ptr += 1
                count += 1

            else:
                word_ptr += 1
                tar_ptr += 1
                
        if word[-1] == 'a':
            count += 2
        if word[-1] == 'b':
            count += 1
        return count
