"""empty message

Revision ID: 4e5f1d94c58b
Revises: a09650c4e541
Create Date: 2016-04-06 12:53:41.995805

"""

# revision identifiers, used by Alembic.
revision = '4e5f1d94c58b'
down_revision = 'a09650c4e541'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('author', 'password',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=60),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'password',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    ### end Alembic commands ###
