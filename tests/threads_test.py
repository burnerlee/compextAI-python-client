import src.compextAI.threads as threads
from src.compextAI.api.api import APIClient

client = APIClient(
    base_url="http://localhost:8080",
    api_key="",
)

listed_threads = threads.list(client)
print("Listed threads:", listed_threads)

created_thread = threads.create(client, title="Test Thread", metadata={"test": "test"})
print("Created thread:", created_thread)

retrieved_thread = threads.retrieve(client, created_thread.thread_id)
print("Retrieved thread:", retrieved_thread)

updated_thread = threads.update(client, created_thread.thread_id, title="Updated Thread", metadata={"test": "updated"})
print("Updated thread:", updated_thread)

deleted_thread = threads.delete(client, created_thread.thread_id)
print("Deleted thread:", deleted_thread)

listed_threads_after_delete = threads.list(client)
print("Listed threads after delete:", listed_threads_after_delete)
