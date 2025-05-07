import requests

def test_apis():
    base_url = "http://127.0.0.1:8000"
    endpoints = [
        # Test case 1: Valid data for adding a person
        {"method": "POST", "url": f"{base_url}/add-person", "data": {"name": "Alice", "age": 25}},
        # Test case 2: Missing age field
        {"method": "POST", "url": f"{base_url}/add-person", "data": {"name": "Bob"}},
        # Test case 3: Invalid age type
        {"method": "POST", "url": f"{base_url}/add-person", "data": {"name": "Charlie", "age": "twenty"}},
        # Test case 4: Empty name field
        {"method": "POST", "url": f"{base_url}/add-person", "data": {"name": "", "age": 30}},
        # Test case 5: Valid data with edge case age
        {"method": "POST", "url": f"{base_url}/add-person", "data": {"name": "Eve", "age": 0}},
    ]

    failed_apis = []

    for endpoint in endpoints:
        try:
            if endpoint["method"] == "POST":
                response = requests.post(endpoint["url"], json=endpoint.get("data", {}))
            elif endpoint["method"] == "GET":
                response = requests.get(endpoint["url"], params=endpoint.get("params", {}))
            else:
                continue

            if response.status_code != 200:
                failed_apis.append({"url": endpoint["url"], "status_code": response.status_code, "response": response.text})

        except Exception as e:
            failed_apis.append({"url": endpoint["url"], "error": str(e)})

    if failed_apis:
        print("Failed APIs:")
        for failed in failed_apis:
            print(failed)
    else:
        print("All APIs are working correctly.")

# Call the function to test APIs
test_apis()