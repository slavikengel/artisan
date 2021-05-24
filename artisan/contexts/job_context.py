import os
from artisan.contexts.context import BaseContext
from artisan.utils import generate_file


class JobContext(BaseContext):
    TEMPLATE_FILE_PATH = "/config/jobs/app"
    HANDLER_FILE_PATH = "/handlers/app"
    TYPE = "job"

    def __init__(self, file_name, **kwargs):
        self.project_directory = os.getcwd()
        self.file_name = file_name
        self.relative_path = kwargs.get("relative_path")
        self.period = kwargs.get("period")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def execute(self) -> None:
        self._generate_template_file()
        self._generate_handler_file()

    def _generate_template_file(self) -> None:
        context = f"expression: 'rate({self.period if self.period else ''} minutes)'"

        generate_file(
            self.project_directory + self.TEMPLATE_FILE_PATH + self.relative_path,
            self.file_name + self.TEMPLATE_EXPANSION,
            context,
        )

    def _generate_handler_file(self) -> None:
        context = (
            "from common import response\n" # TODO discuss about old and new common. Witch one will be import. 
            "from src.common.app import app\n"
            "\n"
            "\n"
            "@app.cli_handler()\n"
            "def request_handler(event):\n"
            "   pass\n"
        )

        generate_file(
            self.project_directory + self.HANDLER_FILE_PATH + self.relative_path,
            self.file_name + self.HANDLER_EXPANSION,
            context
        )
