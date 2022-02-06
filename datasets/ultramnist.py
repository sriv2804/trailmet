from .dataset import SyntheticDataset

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
                 generate_hard_flag: bool = False,
                 img_size: int = 2000,
                 img_scale_range: list = [28, 1000])->None:
        super().__init__(root)
        self.root_path = root
        self.base_data_path = base_data_path
        self.base_data = base_data
        self.base_url = base_url
        self.img_size = img_size

        # check if data exists
        self.check_if_data_exists()
        
    
        
        