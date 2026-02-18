# List operations

# Create List
L = [3, 4, 2, 5]

# Access elements
for I in L:
    print(I)

# Add elements
L.append(6)
L.extend([2, 5])
L.insert(2, 65)

print("List L after adding elements", L)

# Remove elements
L.pop(1)
L.pop()
L.remove(2)

print("List L after removing elements", L)

# Sorting in ascending
L.sort()
print("List L after sorting in ascending order (in place)", L)

A = sorted(L)
print("List A after sorting in ascending order in another variable", A)

# Sorting in descending
L.sort(reverse=True)
print("List L printed in descending order", L)

