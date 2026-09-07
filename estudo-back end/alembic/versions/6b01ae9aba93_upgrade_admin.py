"""upgrade admin

Revision ID: 6b01ae9aba93
Revises: be7fb36421eb
Create Date: 2026-09-06 10:15:42.770326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b01ae9aba93'
down_revision: Union[str, Sequence[str], None] = 'be7fb36421eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column(
           'usuarios',
           sa.Column('admin', sa.Boolean, nullable=False)
       )


def downgrade() -> None:
    """Downgrade schema."""
    pass
