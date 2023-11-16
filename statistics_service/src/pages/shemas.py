from pydantic import UUID4, BaseModel, ConfigDict, Field, field_validator


class PostStatsOutputSchema(BaseModel):
    page_id: int
    post_id: int
    user_id: UUID4
    user_email: str | None = None
    like: int
