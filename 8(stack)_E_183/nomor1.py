from coba import Stack
def cetakHexa(data):
    hx = Stack()
    hxlist = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        hx.push(hxlist[sisa])
    st=""
    for i in range(len(hx)):
        st = st + str(hx.pop())
    return st

print(cetakHexa(31519))
