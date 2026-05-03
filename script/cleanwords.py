import csv

# Change 'my_gre_file.csv' to your actual filename
input_filename = 'data\L-GRE-再要你命3000.csv' 
output_filename = 'data\words_only.csv'

with open(input_filename, mode='r', encoding='utf-8') as infile:
    # Use a generic reader that handles different CSV styles
    reader = csv.reader(infile)
    
    extracted_words = []
    for row in reader:
        if len(row) > 1:
            # In your image, words were in the 2nd column (index 1)
            word = row[0].strip()
            # Basic check: skip empty rows or headers
            if word and word.lower() != 'word':
                extracted_words.append(word)

# Save as a single-column CSV
with open(output_filename, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    for word in extracted_words:
        writer.writerow([word])

print(f"Done! {len(extracted_words)} words saved to {output_filename}")