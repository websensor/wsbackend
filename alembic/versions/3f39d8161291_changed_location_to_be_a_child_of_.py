"""changed location to be a child of capturesample not box

Revision ID: 3f39d8161291
Revises: 3fe804f90c36
Create Date: 2018-10-25 09:01:17.513758

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3f39d8161291'
down_revision = '3fe804f90c36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('capturesample_id', sa.Integer(), nullable=True))
    op.add_column('location', sa.Column('timestamp', sa.DateTime(), nullable=False))
    op.drop_constraint('location_box_id_fkey', 'location', type_='foreignkey')
    op.create_foreign_key(None, 'location', 'capture_sample', ['capturesample_id'], ['id'])
    op.drop_column('location', 'sincets')
    op.drop_column('location', 'entryts')
    op.drop_column('location', 'box_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('box_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('location', sa.Column('entryts', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('location', sa.Column('sincets', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.create_foreign_key('location_box_id_fkey', 'location', 'box', ['box_id'], ['id'])
    op.drop_column('location', 'timestamp')
    op.drop_column('location', 'capturesample_id')
    # ### end Alembic commands ###
