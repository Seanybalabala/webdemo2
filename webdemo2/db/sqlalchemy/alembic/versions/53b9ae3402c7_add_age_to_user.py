"""Add age to user

Revision ID: 53b9ae3402c7
Revises: 016a6017da95
Create Date: 2018-07-25 13:21:04.421498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53b9ae3402c7'
down_revision = '016a6017da95'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'user',
        sa.Column('age', sa.Integer))


def downgrade():
    op.drop_column(
        'user',
        'age'
    )
