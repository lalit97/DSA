
#t = [[-1]*(n+1) for i in range(n+1)]

class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        i, j = 0, n-1
        self.ans = float('inf')
        return self.solve(i, j)


    def solve(self, i, j):
        if i >= j or self.is_palindrome(string[i: j+1]):
            return 0
        for k in range(i, j):
            temp = self.solve(i, k) + self.solve(k+1, j) + 1
            self.ans = min(self.ans, temp)
        return self.ans 

    def is_palindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        ob = Solution()
        print(ob.palindromicPartition(string))