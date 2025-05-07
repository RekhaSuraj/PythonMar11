# UseCase: Real-world example of a generator - reading large files line by line
# Why This Is Good:
# Memory efficient: Only one line is in memory at a time.
# Scalable: Can handle files of any size.
# Clean and Pythonic.

def read_large_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line  # yield each line one at a time


for line in read_large_file("sample_text.txt"):
    print(line.strip())  # or process the line
