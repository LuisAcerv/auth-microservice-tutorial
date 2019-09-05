"""Add a column to client

Revision ID: 30a4bd07f707
Revises: eed3aeae7d27
Create Date: 2019-09-04 23:21:28.142556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30a4bd07f707'
down_revision = 'eed3aeae7d27'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('client', sa.Column('account_name', sa.Text))

def downgrade():
    op.drop_column('client', 'account_name')