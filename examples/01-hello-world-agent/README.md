# Hello World Agent

A simple "Hello World" example demonstrating the basics of Semantic Kernel and building your first AI agent.

## 🎯 What This Example Demonstrates

- Setting up Semantic Kernel
- Configuring Azure OpenAI or OpenAI
- Creating a basic agent
- Running simple prompts
- Understanding the kernel architecture

## 📋 Prerequisites

- Python 3.10 or higher
- Azure OpenAI API key or OpenAI API key
- pip package manager

## 🚀 Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API credentials:
   ```
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-api-key-here
   AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
   ```

   Or for OpenAI:
   ```
   OPENAI_API_KEY=your-openai-api-key
   OPENAI_ORG_ID=your-org-id (optional)
   ```

## 🏃 Running the Example

```bash
python src/main.py
```

## 📚 What You'll Learn

### 1. Kernel Initialization
The kernel is the core component that orchestrates everything:
```python
kernel = semantic_kernel.Kernel()
```

### 2. Service Configuration
Connect your AI service (Azure OpenAI or OpenAI):
```python
kernel.add_service(AzureChatCompletion(...))
```

### 3. Creating Chat Completion
Execute a simple prompt:
```python
result = await kernel.invoke_prompt("Your prompt here")
```

## 🔍 Code Walkthrough

The example consists of:

1. **Environment Setup**: Loading API credentials securely
2. **Kernel Creation**: Initializing the Semantic Kernel
3. **Service Configuration**: Connecting to Azure OpenAI/OpenAI
4. **Prompt Execution**: Running a simple prompt
5. **Result Handling**: Processing and displaying the response

## 🎓 Next Steps

After completing this example, try:

1. **Modify the prompt**: Change the user message to ask different questions
2. **Add system messages**: Guide the agent's behavior with system prompts
3. **Experiment with settings**: Adjust temperature, max_tokens, etc.
4. **Add conversation history**: Build multi-turn conversations

## 📖 Related Documentation

- [Semantic Kernel Quickstart](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel)

## 💡 Tips

- **API Keys**: Never commit your API keys to version control
- **Error Handling**: The example includes basic error handling - expand it for production use
- **Rate Limits**: Be aware of API rate limits when testing
- **Costs**: Monitor your API usage to avoid unexpected costs

## 🐛 Troubleshooting

### Common Issues

1. **Import Error**: Make sure you've installed all dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. **Authentication Error**: Verify your API key and endpoint are correct

3. **Module Not Found**: Ensure you're running from the correct directory

## 🤝 Contributing

Found an issue or have a suggestion? Feel free to open a pull request!

---

Happy coding! 🚀
