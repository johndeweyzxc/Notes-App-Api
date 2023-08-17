from pydantic import BaseModel

class DateInformation(BaseModel):
    created_at: int
    updated_at: int | None = None
    deleted_at: int | None = None