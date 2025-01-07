# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data
from datetime import datetime
from zoneinfo import ZoneInfo

class CustomComponent(Component):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "code"
    name = "CustomComponent"

    inputs = [
        MessageTextInput(
            name="author",
            display_name="Author",
            info="This is a custom component Input to define the Author Name",
            value="Samuel Matioli",
            tool_mode=True,
        ),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        tz = ZoneInfo("UTC")
        data = Data(data={"author": self.author, "updated_at": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")})
        self.status = data
        return data
