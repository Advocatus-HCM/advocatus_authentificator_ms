from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

async def update_user(user_data, user, db: AsyncSession):
    try:
   
        if user_data.email:
            user.email = user_data.email
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
