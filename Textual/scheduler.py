import schedule
from datetime import datetime, timedelta
import time
from pathlib import Path
from subprocess import Popen, CREATE_NO_WINDOW
import tomllib as toml
from dataclasses import dataclass, field


@dataclass
class Task:
    file: Path | str
    name: str = field(init=False)
    extension: str = field(init=False)

    def __post_init__(self) -> None:
        self.file = Path(self.file)
        self.name = self.file.name
        self.extension = self.file.suffix


class TaskHandler:
    handlers = {
        "wscript": [".vbs", ".js"],
        "cmd /k": [".bat", ".cmd"],
        "powershell -ExecutionPolicy RemoteSigned": [".ps1"]}

    def select_application(self, task: Task):
        return next((k for k, v in self.handlers.items() if task.extension in v), None)

    def run(self, task: Task) -> None:
        application = self.select_application(task=task)
        Popen(
            f"{application} {task.file}",
            creationflags=CREATE_NO_WINDOW)


class Config:
    pass


job = Task(file="F:/temp/notepad.bat")
TaskHandler().run(task=job)
