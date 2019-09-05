"""create users table

Revision ID: 2f09903a7813
Revises: 
Create Date: 2019-09-04 21:13:19.938444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f09903a7813'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('users')