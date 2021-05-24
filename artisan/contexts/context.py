from abc import ABC, abstractmethod


class BaseContext(ABC):
    TEMPLATE_EXPANSION = ".yaml"
    HANDLER_EXPANSION = ".py"

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def _generate_template_file(self) -> None:
        pass

    @abstractmethod
    def _generate_handler_file(self) -> None:
        pass
