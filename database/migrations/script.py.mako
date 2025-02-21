"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic
revision = '${up_revision}'
down_revision = ${repr(down_revision)}
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration"""
    ${upgrades if upgrades else "pass"}


def downgrade():
    """Rollback the migration"""
    ${downgrades if downgrades else "pass"}
