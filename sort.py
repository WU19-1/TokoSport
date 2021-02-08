def mergesort(arr):
    if len(arr) > 1:
        # lakukan sorting
        # pertama tama bagi dua dulu arraynya
        mid = len(arr) // 2
        # kita pisahkan dia menjadi 2 array
        # array slicing
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Bagi terus sampai sisa 1 element
        mergesort(left_arr)
        mergesort(right_arr)

        # kembali lagi sorting
        i = 0 # left arr pointer
        j = 0 # right arr pointer
        k = 0 # pointer pada arraynya si temp

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # looping untuk masukin sisa arr kiri (kalau ada)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # looping untuk masukin sisa arr kanan (kalau ada)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def main():
    arr = [4,8,3,2,1]
    mergesort(arr)

    for i in arr:
        print(i)

main()