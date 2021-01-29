def main():
    search_val = 8
    arr = [1, 3, 5, 7, 8]
    high = len(arr) - 1
    binary_search(arr, search_val, 0, high)


def binary_search(arr, val, low, high):
    # Define base case
    if val == arr[high]:
        print(f'{val} found in index {high}')

    # Recursively search list
    if val > high:
        binary_search(arr, val, high, arr[-1])


if __name__ == '__main__':
    main()
