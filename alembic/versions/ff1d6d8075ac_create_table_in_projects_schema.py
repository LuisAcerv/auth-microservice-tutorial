"""Create table in projects schema

Revision ID: ff1d6d8075ac
Revises: d7b70034dca4
Create Date: 2019-09-05 21:10:55.683736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'ff1d6d8075ac'
down_revision = 'd7b70034dca4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users.projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('project_id', postgresql.UUID(), nullable=False, unique=True),
    )

def downgrade():
    op.drop_table('users.projects')