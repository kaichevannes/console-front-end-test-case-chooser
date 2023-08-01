class SpecSection:
    """Represent a section of a confluence spec with a category and an array of tasks."""

    def __init__(self, category):
        self.tasks = []
        self.failed_tasks = []
        self.category = category

    def add_task(self, task):
        """Add a task to this section.

        Args:
            task (str): a task to be appended to the task array
        """
        self.tasks.append(task)

    def task_failed(self, task):
        """Add a task to the failed tasks.

        Args:
            task (str): the task which failed
        """
        self.failed_tasks.append(task)
