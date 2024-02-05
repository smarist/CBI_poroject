import fitz  # PyMuPDF
import re
import json
import os

# Specify the base directory and PDF files range
base_dir = "/Users/Darego/Documents/CBI"
pdf_range = range(1, 25)

# Regex pattern to match the interviewer name and their sentences
# Assuming the interviewer's name is followed by a colon and their speech
pattern = re.compile(r'([A-Za-z]+(?: [A-Za-z]+)*): ([^:]+)')

# Function to convert a single PDF to JSON
def convert_pdf_to_json(pdf_filename, json_filename):
    # Open the PDF file
    pdf_document = fitz.open(pdf_filename)
    interviewer_data = []

    # Extract text and match the pattern on each page
    for page in pdf_document:
        text = page.get_text()
        matches = pattern.findall(text)
        for match in matches:
            interviewer_data.append({
                "Name": match[0],
                "Sentence": match[1].strip()
            })

    # Close the PDF file after extraction
    pdf_document.close()

    # Convert the list to JSON format
    json_output = json.dumps(interviewer_data, indent=4)

    # Save the JSON data to a file
    with open(json_filename, 'w') as json_file:
        json_file.write(json_output)

# Iterate through the range of PDF files
for i in pdf_range:
    pdf_filename = os.path.join(base_dir, f"{i:02d}.pdf")
    json_filename = os.path.join(base_dir, "interview_data", f"{i:02d}.json")
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(json_filename), exist_ok=True)

    # Convert the single PDF file to JSON
    convert_pdf_to_json(pdf_filename, json_filename)
