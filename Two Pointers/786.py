class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        fractions = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))
        fractions.sort()
        return [fractions[k - 1][1], fractions[k - 1][2]]