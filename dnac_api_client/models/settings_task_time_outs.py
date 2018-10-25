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


class SettingsTaskTimeOuts(object):
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
        'config_time_out': 'int',
        'image_download_time_out': 'int',
        'general_time_out': 'int'
    }

    attribute_map = {
        'config_time_out': 'configTimeOut',
        'image_download_time_out': 'imageDownloadTimeOut',
        'general_time_out': 'generalTimeOut'
    }

    def __init__(self, config_time_out=None, image_download_time_out=None, general_time_out=None):  # noqa: E501
        """SettingsTaskTimeOuts - a model defined in OpenAPI"""  # noqa: E501

        self._config_time_out = None
        self._image_download_time_out = None
        self._general_time_out = None
        self.discriminator = None

        if config_time_out is not None:
            self.config_time_out = config_time_out
        if image_download_time_out is not None:
            self.image_download_time_out = image_download_time_out
        if general_time_out is not None:
            self.general_time_out = general_time_out

    @property
    def config_time_out(self):
        """Gets the config_time_out of this SettingsTaskTimeOuts.  # noqa: E501


        :return: The config_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :rtype: int
        """
        return self._config_time_out

    @config_time_out.setter
    def config_time_out(self, config_time_out):
        """Sets the config_time_out of this SettingsTaskTimeOuts.


        :param config_time_out: The config_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :type: int
        """

        self._config_time_out = config_time_out

    @property
    def image_download_time_out(self):
        """Gets the image_download_time_out of this SettingsTaskTimeOuts.  # noqa: E501


        :return: The image_download_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :rtype: int
        """
        return self._image_download_time_out

    @image_download_time_out.setter
    def image_download_time_out(self, image_download_time_out):
        """Sets the image_download_time_out of this SettingsTaskTimeOuts.


        :param image_download_time_out: The image_download_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :type: int
        """

        self._image_download_time_out = image_download_time_out

    @property
    def general_time_out(self):
        """Gets the general_time_out of this SettingsTaskTimeOuts.  # noqa: E501


        :return: The general_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :rtype: int
        """
        return self._general_time_out

    @general_time_out.setter
    def general_time_out(self, general_time_out):
        """Sets the general_time_out of this SettingsTaskTimeOuts.


        :param general_time_out: The general_time_out of this SettingsTaskTimeOuts.  # noqa: E501
        :type: int
        """

        self._general_time_out = general_time_out

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
        if not isinstance(other, SettingsTaskTimeOuts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
