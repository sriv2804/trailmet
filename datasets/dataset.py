import os
import numpy as np

class SyntheticDataset:
    
    def __init__(self, root, base_dataset, self.n_samples):
        self.root_path = root
        self.base_data_path = base_dataset
    
    def generate_dataset():
        
        pass
    
    def generate_sample():
        
        pass
    
    def check_if_data_exists(self):
        if not self.root_path:
            print('Hello') 
            return
        else:
            print('Data exists at ', self.root_path)
            return
        
    def get_base_dataset(self):
        
        # check if base dataset exists, else download it
        if not os.listdir(self.base_data_path):
            
        