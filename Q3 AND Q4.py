#Q3) & Q4) LABEL ENCODING AND HOT ENCODING

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

def one_hot_encoding(categories):
    unique_categories = list(set(categories))
    encoded_values = []
    
    for category in categories:
        encoding = [0] * len(unique_categories)
        index = unique_categories.index(category)
        encoding[index] = 1
        encoded_values.append(encoding)
    
    return encoded_values

if __name__ == "__main__":
    # Example categorical variables
    categories = ['GREEN', 'BLUE', 'RED', 'BLUE', 'RED']
    
    # Convert categorical variables to numeric using label encoding
    numeric_encoding = label_encoding(categories)
    print(f"Label Encoded Categories: {numeric_encoding}")
    
    # Convert categorical variables to one-hot encoding
    one_hot_encoding_result = one_hot_encoding(categories)
    print(f"One-Hot Encoded Categories: {one_hot_encoding_result}")
