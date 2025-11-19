from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset   

class MyDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir_path = Path(data_dir).resolve()
        self.file_list = list(self.data_dir_path.glob("*"))

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        img_path = self.file_list[idx]
        image = Image.open(img_path)
        return image
    
    if __name__ == "__main__":
        my_dataset = MyDataset("04/data")
        print("===== problem1.1 =====")
        print(len(my_dataset))
        print("===== problem1.2 =====") 
        print(my_dataset[0].size)