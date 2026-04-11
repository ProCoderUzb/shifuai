from google import genai
from .models import ChatMessage, NUser as User
from config.settings import API_KEY

manual_model = "gemini-3.1-flash-lite-preview"

def process_chat_message(user:User, message:ChatMessage):
    print(User.session_id)
    client = genai.Client(api_key=API_KEY)
    history = user.get_history()
    chat = client.chats.create(
        model=manual_model,
        history=history,
        config={
            "system_instruction": """You are a AI assistant.
            Your name is Shifu. You will help people people in good manners."""
        }
    )
    user.save()
    for i in range(3):
        try:
            response_raw = chat.send_message(message.text)
            response = response_raw.text
            print("------------ success")
            break
        except Exception as e:
            print("-----------errrrrrorrrr", e)
            pass
        print("---------- try again, error message")
        response = "Please try again later. Server is overloaded !"

    new_response = ChatMessage.objects.create(
        user=user,
        role = "model",
        text = response,
    )

    return True