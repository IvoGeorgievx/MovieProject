"""added model for hall availability

Revision ID: b7494178152b
Revises: 313755ee9335
Create Date: 2023-04-10 13:46:49.920232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "b7494178152b"
down_revision = "313755ee9335"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hall_availability",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("hall_id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["hall_id"],
            ["hall.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("movie", schema=None) as batch_op:
        batch_op.add_column(sa.Column("start_time", sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column("end_time", sa.DateTime(), nullable=False))
        batch_op.drop_column("screen_time")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movie", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "screen_time",
                postgresql.TIMESTAMP(),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.drop_column("end_time")
        batch_op.drop_column("start_time")

    op.drop_table("hall_availability")
    # ### end Alembic commands ###
