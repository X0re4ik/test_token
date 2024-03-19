"""Init2

Revision ID: 8293c28e8c6b
Revises: da801aa56ed9
Create Date: 2024-03-19 09:04:29.818040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8293c28e8c6b'
down_revision: Union[str, None] = 'da801aa56ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
