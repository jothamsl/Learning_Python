def main():
    list = [3,2,4,10,2,8]
    search_val = 10
    for i in range(len(list)):
        if list[i] == search_val:
            print(f"{search_val} found in index {i + 1}")

if __name__ == '__main__':
    main()
