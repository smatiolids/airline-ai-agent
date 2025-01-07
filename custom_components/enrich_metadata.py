# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import DataInput, Output
from langflow.schema import Data


class CustomComponent(Component):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "code"
    name = "CustomComponent"

    inputs = [
        DataInput(
            name="input_data",
            display_name="Input Data",
            info="This is a custom component Input",
            value="Hello, World!",
            tool_mode=True,
        ),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        
        data_objects = []
        
        if self.input_data:
            data_objects.extend(self.input_data)

        # Update each Data object with the new metadata, preserving existing fields
        for data in data_objects:
            data.data["file_name"] = Path( data.data["file_path"]).name
            data.data["category"] = data.data["file_name"].split("_")[0].strip().lower()
            
        data = data_objects
        self.status = data
        return data