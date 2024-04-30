my_array = ["ck","BK","ck"]  # Array with duplicates

# Check for duplicates
has_duplicates = len(my_array) != len(set(my_array))

if has_duplicates:
    print("The array contains duplicates.")
else:
    print("The array does not contain duplicates.")
