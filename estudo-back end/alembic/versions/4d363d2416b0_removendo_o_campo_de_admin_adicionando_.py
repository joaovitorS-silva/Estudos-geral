"""removendo o campo de admin , adicionando role

Revision ID: 4d363d2416b0
Revises: 3cc08dbce007
Create Date: 2026-09-09 23:16:37.815472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d363d2416b0'
down_revision: Union[str, Sequence[str], None] = '3cc08dbce007'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
