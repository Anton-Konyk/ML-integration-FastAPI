from fastapi import FastAPI
from app.schemas import TaskRequest, TaskResponse
from app.model import predict_priority

app = FastAPI(title="Task Priority Prediction API")


@app.post("/predict", response_model=TaskResponse)
def predict(request: TaskRequest):
    """Predict priority (high/low) for a given task description"""
    result = predict_priority(request.task_description)

    return TaskResponse(priority=result)
