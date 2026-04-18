# Function to find the first occurrence of a substring
def find_substring_occurrence(original_string, sub_string):
    try:
        # The index() method finds the first occurrence and returns its index
        index_position = original_string.index(sub_string)
        return index_position
    except ValueError:
        # If the substring is not found, a ValueError is raised
        return -1

# Example usage:
original = "The quick brown fox jumps over the lazy dog"
sub = "fox"

# Call the function
result = find_substring_occurrence(original, sub)

# Print the result
if result != -1:
    print(f"The substring '{sub}' was found at index: {result}")
else:
    print(f"The substring '{sub}' was not found in the original string.")

# Another example where the substring is not present
original2 = "Hello world"
sub2 = "Python"
result2 = find_substring_occurrence(original2, sub2)
if result2 != -1:
    print(f"The substring '{sub2}' was found at index: {result2}")
else:
    print(f"The substring '{sub2}' was not found in the original string.")
