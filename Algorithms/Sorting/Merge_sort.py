#Merge sort

def merge(A, B):
    n_1 = len(A)
    n_2 = len(B)
    a = 0
    b = 0
    merged_list = []
    while(a < n_1 or b < n_2):
        if a < n_1 and b < n_2:
            if A[a] <= B[b]:
                merged_list.append(A[a])
                a += 1
            else:
                merged_list.append(B[b])
                b += 1
        elif a < n_1:
             merged_list.append(A[a])
             a += 1
        else:
             merged_list.append(B[b])
             b += 1
    return merged_list

            
                

    

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    m = (n//2)-1
    first_part = merge_sort(nums[:m+1]) 
    second_part = merge_sort(nums[m+1:])
    return merge(first_part,second_part)


print(merge_sort([1]))


     


