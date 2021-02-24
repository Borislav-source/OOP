class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name == self.name:
            return f"Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        self.due_date = new_date
        return new_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_index, new_comment):
        if comment_index not in range(len(self.comments)):
            return "Cannot find comment"
        self.comments[comment_index] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

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
        data = f'Section {self.name}\n'
        for task in self.tasks:
            data += f"{task.details()}\n"
        return data


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.complete_task("Make bed"))
print(section.clean_section())
print(section.view_section())
