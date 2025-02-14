class ProductOfNumbers:

    def __init__(self):
        self.lastZeroIndex = -1
        self.index = -1
        self.prefixProduct = []

    def add(self, num: int) -> None:
        self.index += 1
        if num == 0:
            self.lastZeroIndex = self.index
            self.prefixProduct.append(num)
        else:
            if not self.prefixProduct or self.prefixProduct[-1] == 0:
                self.prefixProduct.append(num)
            else:
                self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.index - k < self.lastZeroIndex:
            return 0
        else:
            return self.prefixProduct[-1] // (self.prefixProduct[self.index - k] if self.prefixProduct[self.index - k] != 0 and self.index - k >= 0 else 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)