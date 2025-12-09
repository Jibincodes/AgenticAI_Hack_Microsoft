# Agentic AI Hack - Microsoft Zurich

Welcome to the **Agentic AI Hack** repository! This hackathon is organized by **Microsoft Zurich** and focuses on exploring the capabilities of **Agentic AI** using cutting-edge Microsoft technologies including **Semantic Kernel**, **Azure AI Foundry**, and **Microsoft Agent Framework**.

## 🎯 About the Hack

This repository serves as a central hub for information, resources, and projects related to the Agentic AI Hack. The event emphasizes building intelligent agents that can autonomously perform tasks, make decisions, and interact with various systems using Microsoft's comprehensive AI platform and frameworks.

### What is Agentic AI?

Agentic AI refers to artificial intelligence systems that can:
- **Act autonomously** to achieve goals
- **Make decisions** based on context and reasoning
- **Use tools and APIs** to accomplish tasks
- **Plan and execute** multi-step workflows
- **Learn and adapt** from interactions

### What is Semantic Kernel?

[Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) is an open-source SDK that lets you easily build agents that can call your existing code. It provides:
- **AI orchestration** - Combine AI models with conventional programming
- **Plugin architecture** - Integrate various services and APIs
- **Memory and context** - Maintain conversation state and history
- **Planning capabilities** - Automatically create and execute plans
- **Multi-language support** - Available for C#, Python, and Java

### What is Azure AI Foundry?

[Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-studio) (formerly Azure AI Studio) is a comprehensive platform for building, evaluating, and deploying AI applications. It provides:
- **Unified development environment** - Build AI solutions with a single, integrated platform
- **Model catalog** - Access to cutting-edge AI models from OpenAI, Meta, Mistral, and more
- **Prompt flow** - Design, test, and iterate on prompt-based applications
- **Evaluation tools** - Assess AI model performance with built-in metrics
- **Deployment at scale** - Deploy AI applications with enterprise-grade security and compliance
- **RAG capabilities** - Build retrieval-augmented generation applications with your own data

### What is Microsoft Agent Framework?

The [Microsoft Agent Framework](https://github.com/microsoft/autogen) (also known as AutoGen) is a framework for building multi-agent AI systems. Key features include:
- **Multi-agent conversations** - Enable multiple AI agents to collaborate and solve complex tasks
- **Agent specialization** - Create agents with specific roles and capabilities
- **Human-in-the-loop** - Integrate human oversight and decision-making into agent workflows
- **Tool integration** - Agents can use external tools, APIs, and code execution
- **Flexible orchestration** - Support for various conversation patterns and agent interactions
- **Built on proven technology** - Leverages OpenAI's APIs and integrates with Azure services

The framework is particularly useful for:
- Complex problem-solving requiring multiple perspectives
- Automated code generation and debugging
- Multi-step research and analysis tasks
- Conversational AI with specialized domain experts

## 🚀 Getting Started

### Prerequisites

- **Programming Language**: Choose one or more
  - [.NET 8.0+](https://dotnet.microsoft.com/) (for C#)
  - [Python 3.10+](https://www.python.org/) (for Python)
  - [Java 11+](https://www.oracle.com/java/) (for Java)
- **IDE**: Visual Studio Code, Visual Studio, or your preferred IDE
- **API Keys**: 
  - Azure OpenAI or OpenAI API key
  - Other service credentials as needed

### Installation

#### For Python
```bash
# Semantic Kernel
pip install semantic-kernel

# Microsoft Agent Framework (AutoGen)
pip install pyautogen

# Azure AI SDK (for Azure AI Foundry integration)
pip install azure-ai-inference azure-identity
```

#### For C#
```bash
# Semantic Kernel
dotnet add package Microsoft.SemanticKernel

# Azure AI SDK
dotnet add package Azure.AI.OpenAI
dotnet add package Azure.Identity
```

#### For Java
```xml
<dependency>
    <groupId>com.microsoft.semantic-kernel</groupId>
    <artifactId>semantickernel-api</artifactId>
</dependency>
```

## 📁 Repository Structure

```
.
├── examples/          # Sample code and demos
├── docs/             # Additional documentation
├── resources/        # Learning materials and links
└── README.md         # This file
```

## 💡 Key Concepts

### Building an Agent with Semantic Kernel

1. **Define Plugins**: Create functions that your agent can call
2. **Configure AI Services**: Connect to Azure OpenAI or OpenAI
3. **Create Kernel**: Initialize the Semantic Kernel
4. **Add Memory**: Enable context and conversation history
5. **Enable Planning**: Let the agent create execution plans
6. **Execute**: Run your agent with user prompts

### Example Use Cases

- **Task Automation**: Agents that automate complex workflows
- **Data Analysis**: AI that can query, analyze, and visualize data
- **Customer Support**: Intelligent chatbots with tool access
- **Code Assistants**: Agents that help with development tasks
- **Research Assistants**: AI that can search, summarize, and synthesize information

## 📚 Resources

### Official Documentation
- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [Azure AI Foundry Portal](https://ai.azure.com/)
- [Microsoft Agent Framework (AutoGen)](https://microsoft.github.io/autogen/)
- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

### Tutorials and Guides
- [Semantic Kernel Quick Start](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide)
- [Building AI Agents](https://learn.microsoft.com/en-us/semantic-kernel/agents/)
- [Plugin Development](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/)
- [Azure AI Foundry Getting Started](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-projects)
- [AutoGen Tutorial](https://microsoft.github.io/autogen/docs/tutorial/introduction)
- [Building Multi-Agent Systems](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns)

### Community
- [Semantic Kernel Discord](https://aka.ms/SKDiscord)
- [Microsoft AI Blog](https://blogs.microsoft.com/ai/)

## 🤝 Contributing

We welcome contributions! Please feel free to:
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-agent`)
3. Commit your changes (`git commit -m 'Add amazing agent'`)
4. Push to the branch (`git push origin feature/amazing-agent`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Event Information

**Location**: Microsoft Zurich  
**Focus**: Agentic AI, Semantic Kernel Framework, Azure AI Foundry, and Microsoft Agent Framework  
**Goal**: Build intelligent, autonomous AI agents that can interact with the world using cutting-edge Microsoft AI technologies

---

Happy Hacking! 🚀✨