class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() 
        arrow_count = 1
        arrow = points[-1][0]

        for i in range(len(points)-2, -1, -1):

            if not points[i][0] <= arrow <= points[i][1]:
                arrow = points[i][0]
                arrow_count += 1
        return arrow_count
        