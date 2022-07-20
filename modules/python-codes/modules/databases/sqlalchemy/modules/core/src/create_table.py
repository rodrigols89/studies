# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations


def create_table(engine, medaDataModel):
    medaDataModel.create_all(engine)
