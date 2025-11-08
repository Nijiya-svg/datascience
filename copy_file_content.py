source_file_name = input("Enter the source filename: ")
destination_file_name = input("Enter the destination filename: ")

with open(source_file_name, 'r') as source_file:
    content = source_file.read()

with open(destination_file_name, 'w') as dest_file:
    dest_file.write(content)

print("Content copied successfully.")
