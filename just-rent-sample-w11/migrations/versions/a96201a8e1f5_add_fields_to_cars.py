"""add fields to cars

Revision ID: a96201a8e1f5
Revises: 6d77d4620e94
Create Date: 2024-03-10 09:08:02.549904

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a96201a8e1f5'
down_revision = '6d77d4620e94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.add_column(sa.Column('displacement', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('car_type', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('seat_number', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('door_number', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('car_length', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('wheelbase', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('power_type', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('brand', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('model', sa.String(length=255), nullable=True))
        batch_op.drop_column('short_link')
        batch_op.drop_column('url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', mysql.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('short_link', mysql.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('model')
        batch_op.drop_column('brand')
        batch_op.drop_column('power_type')
        batch_op.drop_column('wheelbase')
        batch_op.drop_column('car_length')
        batch_op.drop_column('door_number')
        batch_op.drop_column('seat_number')
        batch_op.drop_column('car_type')
        batch_op.drop_column('displacement')

    # ### end Alembic commands ###
