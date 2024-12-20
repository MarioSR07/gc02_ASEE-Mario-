# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from ..models.actor import Actor  # noqa: F401,E501
from ..models.capitulo import Capitulo  # noqa: F401,E501
from ..models.temporada import Temporada  # noqa: F401,E501
from .. import util


class Serie(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, titulo: str=None, genero: str=None, descripcion: str=None, actores: List[Actor]=None, temporadas: List[Temporada]=None, capitulos: List[Capitulo]=None):  # noqa: E501
        """Serie - a model defined in Swagger

        :param id: The id of this Serie.  # noqa: E501
        :type id: str
        :param titulo: The titulo of this Serie.  # noqa: E501
        :type titulo: str
        :param genero: The genero of this Serie.  # noqa: E501
        :type genero: str
        :param descripcion: The descripcion of this Serie.  # noqa: E501
        :type descripcion: str
        :param actores: The actores of this Serie.  # noqa: E501
        :type actores: List[Actor]
        :param temporadas: The temporadas of this Serie.  # noqa: E501
        :type temporadas: List[Temporada]
        :param capitulos: The capitulos of this Serie.  # noqa: E501
        :type capitulos: List[Capitulo]
        """
        self.swagger_types = {
            'id': str,
            'titulo': str,
            'genero': str,
            'descripcion': str,
            'actores': List[Actor],
            'temporadas': List[Temporada],
            'capitulos': List[Capitulo]
        }

        self.attribute_map = {
            'id': 'id',
            'titulo': 'titulo',
            'genero': 'genero',
            'descripcion': 'descripcion',
            'actores': 'actores',
            'temporadas': 'temporadas',
            'capitulos': 'capitulos'
        }
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._descripcion = descripcion
        self._actores = actores
        self._temporadas = temporadas
        self._capitulos = capitulos

    @classmethod
    def from_dict(cls, dikt) -> 'Serie':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Serie of this Serie.  # noqa: E501
        :rtype: Serie
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Serie.


        :return: The id of this Serie.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Serie.


        :param id: The id of this Serie.
        :type id: str
        """

        self._id = id

    @property
    def titulo(self) -> str:
        """Gets the titulo of this Serie.


        :return: The titulo of this Serie.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """Sets the titulo of this Serie.


        :param titulo: The titulo of this Serie.
        :type titulo: str
        """

        self._titulo = titulo

    @property
    def genero(self) -> str:
        """Gets the genero of this Serie.


        :return: The genero of this Serie.
        :rtype: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """Sets the genero of this Serie.


        :param genero: The genero of this Serie.
        :type genero: str
        """

        self._genero = genero

    @property
    def descripcion(self) -> str:
        """Gets the descripcion of this Serie.


        :return: The descripcion of this Serie.
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """Sets the descripcion of this Serie.


        :param descripcion: The descripcion of this Serie.
        :type descripcion: str
        """

        self._descripcion = descripcion

    @property
    def actores(self) -> List[Actor]:
        """Gets the actores of this Serie.


        :return: The actores of this Serie.
        :rtype: List[Actor]
        """
        return self._actores

    @actores.setter
    def actores(self, actores: List[Actor]):
        """Sets the actores of this Serie.


        :param actores: The actores of this Serie.
        :type actores: List[Actor]
        """

        self._actores = actores

    @property
    def temporadas(self) -> List[Temporada]:
        """Gets the temporadas of this Serie.


        :return: The temporadas of this Serie.
        :rtype: List[Temporada]
        """
        return self._temporadas

    @temporadas.setter
    def temporadas(self, temporadas: List[Temporada]):
        """Sets the temporadas of this Serie.


        :param temporadas: The temporadas of this Serie.
        :type temporadas: List[Temporada]
        """

        self._temporadas = temporadas

    @property
    def capitulos(self) -> List[Capitulo]:
        """Gets the capitulos of this Serie.


        :return: The capitulos of this Serie.
        :rtype: List[Capitulo]
        """
        return self._capitulos

    @capitulos.setter
    def capitulos(self, capitulos: List[Capitulo]):
        """Sets the capitulos of this Serie.


        :param capitulos: The capitulos of this Serie.
        :type capitulos: List[Capitulo]
        """

        self._capitulos = capitulos
