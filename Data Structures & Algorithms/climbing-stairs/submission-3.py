class Solution:
    def climbStairs(self, n: int) -> int:
        # You have to watch the video explanation to understand this problem
        '''
            Initially we start by drawing a decision tree to seek for the recursive solution, when we complete the decision tree we realize a pattern where the solution of the tree has so much repition in it. Then we utilize DP to cache the result of the decision subtrees. Then further we realize we are actually doing a fibonnaci sequence based on the steps we do. So from recursive solution we reach an iterative solution. Then further we realise instead of storing the whole DP array we can use only two variables one and two to compute as the latest 2 values are only the major concern for us.
        '''
        one, two = 1, 1
        for i in range(n):
            temp = one
            one = one + two
            two = temp
        return two
        
