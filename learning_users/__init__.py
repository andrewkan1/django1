import pymysql
# # pymysqlclient版本不够高就要运行以下语句
pymysql.version_info = (1, 4, 0, "final", 0)
pymysql.install_as_MySQLdb()
# # 将pymysql伪装成MySQLdb