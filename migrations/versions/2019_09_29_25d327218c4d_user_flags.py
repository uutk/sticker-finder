"""User flags

Revision ID: 25d327218c4d
Revises: c95f92b9e1f1
Create Date: 2019-09-29 19:33:46.075644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25d327218c4d'
down_revision = 'c95f92b9e1f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('furry', sa.Boolean(), server_default='False', nullable=False))
    op.add_column('user', sa.Column('nsfw', sa.Boolean(), server_default='False', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nsfw')
    op.drop_column('user', 'furry')
    # ### end Alembic commands ###
