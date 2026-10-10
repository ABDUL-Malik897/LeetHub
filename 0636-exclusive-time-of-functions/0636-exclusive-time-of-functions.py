class Solution(object):
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, event, timestamp = log.split(":")
            fid = int(fid)
            timestamp = int(timestamp)

            if event == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_time

                stack.append(fid)
                prev_time = timestamp

            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return ans