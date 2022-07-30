SEARCH_IP_BAD_REQUEST = {
    "description": "Bad Request",
    "content": {
        "application/json": {
            "schema": {"detail": "string"},
            "example": {"detail": "'abcxyz' does not appear to be an IPv4 or IPv6 addres"},
        }
    },
}
