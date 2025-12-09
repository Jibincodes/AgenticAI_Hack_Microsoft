# Contributing to Agentic AI Hack

Thank you for your interest in contributing to the Agentic AI Hack repository! This document provides guidelines for contributing your projects, examples, and improvements.

## 🎯 Ways to Contribute

### 1. Share Your Projects
- Add your hackathon project to the `examples/` directory
- Include a README explaining what your agent does
- Share any interesting findings or learnings

### 2. Add Examples
- Create tutorial code demonstrating Semantic Kernel features
- Show best practices for building agentic AI systems
- Document common patterns and solutions

### 3. Improve Documentation
- Fix typos or clarify existing documentation
- Add new resources or learning materials
- Create guides for specific use cases

### 4. Share Resources
- Add helpful links to the resources section
- Share blog posts, videos, or tutorials
- Contribute learning materials

## 📋 Contribution Process

1. **Fork the Repository**
   - Click the "Fork" button on GitHub
   - Clone your fork locally

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clear, well-documented code
   - Follow existing code style
   - Test your changes

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes

## 📝 Code Guidelines

### General Principles
- **Keep it simple**: Focus on clarity and readability
- **Document your code**: Add comments explaining complex logic
- **Use meaningful names**: Variables and functions should be descriptive
- **Follow conventions**: Match the style of existing code

### Python Projects
- Follow PEP 8 style guide
- Use type hints where appropriate
- Include docstrings for functions and classes
- Add requirements.txt for dependencies

### C# Projects
- Follow Microsoft C# coding conventions
- Use XML documentation comments
- Include .csproj files
- Specify NuGet dependencies

### Java Projects
- Follow standard Java conventions
- Use Javadoc comments
- Include pom.xml or build.gradle
- Specify Maven/Gradle dependencies

## 🔒 Security

### API Keys and Secrets
- **Never commit API keys or secrets** to the repository
- Use environment variables for sensitive data
- Add examples using placeholders like `YOUR_API_KEY_HERE`
- Reference .env.example files for configuration

### Example .env.example
```
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## 📁 Project Structure

When adding examples, follow this structure:

```
examples/
└── your-project-name/
    ├── README.md           # Project description and instructions
    ├── src/                # Source code
    ├── requirements.txt    # Python dependencies (if applicable)
    ├── .env.example        # Example environment variables
    └── docs/               # Additional documentation (optional)
```

### README Template for Examples

```markdown
# Your Project Name

Brief description of what your agent does.

## Features
- Feature 1
- Feature 2

## Setup
1. Install dependencies
2. Configure environment variables
3. Run the application

## Usage
How to use your agent

## Technologies
- Semantic Kernel
- Other technologies used

## Author
Your name/GitHub username
```

## ✅ Pull Request Checklist

Before submitting, ensure:
- [ ] Code is well-documented
- [ ] No API keys or secrets in code
- [ ] README is included (for new projects)
- [ ] Dependencies are specified
- [ ] Code follows style guidelines
- [ ] Changes are tested locally

## 🤔 Questions?

If you have questions about contributing:
- Check existing issues and discussions
- Reach out to the organizers
- Ask in the hack event channels

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Celebrate creativity and innovation

## 🙏 Thank You!

Your contributions make this hackathon better for everyone. Thank you for participating and sharing your work!

---

Happy Coding! 🚀
