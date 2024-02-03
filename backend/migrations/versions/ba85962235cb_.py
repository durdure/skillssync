"""empty message

Revision ID: ba85962235cb
Revises: 7821c76f4860
Create Date: 2024-02-03 13:22:46.320561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba85962235cb'
down_revision = '7821c76f4860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=False)

    # ### end Alembic commands ###
