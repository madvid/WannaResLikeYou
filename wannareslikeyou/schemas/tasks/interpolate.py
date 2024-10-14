from pydantic import Field, BaseModel
from typing import Literal, Annotated
import cv2
import numpy as np
from functools import partial 


class LinearInterpolator(BaseModel):
    """docstring"""
    method: Literal["linear"]

    def process(self, src: np.ndarray, x_factor: float, y_factor: float) -> partial[np.ndarray]:
        """docstring"""
        return cv2.resize(src=src,
                          dsize=None,
                          fx=x_factor,
                          fy=y_factor,
                          interpolation=cv2.INTER_LINEAR)


class NearesInterpolator(BaseModel):
    """docstring"""
    method: Literal["nearest"]

    def process(self, src: np.ndarray, x_factor: float, y_factor: float) -> partial[np.ndarray]:
        """docstring"""
        return cv2.resize(src=src,
                          dsize=None,
                          fx=x_factor,
                          fy=y_factor,
                          interpolation=cv2.INTER_NEAREST)


class CubicInterpolator(BaseModel):
    """docstring"""
    method: Literal["cubic"]

    def process(self, src: np.ndarray, x_factor: float, y_factor: float) -> partial[np.ndarray]:
        """docstring"""
        return cv2.resize(src=src,
                          dsize=None,
                          fx=x_factor,
                          fy=y_factor,
                          interpolation=cv2.INTER_CUBIC)


class LanczosInterpolator(BaseModel):
    """docstring"""
    method: Literal["lanczos4"]

    def process(self, src: np.ndarray, x_factor: float, y_factor: float) -> partial[np.ndarray]:
        """docstring"""
        return cv2.resize(src=src,
                          dsize=None,
                          fx=x_factor,
                          fy=y_factor,
                          interpolation=cv2.INTER_LANCZOS4)


Interpolator = Annotated[LinearInterpolator |
                         NearesInterpolator |
                         CubicInterpolator |
                         LanczosInterpolator, Field(discriminator="method")]
