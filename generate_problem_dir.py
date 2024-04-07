import os
import re
import argparse
from string import Template
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
PROBLEM_EXAMPLE = "1. Problem name"
PROBLEM_PATTERN = re.compile(r"(?P<number>\d+)\.\s(?P<name>[a-zA-Z0-9 -_.,]+)")

parser = argparse.ArgumentParser(
    description="Generate problem directory structure",
)

parser.add_argument(
    "-p",
    "--problem",
    type=str,
    help=f"problem name in format \"{PROBLEM_EXAMPLE}\"",
)


def generate_file_by_template(
    output_file: Path,
    template_file: Path,
    **kwargs,
) -> None:
    template: Template | None = None

    with open(template_file, "r") as f:
        template = Template(f.read())

    with open(output_file, "w") as f:
        f.write(template.substitute(**kwargs))


class Problem:
    def __init__(self, name: str) -> None:
        match = PROBLEM_PATTERN.match(name)

        if match is None:
            raise ValueError(
                f"Problem name must be in format \"{PROBLEM_EXAMPLE}\""
            )

        self.initial_name = name
        self.name = match.group("name").strip()
        self.number = match.group("number")

        formatted_name = self.name.lower().replace(' ', '-')
        self.format_name = f"{self.number}-{formatted_name}"

    def generate_dir(self) -> None:
        dir_path = BASE_DIR / self.format_name

        if dir_path.exists():
            raise ValueError(
                f"Problem directory already exists, check the following path: "
                f"{dir_path}",
            )

        # Create problem directory
        dir_path.mkdir()

        # Create __init__.py file
        (dir_path / "__init__.py").touch()

        # Generate solution file
        generate_file_by_template(
            dir_path / "solution.py",
            TEMPLATES_DIR / "solution.py",
            problem=self.initial_name
        )

        # Generate test file
        generate_file_by_template(
            dir_path / "test_solution.py",
            TEMPLATES_DIR / "test_solution.py",
        )


if __name__ == "__main__":
    args = parser.parse_args()

    problem = Problem(args.problem)
    problem.generate_dir()
