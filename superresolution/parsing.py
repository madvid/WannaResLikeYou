"""Functions related to parsingK"""
from pathlib import Path
from ruamel import yaml

from schemas.config import Config
from schemas.image import Image, ImageList

def parsing_config(config_file: str) -> Config:
    """Description."""
    if Path(config_file).exists():
        with open(config_file, 'r', encoding='utf8') as fyaml:
            data_dict = yaml.safe_load(fyaml)
        config = Config.model_validator(data_dict)
        return config
    else:
        raise FileExistsError('No config file found.')


def parsing_inputs(inputs: str | list):
    """Description."""

    imgs = []
    if isinstance(inputs, str):
        imgs.append(Image.load(inputs))
    else:
        for input in inputs:
            imgs.append(Image.load(input))
    image_list = ImageList()


def parsing_output():
    """Description."""
    pass


def parsing_method():
    """Description."""
    pass
