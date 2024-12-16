import time
import sys

# Function to show loading progress
def loading_screen(duration):
    # Number of steps for progress
    steps = 50
    # Iterate through each step
    for i in range(steps + 1):
        # Calculate progress in percentage
        progress = (i / steps) * 100
        # Create a visual progress bar
        bar = '#' * i + '-' * (steps - i)
        # Print the loading message and progress bar
        sys.stdout.write(f"\rLoading... [{bar}] {progress:.2f}%")
        sys.stdout.flush()  # Ensure immediate display
        time.sleep(duration / steps)  # Control the speed of loading

    # After the loop, print a message indicating completion
    sys.stdout.write("\rLoading... [####################] 100.00%\n")
    sys.stdout.flush()
    print("Task Completed!")

# Call the loading screen function with a desired duration (e.g., 5 seconds)
loading_screen(5)