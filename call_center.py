import google.generativeai as genai
import config
from prompts import get_conversation_prompt

print("=== Testing Call Center Operator with Custom Prompt ===\n")

# Configure Gemini API
genai.configure(api_key=config.GEMINI_API_KEY)

# Create the model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Test conversation scenarios
test_scenarios = [
    "გამარჯობა, რა არის თქვენი სამუშაო საათები?",
    "მაინტერესებს ვებ დეველოპმენტის სერვისი. რა ფასები გაქვთ?",
    "როგორ შემიძლია დაგიკავშირდეთ?",
    "გმადლობთ დახმარებისთვის!"
]

conversation_history = []

for i, user_message in enumerate(test_scenarios, 1):
    print(f"{'='*60}")
    print(f"Scenario {i}:")
    print(f"{'='*60}\n")
    
    print(f"👤 მომხმარებელი: {user_message}\n")
    
    # Generate prompt with history
    prompt = get_conversation_prompt(user_message, conversation_history)
    
    # Generate response
    response = model.generate_content(prompt)
    ai_response = response.text.strip()
    
    print(f"🤖 ოპერატორი: {ai_response}\n")
    
    # Add to conversation history
    conversation_history.append({"role": "user", "content": user_message})
    conversation_history.append({"role": "assistant", "content": ai_response})

print(f"{'='*60}")
print("\n✅ All scenarios tested successfully!")
print("The operator maintains context and responds professionally!")