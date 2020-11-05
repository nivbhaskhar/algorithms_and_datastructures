#Quick sort
    
import random
def quick_sort(nums):
    n = len(nums)

    def quick_sort(start,end):
        #print(f"s = {start}, e = {end}")
        if end-start < 1:
            return
        pivotpos = random.randint(start, end)
        temp = nums[start]
        nums[start]=nums[pivotpos]
        nums[pivotpos]=temp
        pivot = nums[start]
        #print(f"pivotpos {pivotpos}, pivot {pivot}")
        #print(nums)
        #move pivot to so that  everything to left of pivot <= pivot
        #and everything to the right of pivot > pivot
        dividing_pointer = start+1
        for to_do_pointer in range(start+1,end+1):
            if nums[to_do_pointer] <= pivot:
                temp = nums[to_do_pointer]
                nums[to_do_pointer] = nums[dividing_pointer]
                nums[dividing_pointer] = temp
                dividing_pointer += 1
        #print(nums)
        nums[start]=nums[dividing_pointer-1]
        nums[dividing_pointer-1] = pivot
        #print(nums)
        #print("*****")
            

        
        
        quick_sort(start,dividing_pointer-1)
        quick_sort(dividing_pointer,end)
    quick_sort(0,n-1)
    print(nums)
    
    

    

quick_sort([1,3,2,7,0,14])


     


