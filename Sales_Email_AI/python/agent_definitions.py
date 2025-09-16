# %%writefile agent_definitions.py
# This would be your actual agents library
from agents import Agent, OpenAIChatCompletionsModel 

# Import shared components
from llm_clients import gemini_client, groq_client, deepseek_client, openai_client
from tools import send_html_email

# ---------------- मॉडल्स ----------------
gemini_model = OpenAIChatCompletionsModel(model="gemini-1.5-flash-latest", openai_client=gemini_client)
llama3_model = OpenAIChatCompletionsModel(model="llama3-70b-8192", openai_client=groq_client)
deepseek_model = OpenAIChatCompletionsModel(model="deepseek-chat", openai_client=deepseek_client)
gpt4o_mini_model = OpenAIChatCompletionsModel(model="gpt-4o-mini", openai_client=openai_client)

# ---------------- सहायक एजेंट्स ----------------
# Sales Agent Personas
sales_agent_professional = Agent(
    name="Professional Sales Agent",
    instructions="You are a professional sales agent for DaySmart Vet, a SaaS platform for veterinary practices. You write serious, formal, and persuasive cold emails.",
    model=deepseek_model
)

sales_agent_humorous = Agent(
    name="Humorous Sales Agent",
    instructions="You are a witty sales agent for DaySmart Vet. You write humorous, engaging, and memorable cold emails designed to get a response.",
    model=gemini_model
)

sales_agent_concise = Agent(
    name="Concise Sales Agent",
    instructions="You are a busy, efficient sales agent for DaySmart Vet. You write concise, to-the-point cold emails that respect the recipient's time.",
    model=llama3_model
)

# Formatting Agents
subject_writer = Agent(
    name="Subject Writer",
    instructions="You are an expert copywriter. Given the body of an email, create a compelling, concise, and click-worthy subject line.",
    model=gpt4o_mini_model
)

html_converter = Agent(
    name="HTML Converter",
    instructions="You are an HTML email developer. Convert a given plain text or markdown email body into a clean, simple, and responsive HTML format.",
    model=gpt4o_mini_model
)

# ---------------- प्रबंधक एजेंट्स ----------------
# Email Manager (Formatter and Sender)
emailer_agent = Agent(
    name="Email Manager",
    instructions="You are an email formatting and sending specialist. Your workflow is: 1. Use the subject_writer tool to get a subject. 2. Use the html_converter tool to get an HTML body. 3. Use the send_html_email tool to send the final email.",
    tools=[subject_writer.as_tool(name="subject_writer", description="Write an email subject"),
           html_converter.as_tool(name="html_converter", description="Convert text to HTML email"),
           send_html_email],
    model=gpt4o_mini_model,
    handoff_description="Formats and sends a finalized email."
)

# Senior Sales Manager (Orchestrator)
senior_sales_manager = Agent(
    name="Senior Sales Manager",
    instructions=(
        "You are the Senior Sales Manager for DaySmart Vet. Your goal is to orchestrate the creation of the best possible sales email.\n"
        "1. Use all three sales agent tools to generate three distinct email drafts.\n"
        "2. Critically evaluate the drafts and select the single best one.\n"
        "3. Hand off the chosen email body to the 'Email Manager' to handle formatting and sending."
    ),
    tools=[
        sales_agent_professional.as_tool(name="professional_agent", description="Draft a professional email"),
        sales_agent_humorous.as_tool(name="humorous_agent", description="Draft a humorous email"),
        sales_agent_concise.as_tool(name="concise_agent", description="Draft a concise email"),
    ],
    handoffs=[emailer_agent],
    model=gpt4o_mini_model
)