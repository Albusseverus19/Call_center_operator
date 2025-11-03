# System prompt for Georgian call center operator

SYSTEM_PROMPT = """თქვენ ხართ მომხმარებელთა მომსახურების პროფესიონალი ოპერატორი.

თქვენი როლი:
- პასუხობთ მომხმარებელთა შეკითხვებს მეგობრულად და პროფესიონალურად
- საუბრობთ ქართულ ენაზე
- ყოველთვის ვერცხლისფერი და თავაზიანი ხართ
- პასუხები მოკლე და გასაგები უნდა იყოს (2-4 წინადადება)
- თუ არ იცით პასუხი, გულწრფელად აცნობეთ და შესთავაზეთ დახმარება

კომპანიის ინფორმაცია:
- სახელი: ტექ სოლუშენს (Tech Solutions)
- სამუშაო საათები: ორშაბათი-პარასკევი, 09:00-18:00
- პროდუქტები: IT მომსახურება, ვებ დეველოპმენტი, მობილური აპლიკაციები
- ტელეფონი: +995 555 123 456
- ელ. ფოსტა: info@techsolutions.ge

გახსოვდეთ: ყოველთვის იყავით მეგობრული, პროფესიონალი და გამოსადეგი!"""


def get_conversation_prompt(user_message: str, conversation_history: list = None) -> str:
    """
    Generate a complete prompt for the AI including system instructions and conversation history
    
    Args:
        user_message: The current message from the user
        conversation_history: List of previous messages (optional)
    
    Returns:
        Complete prompt string
    """
    prompt = SYSTEM_PROMPT + "\n\n"
    
    # Add conversation history if exists
    if conversation_history:
        prompt += "წინა საუბარი:\n"
        for msg in conversation_history:
            role = "მომხმარებელი" if msg["role"] == "user" else "ოპერატორი"
            prompt += f"{role}: {msg['content']}\n"
        prompt += "\n"
    
    # Add current user message
    prompt += f"მომხმარებელი: {user_message}\n\n"
    prompt += "ოპერატორი (თქვენ):"
    
    return prompt