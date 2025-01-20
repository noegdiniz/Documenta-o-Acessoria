"""empty message

Revision ID: 156ed65e09f0
Revises: 9e6c18da07ee
Create Date: 2024-10-21 14:50:34.058008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156ed65e09f0'
down_revision = '9e6c18da07ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('menu', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('user_perfil', sa.String(), nullable=False),
    sa.Column('action', sa.String(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###
