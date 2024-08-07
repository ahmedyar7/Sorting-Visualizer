from visualization import Visualization
from draw_info import DrawInfo


class SortingAlgorithms:
    def __init__(self) -> None:
        self.visuals = Visualization()

    def bubble_sort(self, draw_info, ascending=True):
        lst = draw_info.list

        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                num1 = lst[j]
                num2 = lst[j + 1]

                if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    self.visuals.draw_list(
                        draw_info,
                        color_positions={
                            j: draw_info.RED,
                            j + 1: draw_info.RED,
                        },
                        clear_bg=True,
                    )
                    yield True

        return lst

    def insertion_sort(self, draw_info, ascending=True):
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
                self.visuals.draw_list(
                    draw_info,
                    color_positions={i: draw_info.RED, i - 1: draw_info.RED},
                    clear_bg=True,
                )
                yield True
        return lst

    def selection_sort(self, draw_info, ascending=True):
        lst = draw_info.list

        for i in range(len(lst) - 1):
            min_idx = i
            for j in range(i + 1, len(lst)):
                if (ascending and lst[j] < lst[min_idx]) or (
                    not ascending and lst[j] > lst[min_idx]
                ):
                    min_idx = j

            lst[i], lst[min_idx] = lst[min_idx], lst[i]

            self.visuals.draw_list(
                draw_info, {i: draw_info.RED, min_idx: draw_info.RED}, True
            )
            yield True

        return lst

    def merge_sort(self, draw_info, ascending=True):

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
                    self.visuals.draw_list(
                        draw_info, {start_idx + k: draw_info.RED}, True
                    )
                    k += 1
                    yield True

                while i < len(left_half):
                    lst[k] = left_half[i]
                    draw_info.list[start_idx + k] = lst[k]
                    self.visuals.draw_list(
                        draw_info, {start_idx + k: draw_info.RED}, True
                    )
                    i += 1
                    k += 1
                    yield True

                while j < len(right_half):
                    lst[k] = right_half[j]
                    draw_info.list[start_idx + k] = lst[k]
                    self.visuals.draw_list(
                        draw_info, {start_idx + k: draw_info.RED}, True
                    )
                    j += 1
                    k += 1
                    yield True

        lst = draw_info.list
        yield from merge_sort_recursive(lst, 0)
