"""Initial migration

Revision ID: abcdef123456
Revises: None
Create Date: 2025-02-20 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic
revision = 'abcdef123456'  # Unique migration ID
down_revision = None  # No previous migration since this is the first one
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration: Create tables"""
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('company', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('posted_at', sa.DateTime(), server_default=sa.func.now())
    )

    op.create_table(
        'applicants',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), unique=True, nullable=False),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('resume', sa.String(), nullable=True)  # Stores resume file path
    )

    op.create_table(
        'applications',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('job_id', sa.Integer(), sa.ForeignKey("jobs.id"), nullable=False),
        sa.Column('applicant_id', sa.Integer(), sa.ForeignKey("applicants.id"), nullable=False),
        sa.Column('status', sa.String(), default="Pending"),
        sa.Column('applied_at', sa.DateTime(), server_default=sa.func.now())
    )


def downgrade():
    """Rollback the migration: Drop tables"""
    op.drop_table('applications')
    op.drop_table('applicants')
    op.drop_table('jobs')
