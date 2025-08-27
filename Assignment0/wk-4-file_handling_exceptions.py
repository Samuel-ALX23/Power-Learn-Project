# Create input file with sample content
sample_lines = [
    "Python is a powerful programming language.",
    "It is great for data processing and automation.",
    "File handling is an essential skill in Python.",
    "This exercise demonstrates reading and writing files.",
    "Let's learn and have fun with Python!"
]

with open('input.txt', 'w') as file:
    file.write("\n".join(sample_lines))

# Process the file
try:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    # Count words and convert to uppercase
    total_words = 0
    processed_lines = []
    
    for line in lines:
        words = line.split()
        total_words += len(words)
        processed_lines.append(line.upper())
    
    # Write to output file
    with open('output.txt', 'w') as output_file:
        output_file.write("UPPERCASE CONTENT:\n")
        output_file.write("=" * 40 + "\n")
        output_file.writelines(processed_lines)
        output_file.write("\n" + "=" * 40 + "\n")
        output_file.write(f"TOTAL WORDS: {total_words}\n")
        output_file.write(f"TOTAL LINES: {len(lines)}\n")
    
    print("🎉 File processing completed successfully!")
    print(f"📝 Input file: input.txt")
    print(f"📄 Output file: output.txt")
    print(f"📊 Statistics: {total_words} words across {len(lines)} lines")

except FileNotFoundError:
    print("Error: Could not find input.txt")