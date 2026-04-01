def process_events(events):
    results = []
    seen = set()

    for event in events:
        event_id = event.get("id")

        if event_id in seen:
            continue

        if not is_valid(event):
            results.append(invalid_event(event))
            continue

        seen.add(event_id)

        event_type = event.get("type")

        if event_type == "click":
            results.append(process_click(event))
        elif event_type == "purchase":
            results.append(process_purchase(event))
        else:
            results.append(unknown_event(event))

    return results


def is_valid(event):
    return bool(event.get("timestamp") and event.get("type"))


def unknown_event(event):
    return {
        "event_type": event.get("type", "unknown"),
        "ts": event.get("timestamp"),
        "valid": False,
        "reason": "unsupported_event_type"
    }


def invalid_event(event):
    return {
        "event_type": event.get("type", "unknown"),
        "ts": event.get("timestamp"),
        "valid": False,
        "reason": "invalid_event"
    }


def has_data(event):
    return bool(event.get("data"))


def process_click(event):
    user = event.get("user") or {}

    return {
        "event_type": "click",
        "user_name": user.get("name"),
        "ts": event.get("timestamp"),
        "valid": True
    }


def process_purchase(event):
    if not has_data(event):
        return invalid_event(event)

    data = event.get("data") or {}

    return {
        "event_type": "purchase",
        "amount": data.get("amount", 0),
        "ts": event.get("timestamp"),
        "valid": True
    }