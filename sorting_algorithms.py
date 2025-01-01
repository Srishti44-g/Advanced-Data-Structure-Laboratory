class SortingAlgorithms:
    """Implementation of various sorting algorithms"""
    
    @staticmethod
    def bubble_sort(arr):
        """
        Bubble Sort implementation
        Time Complexity: O(n^2)
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    @staticmethod
    def insertion_sort(arr):
        """
        Insertion Sort implementation
        Time Complexity: O(n^2)
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    @staticmethod
    def quick_sort(arr):
        """
        Quick Sort implementation
        Time Complexity: O(n log n) average case
        """
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)
    
    @staticmethod
    def merge_sort(arr):
        """
        Merge Sort implementation
        Time Complexity: O(n log n)
        """
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left, right):
        """Helper method for merge sort"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def heap_sort(arr):
        """
        Heap Sort implementation
        Time Complexity: O(n log n)
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
                
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
            
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)
            
        return arr
    
    @staticmethod
    def radix_sort(arr):
        """
        Radix Sort implementation
        Time Complexity: O(d * (n + k)) where d is number of digits
        """
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1
                
            for i in range(1, 10):
                count[i] += count[i - 1]
                
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1
                
            for i in range(n):
                arr[i] = output[i]
        
        if not arr:
            return arr
            
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            counting_sort(arr, exp)
            exp *= 10
            
        return arr

# Test implementation
if __name__ == "__main__":
    # Test arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [38, 27, 43, 3, 9, 82, 10],
        [170, 45, 75, 90, 802, 24, 2, 66]
    ]
    
    sorter = SortingAlgorithms()
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Array {i}: {arr}")
        
        # Test each sorting algorithm
        print("Bubble Sort:", sorter.bubble_sort(arr.copy()))
        print("Insertion Sort:", sorter.insertion_sort(arr.copy()))
        print("Quick Sort:", sorter.quick_sort(arr.copy()))
        print("Merge Sort:", sorter.merge_sort(arr.copy()))
        print("Heap Sort:", sorter.heap_sort(arr.copy()))
        print("Radix Sort:", sorter.radix_sort(arr.copy())) 