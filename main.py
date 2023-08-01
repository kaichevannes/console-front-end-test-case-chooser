import sys
import argparse
from display import Display
from output_html_generator import OutputHtmlGenerator
from spec_parser import SpecParser


# Test profiles for B2B, B2C, middleground
def main():
    """Main method."""
    if args.filename is not None:
        spec_parser = SpecParser(args.filename)
    else:
        spec_parser = SpecParser("spec.txt")

    try:
        spec_sections = spec_parser.parse()
    except Exception as e:
        print(e)
        return

    display = Display(spec_sections)
    display.display()

    output_html_generator = OutputHtmlGenerator(
        "output.html",
        display.design_failures,
        display.functionality_failures,
        display.spec_sections,
    )
    output_html_generator.generate_test_output_html()
    output_html_generator.show_html()


def main_interactive():
    """Interactive main method. Get a number of configs."""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ConsoleFrontEndTestCaseChooser",
        description="Generate test cases based on a confluence spec and provide a test output.",
    )
    parser.add_argument("-f", "--filename")
    parser.add_argument("-i", "--interactive", action="store_true")
    args = parser.parse_args()
    if args.interactive:
        main_interactive()
    else:
        main()
