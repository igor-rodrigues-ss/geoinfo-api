DEFAULT_INTERNAL_SERVER_ERROR = {
    "description": "Internal Server Error",
    "content": {
        "application/json": {
            "schema": {"detail": "string"},
            "example": {"detail": "Internal Server Error"},
        }
    },
}
