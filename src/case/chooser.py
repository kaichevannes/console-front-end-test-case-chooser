from src.case.generator import TestCaseGenerator
from config import (
    WINDOWS,
    MAC,
    DESKTOP_PROBABILITY,
    MOBILE_PROBABILITY,
    TABLET_PROBABILITY,
)


class TestCaseChooser:
    """Choose the test case for each task of a given spec section."""

    def __init__(self):
        self.spec_section = None
        self.task_index = -1
        self.current_task = None
        self.mobile_application = not WINDOWS or MAC

    def set_spec_section(self, spec_section):
        """Set the section to generate test cases for."""
        self.spec_section = spec_section
        self.task_index = -1

    def next_test_case(self):
        """Get the next test case to manually test.
        Generally, always check for desktop, sometimes for mobile, rarely for tablet.
        If it a mobile application then always for mobile, rarely for tablet.

        Returns:
            [(os,browser,resolution)]: An array of browser resolution pairs
        """
        if self.spec_section is None:
            raise LookupError(
                "Spec section is None, set the spec section before trying to generate a test case."
            )

        test_case = []
        self.task_index += 1

        if self.task_index >= len(self.spec_section.tasks):
            return test_case

        self.current_task = self.spec_section.tasks[self.task_index]

        if self.mobile_application:
            test_case_generator = TestCaseGenerator(0, 100, TABLET_PROBABILITY)
        else:
            test_case_generator = TestCaseGenerator(
                DESKTOP_PROBABILITY, MOBILE_PROBABILITY, TABLET_PROBABILITY
            )

        return test_case_generator.generate_test_case()
