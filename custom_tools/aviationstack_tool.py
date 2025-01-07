# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import MessageTextInput, Output, DropdownInput, StrInput, SecretStrInput
from langflow.schema import Data
import requests

class CustomComponent(Component):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "code"
    name = "CustomComponent"
    
    # API Reference: https://aviationstack.com/documentation
    inputs = [
        StrInput(
            name="flight_number",
            display_name="Flight Number",
            info="Flight Number (IATA)",
            value="AA3",
            tool_mode=True,
        ),
        StrInput(
            name="dep_iata",
            display_name="Departure Airport Code",
            info="IATA Departure Airport Code",
            value="LAX",
            tool_mode=True,
        ),
        StrInput(
            name="arr_iata",
            display_name="Arrival Airport Code",
            info="IATA Arrival Airport Code",
            value="LAX",
            tool_mode=True,
        ),
        DropdownInput(
            name="flight_status",
            display_name="flight_status",
            info="Flight Status",
            options=["scheduled", "active", "landed", "cancelled", "incident", "diverted"],
            tool_mode=True,
        ),
        SecretStrInput(
            name="aviation_stack_api_key",
            display_name="Aviation Stack API Key",
            info="Aviation Stack API KEY",
            required=True,
        ),
    ]

    outputs = [
        Output(display_name="FlightInfo", name="output", method="flight_info", ),
        Output(display_name="ScheduledFlights", name="output", method="scheduled_flights"),
    ]
    
    def scheduled_flights(self) -> Data:
        url = f"https://api.aviationstack.com/v1/flights?access_key={self.aviation_stack_api_key}&limit=10&arr_iata={self.arr_iata}&dep_iata={self.dep_iata}&flight_status={self.flight_status}"
        res = requests.request("GET", url=url)

        if int(res.status_code) >= 400:
            return res.text

        try:
            res_data = res.json()
            data = Data(value=res_data)
            self.status = data
            return data
        except ValueError:
            self.status = res.status_code
            return res.status_code
            
    def flight_info(self) -> Data:
        url = f"https://api.aviationstack.com/v1/flights?access_key={self.aviation_stack_api_key}&limit=10&flight_iata={self.flight_number}"
        res = requests.request("GET", url=url)

        if int(res.status_code) >= 400:
            return res.text

        try:
            res_data = res.json()
            data = Data(value=res_data)
            self.status = data
            return data
        except ValueError:
            self.status = res.status_code
            return res.status_code            
