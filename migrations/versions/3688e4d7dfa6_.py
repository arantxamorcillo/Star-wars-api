"""empty message

Revision ID: 3688e4d7dfa6
Revises: 2807edd385a2
Create Date: 2021-11-29 13:45:33.023266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3688e4d7dfa6'
down_revision = '2807edd385a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('density', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('hair_colour', sa.String(length=250), nullable=True),
    sa.Column('eye_colour', sa.String(length=250), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['Planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planets',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['Planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'planet_id')
    )
    op.create_table('favorite_characters',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['Character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'character_id')
    )
    op.add_column('user', sa.Column('username', sa.String(length=250), nullable=False))
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_column('user', 'username')
    op.drop_table('favorite_characters')
    op.drop_table('favorite_planets')
    op.drop_table('Character')
    op.drop_table('Planet')
    # ### end Alembic commands ###