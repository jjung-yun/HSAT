def merge_sort(lst,left,right):
    if left<right: #인덱스가 똑같거나 크면 정렬 필요 X
        # mid값은 내림
        mid=(left+right)//2
        merge_sort(lst,left,mid)
        merge_sort(lst,mid+1,right)
        merge(lst,left,mid,right)

def merge(lst,left,mid,right):
    
