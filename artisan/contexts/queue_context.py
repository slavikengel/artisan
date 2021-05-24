import os
from artisan.contexts.context import BaseContext
from artisan.utils import generate_file


class QueueContext(BaseContext):
    TEMPLATE_FILE_PATH = "/config/sqs/app"
    HANDLER_FILE_PATH = "/handlers/app"
    TYPE = "queue"

    def __init__(self, file_name, **kwargs):
        self.project_directory = os.getcwd()
        self.file_name = file_name
        self.relative_path = kwargs.get("relative_path")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def execute(self) -> None:
        self._generate_template_file()
        self._generate_handler_file()

    def _generate_template_file(self) -> None:
        context = "Parameters:\n" \
                  "  VisibilityTimeout:\n" \
                  "LambdaTrigger:"

        generate_file(
            self.project_directory + self.TEMPLATE_FILE_PATH + self.relative_path,
            self.file_name + self.TEMPLATE_EXPANSION,
            context,
        )

    def _generate_handler_file(self) -> None:
        context = (
            "from common import response\n"
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
