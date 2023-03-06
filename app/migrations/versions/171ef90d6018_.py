"""empty message

Revision ID: 171ef90d6018
Revises: fe6797530ec8
Create Date: 2023-02-25 21:34:25.580571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171ef90d6018'
down_revision = 'fe6797530ec8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###