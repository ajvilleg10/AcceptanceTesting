class Task:
    def __init__(self, description, due_date, priority, completed=False):
        self._description = description
        self._due_date = due_date
        self._priority = priority
        self._completed = completed

    @property
    def description(self):
        return self._description

    @property
    def due_date(self):
        return self._due_date

    @property
    def priority(self):
        return self._priority

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value