customer_schema = {
  "type": "object",
  "properties": {
    "customer_name": { "type": "string" },
    "age": { "type": "number" },
    "phone": { "type": "string" },
    "address": { "type": "string" },
    "booking_info": {"type": "object",
        "properties": {
            "room_id": { "type": "string" },
            "check_in": { "type": "string" },
            "check_out": { "type": "string" },
            "payment_method": { "type": "string" }
        },"required": ["room_id", "check_in", "check_out", "payment_method"]
    },
  },"required": ["customer_name", "age", "phone", "address"]
}