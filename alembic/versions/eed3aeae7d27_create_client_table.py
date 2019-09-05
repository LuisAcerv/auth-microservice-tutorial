"""create client table

Revision ID: eed3aeae7d27
Revises: 2f09903a7813
Create Date: 2019-09-04 21:54:02.016317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = 'eed3aeae7d27'
down_revision = '2f09903a7813'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'client',
        sa.Column('client_id', postgresql.UUID(), nullable=False, unique=True),
    )

def downgrade():
    op.drop_table('users')