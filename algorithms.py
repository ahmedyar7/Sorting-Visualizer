from visulizer import draw_list
from main import stop_sound


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(
                    draw_info=draw_info,
                    color_positions={j: draw_info.RED, j + 1: draw_info.RED},
                    clear_bg=True,
                )
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i -= 1
            lst[i] = current
            draw_list(draw_info, {i: draw_info.RED, i - 1: draw_info.RED}, True)
            yield True
    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.list

    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if (ascending and lst[j] < lst[min_idx]) or (
                not ascending and lst[j] > lst[min_idx]
            ):
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        draw_list(draw_info, {i: draw_info.RED, min_idx: draw_info.RED}, True)
        yield True

    stop_sound()
    return lst


def merge_sort(draw_info, ascending=True):
    def merge_sort_recursive(lst, start_idx):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = lst[:mid]
            right_half = lst[mid:]
            yield from merge_sort_recursive(left_half, start_idx)
            yield from merge_sort_recursive(right_half, start_idx + mid)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if (left_half[i] < right_half[j] and ascending) or (
                    left_half[i] > right_half[j] and not ascending
                ):
                    lst[k] = left_half[i]
                    i += 1
                else:
                    lst[k] = right_half[j]
                    j += 1
                draw_info.list[start_idx + k] = lst[k]
                draw_list(draw_info, {start_idx + k: draw_info.RED}, True)
                k += 1
                yield True
            while i < len(left_half):
                lst[k] = left_half[i]
                draw_info.list[start_idx + k] = lst[k]
                draw_list(draw_info, {start_idx + k: draw_info.RED}, True)
                i += 1
                k += 1
                yield True
            while j < len(right_half):
                lst[k] = right_half[j]
                draw_info.list[start_idx + k] = lst[k]
                draw_list(draw_info, {start_idx + k: draw_info.RED}, True)
                j += 1
                k += 1
                yield True

    lst = draw_info.list
    yield from merge_sort_recursive(lst, 0)


def quick_sort(draw_info, ascending=True):
    def partition(low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(
                    draw_info,
                    color_positions={i: draw_info.RED, j: draw_info.RED},
                    clear_bg=True,
                )
                yield True
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_list(
            draw_info,
            color_positions={i + 1: draw_info.RED, high: draw_info.RED},
            clear_bg=True,
        )
        yield True
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            partition_index = yield from partition(low, high)
            yield from quick_sort_recursive(low, partition_index - 1)
            yield from quick_sort_recursive(partition_index + 1, high)

    lst = draw_info.list
    yield from quick_sort_recursive(0, len(lst) - 1)


def heap_sort(draw_info, ascending=True):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and (
            (lst[l] > lst[largest] and ascending)
            or (lst[l] < lst[largest] and not ascending)
        ):
            largest = l

        if r < n and (
            (lst[r] > lst[largest] and ascending)
            or (lst[r] < lst[largest] and not ascending)
        ):
            largest = r

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            draw_list(
                draw_info,
                color_positions={i: draw_info.RED, largest: draw_info.RED},
                clear_bg=True,
            )
            yield True
            yield from heapify(n, largest)

    lst = draw_info.list
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(
            draw_info,
            color_positions={i: draw_info.RED, 0: draw_info.RED},
            clear_bg=True,
        )
        yield True
        yield from heapify(i, 0)

    return lst


def counting_sort(draw_info, ascending=True):
    lst = draw_info.list
    max_val = max(lst)
    min_val = min(lst)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(lst)

    # Step 1: Count the occurrences of each element
    for num in lst:
        count[num - min_val] += 1

    # Step 2: Modify the count array based on the sorting order
    if ascending:
        for i in range(1, len(count)):
            count[i] += count[i - 1]
    else:
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]

    # Step 3: Build the output array using the count array
    for i in range(len(lst) - 1, -1, -1):
        output[count[lst[i] - min_val] - 1] = lst[i]
        count[lst[i] - min_val] -= 1
        draw_list(
            draw_info,
            color_positions={i: draw_info.RED},
            clear_bg=True,
        )
        yield True

    # Step 4: Copy the sorted elements back to the original list
    for i in range(len(lst)):
        lst[i] = output[i]
        draw_list(
            draw_info,
            color_positions={i: draw_info.RED},
            clear_bg=True,
        )
        yield True

    return lst


def radix_sort(draw_info, ascending=True):
    def counting_sort_exp(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        if ascending:
            for i in range(1, 10):
                count[i] += count[i - 1]
        else:
            for i in range(8, -1, -1):
                count[i] += count[i + 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            draw_list(
                draw_info,
                color_positions={i: draw_info.RED},
                clear_bg=True,
            )
            yield True
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    lst = draw_info.list
    max_val = max(lst)
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_exp(lst, exp)
        exp *= 10

    return lst
