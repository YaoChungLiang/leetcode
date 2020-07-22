def moveZerosToEnd(arr):
    write = 0
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[read], arr[write] = arr[write], arr[read]
            write += 1

    return arr

if __name__ == "__main__":
    arr = [1,10,0,2,0,8,3,0]
    print(moveZerosToEnd(arr))