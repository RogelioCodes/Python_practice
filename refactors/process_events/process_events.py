def process_events(events):
    results = []
    seen = []

    for e in events:
        if e.get("id") in seen:
            continue
        else:
            seen.append(e.get("id"))

        if e.get("timestamp") is None:
            continue

        if e.get("type") == "click":
            if "user" in e:
                user = e["user"]
                name = user.get("name") if user else None
            else:
                name = None

            results.append({
                "event_type": "click",
                "user_name": name,
                "ts": e.get("timestamp"),
                "valid": True
            })

        elif e.get("type") == "purchase":
            amount = 0
            if "data" in e:
                if e["data"] is not None:
                    amount = e["data"].get("amount", 0)

            results.append({
                "event_type": "purchase",
                "amount": amount,
                "ts": e.get("timestamp"),
                "valid": True
            })

        else:
            results.append({
                "event_type": e.get("type", "unknown"),
                "valid": False
            })

    return results