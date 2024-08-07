from pydantic import BaseModel

from schemas.methods import MethodConfig
from constants import AllowedMethods


class Config(BaseModel):
    name: AllowedMethods
    method: MethodConfig
