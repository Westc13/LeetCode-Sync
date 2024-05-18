class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        remainder = purchaseAmount % 10
        if remainder < 5:
            roundedAmount = purchaseAmount - remainder
        else:
            roundedAmount = purchaseAmount + (10 - remainder)
        remainingBalance = 100 - roundedAmount
        return remainingBalance