"""Image related schemas."""

import cv2
import numpy as np
import tifffile

from pathlib import Path
from pydantic import BaseModel, ConfigDict
from typing import Self, Literal

from wannareslikeyou.constants import (
    AllowedImgDataType,
    AllowedImgExt
)


class Image(BaseModel):
    """Image schema.
    
    Attributes:
        name: lorem ipsum
        path: lorem ipsum
        width: lorem ipsum
        height: lorem ipsum
        n_channels: lorem ipsum
        data: lorem ipsum
        data_type: lorem ipsum
        extension: lorem ipsum
    """
    name: str
    path: Path
    width: int
    height: int
    n_channels: int
    data: np.ndarray
    data_type: Literal["uint8", "float32"]
    extension: Literal[".npy", ".png", ".jpeg", ".tiff"]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def export(self):
        """docstring"""
        img_path = Path(self.path)
        # if not img_path.exists():
        #     raise FileExistsError("Cannot load image, path '%s' does not exist.", img_path.as_posix())
        
        if img_path.suffix not in AllowedImgExt:
            raise ValueError(f"Image extension ({img_path.suffix}) not handles.")
        else:
            name = img_path.stem
            extension = img_path.suffix
            if img_path.suffix == ".npy":
                np.save(file=img_path, arr=self.data)
            elif img_path.suffix in [".jpeg", ".png"]:
                cv2.imwrite(img_path, self.data)
            elif img_path.suffix == ".tiff":
                tifffile.imwrite(img_path, self.data)
            else:
                raise ValueError("Unexpected image type file.")

    def save(self):
        """docstring"""
        pass

    @classmethod
    def load(cls: Self, path: str) -> Self:
        """docstring"""
        img_path = Path(path)
        if not img_path.exists():
            raise FileExistsError("Cannot load image, path '%s' does not exist.", img_path.as_posix())
        
        if img_path.suffix not in AllowedImgExt:
            raise ValueError("Image extension (%s) not handles.", img_path.suffix)
        else:
            name = img_path.stem
            extension = img_path.suffix
            if img_path.suffix == ".npy":
                data = np.load(img_path)
            elif img_path.suffix in [".jpeg", ".png"]:
                data = cv2.imread(img_path)
            elif img_path.suffix == ".tiff":
                data = tifffile.imread(img_path)
            else:
                raise ValueError("Unexpected image type file.")
            
            data_type = str(data.dtype)
            if data.ndim == 2:
                n_channels = 2
                height = data.shape[1]
                width = data.shape[2]
            elif data.ndim == 3:
                n_channels = 3
                height = data.shape[1]
                width = data.shape[2]
            else:
                raise ValueError("Unexpected number of channels for image.")
            image = Image(name=name,
                          path=img_path,
                          width=width,
                          height=height,
                          n_channels=n_channels,
                          data=data,
                          data_type=data_type,
                          extension=extension)
        return image


class ImageList(BaseModel):
    """ImageList schema.
    
    Attributes:
        images_list: lorem ipsum    
    """
    images_list: list[Image]

    def export(self):
        for img in self.images_list:
            img.export()
    
    def save(self):
        for img in self.images_list:
            img.save()
    
    @classmethod
    def load(cls: Self, path_list: list) -> Self:
        imgs = []
        for path in path_list:
            imgs.append(Image.load(path))
        
        imgs_list = ImageList(images_list=imgs)
        return imgs_list
