"""empty message

Revision ID: 077320a5d585
Revises: d08fc0dc4047
Create Date: 2023-01-18 16:27:44.978636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077320a5d585'
down_revision = 'd08fc0dc4047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('_password')

    # ### end Alembic commands ###
