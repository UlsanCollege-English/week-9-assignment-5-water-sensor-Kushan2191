"""
HW05 — Water Sensor: Streaming Median

Implement streaming_median(nums) -> list
"""

import heapq

def streaming_median(nums):
    low = []  # max-heap for lower half (use negatives)
    high = []  # min-heap for upper half
    medians = []

    for num in nums:
        # Push to low (max-heap)
        heapq.heappush(low, -num)

        # Move largest in low to high
        heapq.heappush(high, -heapq.heappop(low))

        # Balance: if high has more elements, move back to low
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Compute median
        if len(low) > len(high):
            medians.append(-low[0])
        else:
            medians.append((-low[0] + high[0]) / 2.0)

    return medians
