class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [item for item in zip(position, speed)]
        pair.sort(reverse=True)
  
        prev, fleets = 0, 0
        for item in pair:
            time = (target - item[0]) / item[1]
            if time > prev:
                fleets += 1
                prev = time

        return fleets
