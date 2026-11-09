from src.utils.db import Base
import uuid
from sqlalchemy import Column, UUID, DateTime, String, ForeignKey
from sqlalchemy.sql import func

class ContentLibrary(Base):
    __tablename__ = "content_library"
    
    id = Column(UUID(as_uuid = True), primary_key = True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid = True), ForeignKey("user_table.id", ondelete="CASCADE"))
    original_name = Column(String(50), index=True, nullable=False)
    stored_path = Column(String(255), unique=True, index = True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    