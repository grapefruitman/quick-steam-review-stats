import re
import statistics
from bs4 import BeautifulSoup
import os


#sets up vars 
text_file_path = 'rawTagData.txt'
input_file_path = text_file_path
output_file_path = 'processedDataWithMeanMed.txt'


def find_first_html_file():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Iterate through the files and find the first .html file
    for file in files:
        if file.endswith(".html"):
            return file

    # If no .html file is found, return None
    return None

#this var needs to be after the function for some reason
html_file_path = find_first_html_file()


def create_text_file(file_path):
    with open(file_path, 'w') as file:
        file.write("HTML Tags with 'test class' attribute:\n")

def append_tags_to_file(html_content, file_path):
    soup = BeautifulSoup(html_content, 'html.parser')
    test_class_tags = soup.find_all(class_='hours')

    with open(file_path, 'a') as file:
        for tag in test_class_tags:
            file.write(f"{tag.name}: {tag.text}\n")

def process_text_file(input_file_path, output_file_path):
    # Read lines from the input file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Extract numbers from each line using regular expressions
    numbers = []
    for line in lines:
        # Use regular expression to extract numbers and decimals
        matches = re.findall(r'[-+]?\d*\.\d+|\d+', line)
        numbers.extend(map(float, matches))

    # Calculate average and median
    average = statistics.mean(numbers)
    median = statistics.median(numbers)

    # Prepend average and median to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Average: {average}\n")
        output_file.write(f"Median: {median}\n")

        for number in numbers:
            output_file.write(str(number) + '\n')


    # Specify the HTML file path


    # Specify the text file path


    # Create the initial text file
create_text_file(text_file_path)

    # Read HTML content from the file
with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Append tags with class 'test class' to the text file
append_tags_to_file(html_content, text_file_path)


process_text_file(input_file_path, output_file_path)

print(f"Processed data and appended average and median to {output_file_path}")

