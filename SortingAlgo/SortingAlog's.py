class Sorting:
    
    
    
    def BubbleSort(self, lst):
        for i in range (len(lst)-1):
            for j in range(len(lst)-i-1):
                if(lst[j] > lst[j+1]):
                    lst[j], lst[j+1] = lst[j+1], lst[j]

        return lst
    
    def selectionSort(self, lst):
        for i in range(len(lst)):
            min_idx=i
            for j in range(i+1, len(lst)):
                if lst[min_idx] > lst[j]:
                    min_idx = j
            
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
        return lst
    
    def MergeSort(self, arr, lo, hi):
        
        if lo == hi:
            return
        
        
        mid = (lo+hi)//2
        
        self.MergeSort(arr,lo, mid)
        self.MergeSort(arr,mid+1, hi)
        self.Merge(arr, lo, mid, hi)
    
    def MergeSortPrintingArray(self, arr):
        lo = 0
        hi = len(arr)-1

        self.MergeSort(arr, lo, hi)
        print(arr)
    
    def Merge(self, arr, lo, mid, hi):
        res = []
        left = lo
        right = mid+1
        
        while left <= mid and right <= hi:
            if(arr[left] <= arr[right]):
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right += 1
        
        while left <= mid:
            res.append(arr[left])
            left += 1
        
        while right <= hi:
            res.append(arr[right])
            right += 1
        
        for i in range(lo, hi+1):
            arr[i] = res[i-lo]
            
        
    ''' ............................. ............................................................
              '''  
        
    def QuickSortPrinting(self, arr):
        lb = 0
        ub = len(arr)-1
        
        self.quickSort(arr, lb, ub)
        return arr
    
    # Function to do quick sort
    def quickSort(self, arr, lb, ub):
        if (lb < ub):
            loc = self.Partition(arr, lb, ub)
            self.quickSort(arr, lb, loc - 1)
            self.quickSort(arr, loc+1, ub)

    def Partition(self, arr, lb, ub):
        pivot = arr[lb]
        start = lb
        end = ub
        while start < end:
            
            while arr[start] <= pivot:
                start+=1
            while arr[end] > pivot:
                end -= 1
            
            if(start < end):
                arr[start], arr[end] = arr[end], arr[start]
        
        arr[lb], arr[end] = arr[end], arr[lb]
        return end
        
    




lst = [2,5,4,0,62,700,25]
x = Sorting()
print(x.QuickSortPrinting(lst))
# print(x.selectionSort(lst))