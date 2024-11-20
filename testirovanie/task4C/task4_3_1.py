import asyncio

class Solution:

    def __init__(self):
        self.lst_positive = []
        self.lst_negative = []

    async def generate_array_positive(self):
        for positive in range(0, 11):
            self.lst_positive.append(positive)
        return self.lst_positive

    async def generate_array_negative(self):
        for negative in range(-10, 0):
            self.lst_negative.append(negative)
        return self.lst_negative

    async def generate_arrays(self):
        await asyncio.gather(
            self.generate_array_negative(),
            self.generate_array_positive()
        )
        return self.lst_negative, self.lst_positive

if __name__ == '__main__':  
    solution = Solution()
    result = asyncio.run(solution.generate_arrays())
    print(result)