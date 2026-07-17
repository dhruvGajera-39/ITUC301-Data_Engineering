import os
import shutil
import pandas as pd

# Folder paths
input_folder = "incoming_files"
quarantine_folder = "quarantine"

# Create quarantine folder if it doesn't exist
os.makedirs(quarantine_folder, exist_ok=True)

# Open quality log file
with open("quality.log", "a") as log:

    # Read every file in incoming_files
    for file in os.listdir(input_folder):

        # Process only CSV files
        if file.endswith(".csv"):

            filepath = os.path.join(input_folder, file)

            # Read CSV
            df = pd.read_csv(filepath)

            # Check if CustomerID column exists
            if "CustomerID" not in df.columns:

                # Move invalid file
                shutil.move(filepath, os.path.join(quarantine_folder, file))

                # Write to log
                log.write(f"{file} moved to quarantine (CustomerID missing)\n")

                print(file, "moved to quarantine")

            else:
                print(file, "is valid")