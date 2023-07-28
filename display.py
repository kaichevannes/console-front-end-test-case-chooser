from test_case_chooser import TestCaseChooser
from spec_parser import SpecParser
from config import WINDOWS, MAC, MOBILE, TABLET

class Display:
    """Display the test cases to the user."""
    
    def __init__(self):
        """"""
        self.test_case_chooser = TestCaseChooser(WINDOWS, MAC, MOBILE, TABLET)
        
    def display(self, filename):
        """Display the contents of the file provided to the user along with test cases"""
        spec_parser = SpecParser(filename)
        spec_section = spec_parser.parse()
        
        for section in spec_section:
            self.test_case_chooser.set_spec_section(section)
            print(f"Section Category = {section.category}")
            
            test_case = self.test_case_chooser.next_test_case()
            while test_case:
                print()
                print(f"Task = {self.test_case_chooser.current_task}")
                for test in test_case:
                    print(f"Browser = {test[0]}")
                    print(f"Resolution = {test[1]}")
                print()
                test_case = self.test_case_chooser.next_test_case()
        