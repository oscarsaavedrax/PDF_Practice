from PyPDF2 import PdfWriter

# Import local path 
import CONFIG

# Prints underline for formatting
def print_line():
    print("-" * 26)

# Prints the menu options
def print_menu():
    print("\nMENU OPTIONS")
    print("1. Combine")
    print("2. Extract")
    print("3. Quit")
    print_line()
    
# Function to combine all files for load sheet
def combine():
    print("\nCOMBINE PAGES")
    
    # Get load name from user
    load_name = input("Enter the load name: ")
    
    # Create file names
    cover_file_name = CONFIG.PATH + f"{load_name} Cover.pdf"
    confirmation_file_name = CONFIG.PATH + f"{load_name} Load Con.pdf"
    bol_file_name = CONFIG.PATH + f"{load_name} BOL.pdf"
    load_sheet_name = CONFIG.PATH + f"{load_name}.pdf"
    
    # Create new pdf writer object
    merger = PdfWriter()
    
    # Open input files
    cover = open(cover_file_name, "rb")
    print(f"\nOpening covering page\n{cover_file_name.replace(CONFIG.PATH, '')}")
    confirmation = open(confirmation_file_name, "rb")
    print(f"\nOpening confirmation page\n{confirmation_file_name.replace(CONFIG.PATH, '')}")
    bol = open(bol_file_name, "rb")
    print(f"\nOpening bol page\n{bol_file_name.replace(CONFIG.PATH, '')}")
    
    # Merge all the files into one
    merger.append(cover)
    merger.append(confirmation)
    merger.append(bol)
    print("\nMerging all files together...")
    
    # Open the output file
    load_sheet = open(load_sheet_name, "wb")
    print(f"\nOpening output file\n{load_sheet_name.replace(CONFIG.PATH, '')}")
    
    # Write to the output file
    merger.write(load_sheet)
    print("\nWriting to output file...")
    print("Done.")
    
    # Close all files and the writer object
    merger.close()
    load_sheet.close()
    bol.close()
    confirmation.close()
    cover.close()
    
# Function to extract the POD paperwork from BOL
def extract():
    print("\nEXTRACT PAGES")

# -------------------------------- START -------------------------
# Print starting prompt
print("     PDF EDITING TOOL ")
print_line()

# Get users menu option
print_menu()
menu_option = int(input("Enter a menu option: "))
while menu_option != 3:
    # If user selects combine option
    if menu_option == 1:
        combine()
    # If user selects extract option
    elif menu_option == 2:
        extract()
            
    print_menu()
    menu_option = int(input("Enter a menu option: "))
