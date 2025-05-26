```python
import os

def create_hello_world(file_path='hello_world.html'):
    """
    Creates an HTML5 file with 'Hello, World!' content.
    
    Parameters:
    file_path (str): The path where the HTML file will be created.
                     Defaults to 'hello_world.html' in the current directory.
    
    Returns:
    bool: True if the file was created successfully, False otherwise.
    """
    try:
        # Define the HTML5 content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>"""

        # Write the HTML content to the specified file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"File '{file_path}' created successfully.")
        return True

    except IOError as e:
        # Handle any I/O errors
        print(f"An error occurred while creating the file: {e}")
        return False

def main():
    # Define the path where the HTML file will be created
    output_file_path = os.path.join(os.path.dirname(__file__), 'hello_world.html')
    
    # Create the hello world HTML file
    success = create_hello_world(output_file_path)
    
    if not success:
        print("Failed to create the HTML file.")

if __name__ == "__main__":
    main()
```