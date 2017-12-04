#!/usr/bin/env python3


def peak_in_1d(input_list):
    middle_pos = len(input_list) // 2
    input_list = list(input_list)
    if len(input_list) == 1:
        return input_list[0]
    elif (len(input_list) > middle_pos + 1) and (
            input_list[middle_pos] < input_list[middle_pos + 1]):
        return peak_in_1d(input_list[middle_pos + 1:])
    elif input_list[middle_pos] < input_list[middle_pos - 1]:
        return peak_in_1d(input_list[:middle_pos])
    else:
        return input_list[middle_pos]


def get_nth_column(n, input_list):
    return [l[n] for l in input_list]


def peak_in_2d(input_list):
    if len(input_list) == 1:
        return max(input_list[0])
    n = len(input_list) // 2
    middle_column = get_nth_column(n, input_list)
    max_val = max(middle_column)
    global_max_idx = middle_column.index(max_val)
    if max_val < (input_list[n - 1][global_max_idx]):
        input_list = [get_nth_column(m, input_list) for m in range(0, n)]
        return peak_in_2d(input_list)
    elif max_val < (input_list[n + 1][global_max_idx]):
        input_list = [
            get_nth_column(m, input_list) for m in range(
                n + 1, len(input_list)
            )
        ]
        return peak_in_2d(input_list)
    else:
        return max_val


def peak_in_2d_alt(input_list):
    if len(input_list) == 1:
        return peak_in_1d(input_list[0])
    n = len(input_list) // 2
    middle_column = get_nth_column(n, input_list)
    max_val = peak_in_1d(middle_column)
    global_max_idx = middle_column.index(max_val)
    if max_val < (input_list[n - 1][global_max_idx]):
        input_list = [get_nth_column(m, input_list) for m in range(0, n)]
        return peak_in_2d(input_list)
    elif max_val < (input_list[n + 1][global_max_idx]):
        input_list = [
            get_nth_column(m, input_list) for m in range(
                n + 1, len(input_list)
            )
        ]
        return peak_in_2d(input_list)
    else:
        return max_val


if __name__ == "__main__":
    a = [[10, 8, 10, 10], [14, 13, 12, 11], [15, 9, 11, 21], [16, 17, 19, 20]]
    peak_in_1d(a[0])
    peak_in_2d(a)
    peak_in_2d_alt(a)
