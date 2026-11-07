from src.utils.db import Base
import uuid
from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.sql import func

class UserModel(Base):
    __tablename__ = "user_table"
    
    id = Column(UUID(as_uuid = True), primary_key = True, default=uuid.uuid4, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index = True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    