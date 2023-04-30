import csv
import os
from random import randint
import numpy as np
import pandas as pd
import glob

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


# step 1: load the data, and find extremas
def load_and_process_data(input_path: str):
    """Read the csv files and return the data it contains"""
    directory = os.path.join(abs_path, input_path)
    results = []
    try:
        # get all csv files inside the given directory
        for filename in glob.glob(directory + "/" +"*.csv"):
            with open(filename, "r") as csvfile:
                df = pd.read_csv(csvfile, header=None)
                results.append(find_min_max(df.values.tolist()))

        return results
    except Exception as e:
        raise Exception(e) 

def find_min_max(matrix):
    """Find the maximum and minimum values of each matrix"""
    return [np.max(matrix), np.min(matrix)]


# step 2: export the max/min values as csv
def generate_output(data, output_dir):
    # the output csv file is generated inside the /pipeline-data folder
    generate_csv(data=data, outout_folder="{}/output.csv".format(output_dir))


def run_pipeline(data_folder_path):
    results = load_and_process_data(data_folder_path)
    generate_output(data=results, output_dir=data_folder_path)

if __name__ == "__main__":
    input_folder = "pipeline-data"
    generate_data(input_folder)
    run_pipeline(input_folder)
    print("Pipeline completed!")