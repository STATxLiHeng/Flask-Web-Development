"""empty message

Revision ID: 546c1757132a
Revises: 4aa13b0ebe43
Create Date: 2023-03-16 19:59:34.991796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546c1757132a'
down_revision = '4aa13b0ebe43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hobby', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('hobby')

    # ### end Alembic commands ###
