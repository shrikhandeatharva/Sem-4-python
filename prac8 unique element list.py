def get_unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example usage
sample_list = [1, 1, 1, 2, 2, 3, 3, 4]
unique_list = get_unique_elements(sample_list)
print("Unique list is : ")
print(unique_list)
