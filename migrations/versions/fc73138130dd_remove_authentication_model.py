"""Remove Authentication model

Revision ID: fc73138130dd
Revises: 3f83b96b6178
Create Date: 2024-08-21 17:17:05.374542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc73138130dd'
down_revision = '3f83b96b6178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               nullable=False)

    # Drop the authentication table
    op.drop_table('authentication')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               nullable=True)

    # Recreate the authentication table
    op.create_table(
        'authentication',
        sa.Column('auth_id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('auth_token', sa.String(255), unique=True, nullable=False),
        sa.Column('expires_at', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.func.current_timestamp())
    )
    # ### end Alembic commands ###
