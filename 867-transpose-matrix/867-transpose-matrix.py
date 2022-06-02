class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t = []
        for i in range(len(matrix[0])):
            t.append([matrix[j][i] for j in range(len(matrix))])
        return t