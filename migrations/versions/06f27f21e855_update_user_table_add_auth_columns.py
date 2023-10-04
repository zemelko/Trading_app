"""Update user table, add auth columns

Revision ID: 06f27f21e855
Revises: 4cb81013b809
Create Date: 2023-10-04 21:01:27.611550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06f27f21e855'
down_revision: Union[str, None] = '4cb81013b809'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(length=1024), nullable=False))
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_verified')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###
