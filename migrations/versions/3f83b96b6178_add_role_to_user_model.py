"""Add role to User model

Revision ID: 3f83b96b6178
Revises: d7082bc9a8b6
Create Date: 2024-08-15 18:39:43.432478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '3f83b96b6178'
down_revision = 'd7082bc9a8b6'
branch_labels = None
depends_on = None


def upgrade():
    # Get the current connection
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)

    # Check if the 'role' column already exists in the 'users' table
    columns = [col['name'] for col in inspector.get_columns('users')]
    if 'role' not in columns:
        with op.batch_alter_table('users', schema=None) as batch_op:
            batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=False, server_default='user'))


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')
        
        
