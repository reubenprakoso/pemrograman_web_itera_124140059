from setuptools import find_packages, setup

setup(
    name="pyramid-mahasiswa",
    version="0.1.0",
    description="REST API manajemen mahasiswa dan matakuliah dengan Pyramid",
    packages=find_packages(),
    include_package_data=True,
    package_data={"pyramid_mahasiswa": ["alembic/*.mako", "alembic/versions/*.py"]},
    install_requires=[
        "alembic>=1.13,<2",
        "psycopg2-binary>=2.9,<3",
        "pyramid>=2.0,<3",
        "pyramid-tm>=2.5,<3",
        "SQLAlchemy>=2.0,<3",
        "transaction>=4,<6",
        "waitress>=3,<4",
        "zope.sqlalchemy>=3,<4",
    ],
    extras_require={"testing": ["pytest>=8,<9", "WebTest>=3,<4"]},
    entry_points={"paste.app_factory": ["main = pyramid_mahasiswa:main"]},
)
