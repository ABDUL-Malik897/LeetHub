class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(students)):
            moves = moves + abs(seats[i]- students[i])
        return moves