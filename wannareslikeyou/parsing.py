"""Functions related to parsing"""

from argparse import ArgumentParser
from pathlib import Path
from ruamel import yaml

from schemas.config import Config
from schemas.image import Image, ImageList

def parser_builder():
    """Creating the parser."""
    
    parser = ArgumentParser(prog="Super Resolution",
                            description="Apply super resolution method to enhance image resolution.")
    
    parser.add_argument("-i",
                        "--input",
                        type=str,
                        action="store_true",
                        help="Input directories or files.")
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        help="Ouput directory to save result images.")
    parser.add_argument("-m",
                        "--method",
                        type=str,
                        choices=["Algo1", "Algo2", "Algo3"],
                        help="name of the super resolution method to apply.")
    parser.add_argument("-c",
                        "--config",
                        type=str,
                        help="Configuration file describing the hyperparameter of the method.")
    return parser

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
        imgs.append(Image.load(path=inputs))
    elif isinstance(inputs, list):
        for input_ in inputs:
            imgs.append(Image.load(path=input_))
    else:
        type_error = str(type(inputs))
        raise TypeError("inputs type '%s' is not handled.", type_error)
    
    list_images = ImageList(image_list=imgs)

    return list_images


def parsing_output():
    """Description."""
    pass


def parsing_method():
    """Description."""
    pass
