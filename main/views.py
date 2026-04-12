from django.shortcuts import render, redirect
from .my_request import process_chat_message
from .models import ChatMessage, NUser as User

def home(request):
    # Ensure a session exists and has a key
    if not request.session.session_key:
        request.session.save() 
    
    session_id = request.session.session_key
    # Emergency safety check
    if not session_id:
        return render(request, "home.html", {"error": "Cookies are required."})

    try:
        user = User.objects.get(session_id=session_id)
    except User.DoesNotExist:
        user = User.objects.create(session_id=session_id)
    messages = ChatMessage.objects.filter(user=user)

    if request.method == "POST":
        user_message = request.POST.get("user_message")
        if user_message:
            new_message = ChatMessage.objects.create(
                user=user,
                role = "user",
                text = user_message,
            )
            process_chat_message(user, new_message)
            return redirect('home')

    context = {
        "messages": messages
    }
    return render(request, "home.html", context)

def clear_chat(request):
    if not request.session.session_key:
        print("----key not found")
        return redirect('home')
    session_id = request.session.session_key
    try:
        user = User.objects.get(session_id=session_id)
        messages = ChatMessage.objects.filter(user=user).delete()
    except Exception as e:
        print(e)
        print("----user not found")
    return redirect('home')
