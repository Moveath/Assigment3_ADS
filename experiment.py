import time
import copy
from sorter import insertion_sort, merge_sort
from searcher import binary_search
def measure_sort_time(arr, sort_type):
    arr_copy = copy.copy(arr)
    start = time.time_ns()
    if sort_type == "basic":
        insertion_sort(arr_copy)
    elif sort_type == "advanced":
        merge_sort(arr_copy)
    end = time.time_ns()
    return end - start
def measure_search_time(arr, target):
    start = time.time_ns()
    binary_search(arr, target)
    end = time.time_ns()
    return end - start
def run_all_experiments():
    sizes = [10, 100, 1000]
    labels = ["Small (10)", "Medium (100)", "Large (1000)"]
    print("=" * 60)
    print(f"{'Dataset':<20} {'Insertion Sort':>15} {'Merge Sort':>12} {'Binary Search':>15}")
    print("=" * 60)
    for size, label in zip(sizes, labels):
        from sorter import generate_random_array
        random_arr = generate_random_array(size)
        sorted_arr = sorted(random_arr)
        target = sorted_arr[size // 2]
        ins_time = measure_sort_time(random_arr, "basic")
        merge_time = measure_sort_time(random_arr, "advanced")
        search_time = measure_search_time(sorted_arr, target)
        print(f"{label:<20} {ins_time:>13} ns {merge_time:>10} ns {search_time:>13} ns")
    print("=" * 60)
    print()
    print("Sorted vs Random — Insertion Sort (size=1000)")
    print("-" * 45)
    from sorter import generate_random_array
    random_arr = generate_random_array(1000)
    sorted_arr = sorted(random_arr)
    t_random = measure_sort_time(random_arr, "basic")
    t_sorted = measure_sort_time(sorted_arr, "basic")
    print(f"  Random array : {t_random} ns")
    print(f"  Sorted array : {t_sorted} ns")
    print("-" * 45)