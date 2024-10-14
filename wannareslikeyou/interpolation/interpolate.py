from cv2 import resize

from pathlib import Path
from pydantic import BaseModel
from typing import Literal
from wannareslikeyou.schemas.image import Image
from wannareslikeyou.schemas.tasks.interpolate import Interpolator
from wannareslikeyou.constants import AllowedImgExt

class InterpolationInput(BaseModel):
    """docstring"""
    name: str
    path: str
    type: Literal["image"] = "image"

    def load(self):
        """docstring"""
        return Image.load(path=self.path)


class IntepolationOutput(BaseModel):
    """docstring"""
    name: str
    path: Path
    type: Literal["image"] = "image"
    extension: Literal[".npy", ".png", ".jpeg", ".tiff"]        


class InterpolationConfig(BaseModel):
    """docstring"""
    interpolator: Interpolator
    x_factor: float = 2
    y_factor: float = 2


class InterpolationTask(BaseModel):
    """docstring"""

    input: InterpolationInput
    output: IntepolationOutput
    config: InterpolationConfig

    def apply(self):
        """docstring"""
        in_img = self.input.load()

        out_data = self.config.interpolator.process(src=in_img.data,
                                                    x_factor=self.config.x_factor,
                                                    y_factor=self.config.y_factor)

        out_img = Image.model_validate(
            {
                "name": self.output.name,
                "path": self.output.path,
                "width": out_data.shape[1],  #TODO: write a method stat to fill parameter at instanciation
                "height": out_data.shape[2],  #TODO: write a method stat to fill parameter at instanciation
                "n_channels": out_data.shape[0],  #TODO: write a method stat to fill parameter at instanciation
                "data": out_data,  #TODO: write a method stat to fill parameter at instanciation
                "data_type": str(out_data.dtype),  #TODO: write a method stat to fill parameter at instanciation
                "extension": self.output.extension  #TODO: write a method stat to fill parameter at instanciation
            }
        )
        out_img.export()



        
