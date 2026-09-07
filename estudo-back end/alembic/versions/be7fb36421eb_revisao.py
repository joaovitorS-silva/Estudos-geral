"""Revisao

Revision ID: be7fb36421eb
Revises: 33f6659aa803
Create Date: 2026-09-06 10:13:49.008812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be7fb36421eb'
down_revision: Union[str, Sequence[str], None] = '33f6659aa803'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
