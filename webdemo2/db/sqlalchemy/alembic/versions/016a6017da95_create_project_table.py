"""Create project table

Revision ID: 016a6017da95
Revises: ca888fa021cb
Create Date: 2018-07-25 12:57:53.060982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '016a6017da95'
down_revision = 'ca888fa021cb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'project',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('project_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(64), nullable=False, unique=True)
    )

    op.create_index(op.f('ix_project_project_id'), 'project', ['project_id'])


def downgrade():
    op.drop_table('project')
