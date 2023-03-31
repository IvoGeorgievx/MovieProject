"""alternating password field length

Revision ID: 049662b23c7d
Revises: ece6bfd4755d
Create Date: 2023-03-30 13:52:34.742495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '049662b23c7d'
down_revision = 'ece6bfd4755d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
