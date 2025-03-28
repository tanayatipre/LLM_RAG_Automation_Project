def generate_code(function_name):
    return f"""from automation_functions import {function_name}

def main():
    try:
        result = {function_name}()
        if result:
            print("Output:", result)
        else:
            print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
