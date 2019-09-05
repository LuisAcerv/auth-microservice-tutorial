"""Rename projects pk column name

Revision ID: c7fe165faa42
Revises: f8b8e3a392b0
Create Date: 2019-09-04 23:59:30.440773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7fe165faa42'
down_revision = 'f8b8e3a392b0'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('projects', 'account_name', nullable=True, new_column_name='project_name')


def downgrade():
    op.alter_column('projects', 'project_name', nullable=False, new_column_name='account_name')
