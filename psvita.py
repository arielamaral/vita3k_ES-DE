import pandas as pd
import os

# Function to create .psvita files
def create_psvita_file(name, id):
    file_name = name + ".psvita"
    with open(file_name, "w") as file:
        file.write(f"{id}")

# Read the xlsx file
file_path = "psvita.xlsx"  # Put the path of your xlsx file here
data = pd.read_excel(file_path)

# Check if the output directory exists, if not, create a directory
output_directory = "psvita_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate over the data and create the .psvita files
for index, row in data.iterrows():
    name = row["Name"]
    id = row["ID"]
    create_psvita_file(os.path.join(output_directory, name), id)

# List and print the files in the output directory
print("Created files:")
for file in os.listdir(output_directory):
    print(file)