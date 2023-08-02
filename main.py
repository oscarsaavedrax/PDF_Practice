from PyPDF2 import PdfWriter

# Set path and file names in a configuration page
import CONFIG

# Create the input and output file names
input_file = CONFIG.PATH + CONFIG.INPUT_FILE
output_file = input_file.replace("BOL", "POD")

print(input_file)
print(output_file)

# Create the merger object
merger = PdfWriter()

# Open BOL file
bol = open(input_file, "rb")

# Extract the POD paperwork from BOL
merger.append(fileobj=bol, pages=(1,3))

# Write to an output PDF file
output = open(output_file, "wb")
merger.write(output)

# Close the file descriptors
merger.close()
output.close()
bol.close()