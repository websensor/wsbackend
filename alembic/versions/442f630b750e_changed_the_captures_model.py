"""changed the captures model

Revision ID: 442f630b750e
Revises: e17399e0e301
Create Date: 2019-01-11 23:04:36.985007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '442f630b750e'
down_revision = 'e17399e0e301'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('capture', sa.Column('batvoltagemv', sa.Float(), nullable=True))
    op.add_column('capture', sa.Column('resetsalltime', sa.Integer(), nullable=True))
    op.add_column('capture', sa.Column('status', sa.Integer(), nullable=True))
    op.add_column('capture', sa.Column('timeintmins', sa.Integer(), nullable=True))
    op.add_column('capture', sa.Column('version', sa.Integer(), nullable=True))
    op.drop_column('capture', 'scancount')
    op.drop_column('capture', 'batvoltage')
    op.drop_column('capture', 'smplcount')
    op.drop_column('capture', 'timeint')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('capture', sa.Column('timeint', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('capture', sa.Column('smplcount', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('capture', sa.Column('batvoltage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('capture', sa.Column('scancount', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('capture', 'version')
    op.drop_column('capture', 'timeintmins')
    op.drop_column('capture', 'status')
    op.drop_column('capture', 'resetsalltime')
    op.drop_column('capture', 'batvoltagemv')
    # ### end Alembic commands ###
