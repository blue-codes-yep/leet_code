class Solution:
    def isValid(self, s: str) -> bool:
        correct = ['()', '[]', '{}', ]
        while any(x in s for x in correct):
            for string in correct:
                s = s.replace(string, '')
        return not s
