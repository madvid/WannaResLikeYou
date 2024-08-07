"""Main file to execute super resolution program."""

from argparse import ArgumentParser

from parsing import parsing_config, parsing_inputs, parsing_output, parsing_method
from schemas.task_runner import TaskRunner

def parsing():
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


if __name__ == "__main__":
    parser = parsing()
    args = parser.parse_args()

    # Retrieving config content
    config = parsing_config(args.config)

    # Retrieving and checking the inputs
    inputs = parsing_inputs(args.inputs)

    # Checking the output
    output = parsing_output(args.output)

    # Instanciating the method object
    method = parsing_method()

    # Applying the super resolution to the images
    task_runner = TaskRunner(config.task_runner)

    task_runner.run()
