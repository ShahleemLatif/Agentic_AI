# Automated AI Sales Agent System

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)

An advanced multi-agent AI system designed to automate the entire workflow of creating, refining, and sending cold sales emails. This project uses a team of specialized AI agents, each powered by different large language models, to handle distinct stages of the process, from initial drafting to final delivery.

## 📖 Overview

This system demonstrates a collaborative AI workflow for a fictional company, **Pet Vet**. A managing agent orchestrates several subordinate agents to generate multiple email drafts, select the best one, format it professionally, and send it to a target recipient.

### The Workflow

The process is executed in three main stages:

1.  **✍️ Draft Generation**: Three unique AI sales agents, each with a different personality (professional, humorous, concise), generate distinct email drafts. These agents are powered by models from DeepSeek, Google (Gemini), and Groq (Llama3).
2.  **✅ Selection**: A `Senior Sales Manager` agent reviews the three generated drafts and uses its judgment to select the single most promising option.
3.  **📨 Formatting & Sending**: The selected draft is handed off to an `Email Manager` agent. This agent then:
    * Generates a compelling subject line.
    * Converts the plain text body to clean, responsive HTML.
    * Sends the final email using the SendGrid API.

## ✨ Features

* **Multi-Agent Architecture**: Leverages a team of specialized agents (`Senior_Sales_Manager`, `Email_Manager`, and three distinct sales agents) to modularize tasks.
* **Diverse LLM Integration**: Utilizes multiple state-of-the-art language models, including GPT-4o-mini, Gemini 1.5 Flash, Llama3 70B, and DeepSeek Chat.
* **Tool-Based Collaboration**: Agents use other agents and functions as "tools" to perform sub-tasks, creating a sophisticated chain of command.
* **Automated Formatting**: The `Email_Manager` agent automates the creation of subject lines and HTML email bodies for a professional finish.
* **End-to-End Automation**: Manages the entire process from a single prompt to the final email dispatch.

## 🛠️ Technology Stack

* **Python**: Core programming language.
* **Agents Framework**: The `agents` library is used to define and run the AI agents.
* **LLM APIs**:
    * OpenAI (`gpt-4o-mini`)
    * Google Gemini (`gemini-1.5-flash-latest`)
    * Groq (`llama3-70b-8192`)
    * DeepSeek (`deepseek-chat`)
* **Email Delivery**: SendGrid API for sending emails.
* **Environment Management**: `python-dotenv` for managing API keys securely.
* **Jupyter Notebook**: For interactive development and demonstration.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

* Python 3.10+
* Access to the required LLM APIs (OpenAI, Google, DeepSeek, Groq).
* A SendGrid account with a verified sender email address.

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/automated-ai-sales-agent.git](https://github.com/your-username/automated-ai-sales-agent.git)
    cd automated-ai-sales-agent
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    The notebook mentions a `requirements.txt` file for installation.
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuration

1.  **Create a `.env` file** in the root directory of the project. This file will store your secret API keys.

2.  **Add your API keys** to the `.env` file. The notebook code loads the following keys:
    ```env
    OPENAI_API_KEY="sk-..."
    GOOGLE_GEMINI_API_KEY="..."
    DEEPSEEK_API_KEY="sk-..."
    GROQ_API_KEY="gsk_..."
    SENDGRID_API_KEY="SG...."
    ```

3.  **Update Email Addresses:** Inside the `send_html_email` function in the notebook, you **must** replace the placeholder email addresses with your verified SendGrid sender and the desired recipient.
    ```python
    # From this:
    from_email = Email("your_verified_sender@example.com") 
    to_email = To("recipient@example.com")  

    # To this:
    from_email = Email("your-email@yourdomain.com") 
    to_email = To("target-recipient@email.com")
    ```

### 4. Running the System

1.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
2.  Open the `Agentic_AI_Sales_Agent.ipynb` file.
3.  Run the cells sequentially from top to bottom to execute the entire workflow.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to create an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.