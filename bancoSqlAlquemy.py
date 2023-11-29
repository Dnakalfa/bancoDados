from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(30), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)
print("\nInformação de usuario:")
print(user_prefs.primary_key)
print(user_prefs.constraints)

for table in metadata_obj.sorted_tables:
    print(table)


metadata_bd_obj = MetaData(schema='Bank')
financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

print("")
print("Exibe imformação de financial_info:")
print(financial_info.primary_key)
print(financial_info.constraints)