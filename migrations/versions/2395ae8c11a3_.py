"""empty message

Revision ID: 2395ae8c11a3
Revises: 0a70cf04550a
Create Date: 2024-10-15 14:18:41.060717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2395ae8c11a3'
down_revision = '0a70cf04550a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('perfil', schema=None) as batch_op:
        batch_op.add_column(sa.Column('can_create_dados', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_dados', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_dados', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_dados', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_create_contratos', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_contratos', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_contratos', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_contratos', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_create_categorias', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_categorias', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_categorias', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_categorias', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_aprove_docs', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_docs', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_docs', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_create_empresas', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_empresas', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_empresas', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_empresas', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_create_perfis', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_perfis', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_perfis', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_perfis', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_edit_users', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_delete_uses', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('can_view_users', sa.Boolean(), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('perfil_id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('perfil_id')

    with op.batch_alter_table('perfil', schema=None) as batch_op:
        batch_op.drop_column('can_view_users')
        batch_op.drop_column('can_delete_uses')
        batch_op.drop_column('can_edit_users')
        batch_op.drop_column('can_view_perfis')
        batch_op.drop_column('can_delete_perfis')
        batch_op.drop_column('can_edit_perfis')
        batch_op.drop_column('can_create_perfis')
        batch_op.drop_column('can_view_empresas')
        batch_op.drop_column('can_delete_empresas')
        batch_op.drop_column('can_edit_empresas')
        batch_op.drop_column('can_create_empresas')
        batch_op.drop_column('can_view_docs')
        batch_op.drop_column('can_delete_docs')
        batch_op.drop_column('can_aprove_docs')
        batch_op.drop_column('can_view_categorias')
        batch_op.drop_column('can_delete_categorias')
        batch_op.drop_column('can_edit_categorias')
        batch_op.drop_column('can_create_categorias')
        batch_op.drop_column('can_view_contratos')
        batch_op.drop_column('can_delete_contratos')
        batch_op.drop_column('can_edit_contratos')
        batch_op.drop_column('can_create_contratos')
        batch_op.drop_column('can_view_dados')
        batch_op.drop_column('can_delete_dados')
        batch_op.drop_column('can_edit_dados')
        batch_op.drop_column('can_create_dados')

    # ### end Alembic commands ###
