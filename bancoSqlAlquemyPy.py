from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, inspect, select, func
from sqlalchemy.orm import relationship, Session, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    Beto = User(
        name= "Umberto",
        fullname= "Umberto Alves",
        address= [Address(email_address="umberto_souza@hotamil.com")]
    )
    Carol= User(
        name= "Carolina",
        fullname= "Carolina Alves",
        address= [Address(email_address="carol_souza@hotamil.com")]
    )
    Isabel = User(
        name="Isabel",
        fullname="Isabel Xavier",
        address=[Address(email_address="isabel_xavier@hotamil.com")]
    )

    session.add_all([Beto, Carol, Isabel])

    session.commit()

stmt = select(User).where(User.name.in_(["Umberto", "Carolina"]))

for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))

for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())

for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()

for result in results:
    print(result)


stmt_account = select(func.count('*')).select_from(User)

for result in session.scalars(stmt_account):
    print(result)

session.close()
