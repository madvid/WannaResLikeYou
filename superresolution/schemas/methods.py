from pydantic import BaseModel
from typing import Annotated

class Method1Config(BaseModel):
    """Configuration of super resolution method 1."""
    attribut1: type1
    attribut2: type2

class Method2Config(BaseModel):
    """Configuration of super resolution method 2."""
    attribut1: type1
    attribut2: type2

class Method3Config(BaseModel):
    """Configuration of super resolution method 3."""
    attribut1: type1
    attribut2: type2


MethodConfig = Annotated[Method1Config,
                         Method2Config,
                         Method3Config,
                         "MethodConfig"]
