class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        right = 0
        #print(trainers)
        for left in range(len(players)):
            while right < len(trainers) and players[left] > trainers[right]:
                right += 1
            if right < len(trainers) and players[left] <= trainers[right]:
                right +=1
                count +=1
        return count
            