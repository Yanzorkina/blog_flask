"""empty message

Revision ID: 4328759e5227
Revises: e9eec9210076
Create Date: 2023-01-27 17:10:59.648732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4328759e5227'
down_revision = 'e9eec9210076'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    op.drop_table('article_tag_association')
    # ### end Alembic commands ###