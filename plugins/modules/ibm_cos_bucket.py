#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cos_bucket
short_description: Configure IBM Cloud 'ibm_cos_bucket' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cos_bucket' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    single_site_location:
        description:
            - None
        required: False
        type: str
    region_location:
        description:
            - None
        required: False
        type: str
    storage_class:
        description:
            - (Required for new resource) 
        required: False
        type: str
    bucket_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    resource_instance_id:
        description:
            - (Required for new resource) 
        required: False
        type: str
    cross_region_location:
        description:
            - None
        required: False
        type: str
    s3_endpoint_public:
        description:
            - Public endpoint for the COS bucket
        required: False
        type: str
    s3_endpoint_private:
        description:
            - Private endpoint for the COS bucket
        required: False
        type: str
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    key_protect:
        description:
            - CRN of the key you want to use data at rest encryption
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('storage_class', 'str'),
    ('bucket_name', 'str'),
    ('resource_instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'single_site_location',
    'region_location',
    'storage_class',
    'bucket_name',
    'resource_instance_id',
    'cross_region_location',
    's3_endpoint_public',
    's3_endpoint_private',
    'crn',
    'key_protect',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    single_site_location=dict(
        required=False,
        type='str'),
    region_location=dict(
        required=False,
        type='str'),
    storage_class=dict(
        required=False,
        type='str'),
    bucket_name=dict(
        required=False,
        type='str'),
    resource_instance_id=dict(
        required=False,
        type='str'),
    cross_region_location=dict(
        required=False,
        type='str'),
    s3_endpoint_public=dict(
        required=False,
        type='str'),
    s3_endpoint_private=dict(
        required=False,
        type='str'),
    crn=dict(
        required=False,
        type='str'),
    key_protect=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_cos_bucket',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.3',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
