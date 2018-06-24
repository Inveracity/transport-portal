"""empty message

Revision ID: 29fa65fe0850
Revises: f021805f30bc
Create Date: 2018-06-17 15:13:51.726680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29fa65fe0850'
down_revision = 'f021805f30bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('group', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'group')
    # ### end Alembic commands ###
