class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()
        result = []
        common_count = 0

        for i in range(len(A)):
            seen_A.add(A[i])
            seen_B.add(B[i])

            if A[i] in seen_B:
                common_count += 1
            if B[i] in seen_A and A[i] != B[i]:
                common_count += 1
            
            result.append(common_count)
        return result