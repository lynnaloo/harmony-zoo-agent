# Harmony City Zoo Park Concierge Agent

This agent serves as a helpful and friendly zoo employee that helps visitors from their first inspiration, through planning and booking. It also considers the most current list of exhibits, events, and activities and how the visit could be affected by weather and unexpected closures.

## Agent Details

This agent was build using Google's Agent Development Kit

### Agent Architecture

TBD

### Component Details

*   **Agents:**
    * `inspiration_agent` - interacts with the visitor to suggest exhibits, activities, events, and answer dining questions.
    * `planning_agent` - Given a user information and preferences, it will then generate an itinerary containing the activities.
    * `booking_agent` - Given an itinerary, the booking agent will help reserve tickets and book activities and events.
    
*   **Tools:**
    * `memorize` - a function to memorize information from the dialog that are important planning.
*   **AgentTools:**  
    * `weatyer_grounding` - used to return weather for a given visit day so it can help with planning.
    * `zoo_data_grounding` - provides data on exhibits, activities, events, and dining options.
   
*   **Memory:** 
    * All agents and tools use the Agent Development Kit's internal session state as memory.
    * The session state is used to store information such as the itinerary and booking details.

## Setup and Installation

### Prerequisites

- Python 3.11+
- Google Cloud Project (for Vertex AI integration)
- Google CLoud Storage Bucket
- Google Cloud Vertex AI Search Instance
- Google Agent Development Kit 1.0+
- Poetry: Install Poetry by following the instructions on the official Poetry [website](https://python-poetry.org/docs/)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/lynnaloo/harmony-zoo-agent
    cd harmony-city-zoo-agent
    ```

2.  Install dependencies using Poetry or pip:

    **Note for Linux users:** If you get an error related to `keyring` during the installation, you can disable it by running the following command:
    ```bash
    poetry config keyring.enabled false
    ```
    This is a one-time setup.
    ```bash
    poetry install
    ```

3.  Set up Google Cloud credentials:

    Otherwise:
    - At the top directory `zoo-agent/`, make a `.env` by copying `.env.example`
    - Set the following environment variables.
    - To use Vertex, make sure you have the Vertex AI API enabled in your project.
    ```
    # Choose Model Backend: 0 -> ML Dev, 1 -> Vertex
    GOOGLE_GENAI_USE_VERTEXAI=1
    # ML Dev backend config, when GOOGLE_GENAI_USE_VERTEXAI=0, ignore if using Vertex.
    # GOOGLE_API_KEY=YOUR_VALUE_HERE

    # Vertex backend config
    GOOGLE_CLOUD_PROJECT=__YOUR_CLOUD_PROJECT_ID__
    GOOGLE_CLOUD_LOCATION=us-central1

    # GCS Storage Bucket name
    GOOGLE_CLOUD_STORAGE_BUCKET=YOUR_BUCKET_NAME_HERE

    ```

4. Authenticate your GCloud account.
    ```bash
    gcloud auth application-default login
    ```

5. Activate the virtual environment set up by Poetry, run:
    ```bash
    eval $(poetry env activate)
    (zoo-agent-py3.12) $ # Virtualenv entered
    ```
    Repeat this command whenever you have a new shell, before running the commands in this README.

## Running the Agent

### Using `adk`

via its web interface:
```bash
# Under the zoo_concierge directory:
adk web
```

This will start a local web server on your machine. You may open the URL, select "zoo_concierge" in the top-left drop-down menu, and
a chatbot interface will appear on the right. 

## Deploying the Agent

To deploy the agent to Cloud Run, run the following command under `zoo-agent`:

```bash
make deploy
```