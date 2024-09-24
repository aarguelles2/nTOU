import logging
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from sqlalchemy import create_engine
import os
import pyodbc



credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://tpwlcompricecufa-kv-qa.vault.azure.net/", credential=credential)

# Retrieve connection details (server and database name)
db_connection_info_secret = client.get_secret("tidq-db-connection-info")
db_connection_info = json.loads(db_connection_info_secret.value)
server = db_connection_info["server"]
port = db_connection_info["port"]
database = db_connection_info["database"]
print(database)