# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.API_Usuario.swagger_server.models.base_model_ import Model
from api.API_Usuario.swagger_server import util


class IdContraseaBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, contrasea: str=None):  # noqa: E501
        """IdContraseaBody - a model defined in Swagger

        :param contrasea: The contrasea of this IdContraseaBody.  # noqa: E501
        :type contrasea: str
        """
        self.swagger_types = {
            'contrasea': str
        }

        self.attribute_map = {
            'contrasea': 'contraseña'
        }
        self._contrasea = contrasea

    @classmethod
    def from_dict(cls, dikt) -> 'IdContraseaBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The id_contrasea_body of this IdContraseaBody.  # noqa: E501
        :rtype: IdContraseaBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contrasea(self) -> str:
        """Gets the contrasea of this IdContraseaBody.

        Nueva contraseña  # noqa: E501

        :return: The contrasea of this IdContraseaBody.
        :rtype: str
        """
        return self._contrasea

    @contrasea.setter
    def contrasea(self, contrasea: str):
        """Sets the contrasea of this IdContraseaBody.

        Nueva contraseña  # noqa: E501

        :param contrasea: The contrasea of this IdContraseaBody.
        :type contrasea: str
        """

        self._contrasea = contrasea
