def find_peak_n(arr):
    size=len(arr)
    peak=[]
    for i in range(0,size):
       if i==0:
        a4=arr[i+1]
        if arr[i]>=a4:
           peak.append(i+1)
           break
       elif i==size-1:
           b4=arr[i-1]
           if arr[i]>=b4:
              peak.append(i+1)
              break
       else:
            b4=arr[i-1]
            a4=arr[i+1]
            if arr[i]>=b4 and arr[i]>=a4:
               peak.append(i+1)
               break
    return peak

def find_peak_logn(arr,start,end,size):
    mid=start+(end-start)/2
    mid=int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid ==size - 1 or arr[mid + 1] <= arr[mid])):
        return mid+1
    elif (mid > 0 and arr[mid - 1] >=arr[mid]):
        return find_peak_logn(arr,start,mid - 1,size)
    else:
        return find_peak_logn(arr,mid+1,end,size)
arr=[4, 5, 7, 3, 24, 9]
n=len(arr)
b=find_peak_logn(arr,0,n-1,n)
b=find_peak_n(arr)
