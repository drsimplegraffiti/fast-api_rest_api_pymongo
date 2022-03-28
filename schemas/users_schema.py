def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "password": user["password"],
        "disabled": user["disabled"],
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
