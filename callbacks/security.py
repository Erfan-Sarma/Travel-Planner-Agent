from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.genai import types

def security_guard(
    callback_context: CallbackContext,
    llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """
    Intersects the request before it reaches the model.
    Checks for forbidden keywords to ensure safety.
    """
    forbidden_words = ["dangerous", "border", "war", "خطرناک", "مرزی"]

    for content in llm_request.contents:
        if content.role == "user":
            # Extract and lowercase all text parts
            text = "".join(
                part.text.lower()
                for part in content.parts
                if part.text
            )
            
            if any(word in text for word in forbidden_words):
                # Short-circuit: Return a response immediately
                return LlmResponse(
                    content=types.Content(
                        role="model",
                        parts=[types.Part(text="درخواست شما به دلایل امنیتی مسدود شد.")]
                    )
                )
    return None # Pass through if safe