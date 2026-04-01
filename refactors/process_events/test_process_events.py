from process_events_refactored import process_events


def test_click_event():
    events = [
        {
            "id": 1,
            "type": "click",
            "timestamp": 123,
            "user": {"name": "Alice"}
        }
    ]

    result = process_events(events)

    assert result == [
        {
            "event_type": "click",
            "user_name": "Alice",
            "ts": 123,
            "valid": True
        }
    ]


def test_deduplication():
    events = [
        {"id": 1, "type": "click", "timestamp": 123},
        {"id": 1, "type": "click", "timestamp": 123}
    ]
    result = process_events(events)
    assert len(result) == 1


def test_invalid_event():
    events = [
        {"id": 1, "type": "click"}  # missing timestamp
    ]
    result = process_events(events)
    assert result[0]["valid"] is False


def test_unknown_event():
    events = [
        {"id": 1, "type": "weird", "timestamp": 123}
    ]
    result = process_events(events)
    assert result[0]["reason"] == "unsupported_event_type"


def test_purchase_event():
    events = [
        {"id": 1, "type": "purchase", "timestamp": 123, "data": {"amount": 50}}
    ]
    result = process_events(events)
    assert result[0]["amount"] == 50