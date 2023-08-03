import os
from config import HAS_DESIGN


class HtmlGenerator:
    """Generate the test output file"""

    def __init__(
        self, filename, design_failures, functionality_failures, spec_tested_against
    ):
        """Costructor.

        Args:
            filename (str): the filename to output the generated test results to
            design_failures ([str]): an array containing 0+ design failures
            functionality_failures ([str]): an array containing 0+ functionality failures
            spec_tested_against ([SpecSection]): an array containing the spec sections tested
        """
        self.filename = filename
        self.design_failures = design_failures
        self.functionality_failures = functionality_failures
        self.spec_tested_against = spec_tested_against

    def generate_test_output_html(self):
        """Generate the html for each component of the output and then combine them together."""
        if HAS_DESIGN:
            design_html = self.generate_design_html()
        else:
            design_html = ""

        functionality_html = self.generate_functionality_html()

        with open(self.filename, "w", encoding="UTF-8") as output_file:
            output_file.write(
                design_html + functionality_html
            )

    def generate_design_html(self):
        """Construct the design section of the test output. If the design failures are empty then just add "Design passed", otherwise add an ordered list of failures.
        Template (At least one part of the design failed):
        ---------<em>Design Failures</em>---------<br>
        <ol>
            <li>Design problem 1</li>
            <li>Design problem 2</li>
        </ol>
        ---------------------------------<br><br>

        *Line breaks are used over p tags due to the auto formatting breaking when copy pasting from p tags into Productive.

        Returns:
            str: the design section of the html test output
        """
        if len(self.design_failures) == 0:
            return ""
        
        design_html = "---------<em>Design Failures</em>---------<br>"
        design_html += "<ol>"
        for failure in self.design_failures:
            design_html += f"<li>{failure}</li>"
        design_html += "</ol>"
        design_html += "---------------------------------<br><br>"
        return design_html

    def generate_functionality_html(self):
        """Construct the spec tested against section of the test output.
        
        Template:
        ------<em>Functionality Failures</em>------<br>
        <b>Users</b><br>
        <ul>
            <li><b>Subtask 2</b></li>
            <ol>
                <li>Functionality problem 1</li>
                <li>Functionality problem 2</li>
            </ol>
        </ul>
        ----------------------------------<br>
                
        *Line breaks are used over p tags due to the auto formatting breaking when copy pasting from p tags into Productive.

        Returns:
            str: the spec tested against sectino of the test output
        """
        # Eventually bold the spec sections that failed.
        spec_tested_against_html = "------<em>Functionality Failures</em>------<br>"
        for section in self.spec_tested_against:
            if len(section.failed_tasks) == 0:
                continue
            spec_tested_against_html += f"<b>{section.category}</b>"
            spec_tested_against_html += "<ul>"
            for task in section.tasks:
                if not task in section.failed_tasks:
                    continue
            
                spec_tested_against_html += f"<li><b>{task}</b></li>"
                spec_tested_against_html += "<ol>"
                for reason in section.failed_reasons[task]:
                    spec_tested_against_html += f"<li>{reason}</li>"
                spec_tested_against_html += "</ol>"
            spec_tested_against_html += "</ul>"
        spec_tested_against_html += "----------------------------------<br>"
        return spec_tested_against_html

    def show_html(self):
        """Open the HTML file stored in self.filename in the clients default browser."""
        os.system(f"start {self.filename}")
