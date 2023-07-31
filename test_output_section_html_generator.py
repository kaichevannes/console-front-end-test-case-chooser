# Overcomplicated

class TestOutputSectionHtmlGenerator:
    """Generate a section of the test output, e.g. design or functionality section."""

    def __init__(self, section_name, num_dashes, ordered, test_failures):
        """Constructor

        Args:
            section_name (str): the name of the section
            num_dashes (str): the number of dashes in the last line of the section
            ordered (bool): the type of html list, e.g. ol or ul
            test_failures ([str]): list of test failures for this section
        """
        self.section_name = section_name
        self.num_dashes = num_dashes
        self.ordered = ordered
        self.test_failures = test_failures
    
class TestOutputBasicSectionHtmlGenerator(TestOutputSectionHtmlGenerator):
    def generate_section(self):
        """Generate a section of the test output following the format from output_template.html

        Returns:
            str: HTML content of the section
        """
        section_html = f"-----<em>{self.section_name}</em>-----"
        if len(self.test_failures) == 0:
            section_html += f"{self.section_name} passed"
        else:
            if self.ordered:
                section_html += "<ol>"
            else:
                section_html += "<ul>"

            for failure in self.test_failures:
                section_html += f"<li>{failure}</li>"
        dashes = ["-" for _ in range(0, self.num_dashes)]
        section_html += f"{dashes}<br><br>"
        return section_html
    
    
class TestOutputSpecSectionGenerator(TestOutputSectionHtmlGenerator):
    def generate_section(self):
        """Generate a section of the test output following the format from output_template.html

        Returns:
            str: HTML content of the spec section
        """
        