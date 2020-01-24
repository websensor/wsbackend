"""added locations table

Revision ID: 3fe804f90c36
Revises: cc6bdd11cbe6
Create Date: 2018-10-23 23:49:06.642452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fe804f90c36'
down_revision = 'cc6bdd11cbe6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('box_id', sa.Integer(), nullable=True),
    sa.Column('entryts', sa.DateTime(), nullable=False),
    sa.Column('sincets', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    # ### end Alembic commands ###
