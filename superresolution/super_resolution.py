"""Main file to execute super resolution program."""

from parsing import parsing_config, parsing_inputs, parsing_output, parsing_method
from schemas.task_runner import TaskRunner


def main():
    parser = parser_builder()
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


if __name__ == "__main__":
    main()
