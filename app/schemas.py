from pydantic import BaseModel


class FormData(BaseModel):

    class Config:
        arbitrary_types_allowed = True
        extra = "allow"
