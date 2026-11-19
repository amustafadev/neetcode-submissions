class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posToTime = {p : (target - p) / speed[i] for (i, p) in enumerate(position)}
        position = sorted(position, reverse=True)
  
        prev, fleets = 0, 0
        for p in position:
            time = posToTime[p]
            if time > prev:
                fleets += 1
                prev = time

        return fleets
