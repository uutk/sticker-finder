"""Boolean flag fuzzy on inline query request

Revision ID: 1cc051f593f8
Revises: be7577571b15
Create Date: 2019-08-29 01:37:15.209556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cc051f593f8'
down_revision = 'be7577571b15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inline_query_request', sa.Column('fuzzy', sa.Boolean(), server_default='false', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inline_query_request', 'fuzzy')
    # ### end Alembic commands ###
