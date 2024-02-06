"""Q1) Write a function to calculate the Euclidean distance and Manhattan distance between two 
vectors. The vectors dimension is variable. Please don’t use any distance calculation 
functions available in Python"""
def euclidean_distance(vector1, vector2):
    # Ensure vectors have the same dimensions
    assert len(vector1) == len(vector2), "Vectors must have the same dimension"
    
    # Calculate Euclidean distance
    distance = (sum((vector1[i] - vector2[i]) ** 2 for i in range(len(vector1)))) ** 0.5
    return distance

def manhattan_distance(vector1, vector2):
    # Ensure vectors have the same dimensions
    assert len(vector1) == len(vector2), "Vectors must have the same dimension"
    
    distance = 0
    for i in range(len(vector1)):
        diff = vector1[i] - vector2[i]
        if diff >= 0:
            distance += diff
        else:
            distance -= diff
    
    return distance

# Main program with print statements
if __name__ == "__main__":
    # Example vectors
    vector1 = [1, 2, 3]
    vector2 = [2,2,2]
    
    # Euclidean distance
    euclidean_dist = euclidean_distance(vector1, vector2)
    print(f"Euclidean Distance: {euclidean_dist}")
    
    #  Manhattan distance
    manhattan_dist = manhattan_distance(vector1, vector2)
    print(f"Manhattan Distance: {manhattan_dist}")




    #Q3)
    def label_encoding(categories):
    label_mapping = {}
    encoded_values = []
    label_count = 0
    
    for category in categories:
        if category not in label_mapping:
            label_mapping[category] = label_count
            label_count += 1
        encoded_values.append(label_mapping[category])
    
    return encoded_values

if __name__ == "__main__":
    categories = ['cat', 'dog', 'bird', 'dog', 'bird']
    numeric_encoding = label_encoding(categories)
    print(f"Label Encoded Categories: {numeric_encoding}")


