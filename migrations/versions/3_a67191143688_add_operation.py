"""Add operation

Revision ID: a67191143688
Revises: b156afee0312
Create Date: 2023-10-12 17:21:37.155126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a67191143688'
down_revision: Union[str, None] = 'b156afee0312'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.String(), nullable=True),
    sa.Column('figi', sa.String(), nullable=True),
    sa.Column('instrument_type', sa.String(), nullable=True),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###
