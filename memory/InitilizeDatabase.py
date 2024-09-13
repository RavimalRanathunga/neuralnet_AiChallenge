from langchain_community.chat_message_histories import SQLChatMessageHistory
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

# Create an SQLite engine (or use another database)
engine = create_engine('sqlite:///chat_history.db')
session_id = "test_session_id"
SQLChatMessageHistory(session_id=session_id, connection=engine)
# Define the metadata object
metadata = MetaData()
# Reflect the existing database schema to retrieve the table
message_store = Table('message_store', metadata, autoload_with=engine)
