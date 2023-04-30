import unittest
import os
import csv
from pipeline import load_and_process_data, generate_output, generate_csv
import pandas as pd

abs_path = os.path.dirname(__file__)

# mock data
matrix_1 = [[9965,1562,232], [195128,1355,9876], [992729,6025,456]]
matrix_2 = [[19555,653,23], [895128,91355,8788898], [792729,5025,1456]]
matrix_3 = [[786,876801,876323], [7653,42781,98261873], [233,4,986542]]

class TestPipeline(unittest.TestCase):
    def setUp(self):
        """Generate the testing files"""
        self.results = []
        try:
            os.mkdir(os.path.join(abs_path, "tests")) # create the tests folder
        except OSError as error: 
            pass  
        try: 
            os.remove(os.path.join(abs_path, "./tests/output.csv")) # delete the output csv if it exists
        except OSError as error: 
            pass  
        
        # generate 3 csv files with those content
        matrices = [matrix_1, matrix_2, matrix_3]
        for i, m in enumerate(matrices):
            folder_path = os.path.join(abs_path, "{}/{}".format("tests", "test-data-{}.csv".format(str(i+1))))
            generate_csv(m, folder_path)

    def test_load_and_process_data(self):
        """Check that data are loaded correctly"""
        data = load_and_process_data(input_path="tests")
        # It should successfully load 3 csv files into a list
        self.assertEqual(len(data), 3)

        # check matrix max/min values
        self.assertEqual(data[0], [992729, 232]) # file 1
        self.assertEqual(data[1], [8788898, 23]) # file 2
        self.assertEqual(data[2], [98261873, 4]) # file 3
        return data

    def test_generate_output(self):
        # It should create a two column csv file (tests/output.csv)
        generate_output(data=self.test_load_and_process_data(), output_dir="tests")
        
        # Check its content
        output_dir = os.path.join(abs_path, "tests/output.csv")
        df = pd.read_csv(output_dir, header=None)
        output_content = df.values.tolist()
        self.assertEqual(output_content[0], [992729, 232])
        self.assertEqual(output_content[1], [8788898, 23])
        self.assertEqual(output_content[2], [98261873, 4])


if __name__ == '__main__':
    #unittest.main()
    # order sequence of execution
    test_order = ["test_load_and_process_data", "test_generate_output"] 
    test_loader = unittest.TestLoader()
    test_loader.sortTestMethodsUsing = lambda x, y: test_order.index(x) - test_order.index(y)
    unittest.main(testLoader=test_loader)