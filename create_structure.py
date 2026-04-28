import os

# Define full structure
structure = {
    "agents": [
        "research_agent.py",
        "planner_agent.py",
        "summarizer_agent.py",
        "critic_agent.py",
    ],
    "tools": [
        "web_search.py",
        "arxiv_fetcher.py",
        "pdf_reader.py",
        "code_executor.py",
        "wikipedia.py",
    ],
    "memory": [
        "vector_store.py",
        "session_memory.py",
        "graph_memory.py",
    ],
    "pipelines": [
        "deep_research.py",
        "fact_check.py",
        "report_generator.py",
    ],
    "config": [
        "settings.yaml",
        "prompts.yaml",
    ],
    "api": [
        "routes.py",
        "schemas.py",
    ],
    "data/raw": [],
    "data/processed": [],
    "data/outputs": [],
    "tests": [
        "test_agents.py",
        "test_tools.py",
        "test_pipelines.py",
    ]
}

# Root files
root_files = [
    "main.py",
    "requirements.txt",
    ".env",
    "docker-compose.yml"
]

def create_structure(base_path="."):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # empty file

    for file in root_files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
