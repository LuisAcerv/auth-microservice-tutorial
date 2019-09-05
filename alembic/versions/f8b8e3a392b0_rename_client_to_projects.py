"""Rename client to projects

Revision ID: f8b8e3a392b0
Revises: 30a4bd07f707
Create Date: 2019-09-04 23:57:00.176639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b8e3a392b0'
down_revision = '30a4bd07f707'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('client', 'projects')

def downgrade():
    op.rename_table('projects', 'client')