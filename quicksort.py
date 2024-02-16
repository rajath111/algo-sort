from typing import List, Any

class QuickSort:
    '''
        Quick sort uses divide and conquer. 
    '''

    def __swap(self, list: List[Any], i: int, j: int):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp


    def __quick_sort(self, list: List[Any], start, end):
        '''
            Start and end are inclusive. 
    
            1. Select first number as the pivot
            2. Move the all the number greater than the pivot to left and greater to the right of the pivot
            3. Repeat the steps till start and end are equal
               [5, 6, 7, 2, 1, 8, 3, 10] 
        '''
        
        if start >= end:
            return 
        
        pivot_index = start
        for i in range(start + 1, end + 1):
            # If the curent value is less than the pivot value, move the current value behind the pivot
    
            if list[i] < list[pivot_index]:
                # Do consecutive swaps from current index back to the pivot index
                # print(pivot_index, i, list[i], list[pivot_index], list)
    
                for j in range(i, pivot_index , -1):
                    self.__swap(list, j, j - 1)
    
                pivot_index += 1
    
        self.__quick_sort(list, start, pivot_index - 1)
        self.__quick_sort(list, pivot_index + 1, end)

    
    def sort(self, list: List[Any]):
        self.__quick_sort(list, 0, len(list) - 1)
