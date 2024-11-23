


import inspect
def debug_info():
    
    # Get the caller's frame info
    caller_frame = inspect.stack()[1]
    file_name = caller_frame.filename
    line_number = caller_frame.lineno
    function_name = caller_frame.function
    # Define the specific files you want to print debug information for
    tracked_files = ["views.py"]

    # Check if the filename contains any of the tracked files
    if any(tracked_file in file_name for tracked_file in tracked_files):
        # Print debugging information only if the condition is met
    # Print debugging information from the caller's perspective
        print("Debug Information:")
        print("------------------------------")
        print(f"Directory  : {file_name}")
        print(f"Function   : {function_name}")
        print(f"Line       : {line_number}")
        print("------------------------------")
