"""Buat tabel matakuliah dan constraint validasi akademik.

Revision ID: 0002_matakuliah
Revises: 0001_mahasiswa
"""

import sqlalchemy as sa
from alembic import op

revision = "0002_matakuliah"
down_revision = "0001_mahasiswa"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "matakuliah",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kode_mk", sa.String(length=20), nullable=False),
        sa.Column("nama_mk", sa.String(length=150), nullable=False),
        sa.Column("sks", sa.Integer(), nullable=False),
        sa.Column("semester", sa.Integer(), nullable=False),
        sa.CheckConstraint("sks > 0", name="ck_matakuliah_sks_positive"),
        sa.CheckConstraint("semester > 0", name="ck_matakuliah_semester_positive"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_matakuliah_kode_mk", "matakuliah", ["kode_mk"], unique=True)


def downgrade():
    op.drop_index("ix_matakuliah_kode_mk", table_name="matakuliah")
    op.drop_table("matakuliah")
