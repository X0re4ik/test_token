"""1

Revision ID: 59788ce16786
Revises: b3210336b72e
Create Date: 2024-03-13 07:17:28.262022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59788ce16786'
down_revision: Union[str, None] = 'b3210336b72e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
