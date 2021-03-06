# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dnac_api_client.models.path_response_result_response_egress_physical_interface import PathResponseResultResponseEgressPhysicalInterface  # noqa: F401,E501


class PathResponseResultResponseEgressInterface(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'physical_interface': 'PathResponseResultResponseEgressPhysicalInterface',
        'virtual_interface': 'list[PathResponseResultResponseEgressPhysicalInterface]'
    }

    attribute_map = {
        'physical_interface': 'physicalInterface',
        'virtual_interface': 'virtualInterface'
    }

    def __init__(self, physical_interface=None, virtual_interface=None):  # noqa: E501
        """PathResponseResultResponseEgressInterface - a model defined in Swagger"""  # noqa: E501

        self._physical_interface = None
        self._virtual_interface = None
        self.discriminator = None

        if physical_interface is not None:
            self.physical_interface = physical_interface
        if virtual_interface is not None:
            self.virtual_interface = virtual_interface

    @property
    def physical_interface(self):
        """Gets the physical_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501


        :return: The physical_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501
        :rtype: PathResponseResultResponseEgressPhysicalInterface
        """
        return self._physical_interface

    @physical_interface.setter
    def physical_interface(self, physical_interface):
        """Sets the physical_interface of this PathResponseResultResponseEgressInterface.


        :param physical_interface: The physical_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501
        :type: PathResponseResultResponseEgressPhysicalInterface
        """

        self._physical_interface = physical_interface

    @property
    def virtual_interface(self):
        """Gets the virtual_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501


        :return: The virtual_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501
        :rtype: list[PathResponseResultResponseEgressPhysicalInterface]
        """
        return self._virtual_interface

    @virtual_interface.setter
    def virtual_interface(self, virtual_interface):
        """Sets the virtual_interface of this PathResponseResultResponseEgressInterface.


        :param virtual_interface: The virtual_interface of this PathResponseResultResponseEgressInterface.  # noqa: E501
        :type: list[PathResponseResultResponseEgressPhysicalInterface]
        """

        self._virtual_interface = virtual_interface

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PathResponseResultResponseEgressInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
