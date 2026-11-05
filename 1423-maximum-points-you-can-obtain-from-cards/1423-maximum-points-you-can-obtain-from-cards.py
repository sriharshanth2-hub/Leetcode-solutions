class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)

        score = sum(cardPoints[n-k:])  # Take last k cards
        max_score = score

        for i in range(k):
            score += cardPoints[i] - cardPoints[n-k+i]

            if score > max_score:
                max_score = score

        return max_score