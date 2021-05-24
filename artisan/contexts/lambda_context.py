import os
from artisan.contexts.context import BaseContext
from artisan.utils import generate_file


class LambdaContext(BaseContext):
    TEMPLATE_FILE_PATH = "/config/api/app"
    HANDLER_FILE_PATH = "/handlers/app"
    TYPE = "lambda"

    def __init__(self, file_name, **kwargs):
        self.project_directory = os.getcwd()
        self.file_name = file_name
        self.relative_path = kwargs.get("relative_path")
        self.url = kwargs.get("url")
        self.http_method = kwargs.get("http_method")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def execute(self) -> None:
        self._generate_template_file()
        self._generate_handler_file()

    def _generate_template_file(self) -> None:
        context = (
            f"Method: {self.http_method.upper() if self.http_method else ''}\n"
            f"Path: {self.url if self.url else ''}\n"
            "RequestParameters:\n"
            "  - method.request.header.version:\n"
            "      Required: false\n"
            "  - method.request.header.locale:\n"
            "      Required: false\n"
            "  - method.request.header.language:\n"
            "      Required: false\n"
            "  - method.request.header.timezone:\n"
            "      Required: false\n"
            "  - method.request.header.client-version:\n"
            "      Required: false\n"
        )

        generate_file(
            self.project_directory + self.TEMPLATE_FILE_PATH + self.relative_path,
            self.file_name + self.TEMPLATE_EXPANSION,
            context,
        )

    def _generate_handler_file(self) -> None:
        context = (
            "from common import response\n"
            "from src.common.app import app, Request\n"
            "\n"
            "\n"
            "@app.handler()\n"
            "def request_handler(request: Request):\n"
            "   pass\n"
        )

        generate_file(
            self.project_directory + self.HANDLER_FILE_PATH + self.relative_path,
            self.file_name + self.HANDLER_EXPANSION,
            context
        )

