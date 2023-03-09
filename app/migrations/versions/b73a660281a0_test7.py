"""test7

Revision ID: b73a660281a0
Revises: c8936dfbba3b
Create Date: 2023-03-09 17:30:05.261597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73a660281a0'
down_revision = 'c8936dfbba3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('check', sa.Integer(), nullable=True,default =0))


def downgrade() -> None:
    pass
