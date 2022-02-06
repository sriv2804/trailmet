from .dataset import SyntheticDataset

class CreateUltraMNIST(SyntheticDataset):
    """
    
    Args:
        root (string): Root directory of UltraMNIST dataset
        base_data (string): Path of standard MNIST dataset
        n_channels (int): number of channels in each image
        n_samples ([int, int, int]): number of training, validation and test samples
    
    
    Attributes:
    
    """
    
    
    def __init__(self, root: str, base_data: str, img_size: int = 2000,
                 img_scale_range: list = [28, 1000])->None:
        super().__init__(root)
        self.root_path = root
        self.img_size = img_size
        
        # check if data exists
        self.check_if_data_exists()
        
        #
        
        
        
    def get_r
    def generate_dataset()
    
        
        