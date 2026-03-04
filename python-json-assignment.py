import json

# 1. Ask user for each field individually
request_id = input("Enter Request ID (e.g., req_123): ")
status = input("Enter Status (e.g., success/failed): ")
text = input("Enter Text result (e.g., Hello world): ")
confidence = float(input("Enter Confidence score (e.g., 0.98): "))

# 2. Build the API response dictionary
response = {
    "id": request_id,
    "status": status,
    "result": {
        "text": text,
        "confidence": confidence
    }
}

# 3. Print extracted values
print("\n--- Parsed API Response ---")
print("Request ID:", response["id"])
print("Status:", response["status"])
print("Text:", response["result"]["text"])
print("Confidence:", response["result"]["confidence"])

# 4. Warning if confidence < 0.9
if response["result"]["confidence"] < 0.9:
    print("⚠️ Warning: Confidence score is below 0.9")

# 5. Create a follow-up result dictionary
follow_up = {
    "id": "req_124",
    "status": "success",
    "result": {
        "text": "Follow-up message processed",
        "confidence": 0.95
    }
}

# 6. Convert dictionary to JSON string
follow_up_json = json.dumps(follow_up, indent=2)

# 7. Write JSON output to a file
with open("response.json", "w") as f:
    f.write(follow_up_json)

print("\nFollow-up result written to response.json")