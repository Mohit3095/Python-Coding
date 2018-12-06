""" Code to find runner up score """

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sort_array = list(set(arr))
    sort_array.sort()
    print(sort_array[-2])
