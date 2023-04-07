"""creating Transaction model

Revision ID: 11e7011a9e69
Revises: 945b5df45faf
Create Date: 2023-04-06 13:38:30.278975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11e7011a9e69'
down_revision = '945b5df45faf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    # ### end Alembic commands ###
