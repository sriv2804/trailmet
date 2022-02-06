from .dataset import SyntheticDataset

class UltraMNIST(SyntheticDataset):
    """
    
    Args:
    
    """
    
    
    def __init__(self, root: str, split: str = "train", img_size: int = 2000,
                 img_scale_range: list = [28, 1000]):
        super().__init__(root)
        self.root_path = root
        self.img_size = img_size
        
        # check if data exists
        self.check_if_data_exists()
        
        
        
        
        
        
        
        
        