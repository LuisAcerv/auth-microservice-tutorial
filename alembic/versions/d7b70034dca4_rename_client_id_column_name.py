"""Rename client_id column name

Revision ID: d7b70034dca4
Revises: c7fe165faa42
Create Date: 2019-09-05 00:04:03.842950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7b70034dca4'
down_revision = 'c7fe165faa42'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('projects', 'client_id', nullable=True, new_column_name='project_id')


def downgrade():
    op.alter_column('projects', 'client_id', nullable=False, new_column_name='project_id')
