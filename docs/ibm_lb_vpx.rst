
ibm_lb_vpx -- Configure IBM Cloud 'ibm_lb_vpx' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  private_vlan_id (False, int, None)
    None


  speed (False, int, None)
    (Required for new resource)


  ip_count (False, int, None)
    (Required for new resource)


  public_vlan_id (False, int, None)
    None


  name (False, str, None)
    None


  public_subnet (False, str, None)
    None


  private_subnet (False, str, None)
    None


  management_ip_address (False, str, None)
    None


  version (False, str, None)
    (Required for new resource)


  datacenter (False, str, None)
    (Required for new resource)


  plan (False, str, None)
    (Required for new resource)


  vip_pool (False, list, None)
    None


  tags (False, list, None)
    None


  type (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

