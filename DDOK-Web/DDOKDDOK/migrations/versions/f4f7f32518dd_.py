"""empty message

Revision ID: f4f7f32518dd
Revises: 5f20f3b91c96
Create Date: 2021-08-14 11:55:08.924715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4f7f32518dd'
down_revision = '5f20f3b91c96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_room', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('state', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_room', schema=None) as batch_op:
        batch_op.drop_column('state')
        batch_op.drop_column('title')

    # ### end Alembic commands ###