# Agentic AI Hack - Microsoft Zurich

Welcome to the **Agentic AI Hack** repository! This hackathon is organized by **Microsoft Zurich** and focuses on exploring the capabilities of **Agentic AI** using the **Semantic Kernel framework**.

## 🎯 About the Hack

This repository serves as a central hub for information, resources, and projects related to the Agentic AI Hack. The event emphasizes building intelligent agents that can autonomously perform tasks, make decisions, and interact with various systems using Microsoft's Semantic Kernel framework.

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
pip install semantic-kernel
```

#### For C#
```bash
dotnet add package Microsoft.SemanticKernel
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
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

### Tutorials and Guides
- [Semantic Kernel Quick Start](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide)
- [Building AI Agents](https://learn.microsoft.com/en-us/semantic-kernel/agents/)
- [Plugin Development](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/)

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
**Focus**: Agentic AI and Semantic Kernel Framework  
**Goal**: Build intelligent, autonomous AI agents that can interact with the world

---

Happy Hacking! 🚀✨