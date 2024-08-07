"""Image related schemas."""
from numpy import ndarray
from pathlib import Path
from pydantic import BaseModel
from typing import Self

from constants import AllowedImgDataType, AllowedImgExt


class Image(BaseModel):
    """Image schema."""
    name: str
    path: Path
    width: int
    height: int
    data: ndarray
    data_type: AllowedImgDataType
    extension: AllowedImgExt

    def export(self):
        pass

    def save(self):
        pass

    @classmethod
    def load(path: str) -> Self:
        img_path = Path(path)
        if not img_path.exists():
            raise FileExistsError(f"Cannot load image, path {path} does not exist.")
        
        if not img_path.suffix in AllowedImgExt:
            raise ValueError(f"Image extension ({img_path.suffix}) not handles.")
        else:
            name = img_path.stem
            extension = img_path.suffix
            if img_path.suffix == "npy":
                width = ...
                height = ...
                data = ...
                data_type = ...
            elif img_path.suffix == "jpeg":
                width = ...
                height = ...
                data = ...
                data_type = ...
            elif img_path.suffix == "tif":
                width = ...
                height = ...
                data = ...
                data_type = ...
            elif img_path.suffix == "png":
                width = ...
                height = ...
                data = ...
                data_type = ...
            
            image = Image(name,
                          img_path,
                          width,
                          height,
                          data,
                          data_type,
                          extension)
        return image


class ImageList(BaseModel):
    """ImageList schema."""
    images_list: list(Image)


    def export(self):
        for img in self.images_list:
            img.export()
    
    def save(self):
        for img in self.images_list:
            img.save()

    
    @classmethod
    def load(path_list: list) -> Self:
        imgs = []
        for path in path_list:
            imgs.append(Image.load(path))
        
        imgs_list = ImageList(images_list=imgs)
        return imgs_list