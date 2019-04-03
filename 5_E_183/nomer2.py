def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+i], arr[j]
    return arr

def gabung(a,b):
    c = []
    c = a+b
    n = len(c)
    for i in range(n):
        for j in range(0, n-i-1):
            if c[j] > c[j+1]:
                c[j], c[j+i] = c[j+1], c[j]
    return c

a = [9,2,5,11,4,7,19,1]
b = [13,43,56,12,56]
a, b = bubblesort(a), bubblesort(b)

print(a, "\n", b)
print()
print(gabung(a,b))
