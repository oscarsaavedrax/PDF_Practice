from PyPDF2 import PdfWriter

# Import path and input file names from configuration page
import CONFIG

print("     PDF EDITING TOOL ")
print("-" * 26)

# Create the input and output file names
input_file = CONFIG.PATH + CONFIG.INPUT_FILE
print(f"Importing file: {input_file}")
print("Done.\n")

# Edit input file name to create output file name
output_file = input_file.replace("BOL", "POD")

# Create the merger object
merger = PdfWriter()

# Open BOL file
bol = open(input_file, "rb")
print(f"Opening input file...")
print("Done.\n")

# Extract the POD paperwork from BOL
merger.append(fileobj=bol, pages=(1,3))
print("Extracting pages...")
print("Done.\n")

# Open the output PDF file
output = open(output_file, "wb")
print(f"Opening output file: {output_file}")
print("Done.\n")

# Write to the output file
merger.write(output)
print(f"Writing to output file...")
print("Done.\n")

# Close the file descriptors
merger.close()
output.close()
bol.close()