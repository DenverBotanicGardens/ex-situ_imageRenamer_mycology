import os
import csv

# Function to rename files based on CSV data
def rename_files(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Function to rename files based on CSV data for _02
def rename_files_02(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '_02' +'.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Function to rename files based on CSV data for _03
def rename_files_03(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '_03' +'.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Function to rename files based on CSV data for _04
def rename_files_04(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '_04' +'.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Function to rename files based on CSV data for _05
def rename_files_05(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '_05' +'.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Function to rename files based on CSV data for _06
def rename_files_06(csv_filename, directory):
    with open(csv_filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            old_name = row['fieldNumber']
            new_name = row['catalogNumber']
            
            old_path = os.path.join(directory, old_name + '_06' +'.jpg')
            file_ext = '.jpg'  # Get the file extension
            
            # Check if the new name already exists, and if so, add a suffix
            new_base = new_name
            suffix = 1
            while os.path.exists(os.path.join(directory, new_base + file_ext)):
                new_base = new_name + f"_EX{suffix:02d}"
                suffix += 1
            
            new_path = os.path.join(directory, new_base + file_ext)
            
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            except Exception as e:
                print(f'Error renaming {old_path}: {str(e)}')

# Replace 'existing_new_mapping.csv' with your CSV file path
csv_file = 'C:/Users/richard.levy/Downloads/1696265461-occur.csv'

# Replace 'file_directory' with the path to the directory containing the files
file_directory = 'Q:/Research/Images(new)/MuseumSpecimens/DBG/DBG_ExSitu/2022_CMS_Fair_Ex_Situ_Images_testCopy'

rename_files(csv_file, file_directory)
rename_files_02(csv_file, file_directory)
rename_files_03(csv_file, file_directory)
rename_files_04(csv_file, file_directory)
rename_files_05(csv_file, file_directory)
rename_files_06(csv_file, file_directory)


