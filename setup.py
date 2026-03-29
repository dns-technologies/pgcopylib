from setuptools import (
    Extension,
    setup,
)
from Cython.Build import cythonize

extensions = [
    Extension(
        "pgcopylib.core.functions",
        ["src/pgcopylib/core/functions.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.arrays",
        ["src/pgcopylib/core/types/arrays.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.dates",
        ["src/pgcopylib/core/types/dates.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.digits",
        ["src/pgcopylib/core/types/digits.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.geometrics",
        ["src/pgcopylib/core/types/geometrics.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.ipaddrs",
        ["src/pgcopylib/core/types/ipaddrs.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.jsons",
        ["src/pgcopylib/core/types/jsons.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.strings",
        ["src/pgcopylib/core/types/strings.pyx"],
    ),
    Extension(
        "pgcopylib.core.types.uuids",
        ["src/pgcopylib/core/types/uuids.pyx"],
    ),
]

setup(
    name="pgcopylib",
    version="0.2.4.dev1",
    package_dir={"": "src"},
    ext_modules=cythonize(extensions, language_level="3"),
    packages=[
        "pgcopylib",
        "pgcopylib.common",
        "pgcopylib.core",
        "pgcopylib.core.types",
    ],
    package_data={
        "pgcopylib": [
            "**/*.py",
            "**/*.pyd",
            "**/*.pyi",
            "*.py",
            "*.pyd",
            "*.md",
            "*.txt",
        ]
    },
    exclude_package_data={
        "": ["*.c", "*.pxd", "*.pyx"],
        "pgcopylib": ["**/*.c", "**/*.pxd", "**/*.pyx"],
    },
    include_package_data=True,
    setup_requires=["Cython>=0.29.33"],
    zip_safe=False,
)
