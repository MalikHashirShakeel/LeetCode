from collections import Counter
class Solution:
    def countStudents(self, students, sandwiches):

        count = Counter(students)  
        for sandwich in sandwiches:
            if count[sandwich] > 0:  
                count[sandwich] -= 1
            else:
                return count[0] + count[1]  
        return 0