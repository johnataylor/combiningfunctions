
functionDescriptions = [
    {
        "name": "get_work_order_details",
        "description": "Get details for a work work, this includes the current status",
        "parameters": {
            "type": "object",
            "properties": {
                "work_order_id": {
                    "type": "string",
                    "description": "The identifier for the work order"
                },
            },
            "required": ["work_order_id"],
        },
    },
    {
        "name": "get_work_orders_by_account",
        "description": "Get work orders for an account, returns the identifiers for each work order",
        "parameters": {
            "type": "object",
            "properties": {
                "account_id": {
                    "type": "string",
                    "description": "The identifier for the account"
                },
            },
            "required": ["account_id"],
        },
    },
]
