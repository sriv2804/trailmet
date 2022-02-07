import os
import numpy as np
from .utils import download_mnist as MNIST

import torchvision.datasets as datasets

class SyntheticDataset:
    
    def __init__(self, root, base_data_path, base_data, base_url, generate_hard_flag,
                 n_samples):
        self.root_path = root
        self.base_data_path = base_data_path
        self.base_data = base_data
        self.base_url = base_url
        self.download_base_flag = False
        self.generate_flag = True
        self.generate_hard_flag = False
       
    def check_if_data_exists(self):
        if os.path.exists(self.root_path):
            print('Data exists at ', self.root_path)
            return True
        else:
            return False
    
    def generate_dataset(self, generate_hard_flag = False):
                    
        pass
    
    def generate_sample():
        
        pass
    


                
            
            
            
        