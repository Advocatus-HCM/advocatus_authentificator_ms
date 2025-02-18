from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

async def update_user(user_data, db: AsyncSession):
   try:
       result = await db.execute(select(User).where(User.email == user_data.email))
       user = result.scalars().first()
       if not user:
           raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="User not found"
           )
      
       user.has_logged_in_before = True
       if user_data.password:
           user.password_hash = get_password_hash(user_data.password)
       if user_data.role:
           user.role = user_data.role


       db.add(user)
       await db.commit()


       return {"message": "User updated", "user": user}
  
   except Exception as e:
       await db.rollback()
       raise HTTPException(
           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
           detail=f"An error occurred while updating the user: {str(e)}"
       )


async def delete_user(user, db: AsyncSession):
   try:
       user_to_delete = await db.get(user, user.id_user)
       if user_to_delete:
           await db.delete(user_to_delete)
           await db.commit()
           return True
       return False
   except Exception as e:
       await db.rollback()
       raise HTTPException(
           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
           detail=f"An error occurred while deleting the user: {str(e)}"
       )
