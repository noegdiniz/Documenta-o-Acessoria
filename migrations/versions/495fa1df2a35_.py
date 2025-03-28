"""empty message

Revision ID: 495fa1df2a35
Revises: 10e43ce96e22
Create Date: 2024-10-16 11:08:36.060961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '495fa1df2a35'
down_revision = '10e43ce96e22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cubo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('perfil_id', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('perfil_nome', sa.String(), nullable=False))
        batch_op.drop_column('perfil')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cubo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('perfil', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('perfil_nome')
        batch_op.drop_column('perfil_id')

    # ### end Alembic commands ###
