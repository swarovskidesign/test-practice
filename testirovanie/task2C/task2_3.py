class Solution:

    def __init__(self):
        self.count = 0

    def count_sub_in_sec(self, st: str, sub: str) -> int:
        self.count = st.count(sub)
        return self.count

# или print(st.count(input()))
