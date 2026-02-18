# Movie List

# Movie names
L = ["IT", "Barbie", "Dhurandhar", "Frozen", "Moana"]

# Adding movies
L[2] = "Annabelle"
L.append("Turning Red")
L.insert(3, "Conjuring")

print("List L after adding movies:", L)

# Removing movie name
L.remove("Frozen")
print("List L after removing movie:", L)

# Accessing movies
print("\nAll movies:")
for movie in L:
    print(movie)

# Sorting movies (Ascending)
L.sort()
print("\nMovies in ascending order:", L)

# Sorting movies (Descending)
L.sort(reverse=True)
print("Movies in descending order:", L)

# Length of list
print("\nTotal number of movies:", len(L))
