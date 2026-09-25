class Solution(object):
    def countMaxOrSubsets(self, nums):

        maxOR = [0]
        count = [0]
        n = len(nums)

        def explore(index, currentOR):

            if index == n:

                if currentOR > maxOR[0]:
                    maxOR[0] = currentOR
                    count[0] = 1

                elif currentOR == maxOR[0]:
                    count[0] += 1

                return

            explore(index + 1, currentOR)
            explore(index + 1, currentOR | nums[index])

        explore(0, 0)

        return count[0]