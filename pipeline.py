import csv
import os
from random import randint
import numpy as np
import pandas as pd

abs_path = os.path.dirname(__file__)

N = 50 # Number of input file to be generated
size = (80, 120) # matrix size

def generate_csv(data: list, outout_folder: str):
    """Create csv files"""
    # create the csv file
    with open(outout_folder, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    file.close()

def generate_data(directory):
    """Generate N csv data that contain n x m matrix"""

    for i in range(N):
        rows_list = []
        for _ in range(size[0]):
            # add rows to the the matrix
            row = [randint(0, pow(10, 6)) for _ in range(size[1])]
            rows_list.append(row)
        
        # set the file name
        file_name = "input_file_{}".format(str(i+1)) + ".csv"
        # save files inside the inputs directory
        folder_path = os.path.join(abs_path, "{}/{}".format(directory, file_name))
        
        # create the csv file
        generate_csv(rows_list, folder_path)


# step 1: load the data
def load_data(input_path: str):
    """Read the csv files and return the data it contains"""
    directory = os.path.join(abs_path, input_path)
    data = []
    try:
        # get all files inside the given directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".csv"):
                    df = pd.read_csv(directory + "/" + file, header=None)
                    data.append(df.values.tolist())

        return data
    except Exception as e:
        raise Exception(e) 
    
# step 2: Find min/max value of each file
def find_min_max(data):
    """Find the maximum and minimum values of each matrix"""
    min_max_values = []
    for matrix in data:
        min_max_values.append([np.max(matrix), np.min(matrix)])
    
    return min_max_values


# step 3: export the max/min values as csv
def generate_output(data, output_dir):
    # the output csv file is generated inside the /pipeline-data folder
    generate_csv(data=data, outout_folder="{}/output.csv".format(output_dir))


def run_pipeline(data_folder_path):
    data = load_data(data_folder_path)
    min_max_values = find_min_max(data)
    generate_output(data=min_max_values, output_dir=data_folder_path)

if __name__ == "__main__":
    input_folder = "pipeline-data"
    generate_data(input_folder)
    run_pipeline(input_folder)
    print("Pipeline completed!")