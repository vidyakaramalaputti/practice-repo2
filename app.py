# Define a reusable function
def get_user_role(user_data, target_name):
    # Lookup values in a dictionary safely using .get()
    return user_data.get(target_name, "User not found")

# Sample data
roles = {
    "Alice": "Admin",
    "Bob": "Developer",
    "Charlie": "Guest"
}

# Call the function
print(get_user_role(roles, "Bob"))    # Outputs: Developer
print(get_user_role(roles, "David"))  # Outputs: User not found
