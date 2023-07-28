#from spec_parser import SpecParser
from display import Display

# Test profiles for B2B, B2C, middleground

if __name__ == "__main__":
    # spec_parser = SpecParser("spec.txt")
    # spec_parser.parse()
    # for section in spec_parser.sections:
    #     print("=============================")
    #     print(f"Section Category = {section.category}")
    #     for task in section.tasks:
    #         print(task)
    #     print("=============================")
    display = Display()
    display.display("spec.txt")
