class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()

        for i in range(len(deck)):
            queue.append(i) 
        
        ans = [0] * len(deck)
        for j in deck:
            var = queue.popleft()
            ans[var] = j

            if queue :  
                queue.append(queue.popleft())
        return ans