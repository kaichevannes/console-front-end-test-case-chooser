class SpecSection:
    """Represent a section of a confluence spec with a category and an array of tasks."""

    def __init__(self, category):
        self.tasks = []
        self.category = category

    def add_task(self, task):
        """Add a task to this section.

        Args:
            task (str): A task to be appended to the task array
        """
        self.tasks.append(task)
