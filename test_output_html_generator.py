import os


class TestOutputHtmlGenerator:
    """Generate the test output file"""

    def __init__(
        self, filename, design_errors, functionality_errors, spec_tested_against
    ):
        """Costructor.

        Args:
            filename (str): the filename to output the generated test results to
            design_errors ([str]): an array containing 0+ design errors
            functionality_errors ([str]): an array containing 0+ functionality errors
            spec_tested_against ([SpecSection]): an array containing the spec sections tested
        """
        self.filename = filename
        self.design_errors = design_errors
        self.functionality_errors = functionality_errors
        self.spec_tested_against = spec_tested_against

    def generate_test_output_html(self):
        """Generate the html for each component of the output and then combine them together."""
        design_html = self.generate_design_html()
        functionality_html = self.generate_functionality_html()
        spec_tested_against_html = self.generate_spec_tested_against_html()

        with open(self.filename, "w", encoding="UTF-8") as output_file:
            output_file.write(
                design_html + functionality_html + spec_tested_against_html
            )

    def generate_design_html(self):
        """Construct the design section of the test output. If the design failures are empty then just add "Design passed", otherwise add an ordered list of failures.

        Returns:
            str: the design section of the html test output
        """
        design_html = "-----<em>Design</em>-----<br>"
        if len(self.design_errors) == 0:
            design_html += "Design passed<br>"
        else:
            design_html += "<ol>"
            for error in self.design_errors:
                design_html += f"<li>{error}</li>"
            design_html += "</ol>"
        design_html += "-----------------<br><br>"
        return design_html

    def generate_functionality_html(self):
        """Construct the functionality section of the test output. If the functionality failures are empty then just add "Functionality passed", otherwise add an ordered list of failures.

        Returns:
            str: the functionality section of the html test output
        """
        functionality_html = "-----<em>Functionality</em>-----<br>"
        if len(self.design_errors) == 0:
            functionality_html += "Functionality passed<br>"
        else:
            functionality_html += "<ol>"
            for error in self.functionality_errors:
                functionality_html += f"<li>{error}</li>"
            functionality_html += "</ol>"
        functionality_html += "-----------------------<br><br>"
        return functionality_html

    def generate_spec_tested_against_html(self):
        # Eventually bold the spec sections that failed.
        spec_tested_against_html = "-----<em>Spec Tested Against</em>-----<br>"
        for section in self.spec_tested_against:
            spec_tested_against_html += f"<b>{section.category}</b>"
            spec_tested_against_html += "<ul>"
            for task in section.tasks:
                spec_tested_against_html += f"<li>{task}</li>"
            spec_tested_against_html += "</ul>"
        spec_tested_against_html += "<em>(Bold subsections failed)</em><br>"
        spec_tested_against_html += "--------------------------------<br>"
        return spec_tested_against_html

    def show_html(self):
        """Open the HTML file stored in self.filename in the clients default browser."""
        os.system(f"start {self.filename}")
