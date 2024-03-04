class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 0, 0
        count = senate.count('R')

        while count != len(senate) and count != 0 :
            curr = []
            for char in senate:
                if char == 'R':
                    if r > 0:
                        r -= 1
                    else:
                        curr.append(char)
                        d += 1
                elif char == 'D':
                    if d > 0:
                        d -= 1
                    else:
                        curr.append(char)
                        r += 1
            senate = curr
            count = senate.count('R')
            
        return "Radiant" if count == len(senate) else "Dire"