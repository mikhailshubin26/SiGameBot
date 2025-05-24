from aiogram import types

def getUsername(user: types.User) -> str:
    return f"{user.first_name}".strip() # Return first name of user
