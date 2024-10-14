from argparse import ArgumentParser
from pathlib import Path
from ruamel.yaml import YAML
from wannareslikeyou.schemas.image import Image
from wannareslikeyou.interpolation.interpolate import (
    InterpolationConfig,
    InterpolationTask,
    InterpolationInput,
    IntepolationOutput
    )

def parser():
    """docstring"""
    parser = ArgumentParser()

    parser.add_argument("--input",
                        "-i",
                        type=str,
                        required=True,
                        help="input image.")
    parser.add_argument("--output",
                        "-o",
                        type=str,
                        required=True,
                        help="Path to the output image.")
    parser.add_argument("--overwrite", "-f", )
    parser.add_argument("--config",
                        "-c",
                        type=str,
                        required=True,
                        help="Path to the configuration file.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parser()

    # Loading the input image
    img_in = Image.load(path=args.input)
    
    # Loading the configuration
    with open(args.config, 'r') as fd:
        yaml = YAML()
        data = yaml.load(fd)
    
    config = InterpolationConfig.model_validate(data)

    # Executing the interpolation operation
    interpolator = InterpolationTask(
        input=InterpolationInput(name=img_in.name,
                                 path=args.input),
        output=IntepolationOutput(name=img_in.name,
                                  path=args.output,
                                  extension=Path(args.output).suffix),
        config=config,
    )

    interpolator.apply()
    