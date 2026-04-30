import pymysql

# Spoof version for Django compatibility
pymysql.version_info = (2, 2, 8, "final", 0)
pymysql.install_as_MySQLdb()

# Bypass Django's MariaDB/MySQL version check
import django.db.backends.base.base
django.db.backends.base.base.BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# Bypass MariaDB RETURNING issue
import django.db.backends.mysql.features
django.db.backends.mysql.features.DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)
django.db.backends.mysql.features.DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
