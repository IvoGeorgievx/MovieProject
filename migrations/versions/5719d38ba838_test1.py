"""test1

Revision ID: 5719d38ba838
Revises: 4aed91b70393
Create Date: 2023-04-04 14:24:11.135186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5719d38ba838'
down_revision = '4aed91b70393'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ticket_price', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('ticket_price')

    # ### end Alembic commands ###
