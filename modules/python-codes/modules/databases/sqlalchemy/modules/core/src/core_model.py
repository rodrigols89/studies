# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import Table, Column, Integer, String, MetaData

studentMetaData = MetaData()

student = Table(
    'student', studentMetaData, 
    Column('id', Integer, primary_key = True), 
    Column('name', String(10)), 
    Column('lastname', String(10)), 
)
