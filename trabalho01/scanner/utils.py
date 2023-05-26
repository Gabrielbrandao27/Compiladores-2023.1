def check_array_has_only_null(arr):
    not_null_array = [x for x in arr if x is not None]
    return not len(not_null_array)

def check_array_has_only_falsy(arr):
    not_null_array = [x for x in arr if x ]
    return not len(not_null_array)