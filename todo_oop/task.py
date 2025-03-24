from datetime import datetime

from matplotlib.pyplot import title


class Task:
    def __init__(self, title , date = None):
        self.title = title
        self.date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

    def to_dict(self):
        return {
            "title" : self.title,
            "date"  :self.date
        }
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["date"])
