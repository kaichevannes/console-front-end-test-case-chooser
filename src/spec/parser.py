from src.spec.section import SpecSection

TASK_INDICATORS = ["can", "shall", "must"]


class SpecParser:
    """Parse a text file containing the copy pasted contents of a confluence spec and convert it into an array of sections"""

    def __init__(self, filename):
        self.filename = filename
        self.sections = []

    def parse(self):
        """Parse the file this class was constructed with, ignoring blank lines.

        Returns:
            array(SpecSection): Array of SpecSections
        """
        try:
            with open(self.filename, "r", encoding="UTF-8") as spec_file:
                # Initialise the lines of the file, removing trailing characters and blank lines.
                lines = [line.rstrip() for line in spec_file]
                lines = list(filter(lambda x: x.strip(), lines))

                # Assumes that the first line of the spec is always a category.
                first_line = lines[0]
                remaining_lines = lines[1:]
                current_section = SpecSection(first_line)
                self.sections.append(current_section)
                for line in remaining_lines:
                    words = line.split(" ")
                    first_word = words[0]

                    if first_word.lower() in TASK_INDICATORS:
                        current_section.add_task(line)
                    else:
                        new_section = SpecSection(line)
                        current_section = new_section
                        self.sections.append(current_section)
        except:
            raise Exception(f"Unable to find file: {self.filename}. Make sure it is in the current directory and then try again.")

        return self.sections
