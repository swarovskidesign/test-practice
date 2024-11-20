class Task18:

    def nod(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.nod(b, a % b)

a = int(input())
b = int(input())
task18 = Task18()

result = task18.nod(a, b)
print(result)