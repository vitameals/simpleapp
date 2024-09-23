import pandas as pd

def load_and_process_data():
    # Path to the text file in the same directory
    file_path = os.path.join("PD Data APTWTi - C", "PD Data APTWTi", "Corona", "5.7kV.000.pdb.APTWTi.txt")  # Adjust this if your file is named differently
    try:
        # Read the tab-separated text file
        df = pd.read_csv(file_path, sep="\t", header=None)
        
        # Set column names
        df.columns = ['A', 'B', 'C', 'D', 'E']
        
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
