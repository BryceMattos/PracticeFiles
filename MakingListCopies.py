# Creating list with various types of data

test_list = [1, 5, 4, 3, "index", 9, 3, 5, True]

# Displaying proper practices for created list copies

list_copy = test_list.copy()

list_copy2 = [i for i in test_list]

list_copy3 = test_list(:)

# Now, when editing each list, they will not mess with the previously existing lists
