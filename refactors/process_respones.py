def process_responses(responses):
    results = []

    for r in responses:
        if r["status"] == 200:
            if r["service"] == "user":
                if "data" in r:
                    name = r["data"].get("name", "")
                    age = r["data"].get("age", 0)
                    results.append({
                        "type": "user",
                        "name": name,
                        "age": age,
                        "valid": True
                    })
                else:
                    results.append({
                        "type": "user",
                        "name": "",
                        "age": 0,
                        "valid": False
                    })

            elif r["service"] == "order":
                if "data" in r:
                    amount = r["data"].get("amount", 0)
                    currency = r["data"].get("currency", "USD")
                    results.append({
                        "type": "order",
                        "amount": amount,
                        "currency": currency,
                        "valid": True
                    })
                else:
                    results.append({
                        "type": "order",
                        "amount": 0,
                        "currency": "USD",
                        "valid": False
                    })

        else:
            results.append({
                "type": r["service"],
                "valid": False
            })

    return results