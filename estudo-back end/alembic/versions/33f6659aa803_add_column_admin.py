"""Add Column Admin

Revision ID: 33f6659aa803
Revises: f7e425788a16
Create Date: 2026-09-06 10:09:49.887020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33f6659aa803'
down_revision: Union[str, Sequence[str], None] = 'f7e425788a16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
