class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        total_distance = sum(distance)

        clockwise_distance = 0
        i = start
        while i != destination:
            clockwise_distance += distance[i]
            i = (i+1)%n
        
        counterclockwise_distance = 0
        i = start
        while i != destination:
            i = (i-1) % n
            counterclockwise_distance += distance[i]
        
        return min(clockwise_distance, counterclockwise_distance)
        
        # return min(sum(distance[0:destination]), sum(distance[destination:start]))