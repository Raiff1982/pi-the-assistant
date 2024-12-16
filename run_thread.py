
Import time # type: ignore
from your_api_client import Client  # Import the client library

client = Client(api_key='9pBiKIcMD2erbnU8XSiOlIHh1UyOfk0RzrGfybzNWAZPPmVrHdPlJQQJ99AKACYeBjFXJ3w3AAAAACOGtoia')

# Create a thread
thread = client.beta.threads.create()

# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content={
      "name": "process_data",
      "description": "Process the provided data and optionally learn from a provided file",
      "parameters": {
        "type": "object",
        "properties": {
          "data": {
            "type": "object",
            "description": "The data to process"
          },
          "file_path": {
            "type": "string",
            "description": "Path to the file to learn from (optional)"
          }
        },
        "required": [
          "data"
        ]
      }
    } # Replace this with your prompt
)

# Run the thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Looping until the run completes or fails
while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
elif run.status == 'requires_action':
    # The assistant requires calling some functions
    # and submit the tool outputs back to the run
    pass
else:
    print(run.status)
    