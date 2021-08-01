"""empty message

Revision ID: 682640264e52
Revises: 9decda694eb4
Create Date: 2021-08-01 17:18:32.281542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '682640264e52'
down_revision = '9decda694eb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('song', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
