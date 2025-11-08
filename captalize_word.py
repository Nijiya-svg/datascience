input_file = input("Enter input filename: ")
output_file = input("Enter output filename: ")

with open(input_file, 'r') as infile:
    content = infile.read()

capitalized_content = ' '.join(word.upper() for word in content.split())

with open(output_file, 'w') as outfile:
    outfile.write(capitalized_content)

print("Each word has been capitalized and saved to", output_file)
