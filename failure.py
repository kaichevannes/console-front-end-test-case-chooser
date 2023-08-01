class Failure:
    """Represent a generic failure, either design or functional"""

    def __init__(self, failure_name):
        self.failure_name = failure_name
        self.failures = []

    def check_failure(self):
        """Check if a design or function failed."""
        passed = input(f"{self.failure_name} passed (y/n)? ")
        match passed:
            case "y":
                return False
            case "":
                return False
            case "n":
                return True
            case _:
                self.check_failure()

    def get_failures(self, max_index=float("inf")):
        """Get all design failures."""
        index = 1
        prompt = lambda i: f"{self.failure_name} failure {i} (n to stop): "
        
        failure = input(prompt(index))
        while failure != "n" and failure != "":
            self.failures.append(failure)
            index += 1
            if index > max_index: 
                break
            failure = input(prompt(index))
            
        print(f"self.failures = {self.failures}")


class FunctionalityFailure(Failure):
    """Represent specifically a functional failure."""

    def __init__(self, spec_section):
        super().__init__("Functionality")
        self.spec_section = spec_section

    def get_failures(self, task, max_index = float('inf')):
        """Get a single failure for a given task."""
        super().get_failures(max_index)
        self.spec_section.task_failed(task)
