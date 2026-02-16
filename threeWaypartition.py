class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        s = i = 0
        e = n - 1

        while (i <= e):
            if arr[i] < a:
                arr[i], arr[s] = arr[s], arr[i]
                i += 1
                s += 1
            elif arr[i] > b:
                arr[i], arr[e] = arr[e], arr[i]
                e -= 1

            #Else we just move ahead in the arr.
            else:
                i += 1
