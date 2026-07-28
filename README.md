# CAIE2 AI Post Generation

A Django REST Framework project that integrates an AI content service with a blog application.

The project supports generating post content and summarizing an existing post by its database ID. Generated summaries are saved back to the database together with the generation timestamp.

## Assignment Feature

### Summarize a Post by ID and Persist the Result

The summarization endpoint performs the following workflow:

1. Receives a `post_id`.
2. Retrieves the corresponding post from the database.
3. Returns HTTP `404` when the post does not exist.
4. Sends the post content to the AI summarization service.
5. Saves the generated summary in the `summary` field.
6. Saves the generation time in `summary_generated_at`.
7. Returns the summary and timestamp in the API response.

## Architecture

The AI integration follows a layered structure:

```text
View -> Service -> Client
```

- **View:** Handles HTTP requests, database lookup, persistence, and responses.
- **Service:** Handles validation, prompt construction, and AI use-case logic.
- **Client:** Handles communication with the OpenAI API.

Relevant files:

```text
blog/views/summarize.py
ai/content/service/summarize.py
ai/content/content_client.py
```

## API Endpoint

### Summarize an Existing Post

```http
POST /blog/posts/summarize/<post_id>/
```

Example successful response:

```json
{
  "post_id": 1,
  "summary": "A concise summary of the original post.",
  "summary_generated_at": "2026-07-28T12:00:00Z"
}
```

Possible responses:

- `200 OK`: Summary generated and saved successfully.
- `400 Bad Request`: The post content is invalid.
- `404 Not Found`: The requested post does not exist.
- `503 Service Unavailable`: The AI service is unavailable.

## Project Structure

```text
CAIE2/
├── ai/
│   └── content/
│       ├── content_client.py
│       ├── content_service.py
│       └── service/
│           ├── generate.py
│           ├── summarize.py
│           └── utils.py
├── blog/
│   ├── migrations/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── tests.py
│   └── urls.py
├── config/
│   └── settings.py
├── .env.example
├── AI_PROMPT_SUMMARIZE_POST_ASSIGNMENT.md
├── manage.py
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amer533/CAIE2-AI-Post-Generation.git
cd CAIE2-AI-Post-Generation
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```powershell
Copy-Item .env.example .env
```

Then provide the required values:

```env
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_SCHEMA=public

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4.1-mini
```

Do not commit the `.env` file.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Run the development server

```powershell
python manage.py runserver
```

## Verification

Run the Django system check:

```powershell
python manage.py check
```

Run the automated tests:

```powershell
python manage.py test blog.tests
```

The test suite covers:

- Successful summary generation and persistence.
- Saving `summary_generated_at`.
- Missing post handling with HTTP `404`.
- Invalid content handling with HTTP `400`.
- AI service failure handling with HTTP `503`.

## Configuration

The OpenAI API key and model name are loaded through Django settings from environment variables.

```python
OPENAI_API_KEY = config("OPENAI_API_KEY")

OPENAI_MODEL = config(
    "OPENAI_MODEL",
    default="gpt-4.1-mini",
)
```

The OpenAI client uses the Responses API:

```python
response = self.client.responses.create(
    model=self.model,
    input=prompt,
)
```

## AI Assistance

The prompt used to review the assignment implementation is documented in:

```text
AI_PROMPT_SUMMARIZE_POST_ASSIGNMENT.md
```

## Author

Amer Ziad Jaradat
