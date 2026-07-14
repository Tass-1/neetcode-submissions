from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions and speeds, then sort by position in descending order 
        # (closest to the target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time_ahead = 0.0
        
        for p, s in cars:
            # Calculate the time it would take for this car to reach the target alone
            time_to_target = (target - p) / s
            
            # If this car takes strictly longer than the slowest car/fleet ahead of it,
            # it cannot catch up. Therefore, it forms a new fleet.
            if time_to_target > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time_to_target
                
        return fleets