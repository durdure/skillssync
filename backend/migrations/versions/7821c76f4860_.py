"""empty message

Revision ID: 7821c76f4860
Revises: 3dac67747d29
Create Date: 2024-02-03 12:59:27.295477

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7821c76f4860'
down_revision = '3dac67747d29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('phone_no', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('address')
        batch_op.drop_column('phone_no')
        batch_op.drop_column('bio')

    op.create_table('comment',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('post_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_posted', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='comment_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='comment_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###