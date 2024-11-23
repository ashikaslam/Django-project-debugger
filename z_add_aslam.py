
import os
# Define the project directory and debugger function
project_dir = '/home/aslam/Desktop/projects/debug_sellzy'
debugger_function = 'debugger_by_aslam()'
# Loop through each Python file in the directory and subdirectories
for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()

            new_lines = []
            inside_function = False  # Track whether we're inside a function

            for i, line in enumerate(lines):
                # Append the current line to new_lines
                new_lines.append(line)

                # Detect the function definition line
                if line.strip().startswith('def ') and line.strip().endswith(':'):
                    inside_function = True
                    function_start_index = len(new_lines) - 1  # Track start of function

                # Insert debugger after the function definition, avoiding comments and decorators
                elif inside_function and line.strip() != '' and not line.strip().startswith('#'):
                    # Calculate the indentation level of the first actual line inside the function
                    indentation = ' ' * (len(line) - len(line.lstrip()))

                    # Ensure bounds and avoid duplicate debugger insertion
                    if function_start_index + 1 < len(new_lines) and debugger_function not in new_lines[function_start_index + 1]:
                        new_lines.insert(function_start_index + 1, f"{indentation}{debugger_function}\n")

                    inside_function = False  # Reset the flag after insertion

            # Write modified lines back to the file
            with open(file_path, 'w') as f:
                f.writelines(new_lines)

print("Debugger function inserted in all functions of the project with correct indentation, avoiding comments.")






