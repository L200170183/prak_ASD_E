class urut():
    def __init__(self, arr):
        self.arr = arr
        
    def mergeSort(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 
            L = arr[:mid] 
            R = arr[mid:]   
  
            self.mergeSort(L)  
            self.mergeSort(R) 
  
            i = j = k = 0
          
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
          
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
    def printMerge(self, arr):
        print("ini merge sort")
        self.mergeSort(arr)
        for i in range(len(arr)):         
            print(arr[i],end=" ") 
        print()
        print()
        
    def partition(self, arr,low,high): 
        i = ( low-1 )        
        pivot = arr[high]    
        for j in range(low , high): 
            if   arr[j] <= pivot: 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
  
    def quickSort(self, arr,low,high): 
        if low < high: 
            pi = self.partition(arr,low,high) 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

    def printQuick(self, arr):
        print("ini quick sort")
        n = len(arr) 
        self.quickSort(arr,0,n-1) 
        for i in range(n): 
            print(arr[i],end=" ")
        print()
        print()    
