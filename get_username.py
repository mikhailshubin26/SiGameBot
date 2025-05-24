from aiogram import types

def getUsername(user: types.User) -> str:
    return f"{user.first_name}".strip() # Return first name of user

def getUserId(user: types.User) -> str:
    return f"{user.id}".strip() # Return user id