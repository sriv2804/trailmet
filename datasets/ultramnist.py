from .dataset import SyntheticDataset

class UltraMNIST(SyntheticDataset):
    
    def __init__(self, root: str, split: str = "train", img_size: int = 2000,
                 img_scale_range: list = [28, 1000]):
        super().__init__()
        print('Inherited init created correctly.')
        self.root_path = root
        self.img_size = img_size
        
        
        
    #def _generate_ultramnist(self, ):
        
        
        