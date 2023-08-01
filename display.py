from test_case_chooser import TestCaseChooser
from failure import Failure, FunctionalityFailure
from config import WINDOWS, MAC, MOBILE, TABLET, HAS_DESIGN


class Display:
    """Display the test cases to the user."""

    def __init__(self, spec_sections):
        """"""
        self.test_case_chooser = TestCaseChooser(WINDOWS, MAC, MOBILE, TABLET)
        self.design_failures = []
        self.functionality_failures = []
        self.spec_sections = spec_sections

    def display(self):
        """Display the contents of the file provided to the user along with test cases"""
        # Design
        if HAS_DESIGN:
            design_failure = Failure("Design")
            if design_failure.check_failure():
                design_failure.get_failures()
            self.design_failures = design_failure.failures

        for section in self.spec_sections:
            functionality_failure = FunctionalityFailure(section)
            self.test_case_chooser.set_spec_section(section)
            print(f"Section Category = {section.category}")

            test_case = self.test_case_chooser.next_test_case()
            while test_case:
                local_task = self.test_case_chooser.current_task
                print()
                print(f"Task = {local_task}")
                for test in test_case:
                    print(f"Browser = {test[0]}")
                    print(f"Resolution = {test[1]}")
                if functionality_failure.check_failure():
                    functionality_failure.get_failures(local_task)
                test_case = self.test_case_chooser.next_test_case()

            local_functionality_failures = functionality_failure.failures
            self.functionality_failures += local_functionality_failures
