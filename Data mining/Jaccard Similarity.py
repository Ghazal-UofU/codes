# 19. 1. 2023
# Jaccard Similarity
# Ghazal



def jaccard_set(set1, set2):
    intersection = set(set1).intersection(set(set2))      # Define Jaccard Similarity function for two sets
    print('intersection is= ', intersection)            # intersection finds the common members on sets
    union = set(set1 + set2)
    print('union is = ', union)
    
    print(float(len(intersection) / len(union)))
    
# Define two sets 
a = [0, 1, 2, 5, 6]
b = [0, 2, 3, 4, 5, 7, 9]

 
jaccard_set(a, b)       # Find Jaccard Similarity between the two sets
