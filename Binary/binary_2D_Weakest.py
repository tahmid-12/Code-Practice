from typing import List

class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

		scores = {}

		#go over each row to calculate their score, using row index as the key, score as value using sorted
		for i in range(len(mat)):
			score = 0
			for j in range(len(mat[i])):
				if mat[i][j] == 1:
					score += 1

			scores[i] = score

		#sort the scores by their value
		sortedArray = sorted(scores, key=scores.get)


		#return the array up to k
		return sortedArray[:k]
                
S = Solution();
print(S.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],3))