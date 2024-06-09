# Scenario - Analyzing Customer Data

# Sample Customres
customers = [
    {"name": "Alice", "age": 35, "is_member": True, "purchases": [50, 80, 120]},
    {"name": "Bob", "age": 28, "is_member": False, "purchases": [25,40]},
    {"name": "Charlie", "age": 42, "is_member": True, "purchases": [15, 60, 90, 110]},
]

total_spent = 0 # Initialize variable to track total spending
member_count = 0 # Initialize variable to count member

# Iterate through customers using a for loop
for customer in customers:
    name = customer["name"]
    age = customer["age"]
    is_member = customer["is_member"]
    purchases = customer["purchases"]

    # Conditional statement to check membership status
    if is_member:
        print(f"{name} is a member and has spent:")
        member_count += 1
    else:
        print(f"{name} is not a member and has spent:")
    
    # Calculate total spent for each customer using a while loop
    purchase_index = 0
    while purchase_index < len(purchases):
        purchase = purchases[purchase_index]
        total_spent += purchase
        print(f"    -${purchase}") # Print individual purchase amounts
        purchase_index +=1         # Increment the index
    
    # Continue statement to skip rest of the loop for non-members
    if not is_member:
        continue                   # Skip calculating average for non-members

    # Calculate the average spending of members
    average_spent = total_spent/len(purchases)
    print(f"  Avearge spending: ${average_spent:.2f}\n")

# Calculate overall average spending
if member_count > 0:   # Avoid division by 0
    overall_average = total_spent/member_count   # Calculate only for members
    print(f"Overall average spending of members: ${overall_average:.2f}")