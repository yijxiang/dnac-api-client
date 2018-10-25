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


class FileObjectListResultResponse(object):
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
        'md5_checksum': 'str',
        'sha1_checksum': 'str',
        'attribute_info': 'object',
        'download_path': 'str',
        'encrypted': 'bool',
        'file_size': 'str',
        'name': 'str',
        'id': 'str',
        'name_space': 'str',
        'sftp_server_list': 'list[object]',
        'file_format': 'str',
        'task_id': 'object'
    }

    attribute_map = {
        'md5_checksum': 'md5Checksum',
        'sha1_checksum': 'sha1Checksum',
        'attribute_info': 'attributeInfo',
        'download_path': 'downloadPath',
        'encrypted': 'encrypted',
        'file_size': 'fileSize',
        'name': 'name',
        'id': 'id',
        'name_space': 'nameSpace',
        'sftp_server_list': 'sftpServerList',
        'file_format': 'fileFormat',
        'task_id': 'taskId'
    }

    def __init__(self, md5_checksum=None, sha1_checksum=None, attribute_info=None, download_path=None, encrypted=None, file_size=None, name=None, id=None, name_space=None, sftp_server_list=None, file_format=None, task_id=None):  # noqa: E501
        """FileObjectListResultResponse - a model defined in OpenAPI"""  # noqa: E501

        self._md5_checksum = None
        self._sha1_checksum = None
        self._attribute_info = None
        self._download_path = None
        self._encrypted = None
        self._file_size = None
        self._name = None
        self._id = None
        self._name_space = None
        self._sftp_server_list = None
        self._file_format = None
        self._task_id = None
        self.discriminator = None

        if md5_checksum is not None:
            self.md5_checksum = md5_checksum
        if sha1_checksum is not None:
            self.sha1_checksum = sha1_checksum
        if attribute_info is not None:
            self.attribute_info = attribute_info
        if download_path is not None:
            self.download_path = download_path
        if encrypted is not None:
            self.encrypted = encrypted
        if file_size is not None:
            self.file_size = file_size
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if name_space is not None:
            self.name_space = name_space
        if sftp_server_list is not None:
            self.sftp_server_list = sftp_server_list
        if file_format is not None:
            self.file_format = file_format
        if task_id is not None:
            self.task_id = task_id

    @property
    def md5_checksum(self):
        """Gets the md5_checksum of this FileObjectListResultResponse.  # noqa: E501


        :return: The md5_checksum of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._md5_checksum

    @md5_checksum.setter
    def md5_checksum(self, md5_checksum):
        """Sets the md5_checksum of this FileObjectListResultResponse.


        :param md5_checksum: The md5_checksum of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._md5_checksum = md5_checksum

    @property
    def sha1_checksum(self):
        """Gets the sha1_checksum of this FileObjectListResultResponse.  # noqa: E501


        :return: The sha1_checksum of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha1_checksum

    @sha1_checksum.setter
    def sha1_checksum(self, sha1_checksum):
        """Sets the sha1_checksum of this FileObjectListResultResponse.


        :param sha1_checksum: The sha1_checksum of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._sha1_checksum = sha1_checksum

    @property
    def attribute_info(self):
        """Gets the attribute_info of this FileObjectListResultResponse.  # noqa: E501


        :return: The attribute_info of this FileObjectListResultResponse.  # noqa: E501
        :rtype: object
        """
        return self._attribute_info

    @attribute_info.setter
    def attribute_info(self, attribute_info):
        """Sets the attribute_info of this FileObjectListResultResponse.


        :param attribute_info: The attribute_info of this FileObjectListResultResponse.  # noqa: E501
        :type: object
        """

        self._attribute_info = attribute_info

    @property
    def download_path(self):
        """Gets the download_path of this FileObjectListResultResponse.  # noqa: E501


        :return: The download_path of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_path

    @download_path.setter
    def download_path(self, download_path):
        """Sets the download_path of this FileObjectListResultResponse.


        :param download_path: The download_path of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._download_path = download_path

    @property
    def encrypted(self):
        """Gets the encrypted of this FileObjectListResultResponse.  # noqa: E501


        :return: The encrypted of this FileObjectListResultResponse.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this FileObjectListResultResponse.


        :param encrypted: The encrypted of this FileObjectListResultResponse.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def file_size(self):
        """Gets the file_size of this FileObjectListResultResponse.  # noqa: E501


        :return: The file_size of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileObjectListResultResponse.


        :param file_size: The file_size of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._file_size = file_size

    @property
    def name(self):
        """Gets the name of this FileObjectListResultResponse.  # noqa: E501


        :return: The name of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileObjectListResultResponse.


        :param name: The name of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this FileObjectListResultResponse.  # noqa: E501


        :return: The id of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileObjectListResultResponse.


        :param id: The id of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name_space(self):
        """Gets the name_space of this FileObjectListResultResponse.  # noqa: E501


        :return: The name_space of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this FileObjectListResultResponse.


        :param name_space: The name_space of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._name_space = name_space

    @property
    def sftp_server_list(self):
        """Gets the sftp_server_list of this FileObjectListResultResponse.  # noqa: E501


        :return: The sftp_server_list of this FileObjectListResultResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._sftp_server_list

    @sftp_server_list.setter
    def sftp_server_list(self, sftp_server_list):
        """Sets the sftp_server_list of this FileObjectListResultResponse.


        :param sftp_server_list: The sftp_server_list of this FileObjectListResultResponse.  # noqa: E501
        :type: list[object]
        """

        self._sftp_server_list = sftp_server_list

    @property
    def file_format(self):
        """Gets the file_format of this FileObjectListResultResponse.  # noqa: E501


        :return: The file_format of this FileObjectListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this FileObjectListResultResponse.


        :param file_format: The file_format of this FileObjectListResultResponse.  # noqa: E501
        :type: str
        """

        self._file_format = file_format

    @property
    def task_id(self):
        """Gets the task_id of this FileObjectListResultResponse.  # noqa: E501


        :return: The task_id of this FileObjectListResultResponse.  # noqa: E501
        :rtype: object
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this FileObjectListResultResponse.


        :param task_id: The task_id of this FileObjectListResultResponse.  # noqa: E501
        :type: object
        """

        self._task_id = task_id

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
        if not isinstance(other, FileObjectListResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
