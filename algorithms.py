from visulizer import draw_list


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
                    color_positions={j: draw_info.GREEN, j + 1: draw_info.RED},
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
            draw_list(draw_info, {i: draw_info.GREEN, i - 1: draw_info.RED}, True)
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

        draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True

    return lst
