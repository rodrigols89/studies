# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from connections import get_engine_connection, get_session
from create_table import create_table
from core_model import studentMetaData, student

student_list = [
    {
        'name': 'Maria',
        'lastname': 'Jose'
    },
    {
        'name': 'João',
        'lastname': 'Benedito'
    },
    {
        'name': 'Herbet',
        'lastname': 'Silva'
    },
    {
        'name': 'Jhon',
        'lastname': 'Allan'
    },
    {
        'name': 'Mary',
        'lastname': 'Key'
    },
    {
        'name': 'Wesley',
        'lastname': 'Lima'
    }
]


if __name__ == '__main__':

    # Testing connection.
    #print('\nTesting connection:')
    engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')
    #print(engine)
    #print(type(engine))
    #print(bool(engine))


    Session = get_session(engine)
    print(Session)
    print(type(Session))
    print(bool(Session))


    # Testing connect() method.
    #print('\nTesting connect():')
    conn = engine.connect()
    #print(conn)
    #print(type(conn))
    #print(bool(conn))


    # Testing create table.
    #print('\nTesting create table:')
    #ct_result = studentMetaData.create_all(engine)
    #print(ct_result)
    #print(type(ct_result))
    #print(bool(ct_result))


    # Testing create table generic.
    #print('\nTesting create table generic:')
    #ct_generic = create_table(engine=engine, medaDataModel=studentMetaData)
    #print(ct_generic)
    #print(type(ct_generic))
    #print(bool(ct_generic))


    # Testing inserting data.
    #print('\nTesting insert data:')
    #print(type(student_dict))
    #ins = student.insert().values(student_dict)
    #print(ins)
    #conn.execute(student.insert(), student_list)
    #select_query = student.select().where(student.c.id > 3)
    #s_result = conn.execute(select_query)
    #for row in s_result:
    #    print(row)

