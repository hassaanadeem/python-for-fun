# picking single card from a deck on O(n)

def find_single_element(lst):
    # Create empty sets to keep track of unique and non-unique elements
    unique_elements = set()
    non_unique_elements = set()

    # Loop through the list and add elements to the appropriate set
    for element in lst:
        if element in non_unique_elements:
            continue
        if element in unique_elements:
            unique_elements.remove(element)
            non_unique_elements.add(element)
        else:
            unique_elements.add(element)

    # Return the first unique element, or None if none exists
    if len(unique_elements) > 0:
        return next(iter(unique_elements))
    else:
        return None

print(find_single_element([1,1,1,2,3,3,4,4,4,5,5,5,5]))
