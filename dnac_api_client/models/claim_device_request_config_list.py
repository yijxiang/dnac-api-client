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


class ClaimDeviceRequestConfigList(object):
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
        'config_id': 'str',
        'config_parameters': 'list[ClaimDeviceRequestConfigParameters]'
    }

    attribute_map = {
        'config_id': 'configId',
        'config_parameters': 'configParameters'
    }

    def __init__(self, config_id=None, config_parameters=None):  # noqa: E501
        """ClaimDeviceRequestConfigList - a model defined in OpenAPI"""  # noqa: E501

        self._config_id = None
        self._config_parameters = None
        self.discriminator = None

        if config_id is not None:
            self.config_id = config_id
        if config_parameters is not None:
            self.config_parameters = config_parameters

    @property
    def config_id(self):
        """Gets the config_id of this ClaimDeviceRequestConfigList.  # noqa: E501


        :return: The config_id of this ClaimDeviceRequestConfigList.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this ClaimDeviceRequestConfigList.


        :param config_id: The config_id of this ClaimDeviceRequestConfigList.  # noqa: E501
        :type: str
        """

        self._config_id = config_id

    @property
    def config_parameters(self):
        """Gets the config_parameters of this ClaimDeviceRequestConfigList.  # noqa: E501


        :return: The config_parameters of this ClaimDeviceRequestConfigList.  # noqa: E501
        :rtype: list[ClaimDeviceRequestConfigParameters]
        """
        return self._config_parameters

    @config_parameters.setter
    def config_parameters(self, config_parameters):
        """Sets the config_parameters of this ClaimDeviceRequestConfigList.


        :param config_parameters: The config_parameters of this ClaimDeviceRequestConfigList.  # noqa: E501
        :type: list[ClaimDeviceRequestConfigParameters]
        """

        self._config_parameters = config_parameters

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
        if not isinstance(other, ClaimDeviceRequestConfigList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
