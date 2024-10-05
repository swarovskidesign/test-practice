a = int(input())

while a >= 0:
    st = input()
    if st.isspace():
        print("COMMENT SHOULD BE DELETED")
    else:
        print(st)
    a -= 1