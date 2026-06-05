from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.section import Section


class SectionRepository:

    @staticmethod
    async def create_section(
        db: AsyncSession,
        section_data: dict
    ):

        new_section = Section(**section_data)

        db.add(new_section)

        await db.commit()

        await db.refresh(new_section)

        return new_section

    @staticmethod
    async def get_sections_by_board(
        db: AsyncSession,
        board_id
    ):

        query = select(Section).where(
            Section.board_id == board_id
        )

        result = await db.execute(query)

        return result.scalars().all()

    @staticmethod
    async def get_section_by_id(
        db: AsyncSession,
        section_id
    ):

        query = select(Section).where(
            Section.id == section_id
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def update_section(
        db: AsyncSession,
        section,
        update_data: dict
    ):

        for key, value in update_data.items():
            setattr(section, key, value)

        await db.commit()

        await db.refresh(section)

        return section

    @staticmethod
    async def delete_section(
        db: AsyncSession,
        section
    ):

        await db.delete(section)

        await db.commit()   