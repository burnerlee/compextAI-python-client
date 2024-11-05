import src.compextAI.messages as messages
import src.compextAI.threads as threads
from src.compextAI.api.api import APIClient

client = APIClient(
    base_url="http://localhost:8080",
    api_key="",
)

created_thread = threads.create(client, title="Test Thread", metadata={"test": "test"})

created_message = messages.create(client, created_thread.thread_id, "Hello, world!", "user")
print("Created message:", created_message)

retrieved_message = messages.retrieve(client, created_message.message_id)
print("Retrieved message:", retrieved_message)

listed_messages = messages.list(client, created_thread.thread_id)
print("Listed messages:", listed_messages)

updated_message = messages.update(client, created_message.message_id, "Hello, world updated!", "user")
print("Updated message:", updated_message)

deleted_message = messages.delete(client, created_message.message_id)
print("Deleted message:", deleted_message)

listed_messages_after_delete = messages.list(client, created_thread.thread_id)
print("Listed messages after delete:", listed_messages_after_delete)

threads.delete(client, created_thread.thread_id)