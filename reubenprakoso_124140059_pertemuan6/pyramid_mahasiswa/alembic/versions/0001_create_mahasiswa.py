"""Buat tabel mahasiswa.

Revision ID: 0001_mahasiswa
Revises:
"""

import sqlalchemy as sa
from alembic import op

revision = "0001_mahasiswa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "mahasiswa",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nim", sa.String(length=32), nullable=False),
        sa.Column("nama", sa.String(length=120), nullable=False),
        sa.Column("jurusan", sa.String(length=120), nullable=False),
        sa.Column("tanggal_lahir", sa.Date(), nullable=True),
        sa.Column("alamat", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_mahasiswa_nim", "mahasiswa", ["nim"], unique=True)


def downgrade():
    op.drop_index("ix_mahasiswa_nim", table_name="mahasiswa")
    op.drop_table("mahasiswa")
