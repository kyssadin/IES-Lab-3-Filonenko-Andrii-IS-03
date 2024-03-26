import json
import logging
from typing import List
from config import STORE_API_BASE_URL

import pydantic_core
import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway

def convert_to_json(processed_agent_data_batch):
    result = []
    
    for p in processed_agent_data_batch:
        result.append(p.model_dump(mode="json"))

    return json.dumps(result)

class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        requests.post(self.api_base_url+"/processed_agent_data", data=convert_to_json(processed_agent_data_batch))
        