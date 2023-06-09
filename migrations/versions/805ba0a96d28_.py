"""empty message

Revision ID: 805ba0a96d28
Revises: f421bf2af177
Create Date: 2023-04-02 11:03:54.813625

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "805ba0a96d28"
down_revision = "f421bf2af177"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movie", schema=None) as batch_op:
        batch_op.add_column(sa.Column("ticket_price", sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movie", schema=None) as batch_op:
        batch_op.drop_column("ticket_price")

    # ### end Alembic commands ###
