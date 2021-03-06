# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dnac_api_client.api_client import ApiClient


class SWIMApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_image_activation_device_post(self, request_body, **kwargs):  # noqa: E501
        """Trigger activation on a device  # noqa: E501

        Performs activation of an image on a given device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_activation_device_post(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :param str client_type: Client-type (Optional)
        :param str client_url: Client-url (Optional)
        :param bool schedule_validate: scheduleValidate, validates data before schedule (Optional)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_image_activation_device_post_with_http_info(request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_image_activation_device_post_with_http_info(request_body, **kwargs)  # noqa: E501
            return data

    def api_v1_image_activation_device_post_with_http_info(self, request_body, **kwargs):  # noqa: E501
        """Trigger activation on a device  # noqa: E501

        Performs activation of an image on a given device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_activation_device_post_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :param str client_type: Client-type (Optional)
        :param str client_url: Client-url (Optional)
        :param bool schedule_validate: scheduleValidate, validates data before schedule (Optional)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['request_body', 'client_type', 'client_url', 'schedule_validate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_image_activation_device_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `api_v1_image_activation_device_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'schedule_validate' in local_var_params:
            query_params.append(('scheduleValidate', local_var_params['schedule_validate']))  # noqa: E501

        header_params = {}
        if 'client_type' in local_var_params:
            header_params['Client-Type'] = local_var_params['client_type']  # noqa: E501
        if 'client_url' in local_var_params:
            header_params['Client-Url'] = local_var_params['client_url']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/image/activation/device', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskIdResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_image_distribution_post(self, request_body, **kwargs):  # noqa: E501
        """Trigger distribution of an image  # noqa: E501

        Performs distribution of an image to a given device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_distribution_post(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_image_distribution_post_with_http_info(request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_image_distribution_post_with_http_info(request_body, **kwargs)  # noqa: E501
            return data

    def api_v1_image_distribution_post_with_http_info(self, request_body, **kwargs):  # noqa: E501
        """Trigger distribution of an image  # noqa: E501

        Performs distribution of an image to a given device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_distribution_post_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['request_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_image_distribution_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `api_v1_image_distribution_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/image/distribution', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskIdResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_image_importation_get(self, **kwargs):  # noqa: E501
        """Get image details with filter  # noqa: E501

        Get image details based on filter criteria, use % for like operations. Example: filterByName = cat3k%  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str image_uuid: imageUuid
        :param str name: name
        :param str family: family
        :param str application_type: applicationType
        :param str image_integrity_status: imageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED
        :param str version: software Image Version
        :param str image_series: image Series
        :param str image_name: image Name
        :param bool is_tagged_golden: is Tagged Golden
        :param bool is_cco_recommended: is recommended from cisco.com
        :param bool is_cco_latest: is latest from cisco.com
        :param int created_time: time in milliseconds (epoch format)
        :param int image_size_greater_than: size in bytes
        :param int image_size_lesser_than: size in bytes
        :param str sort_by: sort results by this field
        :param str sort_order: sort order - 'asc' or 'des'. Default is asc
        :param int limit: limit
        :param int offset: offset
        :return: ImageInfoListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_image_importation_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_image_importation_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_image_importation_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get image details with filter  # noqa: E501

        Get image details based on filter criteria, use % for like operations. Example: filterByName = cat3k%  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str image_uuid: imageUuid
        :param str name: name
        :param str family: family
        :param str application_type: applicationType
        :param str image_integrity_status: imageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED
        :param str version: software Image Version
        :param str image_series: image Series
        :param str image_name: image Name
        :param bool is_tagged_golden: is Tagged Golden
        :param bool is_cco_recommended: is recommended from cisco.com
        :param bool is_cco_latest: is latest from cisco.com
        :param int created_time: time in milliseconds (epoch format)
        :param int image_size_greater_than: size in bytes
        :param int image_size_lesser_than: size in bytes
        :param str sort_by: sort results by this field
        :param str sort_order: sort order - 'asc' or 'des'. Default is asc
        :param int limit: limit
        :param int offset: offset
        :return: ImageInfoListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['image_uuid', 'name', 'family', 'application_type', 'image_integrity_status', 'version', 'image_series', 'image_name', 'is_tagged_golden', 'is_cco_recommended', 'is_cco_latest', 'created_time', 'image_size_greater_than', 'image_size_lesser_than', 'sort_by', 'sort_order', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_image_importation_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'image_uuid' in local_var_params:
            query_params.append(('imageUuid', local_var_params['image_uuid']))  # noqa: E501
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'family' in local_var_params:
            query_params.append(('family', local_var_params['family']))  # noqa: E501
        if 'application_type' in local_var_params:
            query_params.append(('applicationType', local_var_params['application_type']))  # noqa: E501
        if 'image_integrity_status' in local_var_params:
            query_params.append(('imageIntegrityStatus', local_var_params['image_integrity_status']))  # noqa: E501
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'image_series' in local_var_params:
            query_params.append(('imageSeries', local_var_params['image_series']))  # noqa: E501
        if 'image_name' in local_var_params:
            query_params.append(('imageName', local_var_params['image_name']))  # noqa: E501
        if 'is_tagged_golden' in local_var_params:
            query_params.append(('isTaggedGolden', local_var_params['is_tagged_golden']))  # noqa: E501
        if 'is_cco_recommended' in local_var_params:
            query_params.append(('isCCORecommended', local_var_params['is_cco_recommended']))  # noqa: E501
        if 'is_cco_latest' in local_var_params:
            query_params.append(('isCCOLatest', local_var_params['is_cco_latest']))  # noqa: E501
        if 'created_time' in local_var_params:
            query_params.append(('createdTime', local_var_params['created_time']))  # noqa: E501
        if 'image_size_greater_than' in local_var_params:
            query_params.append(('imageSizeGreaterThan', local_var_params['image_size_greater_than']))  # noqa: E501
        if 'image_size_lesser_than' in local_var_params:
            query_params.append(('imageSizeLesserThan', local_var_params['image_size_lesser_than']))  # noqa: E501
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
        if 'sort_order' in local_var_params:
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/image/importation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImageInfoListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_image_importation_source_file_post(self, **kwargs):  # noqa: E501
        """Import an image from local file system  # noqa: E501

        Imports an image to SWIM image repository from local file system. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_source_file_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_third_party: Third party Image check
        :param str third_party_vendor: Third Party Vendor
        :param str third_party_image_family: Third Party image family
        :param str third_party_application_type: Third Party Application Type
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_image_importation_source_file_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_image_importation_source_file_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_image_importation_source_file_post_with_http_info(self, **kwargs):  # noqa: E501
        """Import an image from local file system  # noqa: E501

        Imports an image to SWIM image repository from local file system. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_source_file_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_third_party: Third party Image check
        :param str third_party_vendor: Third Party Vendor
        :param str third_party_image_family: Third Party image family
        :param str third_party_application_type: Third Party Application Type
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['is_third_party', 'third_party_vendor', 'third_party_image_family', 'third_party_application_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_image_importation_source_file_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_third_party' in local_var_params:
            query_params.append(('isThirdParty', local_var_params['is_third_party']))  # noqa: E501
        if 'third_party_vendor' in local_var_params:
            query_params.append(('thirdPartyVendor', local_var_params['third_party_vendor']))  # noqa: E501
        if 'third_party_image_family' in local_var_params:
            query_params.append(('thirdPartyImageFamily', local_var_params['third_party_image_family']))  # noqa: E501
        if 'third_party_application_type' in local_var_params:
            query_params.append(('thirdPartyApplicationType', local_var_params['third_party_application_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/image/importation/source/file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskIdResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_image_importation_source_url_post(self, request_body, **kwargs):  # noqa: E501
        """Trigger now or schedule import of an image from a URL  # noqa: E501

        Imports an image to SWIM image repository, source is any ftp or http URL. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_source_url_post(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :param str schedule_at: Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional) 
        :param str schedule_desc: Custom Description (Optional)
        :param str schedule_origin: Originator of this call (Optional)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_image_importation_source_url_post_with_http_info(request_body, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_image_importation_source_url_post_with_http_info(request_body, **kwargs)  # noqa: E501
            return data

    def api_v1_image_importation_source_url_post_with_http_info(self, request_body, **kwargs):  # noqa: E501
        """Trigger now or schedule import of an image from a URL  # noqa: E501

        Imports an image to SWIM image repository, source is any ftp or http URL. The image files with extensions bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 are supported. Set siteUuid as -1 to tag as golden image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_image_importation_source_url_post_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[object] request_body: request (required)
        :param str schedule_at: Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional) 
        :param str schedule_desc: Custom Description (Optional)
        :param str schedule_origin: Originator of this call (Optional)
        :return: TaskIdResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['request_body', 'schedule_at', 'schedule_desc', 'schedule_origin']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_image_importation_source_url_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_body' is set
        if ('request_body' not in local_var_params or
                local_var_params['request_body'] is None):
            raise ValueError("Missing the required parameter `request_body` when calling `api_v1_image_importation_source_url_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'schedule_at' in local_var_params:
            query_params.append(('scheduleAt', local_var_params['schedule_at']))  # noqa: E501
        if 'schedule_desc' in local_var_params:
            query_params.append(('scheduleDesc', local_var_params['schedule_desc']))  # noqa: E501
        if 'schedule_origin' in local_var_params:
            query_params.append(('scheduleOrigin', local_var_params['schedule_origin']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/image/importation/source/url', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskIdResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
