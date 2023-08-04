from case.chooser import TestCaseChooser
from failure import Failure, FunctionalityFailure
import config

class Display:
    """Display the test cases to the user."""

    def __init__(self, spec_sections):
        """"""
        self.test_case_chooser = TestCaseChooser()
        self.design_failures = []
        self.functionality_failures = []
        self.spec_sections = spec_sections

    def display(self):
        """Display the contents of the file provided to the user along with test cases"""
        # Design
        print(f"config.has_design = {config.has_design}")
        if config.has_design:
            design_failure = Failure("Design")
            if design_failure.check_failure():
                design_failure.get_failures()
            self.design_failures = design_failure.failures

        for section in self.spec_sections:
            
            self.test_case_chooser.set_spec_section(section)
            print(f"Section Category = {section.category}")

            test_case = self.test_case_chooser.next_test_case()
            while test_case:
                functionality_failure = FunctionalityFailure(section)
                local_task = self.test_case_chooser.current_task
                # TODO: Isolate this
                print()
                print(f"Task = {local_task}")
                for test in test_case:
                    print(f"Browser = {test[0]} {test[1]}")
                    print(f"Resolution = {test[2]}")
                if functionality_failure.check_failure():
                    functionality_failure.get_failures(local_task)
                test_case = self.test_case_chooser.next_test_case()

                task_failures = functionality_failure.failures
                self.functionality_failures += task_failures
