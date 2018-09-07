# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dnac_api_client.api_client import ApiClient


class TaskApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_task_count_get(self, **kwargs):  # noqa: E501
        """Get task count  # noqa: E501

        This method is used to retrieve task count  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_count_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_time: This is the epoch start time from which tasks need to be fetched
        :param str end_time: This is the epoch end time upto which audit records need to be fetched
        :param str data: Fetch tasks that contains this data
        :param str error_code: Fetch tasks that have this error code
        :param str service_type: Fetch tasks with this service type
        :param str username: Fetch tasks with this username
        :param str progress: Fetch tasks that contains this progress
        :param str is_error: Fetch tasks ended as success or failure. Valid values: true, false
        :param str failure_reason: Fetch tasks that contains this failure reason
        :param str parent_id: Fetch tasks that have this parent Id
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v1_task_count_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_task_count_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_task_count_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get task count  # noqa: E501

        This method is used to retrieve task count  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_count_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_time: This is the epoch start time from which tasks need to be fetched
        :param str end_time: This is the epoch end time upto which audit records need to be fetched
        :param str data: Fetch tasks that contains this data
        :param str error_code: Fetch tasks that have this error code
        :param str service_type: Fetch tasks with this service type
        :param str username: Fetch tasks with this username
        :param str progress: Fetch tasks that contains this progress
        :param str is_error: Fetch tasks ended as success or failure. Valid values: true, false
        :param str failure_reason: Fetch tasks that contains this failure reason
        :param str parent_id: Fetch tasks that have this parent Id
        :return: CountResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'data', 'error_code', 'service_type', 'username', 'progress', 'is_error', 'failure_reason', 'parent_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_task_count_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'data' in params:
            query_params.append(('data', params['data']))  # noqa: E501
        if 'error_code' in params:
            query_params.append(('errorCode', params['error_code']))  # noqa: E501
        if 'service_type' in params:
            query_params.append(('serviceType', params['service_type']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'progress' in params:
            query_params.append(('progress', params['progress']))  # noqa: E501
        if 'is_error' in params:
            query_params.append(('isError', params['is_error']))  # noqa: E501
        if 'failure_reason' in params:
            query_params.append(('failureReason', params['failure_reason']))  # noqa: E501
        if 'parent_id' in params:
            query_params.append(('parentId', params['parent_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/task/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_task_get(self, **kwargs):  # noqa: E501
        """Get filtered tasks  # noqa: E501

        This method is used to retrieve task(s) based on various filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_time: This is the epoch start time from which tasks need to be fetched
        :param str end_time: This is the epoch end time upto which audit records need to be fetched
        :param str data: Fetch tasks that contains this data
        :param str error_code: Fetch tasks that have this error code
        :param str service_type: Fetch tasks with this service type
        :param str username: Fetch tasks with this username
        :param str progress: Fetch tasks that contains this progress
        :param str is_error: Fetch tasks ended as success or failure. Valid values: true, false
        :param str failure_reason: Fetch tasks that contains this failure reason
        :param str parent_id: Fetch tasks that have this parent Id
        :param str offset: offset
        :param str limit: limit
        :param str sort_by: Sort results by this field
        :param str order: Sort order - asc or dsc
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v1_task_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_task_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_task_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get filtered tasks  # noqa: E501

        This method is used to retrieve task(s) based on various filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_time: This is the epoch start time from which tasks need to be fetched
        :param str end_time: This is the epoch end time upto which audit records need to be fetched
        :param str data: Fetch tasks that contains this data
        :param str error_code: Fetch tasks that have this error code
        :param str service_type: Fetch tasks with this service type
        :param str username: Fetch tasks with this username
        :param str progress: Fetch tasks that contains this progress
        :param str is_error: Fetch tasks ended as success or failure. Valid values: true, false
        :param str failure_reason: Fetch tasks that contains this failure reason
        :param str parent_id: Fetch tasks that have this parent Id
        :param str offset: offset
        :param str limit: limit
        :param str sort_by: Sort results by this field
        :param str order: Sort order - asc or dsc
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'data', 'error_code', 'service_type', 'username', 'progress', 'is_error', 'failure_reason', 'parent_id', 'offset', 'limit', 'sort_by', 'order']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_task_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'data' in params:
            query_params.append(('data', params['data']))  # noqa: E501
        if 'error_code' in params:
            query_params.append(('errorCode', params['error_code']))  # noqa: E501
        if 'service_type' in params:
            query_params.append(('serviceType', params['service_type']))  # noqa: E501
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'progress' in params:
            query_params.append(('progress', params['progress']))  # noqa: E501
        if 'is_error' in params:
            query_params.append(('isError', params['is_error']))  # noqa: E501
        if 'failure_reason' in params:
            query_params.append(('failureReason', params['failure_reason']))  # noqa: E501
        if 'parent_id' in params:
            query_params.append(('parentId', params['parent_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/task', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDTOListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_task_operation_operation_id_offset_limit_get(self, operation_id, offset, limit, **kwargs):  # noqa: E501
        """getTaskByOperationId  # noqa: E501

        This method is used to find root tasks assoicated to an operationid   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_operation_operation_id_offset_limit_get(operation_id, offset, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str operation_id: operationId (required)
        :param int offset: Index, minimum value is 0 (required)
        :param int limit: The maximum value of {limit} supported is 500. <br/> Base 1 indexing for {limit}, minimum value is 1 (required)
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v1_task_operation_operation_id_offset_limit_get_with_http_info(operation_id, offset, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_task_operation_operation_id_offset_limit_get_with_http_info(operation_id, offset, limit, **kwargs)  # noqa: E501
            return data

    def api_v1_task_operation_operation_id_offset_limit_get_with_http_info(self, operation_id, offset, limit, **kwargs):  # noqa: E501
        """getTaskByOperationId  # noqa: E501

        This method is used to find root tasks assoicated to an operationid   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_operation_operation_id_offset_limit_get_with_http_info(operation_id, offset, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str operation_id: operationId (required)
        :param int offset: Index, minimum value is 0 (required)
        :param int limit: The maximum value of {limit} supported is 500. <br/> Base 1 indexing for {limit}, minimum value is 1 (required)
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['operation_id', 'offset', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_task_operation_operation_id_offset_limit_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'operation_id' is set
        if ('operation_id' not in params or
                params['operation_id'] is None):
            raise ValueError("Missing the required parameter `operation_id` when calling `api_v1_task_operation_operation_id_offset_limit_get`")  # noqa: E501
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `api_v1_task_operation_operation_id_offset_limit_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `api_v1_task_operation_operation_id_offset_limit_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'operation_id' in params:
            path_params['operationId'] = params['operation_id']  # noqa: E501
        if 'offset' in params:
            path_params['offset'] = params['offset']  # noqa: E501
        if 'limit' in params:
            path_params['limit'] = params['limit']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/task/operation/{operationId}/{offset}/{limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDTOListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_task_task_id_get(self, task_id, **kwargs):  # noqa: E501
        """getTruststoreFileCount  # noqa: E501

        This method is used to retrieve a task based on their id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_task_id_get(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: UUID of the Task (required)
        :return: TaskDTOResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v1_task_task_id_get_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_task_task_id_get_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def api_v1_task_task_id_get_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """getTruststoreFileCount  # noqa: E501

        This method is used to retrieve a task based on their id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_task_id_get_with_http_info(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: UUID of the Task (required)
        :return: TaskDTOResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_task_task_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `api_v1_task_task_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['taskId'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/task/{taskId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDTOResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_task_task_id_tree_get(self, task_id, **kwargs):  # noqa: E501
        """Get Task Tree  # noqa: E501

        This method is used to retrieve a task with its children tasks based on their id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_task_id_tree_get(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: UUID of the Task (required)
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v1_task_task_id_tree_get_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_task_task_id_tree_get_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def api_v1_task_task_id_tree_get_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Get Task Tree  # noqa: E501

        This method is used to retrieve a task with its children tasks based on their id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v1_task_task_id_tree_get_with_http_info(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: UUID of the Task (required)
        :return: TaskDTOListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_task_task_id_tree_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `api_v1_task_task_id_tree_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['taskId'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/task/{taskId}/tree', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDTOListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)