"""phone

Revision ID: ace0220dc3a5
Revises: 75423a1798ea
Create Date: 2025-05-06 20:56:48.994525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ace0220dc3a5'
down_revision: Union[str, None] = '75423a1798ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('phone', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointments', 'phone')
    # ### end Alembic commands ###
