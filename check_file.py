import os

# Specify the full path to your Excel file
file_path = r'C:\Users\vskee\OneDrive\Desktop\material_dashboard\sample_data_material.xlsx'

# Check if the file exists
if os.path.isfile(file_path):
    print("✅ File found.")
else:
    print("❌ File not found.")

