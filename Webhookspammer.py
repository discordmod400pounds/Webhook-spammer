import requests

# Replace the URL with your own Discord webhook URL
webhook_url = 'Put webhook here'

# Set the message content and number of requests
message = 'Text here'
num_requests = 100

# Send multiple requests to the webhook
for i in range(num_requests):
    payload = {'content': message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(f'Request {i+1} successful')
    else:
        print(f'Request {i+1} failed with status code {response.status_code}')
