class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        answer = []
        
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            
            trimmed.sort()
            
            answer.append(trimmed[k - 1][1])
        
        return answer 