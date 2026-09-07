"""campo FALSO COMO DEFALULT

Revision ID: 3cc08dbce007
Revises: 6b01ae9aba93
Create Date: 2026-09-06 10:19:13.566667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cc08dbce007'
down_revision: Union[str, Sequence[str], None] = '6b01ae9aba93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.add_column(
             'usuarios',
             sa.Column('admin', sa.Boolean, default=False , bool=False)
         )
  

