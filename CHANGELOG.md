# Version History

## 0.2.4.dev1

* Developer release (not public to pip)
* Add pytest coverage
* Add flatten helper for nested arrays
* Add error handling for empty files in PGCopyReader
* Add comprehensive tests for all 32 data types including arrays and edge cases
* Decompose project structure
* Fix read_int8 overflow for maximum int64 values
* Fix read_bits and write_bits functions (add length prefix (4 bytes) and proper bit packing)
* Fix read_macaddr (return lowercase string to match PostgreSQL output format)
* Fix read_path and write_path (change closed flag from 1 byte to 4 bytes)
* Fix read_polygon and write_polygon (correct point coordinates reading)
* Fix write_timestamptz (proper timezone conversion to UTC)
* Fix empty arrays handling (write valid PostgreSQL array header with zero dimension)
* Fix NULL array elements (use 0xFFFFFFFF marker)
* Improve read_array and write_array to support multidimensional arrays
* Refactor PGCopyReader and PGCopyWriter
* Remove Cython source code from wheel package
* Change PGCopyReader and PGCopyWriter `__repr__`() method

## 0.2.4.dev0

* Developer release (not public to pip)
* Improve errors when write integers from floats and Decimals
* Update README.md

## 0.2.3.3

* Change documentation link
* Add requirements.txt
* Add depends python-dateutil>=2.8.0

## 0.2.3.2

* Delete BufferObject
* Rollback to stable functions from 0.2.2.6 version
* Improve unix systems support for array read function
* Fix compile from source on unix systems

## 0.2.3.1

* Add BufferObject

## 0.2.3.0

* Fix unpack requires a buffer of 4 bytes for unix systems

## 0.2.2.8

* Fix TypeError: an integer is required

## 0.2.2.7

* Improve array read length for unix systems
* Back compile depends to cython>=0.29.33
* Make wheels for python 3.10-3.14

## 0.2.2.6

* Downgrade compile depends to cython==0.29.33
* Make wheels for python 3.10 and 3.11 only

## 0.2.2.5

* Improve invalid byte sequence for encoding "UTF8": 0x00
* Disable Linux Aarch64

## 0.2.2.4

* Add auto convert String/FixedString(36) from Clickhouse data to Postgres uuid

## 0.2.2.3

* Fix write_timestamp error Can't subtract offset-naive and offset-aware datetimes

## 0.2.2.2

* Improve functions write_time and write_timetz
for support write from datetime.timedelta object

## 0.2.2.1

* Add PGOid.attname for system atributes names

## 0.2.2.0

* Update setuptools minimal version
* Fix nullable data read (thnx to @Art_Dmitriev)

## 0.2.1.9

* Update python version support to 3.10-3.14
* Change str and repr column view
* Change development status to 4 - Beta
* Add auto upload to pip

## 0.2.1.8

* Add wheels automake
* Improve strings functions
* Small refactors

## 0.2.1.7

* Add *.pyi files for cython modules descriptions
* Change str and repr methods
* Refactor some code
* Update MANIFEST.in

## 0.2.1.6

* Fix PostgreSQLDtype polars compatible types
* Fix digits dtype convert
* Fix write_numeric function

## 0.2.1.5

* Update MANIFEST.in
* Improve pyproject.toml license file approve
* Add CHANGELOG.md to pip package
* Add close() method to PGCopyReader & PGCopyWriter
* Add tell() method to PGCopyReader

## 0.2.1.4

* Reafactor write_date function
* Add MANIFEST.in
* Add MIT License

## 0.2.1.3

* Fix write_timestamp function
* Improve pandas.Timestamp write errors for date & datetime write functions
* Add date to datetime & datetime to date convert

## 0.2.1.2

* Fix PostgreSQLDtype values

## 0.2.1.1

* Change read_functions & write_functions to postgres_dtype

## 0.2.1.0

* Refactor project
* Redistribute project directories
* Improve some functions

## 0.2.0.1

* Setup.py code refactor
* Some fixes
* Cast Py_ssize_t data types to Cython data types

## 0.2.0.0

* Full refactor project
* Rewrite code to Cython for more performance
* Change PGCopy to PGCopyReader
* Speed up converter functions
* PGCopyReader now have only read_row generator to read one row and to_rows generator to read all rows
* PGCopyWriter now have methods write_row, from_rows, write and tell. fileobj now is optional.

## 0.1.3

* Rename PGCopyWriter.close() method to PGCopyWriter.finalize()
* Add PGCopyWriter.tell() method

## 0.1.2

* Add size parameter to PGCopy.read() method

## 0.1.1

* Fix read functions
* Add initialize PGCopyWriter from PGCopy object with method writer()

## 0.1.0

* Refactor over 60% code
* Remove self.columns
* Rename self.dtypes to self.pgtypes
* Change self.pgtypes object from PGDataType to PGOid
* Change self.__str__ & self.__repr__ output
* Add write functions
* Add class PGCopyWriter
* Add PGCopy.write method for initialize PGCopyWriter from PGCopy
* Add CHANGELOG.md

## 0.0.3

* Rename project to pgcopylib
* Refactor geometric types move from digits.py to geometrics.py
* Fix README.md
* Remove check -1 value in end of file for optimize PGCopy class initialization
* Publish library to Pip

## 0.0.2

* Add data type parsers
* Add geometric types
* Improve docs
* Rename Colums to Columns

## 0.0.1

First version of the library pgcopy_parser
