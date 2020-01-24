"""changed logitem table to be boxview

Revision ID: 330f68646851
Revises: 8db1d7fca2ef
Create Date: 2019-02-05 19:39:25.393127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '330f68646851'
down_revision = '8db1d7fca2ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('box_view',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('box_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('view_logitem')
    op.drop_table('scan_logitem')
    op.drop_table('logitem')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scan_logitem',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['logitem.id'], name='scan_logitem_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='scan_logitem_pkey')
    )
    op.create_table('view_logitem',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['logitem.id'], name='view_logitem_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='view_logitem_pkey')
    )
    op.create_table('logitem',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('box_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('eventname', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], name='logitem_box_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='logitem_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='logitem_pkey')
    )
    op.drop_table('box_view')
    # ### end Alembic commands ###
