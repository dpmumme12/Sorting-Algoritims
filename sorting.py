def bubble_sort(arr):
    
    for n in range(len(arr)-1,-1,-1):
        for i in range(n-1, -1, -1):
            
            if arr[i] > arr[n]:
                temp = arr[i]
                arr[i] = arr[n]
                arr[n] = temp
                

def selection_sort(arr):
  
    for n in range(len(arr)-1,0,-1):
        position_of_max = n
        i = 0
        while i < n:
            
            if arr[i] > arr[position_of_max]:
                position_of_max = i
            i += 1
                  
        temp = arr[n]
        arr[n] = arr[position_of_max]
        arr[position_of_max] = temp


def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        currentvalue = arr[i]
        position = i
        
        while position > 0 and arr[position - 1] > currentvalue:
            
            arr[position] = arr[position - 1]
            position -= 1
            
        arr[position] = currentvalue


def shell_sort(arr):
    
    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        for start in range(sublistcount):
            
            shell_insertion_sort(arr,start,sublistcount)
            
        sublistcount = sublistcount // 2
            
            
def shell_insertion_sort(arr, start, gap):
    
    for i in range(start + gap, len(arr), gap):
        
        currentvalue = arr[i]
        position = i
        
        while position > 0 and arr[position - gap] > currentvalue:
            
            arr[position] = arr[position - gap]
            position -= gap
            
        arr[position] = currentvalue


def merge_sort(arr):
    
    if len(arr) > 1:
        
        mid = len(arr) // 2
        
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] > righthalf[j]:
                arr[k] = righthalf[j]
                j += 1
                k += 1
                
            else:
                arr[k] = lefthalf[i]
                i += 1
                k += 1
                
                
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1