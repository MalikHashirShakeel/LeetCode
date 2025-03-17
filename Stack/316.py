class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurences = {char : i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and stack[-1] > char and last_occurences[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)