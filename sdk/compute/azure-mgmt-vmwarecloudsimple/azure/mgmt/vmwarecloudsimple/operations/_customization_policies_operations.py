# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CustomizationPoliciesOperations(object):
    """CustomizationPoliciesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2019-04-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-04-01"

        self.config = config

    def list(
            self, region_id, pc_name, guest_os_type=None, custom_headers=None, raw=False, **operation_config):
        """Implements get of customization policies list.

        Returns list of customization policies in region for private cloud.

        :param region_id: The region Id (westus, eastus)
        :type region_id: str
        :param pc_name: The private cloud name
        :type pc_name: str
        :param guest_os_type: If specified response will be filtered by guest
         os type. Possible values include: 'linux', 'windows', 'other'
        :type guest_os_type: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of CustomizationPolicy
        :rtype:
         ~azure.mgmt.vmwarecloudsimple.models.CustomizationPolicyPaged[~azure.mgmt.vmwarecloudsimple.models.CustomizationPolicy]
        :raises:
         :class:`CSRPErrorException<azure.mgmt.vmwarecloudsimple.models.CSRPErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'regionId': self._serialize.url("region_id", region_id, 'str'),
                    'pcName': self._serialize.url("pc_name", pc_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if guest_os_type is not None:
                    query_parameters['guestOSType'] = self._serialize.query("guest_os_type", guest_os_type, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.CSRPErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.CustomizationPolicyPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies'}

    def get(
            self, region_id, pc_name, customization_policy_name, custom_headers=None, raw=False, **operation_config):
        """Implements get of customization policy.

        Returns resource pool templates by its name.

        :param region_id: The region Id (westus, eastus)
        :type region_id: str
        :param pc_name: The private cloud name
        :type pc_name: str
        :param customization_policy_name: customization policy name
        :type customization_policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CustomizationPolicy or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.vmwarecloudsimple.models.CustomizationPolicy or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CSRPErrorException<azure.mgmt.vmwarecloudsimple.models.CSRPErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'regionId': self._serialize.url("region_id", region_id, 'str'),
            'pcName': self._serialize.url("pc_name", pc_name, 'str'),
            'customizationPolicyName': self._serialize.url("customization_policy_name", customization_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CSRPErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('CustomizationPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies/{customizationPolicyName}'}
