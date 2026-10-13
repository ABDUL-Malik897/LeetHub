class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = list(zip(heights, names))
        people.sort(reverse=True)

        return [name for height, name in people]
