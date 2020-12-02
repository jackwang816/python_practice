def swap(nums, i, j):
    # t = nums[i]
    # nums[i] = nums[j]
    # nums[j] = t
    nums[i], nums[j] = nums[j], nums[i]
def quickSort(nums, begin, end):
    if begin >= end:
        return
    mid, i, j= begin, begin, end
    while i < j:
        if mid == i:
            if nums[mid] > nums[j]:
                swap(nums, mid, j)
                mid = j
                i+=1
            else:
                j-=1
        else:
            if nums[mid] <= nums[i]:
                swap(nums, mid, i)
                mid = i
                j -= 1
            else:
                i +=1
    quickSort(nums, begin, mid-1)
    quickSort(nums, mid+1, end)            

def quickSort_new(nums, begin, end):
    if begin >= end:
        return
    pivot, i = nums[end], begin-1
    for j in range(begin, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[end], nums[i+1] = nums[i+1], nums[end]
    quickSort_new(nums, begin, i)
    quickSort_new(nums, i+2, end)

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    # quickSort(nums, 0, len(nums)-1)
    quickSort_new(nums, 0, len(nums)-1)
    print nums


    