def sort_by_coach_name(arr):
    if len(arr) > 1:
        # lakukan sorting
        # pertama tama bagi dua dulu arraynya
        mid = len(arr) // 2
        # kita pisahkan dia menjadi 2 array
        # array slicing
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Bagi terus sampai sisa 1 element
        sort_by_coach_name(left_arr)
        sort_by_coach_name(right_arr)

        # kembali lagi sorting
        i = 0 # left arr pointer
        j = 0 # right arr pointer
        k = 0 # pointer pada arraynya si temp

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].coach_name < right_arr[j].coach_name:
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

def sort_by_coach_pay_rate(arr):
    if len(arr) > 1:
        # lakukan sorting
        # pertama tama bagi dua dulu arraynya
        mid = len(arr) // 2
        # kita pisahkan dia menjadi 2 array
        # array slicing
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Bagi terus sampai sisa 1 element
        sort_by_coach_pay_rate(left_arr)
        sort_by_coach_pay_rate(right_arr)

        # kembali lagi sorting
        i = 0 # left arr pointer
        j = 0 # right arr pointer
        k = 0 # pointer pada arraynya si temp

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].coach_pay_rate < right_arr[j].coach_pay_rate:
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

def sort_by_coach_rating(arr):
    if len(arr) > 1:
        # lakukan sorting
        # pertama tama bagi dua dulu arraynya
        mid = len(arr) // 2
        # kita pisahkan dia menjadi 2 array
        # array slicing
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Bagi terus sampai sisa 1 element
        sort_by_coach_rating(left_arr)
        sort_by_coach_rating(right_arr)

        # kembali lagi sorting
        i = 0 # left arr pointer
        j = 0 # right arr pointer
        k = 0 # pointer pada arraynya si temp

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].coach_rating <= right_arr[j].coach_rating:
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