"""empty message

Revision ID: f3ac62e6a8ef
Revises: fd936ea0ceb6
Create Date: 2023-09-06 22:12:12.666315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3ac62e6a8ef'
down_revision = 'fd936ea0ceb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('seeking_talent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=500), nullable=True))

    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
        batch_op.add_column(sa.Column('seeking_talent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('seeking_talent')
        batch_op.drop_column('genres')
        batch_op.drop_column('website_link')

    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('seeking_talent')
        batch_op.drop_column('website_link')

    op.drop_table('Show')
    # ### end Alembic commands ###
