# 2. Create the Cleanup Logic
# Create a new file, perhaps src/utils/cleanup.py, to hold the logic. This function queries the database for files older than 24 hours, unlinks (deletes) the physical file, and then deletes the database row.

# Python
# from datetime import datetime, timedelta
# from pathlib import Path
# from src.utils.db import SessionLocal # Adjust this import to wherever your DB session maker is
# from src.content_library.model import ContentLibrary

# def delete_expired_files():
#     # Open a fresh database session specifically for this background task
#     db = SessionLocal()
#     try:
#         # Define the 24-hour cutoff
#         cutoff_time = datetime.utcnow() - timedelta(hours=24)
        
#         # Find all records older than 24 hours
#         expired_files = db.query(ContentLibrary).filter(ContentLibrary.created_at < cutoff_time).all()
        
#         for file_record in expired_files:
#             # 1. Delete the physical file from the Windows/Linux file system
#             file_path = Path(file_record.stored_path)
#             if file_path.exists():
#                 file_path.unlink() # This deletes the file
                
#             # 2. Delete the database record
#             db.delete(file_record)
            
#         # Commit all deletions to the database
#         db.commit()
        
#         if expired_files:
#             print(f"Cleanup Script: Deleted {len(expired_files)} expired files.")
            
#     except Exception as e:
#         print(f"Error during cleanup: {str(e)}")
#     finally:
#         db.close()