def count_sheeps(array):
    # Initialize a counter for sheep present
    sheep_count = 0
    
    # Iterate through the array
    for sheep in array:
        # Check if the sheep is present (True)
        if sheep == True:
            sheep_count += 1  # Increment the counter
    
    return sheep_count

# Example usage:
sheep_array = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]

result = count_sheeps(sheep_array)
print("Number of sheep present:", result)  # Output: Number of sheep present: 17
