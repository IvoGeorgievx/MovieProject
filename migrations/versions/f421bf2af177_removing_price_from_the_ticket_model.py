"""removing price from the ticket model

Revision ID: f421bf2af177
Revises: f1f565378d26
Create Date: 2023-04-02 10:58:58.791984

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "f421bf2af177"
down_revision = "f1f565378d26"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ticket", schema=None) as batch_op:
        batch_op.drop_column("price")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ticket", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "price",
                sa.DOUBLE_PRECISION(precision=53),
                autoincrement=False,
                nullable=False,
            )
        )

    # ### end Alembic commands ###
