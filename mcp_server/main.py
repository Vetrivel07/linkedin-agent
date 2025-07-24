from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from mcp_server.agent_runner import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate_and_post")
async def generate_and_post(request: Request):
    data = await request.json()
    user_prompt = data.get("user_prompt")
    if not user_prompt:
        return {"status": "failed", "message": "Missing prompt input"}
    
    try:
        result = run_agent(user_prompt)
        return {"status": "success", "url": "https://www.linkedin.com/in/<your-linkedin-username>"}
    except Exception as e:
        return {"status": "failed", "message": str(e)}