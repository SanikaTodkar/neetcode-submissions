class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 0

            frequency[num] += 1

        sorted_nums = sorted(frequency, key=frequency.get, reverse=True)

        return sorted_nums[:k]
        