import os
import sys

import numpy as np
import scipy.misc
import torch
from torchvision import transforms
import torchvision.datasets as datasets

import matplotlib.pyplot as plt
import random

from .create_dataset import SyntheticDataset

class CreateUltraMNIST(SyntheticDataset):
    """
    
    Args:
        root (string): Root directory of UltraMNIST dataset
        base_data_path (string): Path of standard MNIST dataset
        base_url (string): URL for the base dataset for downloading
        n_channels (int): number of channels in each image
        n_samples ([int, int, int]): number of training, validation and test samples
    
    
    Attributes:
    
    """
    
    def __init__(self, root: str, base_data_path: str, base_data: str, base_url: str = '',
                 generate_hard_flag: bool = False, n_samples: list = [20000, 5000, 5000],
                 img_size: int = 2000, img_scale_fact: list = [1, 40],
                 max_dpimg = 3)->None:
        super().__init__(root, base_data_path, base_data, base_url, generate_hard_flag, 
                        n_samples)
        self.root_path = root
        self.base_data_path = base_data_path
        self.base_data = base_data
        self.base_url = base_url
        self.n_samples = n_samples
        self.img_size = img_size
        self.img_scale_fact = img_scale_fact
        self.max_dpimg = max_dpimg

        # check if data exists
        self.data_exists_flag = self.check_if_data_exists()
        
    def generate_dataset(self):
        
        if self.data_exists_flag:
            raise Exception('Data already exists, delete the content to download again')
            
        print('Checking for base dataset, if needed')
        base_loader = self.get_base_dataset()
        
        print('Preparing storage locations')
        os.mkdir(self.root_path)
        
        # creating train test and validation folders
        os.mkdir(os.path.join(self.root_path, 'train'))
        os.mkdir(os.path.join(self.root_path, 'val'))
        os.mkdir(os.path.join(self.root_path, 'test'))
        
        # generating samples
        self._generate_samples(os.path.join(self.root_path, 'train'), self.n_samples[0])
        
    
    def _generate_samples(self, data_path, n_samples):
        
        #iterate over sample generation
        for i in range(n_samples):
            
            # generating one batch of base_loader
            images, labels = next(iter(self.base_loader))
            print(images.shape, labels.shape)
            plt.imshow(images[0, 0,:,:])
            plt.show()
            plt.imshow(images[1, 0,:,:])
            plt.show()
            plt.imshow(images[2, 0,:,:])
            plt.show()
            print(labels)
            
            # generating the background mesh
            img, label = self._generate_one_sample(images, labels)
            
            
            
    def _generate_one_sample(self, images, labels):
        
        # creating the background
        img = np.zeros((self.img_size, self.img_size))
        label = 0
        # Add scaled versions of base image into the main image at random locations
        for i in range(images.shape[0]):
            sub_img = images[i, 0, :, :]
            # random sample a resoltion
            res_fact = random.randint(self.img_scale_fact[0], self.img_scale_fact[1])
            print(res_fact)
            scaled_simg = np.kron(sub_img, np.ones((res_fact,res_fact)))
            
            # add to img
            sub_len = scaled_simg.shape[0]
            randx = random.randint(0, img.shape[0]-sub_len)
            randy = random.randint(0, img.shape[0]-sub_len)
            
            img[randx:randx+sub_len, randy:randy+sub_len] += scaled_simg
            
            # updating the label
            label += labels[i]
        img[img > 1] = 1
        plt.imshow(img)
        print(label)
        sys.exit(0)
                   
        return
    
    def get_base_dataset(self):
        
        # check if base dataset exists, else download it
        if not os.path.exists(self.base_data_path):
            print('Base dataset does not exist at specified path, downloading now...')
            self.download_base_flag = True
            
        transform = transforms.Compose([
            # you can add other transformations in this list
            transforms.ToTensor()
        ])

        if self.download_base_flag:            
            mnist_trainset = datasets.MNIST(root=self.base_data_path, train=True, download=True, transform=transform)
            print(mnist_trainset)
        else:
            mnist_trainset = datasets.MNIST(root=self.base_data_path, train=True, download=False, transform=transform)
            print(mnist_trainset)
        
        # for data generation, mnist samples will be extracted using base_loader
        self.base_loader = torch.utils.data.DataLoader(mnist_trainset, batch_size=self.max_dpimg, shuffle=True)
        
        return
        
    
        
        