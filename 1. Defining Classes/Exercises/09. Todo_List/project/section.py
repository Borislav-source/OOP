class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task):
        for t in self.tasks:
            if t.name == task:
                t.completed = True
                return f"Completed task {task}"
        return f"Could not find task with the name {task}"

    def clean_section(self):
        for task in range(len(self.tasks)):
            if self.tasks[task].completed:
                self.tasks[task] = None
        count_of_removed_tasks = self.tasks.count(None)
        self.tasks = [t for t in self.tasks if t is not None]
        return f"Cleared {count_of_removed_tasks} tasks."

    def view_section(self):
        data = f'Section {self.name}:\n'
        for task in self.tasks:
            data += f"{task.details()}\n"
        return data
