import os

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Define the file name and path
file_name = "wave-vector-lines.txt"
file_path = os.path.join(current_directory, file_name)

# Generate lines of text from "wave-vector-01.svg" to "wave-vector-44.svg"
with open(file_path, "w") as f:
    for i in range(1, 45):
        # Format the number with leading zeros
        num_str = f"{i:02}"
        line = f'<img src="../../poster/assets/background-waves/wave-vector-{num_str}.svg" id="wave-vector-{num_str}" class="wave-vector">\n'
        f.write(line)

print(f"Text file '{file_name}' has been created in the directory: {current_directory}")
