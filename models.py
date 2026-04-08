from pydantic import BaseModel
from typing import Dict, Any, Optional

class Observation(BaseModel):
    task_id: str
    content: str
    metadata: Dict[str, Any]

class Action(BaseModel):
    action_type: str
    payload: Dict[str, Any]

class Reward(BaseModel):
    score: float
    feedback: Optional[str] = None