def process_responses(responses):
    results = []

    for r in responses:
        if not is_successful(r):
            results.append(invalid_response(r))
            continue

        if r["service"] == "user":
            results.append(process_user(r))
        elif r["service"] == "order":
            results.append(process_order(r))

    return results

def is_successful(response):
    return response["status"] == 200

def has_data(response):
    return "data" in response and response["data"] is not None
    
def invalid_response(response):
    return {
        "type": response["service"],
        "valid": False
    }
def process_order(response):
    data = response.get("data", {})

    return {
        "type": "order",
        "amount": data.get("amount", 0),
        "currency": data.get("currency", "USD"),
        "valid": has_data(response)
    }

def process_user(response):
    data = response.get("data", {})

    return {
        "type": "user",
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "valid": has_data(response)
    }

