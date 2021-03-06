# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PathResponseResultResponseIngressInterface(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'physical_interface': 'PathResponseResultResponseEgressVirtualInterface',
        'virtual_interface': 'list[PathResponseResultResponseEgressVirtualInterface]'
    }

    attribute_map = {
        'physical_interface': 'physicalInterface',
        'virtual_interface': 'virtualInterface'
    }

    def __init__(self, physical_interface=None, virtual_interface=None):  # noqa: E501
        """PathResponseResultResponseIngressInterface - a model defined in OpenAPI"""  # noqa: E501

        self._physical_interface = None
        self._virtual_interface = None
        self.discriminator = None

        if physical_interface is not None:
            self.physical_interface = physical_interface
        if virtual_interface is not None:
            self.virtual_interface = virtual_interface

    @property
    def physical_interface(self):
        """Gets the physical_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501


        :return: The physical_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501
        :rtype: PathResponseResultResponseEgressVirtualInterface
        """
        return self._physical_interface

    @physical_interface.setter
    def physical_interface(self, physical_interface):
        """Sets the physical_interface of this PathResponseResultResponseIngressInterface.


        :param physical_interface: The physical_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501
        :type: PathResponseResultResponseEgressVirtualInterface
        """

        self._physical_interface = physical_interface

    @property
    def virtual_interface(self):
        """Gets the virtual_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501


        :return: The virtual_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501
        :rtype: list[PathResponseResultResponseEgressVirtualInterface]
        """
        return self._virtual_interface

    @virtual_interface.setter
    def virtual_interface(self, virtual_interface):
        """Sets the virtual_interface of this PathResponseResultResponseIngressInterface.


        :param virtual_interface: The virtual_interface of this PathResponseResultResponseIngressInterface.  # noqa: E501
        :type: list[PathResponseResultResponseEgressVirtualInterface]
        """

        self._virtual_interface = virtual_interface

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PathResponseResultResponseIngressInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
