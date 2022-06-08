# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.aws_cloud_region import AwsCloudRegion
from bitmovin_api_sdk.models.external_id_mode import ExternalIdMode
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class S3RoleBasedInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 bucket_name=None,
                 role_arn=None,
                 external_id=None,
                 external_id_mode=None,
                 cloud_region=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, ExternalIdMode, AwsCloudRegion) -> None
        super(S3RoleBasedInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._bucket_name = None
        self._role_arn = None
        self._external_id = None
        self._external_id_mode = None
        self._cloud_region = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if role_arn is not None:
            self.role_arn = role_arn
        if external_id is not None:
            self.external_id = external_id
        if external_id_mode is not None:
            self.external_id_mode = external_id_mode
        if cloud_region is not None:
            self.cloud_region = cloud_region

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(S3RoleBasedInput, self), 'openapi_types'):
            types = getattr(super(S3RoleBasedInput, self), 'openapi_types')

        types.update({
            'bucket_name': 'string_types',
            'role_arn': 'string_types',
            'external_id': 'string_types',
            'external_id_mode': 'ExternalIdMode',
            'cloud_region': 'AwsCloudRegion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(S3RoleBasedInput, self), 'attribute_map'):
            attributes = getattr(super(S3RoleBasedInput, self), 'attribute_map')

        attributes.update({
            'bucket_name': 'bucketName',
            'role_arn': 'roleArn',
            'external_id': 'externalId',
            'external_id_mode': 'externalIdMode',
            'cloud_region': 'cloudRegion'
        })
        return attributes

    @property
    def bucket_name(self):
        # type: () -> string_types
        """Gets the bucket_name of this S3RoleBasedInput.

        Amazon S3 bucket name (required)

        :return: The bucket_name of this S3RoleBasedInput.
        :rtype: string_types
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        # type: (string_types) -> None
        """Sets the bucket_name of this S3RoleBasedInput.

        Amazon S3 bucket name (required)

        :param bucket_name: The bucket_name of this S3RoleBasedInput.
        :type: string_types
        """

        if bucket_name is not None:
            if not isinstance(bucket_name, string_types):
                raise TypeError("Invalid type for `bucket_name`, type has to be `string_types`")

        self._bucket_name = bucket_name

    @property
    def role_arn(self):
        # type: () -> string_types
        """Gets the role_arn of this S3RoleBasedInput.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access.  This role has to be created by the owner of the account with the S3 bucket (i.e., you as a customer). For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\" is the Bitmovin user used for the access. The `Condition` is optional but we highly recommend it, see property `externalId` below for more information.  This setup allows Bitmovin assume the provided IAM role and to read data from your S3 bucket. Please note that the IAM role has to have read access on S3.  For more information about role creation please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console (required)

        :return: The role_arn of this S3RoleBasedInput.
        :rtype: string_types
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        # type: (string_types) -> None
        """Sets the role_arn of this S3RoleBasedInput.

        Amazon ARN of the IAM Role (Identity and Access Management Role) that will be assumed for S3 access.  This role has to be created by the owner of the account with the S3 bucket (i.e., you as a customer). For Bitmovin to be able to assume this role, the following has to be added to the trust policy of the role:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\" is the Bitmovin user used for the access. The `Condition` is optional but we highly recommend it, see property `externalId` below for more information.  This setup allows Bitmovin assume the provided IAM role and to read data from your S3 bucket. Please note that the IAM role has to have read access on S3.  For more information about role creation please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console (required)

        :param role_arn: The role_arn of this S3RoleBasedInput.
        :type: string_types
        """

        if role_arn is not None:
            if not isinstance(role_arn, string_types):
                raise TypeError("Invalid type for `role_arn`, type has to be `string_types`")

        self._role_arn = role_arn

    @property
    def external_id(self):
        # type: () -> string_types
        """Gets the external_id of this S3RoleBasedInput.

        External ID used together with the IAM role identified by `roleArn` to assume S3 access.  This ID is provided by the API if `externalIdMode` is set to `GLOBAL` or `GENERATED`. If present, it has to be added to the trust policy of the IAM role `roleArn` configured above, otherwise the API won't be able to read from the S3 bucket. An appropriate trust policy would look like this:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"{{externalId}}\" is the generated ID.  This property is optional but we recommend it as an additional security feature. We will use both the `roleArn` and the `externalId` to access your S3 data. If the Amazon IAM role has an external ID configured but it is not provided in the input configuration Bitmovin won't be able to read from the S3 bucket. Also if the external ID does not match the one configured for the IAM role on AWS side, Bitmovin won't be able to access the S3 bucket.  If you need to change the external ID that is used by your IAM role, you need to create a new input, and use the external ID provided by the API to update your IAM role.  For more information please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html 

        :return: The external_id of this S3RoleBasedInput.
        :rtype: string_types
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        # type: (string_types) -> None
        """Sets the external_id of this S3RoleBasedInput.

        External ID used together with the IAM role identified by `roleArn` to assume S3 access.  This ID is provided by the API if `externalIdMode` is set to `GLOBAL` or `GENERATED`. If present, it has to be added to the trust policy of the IAM role `roleArn` configured above, otherwise the API won't be able to read from the S3 bucket. An appropriate trust policy would look like this:  ``` {   \"Effect\": \"Allow\",   \"Principal\": {     \"AWS\": \"arn:aws:iam::630681592166:user/bitmovinCustomerS3Access\"   },   \"Action\": \"sts:AssumeRole\",   \"Condition\": {     \"StringEquals\": {       \"sts:ExternalId\": \"{{externalId}}\"     }   } } ```  where \"{{externalId}}\" is the generated ID.  This property is optional but we recommend it as an additional security feature. We will use both the `roleArn` and the `externalId` to access your S3 data. If the Amazon IAM role has an external ID configured but it is not provided in the input configuration Bitmovin won't be able to read from the S3 bucket. Also if the external ID does not match the one configured for the IAM role on AWS side, Bitmovin won't be able to access the S3 bucket.  If you need to change the external ID that is used by your IAM role, you need to create a new input, and use the external ID provided by the API to update your IAM role.  For more information please visit https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html 

        :param external_id: The external_id of this S3RoleBasedInput.
        :type: string_types
        """

        if external_id is not None:
            if not isinstance(external_id, string_types):
                raise TypeError("Invalid type for `external_id`, type has to be `string_types`")

        self._external_id = external_id

    @property
    def external_id_mode(self):
        # type: () -> ExternalIdMode
        """Gets the external_id_mode of this S3RoleBasedInput.


        :return: The external_id_mode of this S3RoleBasedInput.
        :rtype: ExternalIdMode
        """
        return self._external_id_mode

    @external_id_mode.setter
    def external_id_mode(self, external_id_mode):
        # type: (ExternalIdMode) -> None
        """Sets the external_id_mode of this S3RoleBasedInput.


        :param external_id_mode: The external_id_mode of this S3RoleBasedInput.
        :type: ExternalIdMode
        """

        if external_id_mode is not None:
            if not isinstance(external_id_mode, ExternalIdMode):
                raise TypeError("Invalid type for `external_id_mode`, type has to be `ExternalIdMode`")

        self._external_id_mode = external_id_mode

    @property
    def cloud_region(self):
        # type: () -> AwsCloudRegion
        """Gets the cloud_region of this S3RoleBasedInput.


        :return: The cloud_region of this S3RoleBasedInput.
        :rtype: AwsCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (AwsCloudRegion) -> None
        """Sets the cloud_region of this S3RoleBasedInput.


        :param cloud_region: The cloud_region of this S3RoleBasedInput.
        :type: AwsCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, AwsCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `AwsCloudRegion`")

        self._cloud_region = cloud_region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(S3RoleBasedInput, self), "to_dict"):
            result = super(S3RoleBasedInput, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, S3RoleBasedInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
