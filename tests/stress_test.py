import aiohttp
import asyncio
import json
import random
import time

# Define the URL and headers
url = 'http://localhost:8000/create_message'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Define the message data
data = {
    "message": "Hello, this is a stress test message!"
}

# Function to send a POST request
async def send_post_request(session):
    await asyncio.sleep(random.uniform(0.1, 1.5))  # Random delay
    start_time = time.time()
    async with session.post(url, headers=headers, data=json.dumps(data)) as response:
        end_time = time.time()
        duration = end_time - start_time
        status_code = response.status
        response_data = await response.json()
        return status_code, response_data, duration

# Function to create tasks and gather responses
async def stress_test(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [send_post_request(session) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)
        return responses

# Number of requests to send
num_requests = 100

# Run the stress test
responses = asyncio.run(stress_test(num_requests))

# Calculate statistics
total_time = sum(response[2] for response in responses)
average_time = total_time / num_requests
min_time = min(response[2] for response in responses)
max_time = max(response[2] for response in responses)

# Print the results
for status_code, response_data, duration in responses:
    print(f"Status code: {status_code}, Response: {response_data}, Duration: {duration:.4f} seconds")

print("\n--- Statistics ---")
print(f"Total time taken: {total_time:.4f} seconds")
print(f"Average time per request: {average_time:.4f} seconds")
print(f"Minimum time taken for a request: {min_time:.4f} seconds")
print(f"Maximum time taken for a request: {max_time:.4f} seconds")
