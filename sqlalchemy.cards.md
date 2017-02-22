> What is official short description for SQLAlchemy?

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

> SQLAlchemy is most famous for its object-relational mapper (ORM), an optional component that provides the data mapper pattern. What is data mapper pattern?

Classes can be mapped to the database in open ended, multiple ways - allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.

> Who is the original author of SQLAlchemy?

Michael Bayer

> When was SQLAlchemy first released?

February 14, 2006

> What license is SQLAlchemy?

MIT License

> Michael Bayer is the original author of SQLAlchemy, what other library is he famous for?

Mako templates

> What is SQLAlchemy Core?

The Core is itself a fully featured SQL abstraction toolkit, providing a smooth layer of abstraction over a wide variety of DBAPI implementations and behaviors, as well as a SQL Expression Language which allows expression of the SQL language via generative Python expressions. A schema representation system that can both emit DDL statements as well as introspect existing schemas, and a type system that allows any mapping of Python types to database types, rounds out the system. The Object Relational Mapper is then an optional package which builds upon the Core

> What is DBAPI?

Python Database API, defined in PEP 249. Defined to encourage similarity between the Python modules that are used to access databases.

> What is `Unit of Work pattern`?

The Unit Of Work system, a central part of SQLAlchemy's Object Relational Mapper (ORM), organizes pending insert/update/delete operations into queues and flushes them all in one batch. To accomplish this it performs a topological "dependency sort" of all modified items in the queue so as to honor inter-row dependencies, and groups redundant statements together where they can sometimes be batched even further. This produces the maximum efficiency and transaction safety, and minimizes chances of deadlocks. Modeled after Fowler's "Unit of Work" pattern as well as Hibernate, Java's leading object-relational mapper.

> What is DDL?

A data definition language or data description language (DDL) is a syntax similar to a computer programming language for defining data structures, especially database schemas.
