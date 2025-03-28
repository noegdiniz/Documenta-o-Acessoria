"""empty message

Revision ID: 352fe3b21681
Revises: 5bcc60a6d982
Create Date: 2024-10-09 09:40:55.355070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352fe3b21681'
down_revision = '5bcc60a6d982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('documento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('empresa_nome', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('documento', schema=None) as batch_op:
        batch_op.drop_column('empresa_nome')

    # ### end Alembic commands ###
