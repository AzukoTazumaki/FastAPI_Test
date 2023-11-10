from typing import Optional, List

from pydantic import validator
from sqlmodel import SQLModel, Field, Relationship, Column, JSON


class Products(SQLModel, table=True):
    __tablename__ = 'products'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    old_price: int | None = None
    description: List[str] = Field(sa_column=Column(JSON))
    beats: List['Beats'] = Relationship(back_populates='product')
    mixing: Optional['Mixing'] = Relationship(back_populates='product')
    mastering: Optional['Mastering'] = Relationship(back_populates='product')
    mixing_and_mastering: Optional['MixingAndMastering'] = Relationship(back_populates='product')
    ghostwriting: Optional['Ghostwriting'] = Relationship(back_populates='product')

    class Config:
        arbitrary_types_allowed = True
