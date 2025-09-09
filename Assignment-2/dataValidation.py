import re

def is_valid_input(value, data_type):
    if data_type == "integer":
        try:
            int(value)
            return True
        except ValueError:
            return False
    elif data_type == "float":
        try:
            float(value)
            return True
        except ValueError:
            return False
    elif data_type == "email":
        # Simple email regex
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, value))
    else:
        return False


# Example usage
if __name__ == "__main__":

    input_value = input("Enter input value: ")
    data_type = input("Enter data type (integer, float, email): ")

    print(is_valid_input(input_value, data_type))