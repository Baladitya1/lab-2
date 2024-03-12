#Q1) 
def distance_calculator(vector1, vector2):
    # Prompt the user to choose between Manhattan or Euclidean distance
    choice = input("Manhattan distance or Euclidean distance (M/E): ")
    
    # Initialize an empty list to store the vectors
    vectors = []
    
    if choice.lower() == "e":
        try:
            # Append the input vectors to the list
            vectors.append(vector1)
            vectors.append(vector2)
            sum_of_squares = 0
            
            # Calculate the Euclidean distance
            for i in range(len(vectors[0])):
                sum_of_squares += (vectors[0][i] - vectors[1][i]) ** 2
            
            # Take the square root 
            distance = sum_of_squares ** (1/2)
            return distance
        except:
            return "Vectors must be of the same dimensions"
    
    elif choice.lower() == "m":
        try:
            # Append the input vectors to the list
            vectors.append(vector1)
            vectors.append(vector2)
            
            # Initialize the sum of absolute differences
            sum_of_abs_diffs = 0
            
            # Calculate the Manhattan distance
            for i in range(len(vectors[0])):
                sum_of_abs_diffs += abs(vectors[0][i] - vectors[1][i])
            
            # Manhattan distance is simply the sum of absolute differences
            distance = sum_of_abs_diffs
            return distance
        
        except:
            return "Vectors must be of the same dimensions"

# Define two vectors
vector1 = [1, 2, 3]
vector2 = [2, 2, 2]

# Call the distance_calculator function
result = distance_calculator(vector1, vector2)
print(result)


    #Q3)
   def label_encoding(categories):
    # Initialize an empty dictionary to store label mappings
    label_mapping = {}
    # Initialize an empty list to store the encoded values
    encoded_values = []
    # Initialize a counter to track the current label count
    label_count = 0
    
    # Iterate over each category in the input list
    for category in categories:
        # Check if the category is not already in the label mapping
        if category not in label_mapping:
            #  update the label count
            label_mapping[category] = label_count
            label_count += 1
        
        # Append the encoded value of the category to the list of encoded values
        encoded_values.append(label_mapping[category])
    
    # Return the list of encoded values, simply updating the list with numerical values
    return encoded_values

if __name__ == "__main__":
    # Define the input list of categories
    categories = ['cat', 'dog', 'bird', 'dog', 'bird']
    
    # Apply label encoding to the categories
    numeric_encoding = label_encoding(categories)
    
    # Print the result of label encoding
    print(f"Label Encoded Categories: {numeric_encoding}")

#Q4
def one_hot_encoding(categories):
    # Get unique categories
    unique_categories = list(set(categories))
    
    # Initialize an empty dictionary to store label mappings
    label_mapping = {category: i for i, category in enumerate(unique_categories)}
    
    # Initialize an empty list to store the encoded values
    encoded_values = []
    
    for category in categories:
        # Initialize a list to represent one-hot encoding for each category
        one_hot_encoding = [0] * len(unique_categories)
        
        # Set the index corresponding to the category to 1
        one_hot_encoding[label_mapping[category]] = 1
        
        # Append
        encoded_values.append(one_hot_encoding)
    return encoded_values

if __name__ == "__main__":
    # Define the input list of categories
    categories = ['cat', 'dog', 'bird', 'dog', 'bird']
    
    # Apply one-hot encoding to the categories
    one_hot_encoding_result = one_hot_encoding(categories)
    
    # Print the result of one-hot encoding
    print(f"One-Hot Encoded Categories:\n{one_hot_encoding_result}")



