import argparse
from display import Display
from output_html_generator import OutputHtmlGenerator
from spec_parser import SpecParser
from browser_distribution import WindowsBrowserDistribution


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
    """Interactive main method. Get a number of test cases for windows."""
    browser_distribution = WindowsBrowserDistribution()
    num_test_cases = get_num_test_cases()
    print()
    while num_test_cases > 0:
        test_case = browser_distribution.get_test_case()
        print(f"Browser = {test_case[0]}")
        print(f"Resolution = {test_case[1]}")
        input()
        num_test_cases -= 1


def get_num_test_cases():
    """Get the number of test cases, try again until the user provides a positive integer."""
    user_input = input("Enter the number of test cases to generate: ")

    if user_input == "":
        return float("inf")
    elif user_input.isdigit():
        return int(user_input)
    else:
        return get_num_test_cases()


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
