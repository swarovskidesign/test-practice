class autonum_check:
    
    def __init__(self, num: str, access_alpha: str):
        self.num = num
        self.access_alpha = access_alpha
        
    def seriya_check(self):
        if self.num[0] in self.access_alpha and self.num[4] in self.access_alpha \
        and self.num[5] in self.access_alpha:
            return True
        return False
        
    def reg_num_check(self):
        if self.num[1:4].isdigit():
            return True
        return False
        
    def reg_check(self):
        if len(self.num) == 9:
            if self.num[-2:].isdigit():
                return True
        elif len(self.num) == 10:
            if self.num[-3:].isdigit():
                return True
        return False

check_number = autonum_check(input(), 'АВЕКМНОРСТУХ')


if check_number.seriya_check():
    print("seriya_check passed")
else:
    print("seriya_check failed")

if check_number.reg_num_check():
    print("reg_num_check passed")
else:
    print("reg_num_check failed")

if check_number.reg_check():
    print("reg_check passed")
else:
    print("reg_check failed")

if check_number.seriya_check() and check_number.reg_num_check() and check_number.reg_check():
    print('YES')
else:
    print('NO')

