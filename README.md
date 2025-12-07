# AI Job Recommender System using Local LLM

This project is an AI-powered job recommendation system that helps users analyze their resumes, identify skill gaps, and find relevant job opportunities from LinkedIn and Naukri. It leverages a local Large Language Model (Ollama) for privacy-preserving analysis and Apify for fetching job listings.

## Features

- **Resume Analysis**: Summarizes your resume highlighting key skills, education, and experience.
- **Skill Gap Detection**: Identifies missing skills and certifications required for your target role.
- **Career Roadmap**: Suggests a future roadmap for skill acquisition and career progression.
- **Job Recommendations**: Fetches real-time job listings from LinkedIn and Naukri based on your profile.
- **MCP Server Support**: Includes a Model Context Protocol (MCP) server for fetching jobs via MCP clients.

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: Ollama (Llama 3.2 3B)
- **PDF Processing**: PyMuPDF
- **Job Fetching**: Apify (LinkedIn & Naukri Scrapers)
- **Orchestration**: LangChain
- **Protocol**: Model Context Protocol (MCP)

## Prerequisites

1.  **Python 3.12+**
2.  **Ollama**: Install [Ollama](https://ollama.com/) and pull the required model:
    ```bash
    ollama pull llama3.2:3b
    ```
3.  **Apify Account**: Get your API token from [Apify Console](https://console.apify.com/).

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd ai-job-recommender-system-using-local-llm
    ```

2.  Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:
    Create a `.env` file in the root directory and add your Apify API token:
    ```env
    APIFY_API_TOKEN=your_apify_api_token_here
    ```

## Usage

### Web Application

1.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2.  Open your browser at `http://localhost:8501`.
3.  Upload your resume (PDF format).
4.  View the analysis (Summary, Skill Gaps, Roadmap).
5.  Click "Get Job Recommendations" to search for jobs.

### MCP Server

This project exposes an MCP server to fetch job data.

1.  Run the MCP server (stdio mode):
    ```bash
    mcp run mcp_server.py
    # Or directly with python
    python mcp_server.py
    ```

## Project Structure

- `app.py`: Main Streamlit application.
- `mcp_server.py`: MCP server implementation.
- `src/`:
    - `helper.py`: Helper functions for PDF extraction and Ollama interaction.
    - `job_api.py`: Functions to interact with Apify to fetch jobs.
- `requirements.txt`: Project dependencies.
- `pyproject.toml`: Project configuration and dependency definitions.
