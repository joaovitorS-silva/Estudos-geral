"""adiciona server_default em criado_em

Revision ID: f7e425788a16
Revises: 19cd489c5520
Create Date: 2026-09-05 19:33:01.864833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7e425788a16'
down_revision: Union[str, Sequence[str], None] = '19cd489c5520'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.alter_column(
        'usuarios',
        'criado_em',
        server_default=sa.func.now()
    )


def downgrade() -> None:
    op.alter_column(
        'usuarios',
        'criado_em',
        server_default=None
    )
