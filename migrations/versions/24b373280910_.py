"""empty message

Revision ID: 24b373280910
Revises: 
Create Date: 2017-02-10 16:15:49.522450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b373280910'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group_resource', sa.Column('group_order', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'group_resource', ['group_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'group_resource', type_='unique')
    op.drop_column('group_resource', 'group_order')
    # ### end Alembic commands ###