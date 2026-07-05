from typing import List
from pydantic import BaseModel


class SearchResponse(BaseModel):
    question: str
    answer: str
    sources: List[str]