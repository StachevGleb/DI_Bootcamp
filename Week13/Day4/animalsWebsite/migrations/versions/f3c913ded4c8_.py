"""empty message

Revision ID: f3c913ded4c8
Revises: 
Create Date: 2023-04-02 18:28:19.903006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3c913ded4c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('breed', sa.String(length=64), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=64), nullable=True),
    sa.Column('cart', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    op.drop_table('cart')
    # ### end Alembic commands ###
