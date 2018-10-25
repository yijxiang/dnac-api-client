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


class WirelessInfoResultResponse(object):
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
        'lag_mode_enabled': 'bool',
        'instance_tenant_id': 'str',
        'wireless_license_info': 'str',
        'ap_group_name': 'str',
        'instance_uuid': 'str',
        'admin_enabled_ports': 'list[int]',
        'flex_group_name': 'str',
        'id': 'str',
        'wireless_package_installed': 'bool',
        'eth_mac_address': 'str',
        'device_id': 'str',
        'netconf_enabled': 'bool'
    }

    attribute_map = {
        'lag_mode_enabled': 'lagModeEnabled',
        'instance_tenant_id': 'instanceTenantId',
        'wireless_license_info': 'wirelessLicenseInfo',
        'ap_group_name': 'apGroupName',
        'instance_uuid': 'instanceUuid',
        'admin_enabled_ports': 'adminEnabledPorts',
        'flex_group_name': 'flexGroupName',
        'id': 'id',
        'wireless_package_installed': 'wirelessPackageInstalled',
        'eth_mac_address': 'ethMacAddress',
        'device_id': 'deviceId',
        'netconf_enabled': 'netconfEnabled'
    }

    def __init__(self, lag_mode_enabled=None, instance_tenant_id=None, wireless_license_info=None, ap_group_name=None, instance_uuid=None, admin_enabled_ports=None, flex_group_name=None, id=None, wireless_package_installed=None, eth_mac_address=None, device_id=None, netconf_enabled=None):  # noqa: E501
        """WirelessInfoResultResponse - a model defined in OpenAPI"""  # noqa: E501

        self._lag_mode_enabled = None
        self._instance_tenant_id = None
        self._wireless_license_info = None
        self._ap_group_name = None
        self._instance_uuid = None
        self._admin_enabled_ports = None
        self._flex_group_name = None
        self._id = None
        self._wireless_package_installed = None
        self._eth_mac_address = None
        self._device_id = None
        self._netconf_enabled = None
        self.discriminator = None

        if lag_mode_enabled is not None:
            self.lag_mode_enabled = lag_mode_enabled
        if instance_tenant_id is not None:
            self.instance_tenant_id = instance_tenant_id
        if wireless_license_info is not None:
            self.wireless_license_info = wireless_license_info
        if ap_group_name is not None:
            self.ap_group_name = ap_group_name
        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if admin_enabled_ports is not None:
            self.admin_enabled_ports = admin_enabled_ports
        if flex_group_name is not None:
            self.flex_group_name = flex_group_name
        if id is not None:
            self.id = id
        if wireless_package_installed is not None:
            self.wireless_package_installed = wireless_package_installed
        if eth_mac_address is not None:
            self.eth_mac_address = eth_mac_address
        if device_id is not None:
            self.device_id = device_id
        if netconf_enabled is not None:
            self.netconf_enabled = netconf_enabled

    @property
    def lag_mode_enabled(self):
        """Gets the lag_mode_enabled of this WirelessInfoResultResponse.  # noqa: E501


        :return: The lag_mode_enabled of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: bool
        """
        return self._lag_mode_enabled

    @lag_mode_enabled.setter
    def lag_mode_enabled(self, lag_mode_enabled):
        """Sets the lag_mode_enabled of this WirelessInfoResultResponse.


        :param lag_mode_enabled: The lag_mode_enabled of this WirelessInfoResultResponse.  # noqa: E501
        :type: bool
        """

        self._lag_mode_enabled = lag_mode_enabled

    @property
    def instance_tenant_id(self):
        """Gets the instance_tenant_id of this WirelessInfoResultResponse.  # noqa: E501


        :return: The instance_tenant_id of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_tenant_id

    @instance_tenant_id.setter
    def instance_tenant_id(self, instance_tenant_id):
        """Sets the instance_tenant_id of this WirelessInfoResultResponse.


        :param instance_tenant_id: The instance_tenant_id of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._instance_tenant_id = instance_tenant_id

    @property
    def wireless_license_info(self):
        """Gets the wireless_license_info of this WirelessInfoResultResponse.  # noqa: E501


        :return: The wireless_license_info of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._wireless_license_info

    @wireless_license_info.setter
    def wireless_license_info(self, wireless_license_info):
        """Sets the wireless_license_info of this WirelessInfoResultResponse.


        :param wireless_license_info: The wireless_license_info of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADVANTAGE", "ESSENTIALS"]  # noqa: E501
        if wireless_license_info not in allowed_values:
            raise ValueError(
                "Invalid value for `wireless_license_info` ({0}), must be one of {1}"  # noqa: E501
                .format(wireless_license_info, allowed_values)
            )

        self._wireless_license_info = wireless_license_info

    @property
    def ap_group_name(self):
        """Gets the ap_group_name of this WirelessInfoResultResponse.  # noqa: E501


        :return: The ap_group_name of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._ap_group_name

    @ap_group_name.setter
    def ap_group_name(self, ap_group_name):
        """Sets the ap_group_name of this WirelessInfoResultResponse.


        :param ap_group_name: The ap_group_name of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._ap_group_name = ap_group_name

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this WirelessInfoResultResponse.  # noqa: E501


        :return: The instance_uuid of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this WirelessInfoResultResponse.


        :param instance_uuid: The instance_uuid of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._instance_uuid = instance_uuid

    @property
    def admin_enabled_ports(self):
        """Gets the admin_enabled_ports of this WirelessInfoResultResponse.  # noqa: E501


        :return: The admin_enabled_ports of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._admin_enabled_ports

    @admin_enabled_ports.setter
    def admin_enabled_ports(self, admin_enabled_ports):
        """Sets the admin_enabled_ports of this WirelessInfoResultResponse.


        :param admin_enabled_ports: The admin_enabled_ports of this WirelessInfoResultResponse.  # noqa: E501
        :type: list[int]
        """

        self._admin_enabled_ports = admin_enabled_ports

    @property
    def flex_group_name(self):
        """Gets the flex_group_name of this WirelessInfoResultResponse.  # noqa: E501


        :return: The flex_group_name of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._flex_group_name

    @flex_group_name.setter
    def flex_group_name(self, flex_group_name):
        """Sets the flex_group_name of this WirelessInfoResultResponse.


        :param flex_group_name: The flex_group_name of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._flex_group_name = flex_group_name

    @property
    def id(self):
        """Gets the id of this WirelessInfoResultResponse.  # noqa: E501


        :return: The id of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WirelessInfoResultResponse.


        :param id: The id of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wireless_package_installed(self):
        """Gets the wireless_package_installed of this WirelessInfoResultResponse.  # noqa: E501


        :return: The wireless_package_installed of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: bool
        """
        return self._wireless_package_installed

    @wireless_package_installed.setter
    def wireless_package_installed(self, wireless_package_installed):
        """Sets the wireless_package_installed of this WirelessInfoResultResponse.


        :param wireless_package_installed: The wireless_package_installed of this WirelessInfoResultResponse.  # noqa: E501
        :type: bool
        """

        self._wireless_package_installed = wireless_package_installed

    @property
    def eth_mac_address(self):
        """Gets the eth_mac_address of this WirelessInfoResultResponse.  # noqa: E501


        :return: The eth_mac_address of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._eth_mac_address

    @eth_mac_address.setter
    def eth_mac_address(self, eth_mac_address):
        """Sets the eth_mac_address of this WirelessInfoResultResponse.


        :param eth_mac_address: The eth_mac_address of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._eth_mac_address = eth_mac_address

    @property
    def device_id(self):
        """Gets the device_id of this WirelessInfoResultResponse.  # noqa: E501


        :return: The device_id of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this WirelessInfoResultResponse.


        :param device_id: The device_id of this WirelessInfoResultResponse.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def netconf_enabled(self):
        """Gets the netconf_enabled of this WirelessInfoResultResponse.  # noqa: E501


        :return: The netconf_enabled of this WirelessInfoResultResponse.  # noqa: E501
        :rtype: bool
        """
        return self._netconf_enabled

    @netconf_enabled.setter
    def netconf_enabled(self, netconf_enabled):
        """Sets the netconf_enabled of this WirelessInfoResultResponse.


        :param netconf_enabled: The netconf_enabled of this WirelessInfoResultResponse.  # noqa: E501
        :type: bool
        """

        self._netconf_enabled = netconf_enabled

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
        if not isinstance(other, WirelessInfoResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
