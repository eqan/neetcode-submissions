class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s, sw = deque(students), deque(sandwiches)
        unable_to_eat = 0
        while s and sw and unable_to_eat < len(s):
            if s[0] == sw[0]:
                s.popleft()
                sw.popleft()
                unable_to_eat = 0
            else:
                _s = s.popleft()
                s.append(_s)
                unable_to_eat+=1
        return len(s)