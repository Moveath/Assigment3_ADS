from sorter import insertion_sort, merge_sort, print_array, generate_random_array
from searcher import binary_search
from experiment import run_all_experiments
print("=== Small array (10 elements) ===")
small = generate_random_array(10)
print("Original:         ", end="")
print_array(small)
sorted_small = insertion_sort(small[:])
print("Insertion Sort:   ", end="")
print_array(sorted_small)
merge_small = merge_sort(small[:])
print("Merge Sort:       ", end="")
print_array(merge_small)
target = merge_small[5]
idx = binary_search(merge_small, target)
print(f"Binary Search for {target}: found at index {idx}")
print()
print("=== Medium array (100 elements) ===")
medium = generate_random_array(100)
sorted_medium = merge_sort(medium[:])
target = sorted_medium[50]
idx = binary_search(sorted_medium, target)
print(f"Binary Search for {target}: found at index {idx}")
print()
print("=== Large array (1000 elements) ===")
large = generate_random_array(1000)
sorted_large = merge_sort(large[:])
target = sorted_large[500]
idx = binary_search(sorted_large, target)
print(f"Binary Search for {target}: found at index {idx}")
print()
print("=== Performance Experiments ===")
run_all_experiments()