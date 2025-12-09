"""
Hello World Agent - A Simple Semantic Kernel Example

This example demonstrates:
1. Setting up Semantic Kernel
2. Configuring Azure OpenAI or OpenAI
3. Creating a basic agent
4. Running simple prompts
"""

import asyncio
import os
from dotenv import load_dotenv
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion
from semantic_kernel.contents import ChatHistory

# Load environment variables from .env file
load_dotenv()


async def main():
    """Main function to run the Hello World agent."""
    
    print("=" * 60)
    print("🤖 Welcome to the Hello World Semantic Kernel Agent!")
    print("=" * 60)
    print()
    
    try:
        # Initialize the kernel
        kernel = sk.Kernel()
        
        # Configure AI service - Azure OpenAI or OpenAI
        service_id = "default"
        
        # Try Azure OpenAI first
        if os.getenv("AZURE_OPENAI_ENDPOINT"):
            print("📡 Configuring Azure OpenAI service...")
            kernel.add_service(
                AzureChatCompletion(
                    service_id=service_id,
                    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                )
            )
            print("✅ Azure OpenAI configured successfully!")
        # Otherwise use OpenAI
        elif os.getenv("OPENAI_API_KEY"):
            print("📡 Configuring OpenAI service...")
            kernel.add_service(
                OpenAIChatCompletion(
                    service_id=service_id,
                    ai_model_id="gpt-3.5-turbo",
                    api_key=os.getenv("OPENAI_API_KEY"),
                    org_id=os.getenv("OPENAI_ORG_ID"),
                )
            )
            print("✅ OpenAI configured successfully!")
        else:
            raise ValueError(
                "Please configure either Azure OpenAI or OpenAI credentials in your .env file"
            )
        
        print()
        print("-" * 60)
        print("🎯 Example 1: Simple Prompt")
        print("-" * 60)
        
        # Create a simple prompt
        prompt = "What is Agentic AI and why is it important?"
        print(f"Prompt: {prompt}")
        print()
        
        # Execute the prompt
        print("🤔 Thinking...")
        result = await kernel.invoke_prompt(prompt)
        
        print()
        print("💬 Response:")
        print(result)
        print()
        
        print("-" * 60)
        print("🎯 Example 2: Structured Prompt with System Message")
        print("-" * 60)
        
        # Create a more structured prompt
        chat_history = ChatHistory()
        chat_history.add_system_message(
            "You are a helpful AI assistant specializing in explaining "
            "AI concepts in simple terms for hackathon participants."
        )
        chat_history.add_user_message(
            "Explain Semantic Kernel in 3 sentences."
        )
        
        print("System: AI assistant for hackathon participants")
        print("User: Explain Semantic Kernel in 3 sentences.")
        print()
        
        # Get chat completion service
        chat_service = kernel.get_service(service_id)
        
        print("🤔 Thinking...")
        response = await chat_service.get_chat_message_content(
            chat_history=chat_history,
            settings=kernel.get_prompt_execution_settings_from_service_id(service_id),
        )
        
        print()
        print("💬 Response:")
        print(response)
        print()
        
        print("-" * 60)
        print("✨ Success! Your first Semantic Kernel agent is working!")
        print("-" * 60)
        print()
        print("🎓 Next Steps:")
        print("  1. Modify the prompts to ask different questions")
        print("  2. Experiment with different system messages")
        print("  3. Try building a multi-turn conversation")
        print("  4. Explore creating plugins with custom functions")
        print()
        
    except Exception as e:
        print()
        print("❌ Error:", str(e))
        print()
        print("🔧 Troubleshooting:")
        print("  1. Make sure you've created a .env file from .env.example")
        print("  2. Verify your API keys are correct")
        print("  3. Check that all dependencies are installed: pip install -r requirements.txt")
        print()
        raise


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
