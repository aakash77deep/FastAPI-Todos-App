"""Create phone number for users column

Revision ID: 663de7727bc7
Revises: 
Create Date: 2026-09-22 07:40:45.297056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '663de7727bc7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone_number', sa.String(), nullable=True)
    )

def downgrade() -> None:
    op.drop_column(
        'users', 'phone_number'
    )
