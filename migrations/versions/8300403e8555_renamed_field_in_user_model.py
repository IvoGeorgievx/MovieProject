"""renamed field in user model

Revision ID: 8300403e8555
Revises: 396922404de5
Create Date: 2023-04-03 16:39:02.599007

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "8300403e8555"
down_revision = "396922404de5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("stripe_account", sa.String(), nullable=True))
        batch_op.drop_column("wise_account")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("wise_account", sa.VARCHAR(), autoincrement=False, nullable=True)
        )
        batch_op.drop_column("stripe_account")

    # ### end Alembic commands ###
