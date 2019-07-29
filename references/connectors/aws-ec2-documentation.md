---
id: aws-ec2-documentation
title: AWS EC2 (version v2.*.*)
sidebar_label: AWS EC2
layout: docs.mustache
---

## accept_reserved_instances_exchange_quote

Accepts the Convertible Reserved Instance exchange quote described in the GetReservedInstancesExchangeQuote call.

<details><summary>Parameters</summary>

### $body

Contains the parameters for accepting the quote.

**Type:** object

```json
{
  "TargetConfiguration" : [ {
    "InstanceCount" : "The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request",
    "OfferingId" : "The Convertible Reserved Instance offering ID."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ReservedInstanceId" : [ "string" ]
}
```

</details>

## accept_vpc_endpoint_connections

Accepts one or more interface VPC endpoint connection requests to your VPC endpoint service.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpcEndpointId" : [ "string" ],
  "ServiceId" : "The ID of the endpoint service."
}
```

</details>

## accept_vpc_peering_connection

Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the pending-acceptance state, and you must be the owner of the peer VPC. Use DescribeVpcPeeringConnections to view your outstanding VPC peering connection requests. 
For an inter-region VPC peering connection request, you must accept the VPC peering connection in the region of the accepter VPC.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcPeeringConnectionId" : "The ID of the VPC peering connection. You must specify this parameter in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## allocate_address

Allocates an Elastic IP address to your AWS account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different AWS account. 
[EC2-VPC] If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another AWS account. You cannot recover an Elastic IP address for EC2-Classic. To attempt to recover an Elastic IP address that you released, specify it in this operation. 
An Elastic IP address is for use either in the EC2-Classic platform or in a VPC. By default, you can allocate 5 Elastic IP addresses for EC2-Classic per region and 5 Elastic IP addresses for EC2-VPC per region. 
For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AllocateAddress.

**Type:** object

```json
{
  "Address" : "[EC2-VPC] The Elastic IP address to recover.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Domain" : "Set to vpc to allocate the address for use with instances in a VPC. \nDefault: The address is for use with instances in EC2-Classic."
}
```

</details>

## allocate_hosts

Allocates a Dedicated Host to your account. At a minimum, specify the instance size type, Availability Zone, and quantity of hosts to allocate.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AutoPlacement" : "This is enabled by default. This property allows instances to be automatically placed onto available Dedicated Hosts, when you are launching instances without specifying a host ID. \nDefault: Enabled",
  "AvailabilityZone" : "The Availability Zone for the Dedicated Hosts.",
  "Quantity" : "The number of Dedicated Hosts to allocate to your account with these parameters.",
  "TagSpecification" : [ {
    "Tag" : [ {
      "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
      "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
    } ],
    "resourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are fleet, dedicated-host, instance, snapshot, and volume. To tag a resource after it has been created, see CreateTags."
  } ],
  "InstanceType" : "Specify the instance type for which to configure your Dedicated Hosts. When you specify the instance type, that is the only instance type that you can launch onto that host.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide. "
}
```

</details>

## assign_ipv6_addresses

Assigns one or more IPv6 addresses to the specified network interface. You can specify one or more specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from within the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies per instance type. For information, see IP Addresses Per Network Interface Per Instance Type in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Ipv6AddressCount" : "The number of IPv6 addresses to assign to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.",
  "Ipv6Addresses" : [ "string" ],
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## assign_private_ip_addresses

Assigns one or more secondary private IP addresses to the specified network interface. You can specify one or more specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned within the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For information about instance types, see Instance Types in the Amazon Elastic Compute Cloud User Guide. For more information about Elastic IP addresses, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide. 
AssignPrivateIpAddresses is available only in EC2-VPC.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AssignPrivateIpAddresses.

**Type:** object

```json
{
  "AllowReassignment" : "Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.",
  "PrivateIpAddress" : [ "string" ],
  "SecondaryPrivateIpAddressCount" : "The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## associate_address

Associates an Elastic IP address with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account. 
An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide. 
[EC2-Classic, VPC in an EC2-VPC-only account] If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account. 
[VPC in an EC2-Classic account] If you don't specify a private IP address, the Elastic IP address is associated with the primary IP address. If the Elastic IP address is already associated with a different instance or a network interface, you get an error unless you allow reassociation. You cannot associate an Elastic IP address with an instance or network interface that has an existing Elastic IP address.  
This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the Elastic IP Addresses section of Amazon EC2 Pricing.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AssociateAddress.

**Type:** object

```json
{
  "PrivateIpAddress" : "[EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.",
  "AllowReassociation" : "[EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.",
  "PublicIp" : "The Elastic IP address. This is required for EC2-Classic.",
  "InstanceId" : "The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.",
  "AllocationId" : "[EC2-VPC] The allocation ID. This is required for EC2-VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : "[EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID."
}
```

</details>

## associate_dhcp_options

Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC. 
After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance. 
For more information, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DhcpOptionsId" : "The ID of the DHCP options set, or default to associate no DHCP options with the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## associate_iam_instance_profile

Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InstanceId" : "The ID of the instance.",
  "IamInstanceProfile" : {
    "name" : "The name of the instance profile.",
    "arn" : "The Amazon Resource Name (ARN) of the instance profile."
  }
}
```

</details>

## associate_route_table

Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table from the subnet later. A route table can be associated with multiple subnets. 
For more information, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "RouteTableId" : "The ID of the route table.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SubnetId" : "The ID of the subnet."
}
```

</details>

## associate_subnet_cidr_block

Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet. An IPv6 CIDR block must have a prefix length of /64.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "SubnetId" : "The ID of your subnet.",
  "Ipv6CidrBlock" : "The IPv6 CIDR block for your subnet. The subnet must have a /64 prefix length."
}
```

</details>

## associate_vpc_cidr_block

Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, or you can associate an Amazon-provided IPv6 CIDR block. The IPv6 CIDR block size is fixed at /56. 
For more information about associating CIDR blocks with your VPC and applicable restrictions, see VPC and Subnet Sizing in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "CidrBlock" : "An IPv4 CIDR block to associate with the VPC.",
  "AmazonProvidedIpv6CidrBlock" : "Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block."
}
```

</details>

## attach_classic_link_vpc

Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the running state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it. 
After you've linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again. 
Linking your instance to a VPC is sometimes referred to as attaching your instance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of a ClassicLink-enabled VPC.",
  "InstanceId" : "The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.",
  "SecurityGroupId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## attach_internet_gateway

Attaches an internet gateway to a VPC, enabling connectivity between the internet and the VPC. For more information about your VPC and internet gateway, see the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InternetGatewayId" : "The ID of the internet gateway.",
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## attach_network_interface

Attaches a network interface to an instance.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AttachNetworkInterface.

**Type:** object

```json
{
  "InstanceId" : "The ID of the instance.",
  "DeviceIndex" : "The index of the device for the network interface attachment.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## attach_volume

Attaches an EBS volume to a running or stopped instance and exposes it to the instance with the specified device name. 
Encrypted EBS volumes may only be attached to instances that support Amazon EBS encryption. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide. 
For a list of supported device names, see Attaching an EBS Volume to an Instance. Any device names that aren't reserved for instance store volumes can be used for EBS volumes. For more information, see Amazon EC2 Instance Store in the Amazon Elastic Compute Cloud User Guide. 
If a volume has an AWS Marketplace product code:  
 The volume can be attached only to a stopped instance.  
 AWS Marketplace product codes are copied from the volume to the instance.  
 You must be subscribed to the product.  
 The instance type and operating system of the instance must support the product. For example, you can't detach a volume from a Windows instance and attach it to a Linux instance.   
For more information about EBS volumes, see Attaching Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AttachVolume.

**Type:** object

```json
{
  "VolumeId" : "The ID of the EBS volume. The volume and instance must be within the same Availability Zone.",
  "InstanceId" : "The ID of the instance.",
  "Device" : "The device name (for example, /dev/sdh or xvdh).",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## attach_vpn_gateway

Attaches a virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time. 
For more information, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for AttachVpnGateway.

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "VpnGatewayId" : "The ID of the virtual private gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## authorize_security_group_egress

[EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC. Specifically, this action permits instances to send traffic to one or more destination IPv4 or IPv6 CIDR address ranges, or to one or more destination security groups for the same VPC. This action doesn't apply to security groups for use in EC2-Classic. For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide. For more information about security group limits, see Amazon VPC Limits. 
Each rule consists of the protocol (for example, TCP), plus either a CIDR range or a source group. For the TCP and UDP protocols, you must also specify the destination port or port range. For the ICMP protocol, you must also specify the ICMP type and code. You can use -1 for the type or code to mean all types or all codes. You can optionally specify a description for the rule. 
Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "CidrIp" : "Not supported. Use a set of IP permissions to specify the CIDR.",
  "FromPort" : "Not supported. Use a set of IP permissions to specify the port.",
  "ToPort" : "Not supported. Use a set of IP permissions to specify the port.",
  "SourceSecurityGroupName" : "Not supported. Use a set of IP permissions to specify a destination security group.",
  "SourceSecurityGroupOwnerId" : "Not supported. Use a set of IP permissions to specify a destination security group.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpProtocol" : "Not supported. Use a set of IP permissions to specify the protocol name or number.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group."
}
```

</details>

## authorize_security_group_ingress

Adds one or more ingress rules to a security group. 
Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur. 
[EC2-Classic] This action gives one or more IPv4 CIDR address ranges permission to access a security group in your account, or gives one or more security groups (called the source groups) permission to access a security group for your account. A source group can be for your own AWS account, or another. You can have up to 100 rules per group. 
[EC2-VPC] This action gives one or more IPv4 or IPv6 CIDR address ranges permission to access a security group in your VPC, or gives one or more other security groups (called the source groups) permission to access a security group for your VPC. The security groups must all be for the same VPC or a peer VPC in a VPC peering connection. For more information about VPC security group limits, see Amazon VPC Limits. 
You can optionally specify a description for the security group rule.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.",
  "CidrIp" : "The CIDR IPv4 address range. You can't specify this parameter when specifying a source security group.",
  "FromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. For the ICMP/ICMPv6 type number, use -1 to specify all types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
  "ToPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number. For the ICMP/ICMPv6 code number, use -1 to specify all codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
  "SourceSecurityGroupName" : "[EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead. For EC2-VPC, the source security group must be in the same VPC.",
  "SourceSecurityGroupOwnerId" : "[EC2-Classic] The AWS account ID for the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol and port range, use a set of IP permissions instead.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers). (VPC only) Use -1 to specify all protocols. If you specify -1, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For tcp, udp, and icmp, you must specify a port range. For protocol 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID."
}
```

</details>

## bundle_instance

Bundles an Amazon instance store-backed Windows instance. 
During bundling, only the root device volume (C:\) is bundled. Data on other instance store volumes is not preserved.  
This action is not applicable for Linux/Unix instances or Windows instances that are backed by Amazon EBS.

<details><summary>Parameters</summary>

### $body

Contains the parameters for BundleInstance.

**Type:** object

```json
{
  "Storage" : {
    "S3" : {
      "bucket" : "The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.",
      "uploadPolicySignature" : "The signature of the JSON document.",
      "prefix" : "The beginning of the file name of the AMI.",
      "AWSAccessKeyId" : "The access key ID of the owner of the bucket. Before you specify a value for your access key ID, review and follow the guidance in Best Practices for Managing AWS Access Keys.",
      "uploadPolicy" : "An Amazon S3 upload policy that gives Amazon EC2 permission to upload items into Amazon S3 on your behalf."
    }
  },
  "InstanceId" : "The ID of the instance to bundle. \nType: String \nDefault: None \nRequired: Yes",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## cancel_bundle_task

Cancels a bundling operation for an instance store-backed Windows instance.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelBundleTask.

**Type:** object

```json
{
  "BundleId" : "The ID of the bundle task.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## cancel_conversion_task

Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception. 
For more information, see Importing a Virtual Machine Using the Amazon EC2 CLI.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelConversionTask.

**Type:** object

```json
{
  "ConversionTaskId" : "The ID of the conversion task.",
  "ReasonMessage" : "The reason for canceling the conversion task.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## cancel_export_task

Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelExportTask.

**Type:** object

```json
{
  "ExportTaskId" : "The ID of the export task. This is the ID returned by CreateInstanceExportTask."
}
```

</details>

## cancel_import_task

Cancels an in-process import virtual machine or import snapshot task.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelImportTask.

**Type:** object

```json
{
  "CancelReason" : "The reason for canceling the task.",
  "ImportTaskId" : "The ID of the import image or import snapshot task to be canceled.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## cancel_reserved_instances_listing

Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace. 
For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelReservedInstancesListing.

**Type:** object

```json
{
  "ReservedInstancesListingId" : "The ID of the Reserved Instance listing."
}
```

</details>

## cancel_spot_fleet_requests

Cancels the specified Spot Fleet requests. 
After you cancel a Spot Fleet request, the Spot Fleet launches no new Spot Instances. You must specify whether the Spot Fleet should also terminate its Spot Instances. If you terminate the instances, the Spot Fleet request enters the cancelled_terminating state. Otherwise, the Spot Fleet request enters the cancelled_running state and the instances continue to run until they are interrupted or you terminate them manually.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelSpotFleetRequests.

**Type:** object

```json
{
  "SpotFleetRequestId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "TerminateInstances" : "Indicates whether to terminate instances for a Spot Fleet request if it is canceled successfully."
}
```

</details>

## cancel_spot_instance_requests

Cancels one or more Spot Instance requests.  
Canceling a Spot Instance request does not terminate running Spot Instances associated with the request.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CancelSpotInstanceRequests.

**Type:** object

```json
{
  "SpotInstanceRequestId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## confirm_product_instance

Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user's instance is eligible for support.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ConfirmProductInstance.

**Type:** object

```json
{
  "ProductCode" : "The product code. This must be a product code that you own.",
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## copy_fpga_image

Copies the specified Amazon FPGA Image (AFI) to the current region.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Description" : "The description for the new AFI.",
  "SourceFpgaImageId" : "The ID of the source AFI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency.",
  "SourceRegion" : "The region that contains the source AFI.",
  "Name" : "The name for the new AFI. The default is the name of the source AFI."
}
```

</details>

## copy_image

Initiates the copy of an AMI from the specified source region to the current region. You specify the destination region by using its endpoint when making the request. 
Copies of encrypted backing snapshots for the AMI are encrypted. Copies of unencrypted backing snapshots remain unencrypted, unless you set Encrypted during the copy operation. You cannot create an unencrypted copy of an encrypted backing snapshot. 
For more information about the prerequisites and limits when copying an AMI, see Copying an AMI in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CopyImage.

**Type:** object

```json
{
  "Description" : "A description for the new AMI in the destination region.",
  "KmsKeyId" : "An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  \nThe CMK identifier may be provided in any of the following formats:   \n Key ID  \n Key alias, in the form alias/ExampleAlias    \n ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.   \n ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.    \nAWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.  \nThe specified CMK must exist in the region that the snapshot is being copied to. ",
  "Encrypted" : "Specifies whether the destination snapshots of the copied image should be encrypted. You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK using KmsKeyId. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SourceRegion" : "The name of the region that contains the AMI to copy.",
  "SourceImageId" : "The ID of the AMI to copy.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide.",
  "Name" : "The name of the new AMI in the destination region."
}
```

</details>

## copy_snapshot

Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3. You can copy the snapshot within the same region or from one region to another. You can use the snapshot to create EBS volumes or Amazon Machine Images (AMIs). The snapshot is copied to the regional endpoint that you send the HTTP request to. 
Copies of encrypted EBS snapshots remain encrypted. Copies of unencrypted snapshots remain unencrypted, unless the Encrypted flag is specified during the snapshot copy operation. By default, encrypted snapshot copies use the default AWS Key Management Service (AWS KMS) customer master key (CMK); however, you can specify a non-default CMK with the KmsKeyId parameter. 
To copy an encrypted snapshot that has been shared from another account, you must have permissions for the CMK used to encrypt the snapshot. 
Snapshots created by copying another snapshot have an arbitrary volume ID that should not be used for any purpose. 
For more information, see Copying an Amazon EBS Snapshot in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CopySnapshot.

**Type:** object

```json
{
  "PresignedUrl" : "When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see Query Requests. \nThe PresignedUrl should use the snapshot source endpoint, the CopySnapshot action, and include the SourceRegion, SourceSnapshotId, and DestinationRegion parameters. The PresignedUrl must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in Authenticating Requests by Using Query Parameters (AWS Signature Version 4) in the Amazon Simple Storage Service API Reference. An invalid or improperly signed PresignedUrl will cause the copy operation to fail asynchronously, and the snapshot will move to an error state.",
  "Description" : "A description for the EBS snapshot.",
  "KmsKeyId" : "An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  \nThe CMK identifier may be provided in any of the following formats:   \n Key ID  \n Key alias  \n ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.   \n ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.    \nAWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail. ",
  "SourceSnapshotId" : "The ID of the EBS snapshot to copy.",
  "Encrypted" : "Specifies whether the destination snapshot should be encrypted. You can encrypt a copy of an unencrypted snapshot, but you cannot use it to create an unencrypted copy of an encrypted snapshot. Your default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK using KmsKeyId. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DestinationRegion" : "The destination region to use in the PresignedUrl parameter of a snapshot copy operation. This parameter is only valid for specifying the destination region in a PresignedUrl parameter, where it is required. \nThe snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, ec2.us-east-1.amazonaws.com). With the AWS CLI, this is specified using the --region parameter or the default region in your AWS configuration file.",
  "SourceRegion" : "The ID of the region that contains the snapshot to be copied."
}
```

</details>

## create_customer_gateway

Provides information to AWS about your VPN customer gateway device. The customer gateway is the appliance at your end of the VPN connection. (The device on the AWS side of the VPN connection is the virtual private gateway.) You must provide the Internet-routable IP address of the customer gateway's external interface. The IP address must be static and may be behind a device performing network address translation (NAT). 
For devices that use Border Gateway Protocol (BGP), you can also provide the device's BGP Autonomous System Number (ASN). You can use an existing ASN assigned to your network. If you don't have an ASN already, you can use a private ASN (in the 64512 - 65534 range).  
Amazon EC2 supports all 2-byte ASN numbers in the range of 1 - 65534, with the exception of 7224, which is reserved in the us-east-1 region, and 9059, which is reserved in the eu-west-1 region.  
For more information about VPN customer gateways, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.  
You cannot create more than one customer gateway with the same VPN type, IP address, and BGP ASN parameter values. If you run an identical request more than one time, the first request creates the customer gateway, and subsequent requests return information about the existing customer gateway. The subsequent requests do not create new customer gateway resources.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateCustomerGateway.

**Type:** object

```json
{
  "Type" : "The type of VPN connection that this customer gateway supports (ipsec.1).",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpAddress" : "The Internet-routable IP address for the customer gateway's outside interface. The address must be static.",
  "BgpAsn" : "For devices that support BGP, the customer gateway's BGP ASN. \nDefault: 65000"
}
```

</details>

## create_default_subnet

Creates a default subnet with a size /20 IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see Creating a Default Subnet in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AvailabilityZone" : "The Availability Zone in which to create the default subnet."
}
```

</details>

## create_default_vpc

Creates a default VPC with a size /16 IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see Default VPC and Default Subnets in the Amazon Virtual Private Cloud User Guide. You cannot specify the components of the default VPC yourself. 
If you deleted your previous default VPC, you can create a default VPC. You cannot have more than one default VPC per Region. 
If your account supports EC2-Classic, you cannot use this action to create a default VPC in a Region that supports EC2-Classic. If you want a default VPC in a Region that supports EC2-Classic, see "I really want a default VPC for my existing EC2 account. Is that possible?" in the Default VPCs FAQ.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_dhcp_options

Creates a set of DHCP options for your VPC. After creating the set, you must associate it with the VPC, causing all existing and new instances that you launch in the VPC to use this set of DHCP options. The following are the individual DHCP options you can specify. For more information about the options, see RFC 2132.  
  domain-name-servers - The IP addresses of up to four domain name servers, or AmazonProvidedDNS. The default DHCP option set specifies AmazonProvidedDNS. If specifying more than one domain name server, specify the IP addresses in a single parameter, separated by commas. ITo have your instance to receive a custom DNS hostname as specified in domain-name, you must set domain-name-servers to a custom DNS server.  
  domain-name - If you're using AmazonProvidedDNS in us-east-1, specify ec2.internal. If you're using AmazonProvidedDNS in another region, specify region.compute.internal (for example, ap-northeast-1.compute.internal). Otherwise, specify a domain name (for example, MyCompany.com). This value is used to complete unqualified DNS hostnames. Important: Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP options set is associated with a VPC that has instances with multiple operating systems, specify only one domain name.  
  ntp-servers - The IP addresses of up to four Network Time Protocol (NTP) servers.  
  netbios-name-servers - The IP addresses of up to four NetBIOS name servers.  
  netbios-node-type - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2 (broadcast and multicast are not currently supported). For more information about these node types, see RFC 2132.   
Your VPC automatically starts out with a set of DHCP options that includes only a DNS server that we provide (AmazonProvidedDNS). If you create a set of options, and if your VPC has an internet gateway, make sure to set the domain-name-servers option either to AmazonProvidedDNS or to a domain name server of your choice. For more information, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DhcpConfiguration" : [ {
    "Value" : [ "string" ],
    "key" : "string"
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_egress_only_internet_gateway

[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC for which to create the egress-only internet gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency."
}
```

</details>

## create_fleet

Launches an EC2 Fleet. 
You can create a single EC2 Fleet that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet. 
For more information, see Launching an EC2 Fleet in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TargetCapacitySpecification" : {
    "DefaultTargetCapacityType" : "The default TotalTargetCapacity, which is either Spot or On-Demand.",
    "TotalTargetCapacity" : "The number of units to request, filled using DefaultTargetCapacityType.",
    "OnDemandTargetCapacity" : "The number of On-Demand units to request.",
    "SpotTargetCapacity" : "The number of Spot units to request."
  },
  "Type" : "The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. If you request a certain target capacity, EC2 Fleet only places the required requests. It does not attempt to replenish instances if capacity is diminished, and does not submit requests in alternative capacity pools if capacity is unavailable. To maintain a certain target capacity, EC2 Fleet places the required requests to meet this target capacity. It also automatically replenishes any interrupted Spot Instances. Default: maintain.",
  "OnDemandOptions" : {
    "AllocationStrategy" : "The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify lowest-price, EC2 Fleet uses price to determine the order, launching the lowest price first. If you specify prioritized, EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first. If you do not specify a value, EC2 Fleet defaults to lowest-price."
  },
  "ExcessCapacityTerminationPolicy" : "Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.",
  "SpotOptions" : {
    "AllocationStrategy" : "Indicates how to allocate the target capacity across the Spot pools specified by the Spot Fleet request. The default is lowestPrice.",
    "InstanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
    "InstancePoolsToUseCount" : "The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot AllocationStrategy is set to lowest-price. EC2 Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ValidFrom" : "The start date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.",
  "ReplaceUnhealthyInstances" : "Indicates whether EC2 Fleet should replace unhealthy instances.",
  "LaunchTemplateConfigs" : [ {
    "LaunchTemplateSpecification" : {
      "LaunchTemplateName" : "The name of the launch template.",
      "Version" : "The version number of the launch template. ",
      "LaunchTemplateId" : "The ID of the launch template."
    },
    "Overrides" : [ {
      "WeightedCapacity" : "The number of units provided by the specified instance type.",
      "Priority" : "The priority for the launch template override. If AllocationStrategy is set to prioritized, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at 0. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority.",
      "AvailabilityZone" : "The Availability Zone in which to launch the instances.",
      "SubnetId" : "The ID of the subnet in which to launch the instances.",
      "InstanceType" : "The instance type.",
      "MaxPrice" : "The maximum price per unit hour that you are willing to pay for a Spot Instance."
    } ]
  } ],
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency.",
  "TagSpecification" : [ {
    "Tag" : [ {
      "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
      "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
    } ],
    "resourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are fleet, dedicated-host, instance, snapshot, and volume. To tag a resource after it has been created, see CreateTags."
  } ],
  "ValidUntil" : "The end date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. The default end date is 7 days from the current date.",
  "TerminateInstancesWithExpiration" : "Indicates whether running instances should be terminated when the EC2 Fleet expires."
}
```

</details>

## create_flow_logs

Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC.  
Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see Flow Log Records in the Amazon Virtual Private Cloud User Guide. 
When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket. 
For more information, see VPC Flow Logs in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ResourceType" : "The type of resource on which to create the flow log.",
  "LogDestination" : "Specifies the destination to which the flow log data is to be published. Flow log data can be published to an CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType. \nIf LogDestinationType is not specified or cloud-watch-logs, specify the Amazon Resource Name (ARN) of the CloudWatch Logs log group. \nIf LogDestinationType is s3, specify the ARN of the Amazon S3 bucket. You can also specify a subfolder in the bucket. To specify a subfolder in the bucket, use the following ARN format: bucket_ARN/subfolder_name/. For example, to specify a subfolder named my-logs in a bucket named my-bucket, use the following ARN: arn:aws:s3:::my-bucket/my-logs/. You cannot use AWSLogs as a subfolder name. This is a reserved term.",
  "LogGroupName" : "The name of the log group.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.",
  "DeliverLogsPermissionArn" : "The ARN for the IAM role that's used to post flow logs to a log group.",
  "LogDestinationType" : "Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3. To publish flow log data to CloudWatch Logs, specify cloud-watch-logs. To publish flow log data to Amazon S3, specify s3. \nDefault: cloud-watch-logs ",
  "TrafficType" : "The type of traffic to log."
}
```

</details>

## create_fpga_image

Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP). 
The create operation is asynchronous. To verify that the AFI is ready for use, check the output logs. 
An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on one or more FPGA-accelerated instances. For more information, see the AWS FPGA Hardware Development Kit.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LogsStorageLocation" : {
    "Bucket" : "The name of the S3 bucket.",
    "Key" : "The key."
  },
  "InputStorageLocation" : {
    "Bucket" : "The name of the S3 bucket.",
    "Key" : "The key."
  },
  "Description" : "A description for the AFI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency.",
  "Name" : "A name for the AFI."
}
```

</details>

## create_image

Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped. 
If you customized your instance with instance store volumes or EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes. 
For more information, see Creating Amazon EBS-Backed Linux AMIs in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateImage.

**Type:** object

```json
{
  "Description" : "A description for the new image.",
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "BlockDeviceMapping" : [ {
    "noDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
    "virtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nNVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
    "ebs" : {
      "volumeType" : "The volume type: gp2, io1, st1, sc1, or standard. \nDefault: standard ",
      "snapshotId" : "The ID of the snapshot.",
      "encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption.  \nIf you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.",
      "KmsKeyId" : "Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted. \nThis parameter is only supported on BlockDeviceMapping objects called by RunInstances, RequestSpotFleet, and RequestSpotInstances.",
      "iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
      "deleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination.",
      "volumeSize" : "The size of the volume, in GiB. \nConstraints: 1-16384 for General Purpose SSD (gp2), 4-16384 for Provisioned IOPS SSD (io1), 500-16384 for Throughput Optimized HDD (st1), 500-16384 for Cold HDD (sc1), and 1-1024 for Magnetic (standard) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size."
    },
    "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
  } ],
  "NoReboot" : "By default, Amazon EC2 attempts to shut down and reboot the instance before creating the image. If the 'No Reboot' option is set, Amazon EC2 doesn't shut down the instance before creating the image. When this option is used, file system integrity on the created image can't be guaranteed.",
  "Name" : "A name for the new image. \nConstraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)"
}
```

</details>

## create_instance_export_task

Exports a running or stopped instance to an S3 bucket. 
For information about the supported operating systems, image formats, and known limitations for the types of instances you can export, see Exporting an Instance as a VM Using VM Import/Export in the VM Import/Export User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateInstanceExportTask.

**Type:** object

```json
{
  "Description" : "A description for the conversion task or the resource being exported. The maximum length is 255 bytes.",
  "InstanceId" : "The ID of the instance.",
  "ExportToS3" : {
    "diskImageFormat" : "The format for the exported image.",
    "containerFormat" : "The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.",
    "s3Prefix" : "The image is written to a single object in the S3 bucket at the S3 key s3prefix + exportTaskId + '.' + diskImageFormat.",
    "s3Bucket" : "The S3 bucket for the destination image. The destination bucket must exist and grant WRITE and READ_ACP permissions to the AWS account vm-import-export@amazon.com."
  },
  "TargetEnvironment" : "The target virtualization environment."
}
```

</details>

## create_internet_gateway

Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using AttachInternetGateway. 
For more information about your VPC and internet gateway, see the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_key_pair

Creates a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#1 private key. If a key with the specified name already exists, Amazon EC2 returns an error. 
You can have up to five thousand key pairs per region. 
The key pair returned to you is available only in the region in which you create it. If you prefer, you can create your own key pair using a third-party tool and upload it to any region using ImportKeyPair. 
For more information, see Key Pairs in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "KeyName" : "A unique name for the key pair. \nConstraints: Up to 255 ASCII characters",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_launch_template

Creates a launch template. A launch template contains the parameters to launch an instance. When you launch an instance using RunInstances, you can specify a launch template instead of providing the launch parameters in the request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LaunchTemplateData" : {
    "UserData" : "The Base64-encoded user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows).",
    "InstanceInitiatedShutdownBehavior" : "Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown). \nDefault: stop ",
    "SecurityGroupId" : [ "string" ],
    "CpuOptions" : {
      "ThreadsPerCore" : "The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of 1. Otherwise, specify the default value of 2.",
      "CoreCount" : "The number of CPU cores for the instance."
    },
    "NetworkInterface" : [ {
      "Description" : "A description for the network interface.",
      "PrivateIpAddress" : "The primary private IPv4 address of the network interface.",
      "PrivateIpAddresses" : [ {
        "privateIpAddress" : "The private IPv4 addresses.",
        "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
      } ],
      "SecondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses to assign to a network interface.",
      "DeviceIndex" : "The device index for the network interface attachment.",
      "Ipv6AddressCount" : "The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.",
      "SecurityGroupId" : [ "string" ],
      "Ipv6Addresses" : [ {
        "Ipv6Address" : "The IPv6 address."
      } ],
      "SubnetId" : "The ID of the subnet for the network interface.",
      "AssociatePublicIpAddress" : "Associates a public IPv4 address with eth0 for a new network interface.",
      "NetworkInterfaceId" : "The ID of the network interface.",
      "DeleteOnTermination" : "Indicates whether the network interface is deleted when the instance is terminated."
    } ],
    "ElasticGpuSpecification" : [ {
      "Type" : "The type of Elastic GPU."
    } ],
    "IamInstanceProfile" : {
      "Arn" : "The Amazon Resource Name (ARN) of the instance profile.",
      "Name" : "The name of the instance profile."
    },
    "KernelId" : "The ID of the kernel.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User Provided Kernels in the Amazon Elastic Compute Cloud User Guide.",
    "TagSpecification" : [ {
      "ResourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are instance and volume. To tag a resource after it has been created, see CreateTags.",
      "Tag" : [ {
        "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
        "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
      } ]
    } ],
    "SecurityGroup" : [ "string" ],
    "EbsOptimized" : "Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.",
    "KeyName" : "The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair.  \nIf you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.",
    "DisableApiTermination" : "If set to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API. To change this attribute to false after launch, use ModifyInstanceAttribute.",
    "Placement" : {
      "GroupName" : "The name of the placement group for the instance.",
      "Tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware.",
      "SpreadDomain" : "Reserved for future use.",
      "AvailabilityZone" : "The Availability Zone for the instance.",
      "Affinity" : "The affinity setting for an instance on a Dedicated Host.",
      "HostId" : "The ID of the Dedicated Host for the instance."
    },
    "InstanceMarketOptions" : {
      "SpotOptions" : {
        "SpotInstanceType" : "The Spot Instance request type.",
        "InstanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
        "MaxPrice" : "The maximum hourly price you're willing to pay for the Spot Instances.",
        "BlockDurationMinutes" : "The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).",
        "ValidUntil" : "The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached. The default end date is 7 days from the current date."
      },
      "MarketType" : "The market type."
    },
    "ImageId" : "The ID of the AMI, which you can get by using DescribeImages.",
    "BlockDeviceMapping" : [ {
      "Ebs" : {
        "SnapshotId" : "The ID of the snapshot.",
        "VolumeType" : "The volume type.",
        "KmsKeyId" : "The ARN of the AWS Key Management Service (AWS KMS) CMK used for encryption.",
        "Encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can't specify an encryption value.",
        "Iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
        "VolumeSize" : "The size of the volume, in GiB. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.",
        "DeleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination."
      },
      "NoDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
      "VirtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.",
      "DeviceName" : "The device name (for example, /dev/sdh or xvdh)."
    } ],
    "InstanceType" : "The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide.",
    "RamDiskId" : "The ID of the RAM disk.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User Provided Kernels in the Amazon Elastic Compute Cloud User Guide.",
    "Monitoring" : {
      "Enabled" : "Specify true to enable detailed monitoring. Otherwise, basic monitoring is enabled."
    },
    "CreditSpecification" : {
      "CpuCredits" : "The credit option for CPU usage of a T2 or T3 instance. Valid values are standard and unlimited."
    }
  },
  "LaunchTemplateName" : "A name for the launch template.",
  "VersionDescription" : "A description for the first version of the launch template.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency."
}
```

</details>

## create_launch_template_version

Creates a new version for a launch template. You can specify an existing version of launch template from which to base the new version. 
Launch template versions are numbered in the order in which they are created. You cannot specify, change, or replace the numbering of launch template versions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LaunchTemplateData" : {
    "UserData" : "The Base64-encoded user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows).",
    "InstanceInitiatedShutdownBehavior" : "Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown). \nDefault: stop ",
    "SecurityGroupId" : [ "string" ],
    "CpuOptions" : {
      "ThreadsPerCore" : "The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of 1. Otherwise, specify the default value of 2.",
      "CoreCount" : "The number of CPU cores for the instance."
    },
    "NetworkInterface" : [ {
      "Description" : "A description for the network interface.",
      "PrivateIpAddress" : "The primary private IPv4 address of the network interface.",
      "PrivateIpAddresses" : [ {
        "privateIpAddress" : "The private IPv4 addresses.",
        "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
      } ],
      "SecondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses to assign to a network interface.",
      "DeviceIndex" : "The device index for the network interface attachment.",
      "Ipv6AddressCount" : "The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.",
      "SecurityGroupId" : [ "string" ],
      "Ipv6Addresses" : [ {
        "Ipv6Address" : "The IPv6 address."
      } ],
      "SubnetId" : "The ID of the subnet for the network interface.",
      "AssociatePublicIpAddress" : "Associates a public IPv4 address with eth0 for a new network interface.",
      "NetworkInterfaceId" : "The ID of the network interface.",
      "DeleteOnTermination" : "Indicates whether the network interface is deleted when the instance is terminated."
    } ],
    "ElasticGpuSpecification" : [ {
      "Type" : "The type of Elastic GPU."
    } ],
    "IamInstanceProfile" : {
      "Arn" : "The Amazon Resource Name (ARN) of the instance profile.",
      "Name" : "The name of the instance profile."
    },
    "KernelId" : "The ID of the kernel.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User Provided Kernels in the Amazon Elastic Compute Cloud User Guide.",
    "TagSpecification" : [ {
      "ResourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are instance and volume. To tag a resource after it has been created, see CreateTags.",
      "Tag" : [ {
        "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
        "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
      } ]
    } ],
    "SecurityGroup" : [ "string" ],
    "EbsOptimized" : "Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.",
    "KeyName" : "The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair.  \nIf you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.",
    "DisableApiTermination" : "If set to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API. To change this attribute to false after launch, use ModifyInstanceAttribute.",
    "Placement" : {
      "GroupName" : "The name of the placement group for the instance.",
      "Tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware.",
      "SpreadDomain" : "Reserved for future use.",
      "AvailabilityZone" : "The Availability Zone for the instance.",
      "Affinity" : "The affinity setting for an instance on a Dedicated Host.",
      "HostId" : "The ID of the Dedicated Host for the instance."
    },
    "InstanceMarketOptions" : {
      "SpotOptions" : {
        "SpotInstanceType" : "The Spot Instance request type.",
        "InstanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
        "MaxPrice" : "The maximum hourly price you're willing to pay for the Spot Instances.",
        "BlockDurationMinutes" : "The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).",
        "ValidUntil" : "The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached. The default end date is 7 days from the current date."
      },
      "MarketType" : "The market type."
    },
    "ImageId" : "The ID of the AMI, which you can get by using DescribeImages.",
    "BlockDeviceMapping" : [ {
      "Ebs" : {
        "SnapshotId" : "The ID of the snapshot.",
        "VolumeType" : "The volume type.",
        "KmsKeyId" : "The ARN of the AWS Key Management Service (AWS KMS) CMK used for encryption.",
        "Encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can't specify an encryption value.",
        "Iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
        "VolumeSize" : "The size of the volume, in GiB. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.",
        "DeleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination."
      },
      "NoDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
      "VirtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.",
      "DeviceName" : "The device name (for example, /dev/sdh or xvdh)."
    } ],
    "InstanceType" : "The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide.",
    "RamDiskId" : "The ID of the RAM disk.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User Provided Kernels in the Amazon Elastic Compute Cloud User Guide.",
    "Monitoring" : {
      "Enabled" : "Specify true to enable detailed monitoring. Otherwise, basic monitoring is enabled."
    },
    "CreditSpecification" : {
      "CpuCredits" : "The credit option for CPU usage of a T2 or T3 instance. Valid values are standard and unlimited."
    }
  },
  "LaunchTemplateName" : "The name of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "VersionDescription" : "A description for the version of the launch template.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SourceVersion" : "The version number of the launch template version on which to base the new version. The new version inherits the same launch parameters as the source version, except for parameters that you specify in LaunchTemplateData.",
  "LaunchTemplateId" : "The ID of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency."
}
```

</details>

## create_nat_gateway

Creates a NAT gateway in the specified public subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. Internet-bound traffic from a private subnet can be routed to the NAT gateway, therefore enabling instances in the private subnet to connect to the internet. For more information, see NAT Gateways in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AllocationId" : "The allocation ID of an Elastic IP address to associate with the NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.",
  "SubnetId" : "The subnet in which to create the NAT gateway.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency. \nConstraint: Maximum 64 ASCII characters."
}
```

</details>

## create_network_acl

Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC. 
For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_network_acl_entry

Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules. 
We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules. 
After you add an entry, you can't modify it; you must either replace it, or create an entry and delete the old one. 
For more information about network ACLs, see Network ACLs in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "PortRange" : {
    "from" : "The first port in the range.",
    "to" : "The last port in the range."
  },
  "NetworkAclId" : "The ID of the network ACL.",
  "RuleAction" : "Indicates whether to allow or deny the traffic that matches the rule.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "CidrBlock" : "The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24).",
  "Egress" : "Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).",
  "RuleNumber" : "The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number. \nConstraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.",
  "Ipv6CidrBlock" : "The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64).",
  "Protocol" : "The protocol. A value of -1 or all means all protocols. If you specify all, -1, or a protocol number other than 6 (tcp), 17 (udp), or 1 (icmp), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol 58 (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol 58 (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.",
  "Icmp" : {
    "code" : "The ICMP code. A value of -1 means all codes for the specified ICMP type.",
    "type" : "The ICMP type. A value of -1 means all types."
  }
}
```

</details>

## create_network_interface

Creates a network interface in the specified subnet. 
For more information about network interfaces, see Elastic Network Interfaces in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateNetworkInterface.

**Type:** object

```json
{
  "PrivateIpAddress" : "The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in privateIpAddresses as primary (only one IP address can be designated as primary).",
  "Description" : "A description for the network interface.",
  "SecondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses. \nThe number of IP addresses you can assign to a network interface varies by instance type. For more information, see IP Addresses Per ENI Per Instance Type in the Amazon Virtual Private Cloud User Guide.",
  "PrivateIpAddresses" : [ {
    "privateIpAddress" : "The private IPv4 addresses.",
    "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
  } ],
  "Ipv6AddressCount" : "The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses. If your subnet has the AssignIpv6AddressOnCreation attribute set to true, you can specify 0 to override this setting.",
  "SecurityGroupId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Ipv6Addresses" : [ {
    "ipv6Address" : "The IPv6 address."
  } ],
  "SubnetId" : "The ID of the subnet to associate with the network interface."
}
```

</details>

## create_network_interface_permission

Grants an AWS-authorized account permission to attach the specified network interface to an instance in their account. 
You can grant permission to a single AWS account only, and only one account at a time.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateNetworkInterfacePermission.

**Type:** object

```json
{
  "AwsService" : "The AWS service. Currently not supported.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Permission" : "The type of permission to grant.",
  "AwsAccountId" : "The AWS account ID.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## create_placement_group

Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group.  
A cluster placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A spread placement group places instances on distinct hardware. 
For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreatePlacementGroup.

**Type:** object

```json
{
  "GroupName" : "A name for the placement group. Must be unique within the scope of your account for the region. \nConstraints: Up to 255 ASCII characters",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Strategy" : "The placement strategy."
}
```

</details>

## create_reserved_instances_listing

Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the DescribeReservedInstances operation.  
Only Standard Reserved Instances with a capacity reservation can be sold in the Reserved Instance Marketplace. Convertible Reserved Instances and Standard Reserved Instances with a regional benefit cannot be sold.  
The Reserved Instance Marketplace matches sellers who want to resell Standard Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances. 
To sell your Standard Reserved Instances, you must first register as a seller in the Reserved Instance Marketplace. After completing the registration process, you can create a Reserved Instance Marketplace listing of some or all of your Standard Reserved Instances, and specify the upfront price to receive for them. Your Standard Reserved Instance listings then become available for purchase. To view the details of your Standard Reserved Instance listing, you can use the DescribeReservedInstancesListings operation. 
For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateReservedInstancesListing.

**Type:** object

```json
{
  "InstanceCount" : "The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.",
  "ReservedInstancesId" : "The ID of the active Standard Reserved Instance.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see Ensuring Idempotency.",
  "PriceSchedules" : [ {
    "price" : "The fixed price for the term.",
    "term" : "The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.",
    "currencyCode" : "The currency for transacting the Reserved Instance resale. At this time, the only supported currency is USD."
  } ]
}
```

</details>

## create_route

Creates a route in a route table within a VPC. 
You must specify one of the following targets: internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only internet gateway. 
When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address 192.0.2.3, and the route table includes the following two IPv4 routes:  
  192.0.2.0/24 (goes to some target A)  
  192.0.2.0/28 (goes to some target B)   
Both routes apply to the traffic destined for 192.0.2.3. However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic. 
For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DestinationIpv6CidrBlock" : "The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.",
  "VpcPeeringConnectionId" : "The ID of a VPC peering connection.",
  "RouteTableId" : "The ID of the route table for the route.",
  "InstanceId" : "The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.",
  "EgressOnlyInternetGatewayId" : "[IPv6 traffic only] The ID of an egress-only internet gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DestinationCidrBlock" : "The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match.",
  "GatewayId" : "The ID of an internet gateway or virtual private gateway attached to your VPC.",
  "NetworkInterfaceId" : "The ID of a network interface.",
  "NatGatewayId" : "[IPv4 traffic only] The ID of a NAT gateway."
}
```

</details>

## create_route_table

Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet. 
For more information, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_security_group

Creates a security group. 
A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide and Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide.  
EC2-Classic: You can have up to 500 security groups. 
EC2-VPC: You can create up to 500 security groups per VPC.  
When you create a security group, you specify a friendly name of your choice. You can have a security group for use in EC2-Classic with the same name as a security group for use in a VPC. However, you can't have two security groups for use in EC2-Classic with the same name or two security groups for use in a VPC with the same name. 
You have a default security group for use in EC2-Classic and a default security group for use in your VPC. If you don't specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other. 
You can add or remove rules from your security groups using AuthorizeSecurityGroupIngress, AuthorizeSecurityGroupEgress, RevokeSecurityGroupIngress, and RevokeSecurityGroupEgress.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "The name of the security group. \nConstraints: Up to 255 characters in length. Cannot start with sg-. \nConstraints for EC2-Classic: ASCII characters \nConstraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&amp;;{}!$*",
  "GroupDescription" : "A description for the security group. This is informational only. \nConstraints: Up to 255 characters in length \nConstraints for EC2-Classic: ASCII characters \nConstraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&amp;;{}!$*",
  "VpcId" : "[EC2-VPC] The ID of the VPC. Required for EC2-VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_snapshot

Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use snapshots for backups, to make copies of EBS volumes, and to save data before shutting down an instance. 
When a snapshot is created, any AWS Marketplace product codes that are associated with the source volume are propagated to the snapshot. 
You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your EBS volume at the time the snapshot command is issued; this may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the volume long enough to take a snapshot, your snapshot should be complete. However, if you cannot pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You may remount and use your volume while the snapshot status is pending. 
To create a snapshot for EBS volumes that serve as root devices, you should stop the instance before taking the snapshot. 
Snapshots that are taken from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. Your encrypted volumes and any associated snapshots always remain protected. 
You can tag your snapshots during creation. For more information, see Tagging Your Amazon EC2 Resources in the Amazon Elastic Compute Cloud User Guide. 
For more information, see Amazon Elastic Block Store and Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateSnapshot.

**Type:** object

```json
{
  "VolumeId" : "The ID of the EBS volume.",
  "Description" : "A description for the snapshot.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "TagSpecification" : [ {
    "Tag" : [ {
      "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
      "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
    } ],
    "resourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are fleet, dedicated-host, instance, snapshot, and volume. To tag a resource after it has been created, see CreateTags."
  } ]
}
```

</details>

## create_spot_datafeed_subscription

Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per AWS account. For more information, see Spot Instance Data Feed in the Amazon EC2 User Guide for Linux Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateSpotDatafeedSubscription.

**Type:** object

```json
{
  "Bucket" : "The Amazon S3 bucket in which to store the Spot Instance data feed.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Prefix" : "A prefix for the data feed file names."
}
```

</details>

## create_subnet

Creates a subnet in an existing VPC. 
When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet. After you create a subnet, you can't change its CIDR block. The size of the subnet's IPv4 CIDR block can be the same as a VPC's IPv4 CIDR block, or a subset of a VPC's IPv4 CIDR block. If you create more than one subnet in a VPC, the subnets' CIDR blocks must not overlap. The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). 
If you've associated an IPv6 CIDR block with your VPC, you can create a subnet with an IPv6 CIDR block that uses a /64 prefix length.   
AWS reserves both the first four and the last IPv4 address in each subnet's CIDR block. They're not available for use.  
If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle. 
If you launch an instance in a VPC using an Amazon EBS-backed AMI, the IP address doesn't change if you stop and restart the instance (unlike a similar instance launched outside a VPC, which gets a new IP address when restarted). It's therefore possible to have a subnet with no running instances (they're all stopped), but no remaining IP addresses available. 
For more information about subnets, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "CidrBlock" : "The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24.",
  "AvailabilityZone" : "The Availability Zone for the subnet. \nDefault: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.",
  "Ipv6CidrBlock" : "The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length."
}
```

</details>

## create_tags

Adds or overwrites one or more tags for the specified Amazon EC2 resource or resources. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource. 
For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide. For more information about creating IAM policies that control users' access to resources based on tags, see Supported Resource-Level Permissions for Amazon EC2 API Actions in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Tag" : [ {
    "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
    "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
  } ]
}
```

</details>

## create_volume

Creates an EBS volume that can be attached to an instance in the same Availability Zone. The volume is created in the regional endpoint that you send the HTTP request to. For more information see Regions and Endpoints. 
You can create a new empty volume or restore a volume from an EBS snapshot. Any AWS Marketplace product codes from the snapshot are propagated to the volume. 
You can create encrypted volumes with the Encrypted parameter. Encrypted volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are also automatically encrypted. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide. 
You can tag your volumes during creation. For more information, see Tagging Your Amazon EC2 Resources in the Amazon Elastic Compute Cloud User Guide. 
For more information, see Creating an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateVolume.

**Type:** object

```json
{
  "SnapshotId" : "The snapshot from which to create the volume.",
  "VolumeType" : "The volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes. \nDefaults: If no volume type is specified, the default is standard in us-east-1, eu-west-1, eu-central-1, us-west-2, us-west-1, sa-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, us-gov-west-1, and cn-north-1. In all other regions, EBS defaults to gp2.",
  "KmsKeyId" : "An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  \nThe CMK identifier may be provided in any of the following formats:   \n Key ID  \n Key alias  \n ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.   \n ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.    \nAWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail. ",
  "Size" : "The size of the volume, in GiBs. \nConstraints: 1-16384 for gp2, 4-16384 for io1, 500-16384 for st1, 500-16384 for sc1, and 1-1024 for standard. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.",
  "Encrypted" : "Specifies whether the volume should be encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or vice versa. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AvailabilityZone" : "The Availability Zone in which to create the volume. Use DescribeAvailabilityZones to list the Availability Zones that are currently available to you.",
  "Iops" : "The number of I/O operations per second (IOPS) to provision for the volume, with a maximum ratio of 50 IOPS/GiB. Range is 100 to 32000 IOPS for volumes in most regions. For exceptions, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nThis parameter is valid only for Provisioned IOPS SSD (io1) volumes.",
  "TagSpecification" : [ {
    "Tag" : [ {
      "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
      "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
    } ],
    "resourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are fleet, dedicated-host, instance, snapshot, and volume. To tag a resource after it has been created, see CreateTags."
  } ]
}
```

</details>

## create_vpc

Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). For more information about how large to make your VPC, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide. 
You can optionally request an Amazon-provided IPv6 CIDR block for the VPC. The IPv6 CIDR block uses a /56 prefix length, and is allocated from Amazon's pool of IPv6 addresses. You cannot choose the IPv6 range for your VPC. 
By default, each instance you launch in the VPC has the default DHCP options, which include only a default DNS server that we provide (AmazonProvidedDNS). For more information, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide. 
You can specify the instance tenancy value for the VPC when you create it. You can't change this value for the VPC after you create it. For more information, see Dedicated Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InstanceTenancy" : "The tenancy options for instances launched into the VPC. For default, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For dedicated, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.  \n Important: The host value cannot be used with this parameter. Use the default or dedicated values only. \nDefault: default ",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "CidrBlock" : "The IPv4 network range for the VPC, in CIDR notation. For example, 10.0.0.0/16.",
  "AmazonProvidedIpv6CidrBlock" : "Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block."
}
```

</details>

## create_vpc_endpoint

Creates a VPC endpoint for a specified service. An endpoint enables you to create a private connection between your VPC and the service. The service may be provided by AWS, an AWS Marketplace partner, or another AWS account. For more information, see VPC Endpoints in the Amazon Virtual Private Cloud User Guide. 
A gateway endpoint serves as a target for a route in your route table for traffic destined for the AWS service. You can specify an endpoint policy to attach to the endpoint that will control access to the service from your VPC. You can also specify the VPC route tables that use the endpoint. 
An interface endpoint is a network interface in your subnet that serves as an endpoint for communicating with the specified service. You can specify the subnets in which to create an endpoint, and the security groups to associate with the endpoint network interface. 
Use DescribeVpcEndpointServices to get a list of supported services.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateVpcEndpoint.

**Type:** object

```json
{
  "PrivateDnsEnabled" : "(Interface endpoint) Indicate whether to associate a private hosted zone with the specified VPC. The private hosted zone contains a record set for the default public DNS name for the service for the region (for example, kinesis.us-east-1.amazonaws.com) which resolves to the private IP addresses of the endpoint network interfaces in the VPC. This enables you to make requests to the default public DNS name for the service instead of the public DNS names that are automatically generated by the VPC endpoint service. \nTo use a private hosted zone, you must set the following VPC attributes to true: enableDnsHostnames and enableDnsSupport. Use ModifyVpcAttribute to set the VPC attributes. \nDefault: false ",
  "RouteTableId" : [ "string" ],
  "VpcId" : "The ID of the VPC in which the endpoint will be used.",
  "ServiceName" : "The service name. To get a list of available services, use the DescribeVpcEndpointServices request, or get the name from the service provider.",
  "SecurityGroupId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "PolicyDocument" : "(Gateway endpoint) A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format. If this parameter is not specified, we attach a default policy that allows full access to the service.",
  "VpcEndpointType" : "The type of endpoint. \nDefault: Gateway",
  "SubnetId" : [ "string" ],
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency."
}
```

</details>

## create_vpc_endpoint_connection_notification

Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see Create a Topic in the Amazon Simple Notification Service Developer Guide. 
You can create a connection notification for interface endpoints only.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConnectionEvents" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.",
  "VpcEndpointId" : "The ID of the endpoint. ",
  "ConnectionNotificationArn" : "The ARN of the SNS topic for the notifications.",
  "ServiceId" : "The ID of the endpoint service."
}
```

</details>

## create_vpc_endpoint_service_configuration

Creates a VPC endpoint service configuration to which service consumers (AWS accounts, IAM users, and IAM roles) can connect. Service consumers can create an interface VPC endpoint to connect to your service. 
To create an endpoint service configuration, you must first create a Network Load Balancer for your service. For more information, see VPC Endpoint Services in the Amazon Virtual Private Cloud User Guide. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NetworkLoadBalancerArn" : [ "string" ],
  "AcceptanceRequired" : "Indicate whether requests from service consumers to create an endpoint to your service must be accepted. To accept a request, use AcceptVpcEndpointConnections.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency."
}
```

</details>

## create_vpc_peering_connection

Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another AWS account and can be in a different Region to the requester VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks.  
Limitations and rules apply to a VPC peering connection. For more information, see the limitations section in the VPC Peering Guide.  
The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected. 
If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of failed.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the requester VPC. You must specify this parameter in the request.",
  "PeerVpcId" : "The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "PeerRegion" : "The region code for the accepter VPC, if the accepter VPC is located in a region other than the region in which you make the request. \nDefault: The region in which you make the request.",
  "PeerOwnerId" : "The AWS account ID of the owner of the accepter VPC. \nDefault: Your AWS account ID"
}
```

</details>

## create_vpn_connection

Creates a VPN connection between an existing virtual private gateway and a VPN customer gateway. The only supported connection type is ipsec.1. 
The response includes information that you need to give to your network administrator to configure your customer gateway.  
We strongly recommend that you use HTTPS when calling this operation because the response contains sensitive cryptographic information for configuring your customer gateway.  
If you decide to shut down your VPN connection for any reason and later create a new VPN connection, you must reconfigure your customer gateway with the new information returned from this call. 
This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error. 
For more information, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateVpnConnection.

**Type:** object

```json
{
  "Options" : {
    "TunnelOptions" : [ {
      "PreSharedKey" : "The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway. \nConstraints: Allowed characters are alphanumeric characters and ._. Must be between 8 and 64 characters in length and cannot start with zero (0).",
      "TunnelInsideCidr" : "The range of inside IP addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway.  \nConstraints: A size /30 CIDR block from the 169.254.0.0/16 range. The following CIDR blocks are reserved and cannot be used:  \n  169.254.0.0/30   \n  169.254.1.0/30   \n  169.254.2.0/30   \n  169.254.3.0/30   \n  169.254.4.0/30   \n  169.254.5.0/30   \n  169.254.169.252/30  "
    } ],
    "staticRoutesOnly" : "Indicate whether the VPN connection uses static routes only. If you are creating a VPN connection for a device that does not support BGP, you must specify true. Use CreateVpnConnectionRoute to create a static route. \nDefault: false "
  },
  "Type" : "The type of VPN connection (ipsec.1).",
  "CustomerGatewayId" : "The ID of the customer gateway.",
  "VpnGatewayId" : "The ID of the virtual private gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## create_vpn_connection_route

Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway. 
For more information about VPN connections, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateVpnConnectionRoute.

**Type:** object

```json
{
  "VpnConnectionId" : "The ID of the VPN connection.",
  "DestinationCidrBlock" : "The CIDR block associated with the local subnet of the customer network."
}
```

</details>

## create_vpn_gateway

Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself. 
For more information about virtual private gateways, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for CreateVpnGateway.

**Type:** object

```json
{
  "Type" : "The type of VPN connection this virtual private gateway supports.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AvailabilityZone" : "The Availability Zone for the virtual private gateway.",
  "AmazonSideAsn" : "A private Autonomous System Number (ASN) for the Amazon side of a BGP session. If you're using a 16-bit ASN, it must be in the 64512 to 65534 range. If you're using a 32-bit ASN, it must be in the 4200000000 to 4294967294 range. \nDefault: 64512"
}
```

</details>

## delete_customer_gateway

Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteCustomerGateway.

**Type:** object

```json
{
  "CustomerGatewayId" : "The ID of the customer gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_dhcp_options

Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DhcpOptionsId" : "The ID of the DHCP options set.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_egress_only_internet_gateway

Deletes an egress-only internet gateway.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "EgressOnlyInternetGatewayId" : "The ID of the egress-only internet gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_fleets

Deletes the specified EC2 Fleet. 
After you delete an EC2 Fleet, it launches no new instances. You must specify whether an EC2 Fleet should also terminate its instances. If you terminate the instances, the EC2 Fleet enters the deleted_terminating state. Otherwise, the EC2 Fleet enters the deleted_running state, and the instances continue to run until they are interrupted or you terminate them manually. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "FleetId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "TerminateInstances" : "Indicates whether to terminate instances for an EC2 Fleet if it is deleted successfully."
}
```

</details>

## delete_flow_logs

Deletes one or more flow logs.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "FlowLogId" : [ "string" ]
}
```

</details>

## delete_fpga_image

Deletes the specified Amazon FPGA Image (AFI).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "FpgaImageId" : "The ID of the AFI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_internet_gateway

Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InternetGatewayId" : "The ID of the internet gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_key_pair

Deletes the specified key pair, by removing the public key from Amazon EC2.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "KeyName" : "The name of the key pair.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_launch_template

Deletes a launch template. Deleting a launch template deletes all of its versions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LaunchTemplateName" : "The name of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "LaunchTemplateId" : "The ID of the launch template. You must specify either the launch template ID or launch template name in the request."
}
```

</details>

## delete_launch_template_versions

Deletes one or more versions of a launch template. You cannot delete the default version of a launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must delete the entire launch template using DeleteLaunchTemplate.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LaunchTemplateName" : "The name of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "LaunchTemplateVersion" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "LaunchTemplateId" : "The ID of the launch template. You must specify either the launch template ID or launch template name in the request."
}
```

</details>

## delete_nat_gateway

Deletes the specified NAT gateway. Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NatGatewayId" : "The ID of the NAT gateway."
}
```

</details>

## delete_network_acl

Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NetworkAclId" : "The ID of the network ACL.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_network_acl_entry

Deletes the specified ingress or egress entry (rule) from the specified network ACL.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NetworkAclId" : "The ID of the network ACL.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Egress" : "Indicates whether the rule is an egress rule.",
  "RuleNumber" : "The rule number of the entry to delete."
}
```

</details>

## delete_network_interface

Deletes the specified network interface. You must detach the network interface before you can delete it.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteNetworkInterface.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## delete_network_interface_permission

Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. However, you can force delete the permission, regardless of any attachment.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteNetworkInterfacePermission.

**Type:** object

```json
{
  "Force" : "Specify true to remove the permission even if the network interface is attached to an instance.",
  "NetworkInterfacePermissionId" : "The ID of the network interface permission.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_placement_group

Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeletePlacementGroup.

**Type:** object

```json
{
  "GroupName" : "The name of the placement group.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_route

Deletes the specified route from the specified route table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DestinationIpv6CidrBlock" : "The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.",
  "RouteTableId" : "The ID of the route table.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DestinationCidrBlock" : "The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly."
}
```

</details>

## delete_route_table

Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "RouteTableId" : "The ID of the route table.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_security_group

Deletes a security group. 
If you attempt to delete a security group that is associated with an instance, or is referenced by another security group, the operation fails with InvalidGroup.InUse in EC2-Classic or DependencyViolation in EC2-VPC.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "[EC2-Classic, default VPC] The name of the security group. You can specify either the security group name or the security group ID.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "GroupId" : "The ID of the security group. Required for a nondefault VPC."
}
```

</details>

## delete_snapshot

Deletes the specified snapshot. 
When you make periodic snapshots of a volume, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the volume. 
You cannot delete a snapshot of the root device of an EBS volume used by a registered AMI. You must first de-register the AMI before you can delete the snapshot. 
For more information, see Deleting an Amazon EBS Snapshot in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteSnapshot.

**Type:** object

```json
{
  "SnapshotId" : "The ID of the EBS snapshot.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_spot_datafeed_subscription

Deletes the data feed for Spot Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteSpotDatafeedSubscription.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_subnet

Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SubnetId" : "The ID of the subnet."
}
```

</details>

## delete_tags

Deletes the specified set of tags from the specified set of resources. 
To list the current tags, use DescribeTags. For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Tag" : [ {
    "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
    "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
  } ]
}
```

</details>

## delete_volume

Deletes the specified EBS volume. The volume must be in the available state (not attached to an instance). 
The volume can remain in the deleting state for several minutes. 
For more information, see Deleting an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteVolume.

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_vpc

Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except the default one), and so on.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_vpc_endpoint_connection_notifications

Deletes one or more VPC endpoint connection notifications.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConnectionNotificationId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_vpc_endpoint_service_configurations

Deletes one or more VPC endpoint service configurations in your account. Before you delete the endpoint service configuration, you must reject any Available or PendingAcceptance interface endpoint connections that are attached to the service.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ServiceId" : [ "string" ]
}
```

</details>

## delete_vpc_endpoints

Deletes one or more specified VPC endpoints. Deleting a gateway endpoint also deletes the endpoint routes in the route tables that were associated with the endpoint. Deleting an interface endpoint deletes the endpoint network interfaces.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteVpcEndpoints.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpcEndpointId" : [ "string" ]
}
```

</details>

## delete_vpc_peering_connection

Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the accepter VPC can delete the VPC peering connection if it's in the active state. The owner of the requester VPC can delete a VPC peering connection in the pending-acceptance state. You cannot delete a VPC peering connection that's in the failed state.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcPeeringConnectionId" : "The ID of the VPC peering connection.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## delete_vpn_connection

Deletes the specified VPN connection. 
If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting the VPN connection. If you believe that the tunnel credentials for your VPN connection have been compromised, you can delete the VPN connection and create a new one that has new keys, without needing to delete the VPC or virtual private gateway. If you create a new VPN connection, you must reconfigure the customer gateway using the new configuration information returned with the new VPN connection ID.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteVpnConnection.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpnConnectionId" : "The ID of the VPN connection."
}
```

</details>

## delete_vpn_connection_route

Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteVpnConnectionRoute.

**Type:** object

```json
{
  "VpnConnectionId" : "The ID of the VPN connection.",
  "DestinationCidrBlock" : "The CIDR block associated with the local subnet of the customer network."
}
```

</details>

## delete_vpn_gateway

Deletes the specified virtual private gateway. We recommend that before you delete a virtual private gateway, you detach it from the VPC and delete the VPN connection. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeleteVpnGateway.

**Type:** object

```json
{
  "VpnGatewayId" : "The ID of the virtual private gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## deregister_image

Deregisters the specified AMI. After you deregister an AMI, it can't be used to launch new instances; however, it doesn't affect any instances that you've already launched from the AMI. You'll continue to incur usage costs for those instances until you terminate them. 
When you deregister an Amazon EBS-backed AMI, it doesn't affect the snapshot that was created for the root volume of the instance during the AMI creation process. When you deregister an instance store-backed AMI, it doesn't affect the files that you uploaded to Amazon S3 when you created the AMI.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DeregisterImage.

**Type:** object

```json
{
  "ImageId" : "The ID of the AMI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_account_attributes

Describes attributes of your AWS account. The following are the supported account attributes:  
  supported-platforms: Indicates whether your account can launch instances into EC2-Classic and EC2-VPC, or only into EC2-VPC.  
  default-vpc: The ID of the default VPC for your account, or none.  
  max-instances: The maximum number of On-Demand Instances that you can run.  
  vpc-max-security-groups-per-interface: The maximum number of security groups that you can assign to a network interface.  
  max-elastic-ips: The maximum number of Elastic IP addresses that you can allocate for use with EC2-Classic.   
  vpc-max-elastic-ips: The maximum number of Elastic IP addresses that you can allocate for use with EC2-VPC. 

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeAccountAttributes.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AttributeName" : [ "string. Possible values: supported-platforms | default-vpc" ]
}
```

</details>

## describe_addresses

Describes one or more of your Elastic IP addresses. 
An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeAddresses.

**Type:** object

```json
{
  "PublicIp" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "AllocationId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_aggregate_id_format

Describes the longer ID format settings for all resource types in a specific region. This request is useful for performing a quick audit to determine whether a specific region is fully opted in for longer IDs (17-character IDs). 
This request only returns information about resource types that support longer IDs. 
The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_availability_zones

Describes one or more of the Availability Zones that are available to you. The results include zones only for the region you're currently using. If there is an event impacting an Availability Zone, you can use this request to view the state and any provided message for that Availability Zone. 
For more information, see Regions and Availability Zones in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeAvailabilityZones.

**Type:** object

```json
{
  "ZoneName" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_bundle_tasks

Describes one or more of your bundling tasks.  
Completed bundle tasks are listed for only a limited time. If your bundle task is no longer in the list, you can still register an AMI from it. Just use RegisterImage with the Amazon S3 bucket name and image manifest name you provided to the bundle task.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeBundleTasks.

**Type:** object

```json
{
  "BundleId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_classic_link_instances

Describes one or more of your linked EC2-Classic instances. This request only returns information about EC2-Classic instances linked to a VPC through ClassicLink. You cannot use this request to return information about other instances.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "InstanceId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000. If MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the instance IDs parameter in the same request. \nConstraint: If the value is greater than 1000, we return only 1000 items.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_conversion_tasks

Describes one or more of your conversion tasks. For more information, see the VM Import/Export User Guide. 
For information about the import manifest referenced by this API action, see VM Import Manifest.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeConversionTasks.

**Type:** object

```json
{
  "ConversionTaskId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_customer_gateways

Describes one or more of your VPN customer gateways. 
For more information about VPN customer gateways, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeCustomerGateways.

**Type:** object

```json
{
  "CustomerGatewayId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_dhcp_options

Describes one or more of your DHCP options sets. 
For more information, see DHCP Options Sets in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DhcpOptionsId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_egress_only_internet_gateways

Describes one or more of your egress-only internet gateways.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000. If MaxResults is given a value larger than 1000, only 1000 results are returned.",
  "EgressOnlyInternetGatewayId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_elastic_gpus

Describes the Elastic GPUs associated with your instances. For more information about Elastic GPUs, see Amazon EC2 Elastic GPUs.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ElasticGpuId" : [ "string" ],
  "NextToken" : "The token to request the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_export_tasks

Describes one or more of your export tasks.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeExportTasks.

**Type:** object

```json
{
  "ExportTaskId" : [ "string" ]
}
```

</details>

## describe_fleet_history

Describes the events for the specified EC2 Fleet during the specified time.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token for the next set of results.",
  "EventType" : "The type of events to describe. By default, all events are described.",
  "FleetId" : "The ID of the EC2 Fleet.",
  "MaxResults" : "The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.",
  "StartTime" : "The start date and time for the events, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_fleet_instances

Describes the running instances for the specified EC2 Fleet.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token for the next set of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "FleetId" : "The ID of the EC2 Fleet.",
  "MaxResults" : "The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_fleets

Describes one or more of your EC2 Fleet.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token for the next set of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "FleetId" : [ "string" ],
  "MaxResults" : "The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_flow_logs

Describes one or more flow logs. To view the information in your flow logs (the log streams for the network interfaces), you must use the CloudWatch Logs console or the CloudWatch Logs API.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000. If MaxResults is given a value larger than 1000, only 1000 results are returned. You cannot specify this parameter and the flow log IDs parameter in the same request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "FlowLogId" : [ "string" ]
}
```

</details>

## describe_fpga_image_attribute

Describes the specified attribute of the specified Amazon FPGA Image (AFI).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "FpgaImageId" : "The ID of the AFI.",
  "Attribute" : "The AFI attribute.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_fpga_images

Describes one or more available Amazon FPGA Images (AFIs). These include public AFIs, private AFIs that you own, and AFIs owned by other AWS accounts for which you have load permissions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "FpgaImageId" : [ "string" ],
  "Owner" : [ "string" ],
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_host_reservation_offerings

Describes the Dedicated Host reservations that are available to purchase. 
The results describe all the Dedicated Host reservation offerings, including offerings that may not match the instance family and region of your Dedicated Hosts. When purchasing an offering, ensure that the instance family and Region of the offering matches that of the Dedicated Hosts with which it is to be associated. For more information about supported instance types, see Dedicated Hosts Overview in the Amazon Elastic Compute Cloud User Guide. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to use to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500. If maxResults is given a larger value than 500, you receive an error.",
  "MaxDuration" : "This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.",
  "MinDuration" : "This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.",
  "OfferingId" : "The ID of the reservation offering."
}
```

</details>

## describe_host_reservations

Describes reservations that are associated with Dedicated Hosts in your account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to use to retrieve the next page of results.",
  "HostReservationIdSet" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500. If maxResults is given a larger value than 500, you receive an error."
}
```

</details>

## describe_hosts

Describes one or more of your Dedicated Hosts. 
The results describe only the Dedicated Hosts in the region you're currently using. All listed instances consume capacity on your Dedicated Host. Dedicated Hosts that have recently been released are listed with the state released.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned nextToken value. This value can be between 5 and 500. If maxResults is given a larger value than 500, you receive an error. You cannot specify this parameter and the host IDs parameter in the same request.",
  "HostId" : [ "string" ]
}
```

</details>

## describe_iam_instance_profile_associations

Describes your IAM instance profile associations.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "AssociationId" : [ "string" ]
}
```

</details>

## describe_id_format

Describes the ID format settings for your resources on a per-region basis, for example, to view which resource types are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. 
The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway.  
These settings apply to the IAM user who makes the request; they do not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user, unless they explicitly override the settings by running the ModifyIdFormat command. Resources created with longer IDs are visible to all IAM users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeIdFormat.

**Type:** object

```json
{
  "Resource" : "The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway "
}
```

</details>

## describe_identity_id_format

Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide.  
The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway.  
These settings apply to the principal specified in the request. They do not apply to the principal that makes the request.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeIdentityIdFormat.

**Type:** object

```json
{
  "PrincipalArn" : "The ARN of the principal, which can be an IAM role, IAM user, or the root user.",
  "Resource" : "The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway "
}
```

</details>

## describe_image_attribute

Describes the specified attribute of the specified AMI. You can specify only one attribute at a time.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeImageAttribute.

**Type:** object

```json
{
  "Attribute" : "The AMI attribute. \n Note: Depending on your account privileges, the blockDeviceMapping attribute may return a Client.AuthFailure error. If this happens, use DescribeImages to get information about the block device mapping for the AMI.",
  "ImageId" : "The ID of the AMI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_images

Describes one or more of the images (AMIs, AKIs, and ARIs) available to you. Images available to you include public images, private images that you own, and private images owned by other AWS accounts but for which you have explicit launch permissions.  
Deregistered images are included in the returned results for an unspecified interval after deregistration.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeImages.

**Type:** object

```json
{
  "Owner" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "ImageId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ExecutableBy" : [ "string" ]
}
```

</details>

## describe_import_image_tasks

Displays details about an import virtual machine or import snapshot tasks that are already created.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeImportImageTasks.

**Type:** object

```json
{
  "Filters" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "NextToken" : "A token that indicates the next page of results.",
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.",
  "ImportTaskId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_import_snapshot_tasks

Describes your import snapshot tasks.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeImportSnapshotTasks.

**Type:** object

```json
{
  "Filters" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "NextToken" : "A token that indicates the next page of results.",
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.",
  "ImportTaskId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_instance_attribute

Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Valid attribute values are: instanceType | kernel | ramdisk | userData | disableApiTermination | instanceInitiatedShutdownBehavior | rootDeviceName | blockDeviceMapping | productCodes | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport 

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeInstanceAttribute.

**Type:** object

```json
{
  "Attribute" : "The instance attribute. \nNote: The enaSupport attribute is not supported at this time.",
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_instance_credit_specifications

Describes the credit option for CPU usage of one or more of your T2 or T3 instances. The credit options are standard and unlimited. 
If you do not specify an instance ID, Amazon EC2 returns T2 and T3 instances with the unlimited credit option, as well as instances that were previously configured as T2 or T3 with the unlimited credit option. For example, if you resize a T2 instance, while it is configured as unlimited, to an M4 instance, Amazon EC2 returns the M4 instance. 
If you specify one or more instance IDs, Amazon EC2 returns the credit option (standard or unlimited) of those instances. If you specify an instance ID that is not valid, such as an instance that is not a T2 or T3 instance, an error is returned. 
Recently terminated instances might appear in the returned results. This interval is usually less than one hour. 
If an Availability Zone is experiencing a service disruption and you specify instance IDs in the affected zone, or do not specify any instance IDs at all, the call fails. If you specify only instance IDs in an unaffected zone, the call works normally. 
For more information, see Burstable Performance Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "InstanceId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_instance_status

Describes the status of one or more instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances. 
Instance status includes the following components:  
  Status checks - Amazon EC2 performs status checks on running EC2 instances to identify hardware and software issues. For more information, see Status Checks for Your Instances and Troubleshooting Instances with Failed Status Checks in the Amazon Elastic Compute Cloud User Guide.  
  Scheduled events - Amazon EC2 can schedule events (such as reboot, stop, or terminate) for your instances related to hardware issues, software updates, or system maintenance. For more information, see Scheduled Events for Your Instances in the Amazon Elastic Compute Cloud User Guide.  
  Instance state - You can manage your instances from the moment you launch them through their termination. For more information, see Instance Lifecycle in the Amazon Elastic Compute Cloud User Guide. 

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeInstanceStatus.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IncludeAllInstances" : "When true, includes the health status for all instances. When false, includes the health status for running instances only. \nDefault: false "
}
```

</details>

## describe_instances

Describes one or more of your instances. 
If you specify one or more instance IDs, Amazon EC2 returns information for those instances. If you do not specify instance IDs, Amazon EC2 returns information for all relevant instances. If you specify an instance ID that is not valid, an error is returned. If you specify an instance that you do not own, it is not included in the returned results. 
Recently terminated instances might appear in the returned results. This interval is usually less than one hour. 
If you describe instances in the rare case where an Availability Zone is experiencing a service disruption and you specify instance IDs that are in the affected zone, or do not specify any instance IDs at all, the call fails. If you describe instances and specify only instance IDs that are in an unaffected zone, the call works normally.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeInstances.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_internet_gateways

Describes one or more of your internet gateways.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InternetGatewayId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_key_pairs

Describes one or more of your key pairs. 
For more information about key pairs, see Key Pairs in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "KeyName" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_launch_template_versions

Describes one or more versions of a specified launch template. You can describe all versions, individual versions, or a range of versions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "MinVersion" : "The version number after which to describe launch template versions.",
  "LaunchTemplateName" : "The name of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "NextToken" : "The token to request the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 1 and 200.",
  "LaunchTemplateVersion" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "LaunchTemplateId" : "The ID of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "MaxVersion" : "The version number up to which to describe launch template versions."
}
```

</details>

## describe_launch_templates

Describes one or more launch templates.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LaunchTemplateName" : [ "string" ],
  "NextToken" : "The token to request the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 5 and 1000.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "LaunchTemplateId" : [ "string" ]
}
```

</details>

## describe_moving_addresses

Describes your Elastic IP addresses that are being moved to the EC2-VPC platform, or that are being restored to the EC2-Classic platform. This request does not return information about any other Elastic IP addresses in your account.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeMovingAddresses.

**Type:** object

```json
{
  "NextToken" : "The token to use to retrieve the next page of results.",
  "PublicIp" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value outside of this range, an error is returned. \nDefault: If no value is provided, the default is 1000.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_nat_gateways

Describes one or more of your NAT gateways.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "NatGatewayId" : [ "string" ]
}
```

</details>

## describe_network_acls

Describes one or more of your network ACLs. 
For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NetworkAclId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_network_interface_attribute

Describes a network interface attribute. You can specify only one attribute at a time.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeNetworkInterfaceAttribute.

**Type:** object

```json
{
  "Attribute" : "The attribute of the network interface. This parameter is required.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## describe_network_interface_permissions

Describes the permissions for your network interfaces. 

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeNetworkInterfacePermissions.

**Type:** object

```json
{
  "NextToken" : "The token to request the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "NetworkInterfacePermissionId" : [ "string" ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. If this parameter is not specified, up to 50 results are returned by default."
}
```

</details>

## describe_network_interfaces

Describes one or more of your network interfaces.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeNetworkInterfaces.

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : [ "string" ]
}
```

</details>

## describe_placement_groups

Describes one or more of your placement groups. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribePlacementGroups.

**Type:** object

```json
{
  "GroupName" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_prefix_lists

Describes available AWS services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service. A prefix list ID is required for creating an outbound security group rule that allows traffic from a VPC to access an AWS service through a gateway VPC endpoint. Currently, the services that support this action are Amazon S3 and Amazon DynamoDB.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token for the next set of items to return. (You received this token from a prior call.)",
  "PrefixListId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results. \nConstraint: If the value specified is greater than 1000, we return only 1000 items.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_principal_id_format

Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference.  
By default, all IAM roles and IAM users default to the same ID settings as the root user, unless they explicitly override the settings. This request is useful for identifying those IAM users and IAM roles that have overridden the default ID settings. 
The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to request the next page of results.",
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. ",
  "Resource" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_regions

Describes one or more regions that are currently available to you. 
For a list of the regions supported by Amazon EC2, see Regions and Endpoints.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeRegions.

**Type:** object

```json
{
  "RegionName" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_reserved_instances

Describes one or more of the Reserved Instances that you purchased. 
For more information about Reserved Instances, see Reserved Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeReservedInstances.

**Type:** object

```json
{
  "OfferingType" : "The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.",
  "ReservedInstancesId" : [ "string" ],
  "OfferingClass" : "Describes whether the Reserved Instance is Standard or Convertible.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_reserved_instances_listings

Describes your account's Reserved Instance listings in the Reserved Instance Marketplace. 
The Reserved Instance Marketplace matches sellers who want to resell Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances. 
As a seller, you choose to list some or all of your Reserved Instances, and you specify the upfront price to receive for them. Your Reserved Instances are then listed in the Reserved Instance Marketplace and are available for purchase. 
As a buyer, you specify the configuration of the Reserved Instance to purchase, and the Marketplace matches what you're searching for with what's available. The Marketplace first sells the lowest priced Reserved Instances to you, and continues to sell available Reserved Instance listings to you until your demand is met. You are charged based on the total price of all of the listings that you purchase. 
For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeReservedInstancesListings.

**Type:** object

```json
{
  "ReservedInstancesId" : "One or more Reserved Instance IDs.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "ReservedInstancesListingId" : "One or more Reserved Instance listing IDs."
}
```

</details>

## describe_reserved_instances_modifications

Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is specified, only information about the specific modification is returned. 
For more information, see Modifying Reserved Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeReservedInstancesModifications.

**Type:** object

```json
{
  "ReservedInstancesModificationId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ]
}
```

</details>

## describe_reserved_instances_offerings

Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not receive insufficient capacity errors, and you pay a lower usage rate than the rate charged for On-Demand instances for the actual time used. 
If you have listed your own Reserved Instances for sale in the Reserved Instance Marketplace, they will be excluded from these results. This is to ensure that you do not purchase your own Reserved Instances. 
For more information, see Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeReservedInstancesOfferings.

**Type:** object

```json
{
  "OfferingClass" : "The offering class of the Reserved Instance. Can be standard or convertible.",
  "MaxDuration" : "The maximum duration (in seconds) to filter when searching for offerings. \nDefault: 94608000 (3 years)",
  "IncludeMarketplace" : "Include Reserved Instance Marketplace offerings in the response.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "MinDuration" : "The minimum duration (in seconds) to filter when searching for offerings. \nDefault: 2592000 (1 month)",
  "AvailabilityZone" : "The Availability Zone in which the Reserved Instance can be used.",
  "OfferingType" : "The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type. ",
  "MaxInstanceCount" : "The maximum number of instances to filter when searching for offerings. \nDefault: 20",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "InstanceTenancy" : "The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of dedicated is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances). \n Important: The host value cannot be used with this parameter. Use the default or dedicated values only. \nDefault: default ",
  "ProductDescription" : "The Reserved Instance product platform description. Instances that include (Amazon VPC) in the description are for use with Amazon VPC.",
  "InstanceType" : "The instance type that the reservation will cover (for example, m1.small). For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide.",
  "ReservedInstancesOfferingId" : [ "string" ]
}
```

</details>

## describe_route_tables

Describes one or more of your route tables. 
Each subnet in your VPC must be associated with a route table. If a subnet is not explicitly associated with any route table, it is implicitly associated with the main route table. This command does not return the subnet ID for implicit associations. 
For more information, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "RouteTableId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_scheduled_instance_availability

Finds available schedules that meet the specified criteria. 
You can search for an available schedule no more than 3 months in advance. You must meet the minimum required duration of 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours. 
After you find a schedule that meets your needs, call PurchaseScheduledInstances to purchase Scheduled Instances with that schedule.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeScheduledInstanceAvailability.

**Type:** object

```json
{
  "Recurrence" : {
    "OccurrenceDay" : [ "integer" ],
    "Frequency" : "The frequency (Daily, Weekly, or Monthly).",
    "OccurrenceUnit" : "The unit for OccurrenceDays (DayOfWeek or DayOfMonth). This value is required for a monthly schedule. You can't specify DayOfWeek with a weekly schedule. You can't specify this value with a daily schedule.",
    "OccurrenceRelativeToEnd" : "Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.",
    "Interval" : "The interval quantity. The interval unit depends on the value of Frequency. For example, every 2 weeks or every 2 months."
  },
  "MaxSlotDurationInHours" : "The maximum available duration, in hours. This value must be greater than MinSlotDurationInHours and less than 1,720.",
  "NextToken" : "The token for the next set of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned NextToken value.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "FirstSlotStartTimeRange" : {
    "EarliestTime" : "The earliest date and time, in UTC, for the Scheduled Instance to start.",
    "LatestTime" : "The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future."
  },
  "MinSlotDurationInHours" : "The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours."
}
```

</details>

## describe_scheduled_instances

Describes one or more of your Scheduled Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeScheduledInstances.

**Type:** object

```json
{
  "SlotStartTimeRange" : {
    "EarliestTime" : "The earliest date and time, in UTC, for the Scheduled Instance to start.",
    "LatestTime" : "The latest date and time, in UTC, for the Scheduled Instance to start."
  },
  "NextToken" : "The token for the next set of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned NextToken value.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ScheduledInstanceId" : [ "string" ]
}
```

</details>

## describe_security_group_references

[EC2-VPC only] Describes the VPCs on the other side of a VPC peering connection that are referencing the security groups you've specified in this request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "GroupId" : [ "string" ]
}
```

</details>

## describe_security_groups

Describes one or more of your security groups. 
A security group is for use with instances either in the EC2-Classic platform or in a specific VPC. For more information, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide and Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "GroupId" : [ "string" ]
}
```

</details>

## describe_snapshot_attribute

Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time. 
For more information about EBS snapshots, see Amazon EBS Snapshots in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSnapshotAttribute.

**Type:** object

```json
{
  "SnapshotId" : "The ID of the EBS snapshot.",
  "Attribute" : "The snapshot attribute you would like to view.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_snapshots

Describes one or more of the EBS snapshots available to you. Available snapshots include public snapshots available for any AWS account to launch, private snapshots that you own, and private snapshots owned by another AWS account but for which you've been given explicit create volume permissions. 
The create volume permissions fall into the following categories:  
  public: The owner of the snapshot granted create volume permissions for the snapshot to the all group. All AWS accounts have create volume permissions for these snapshots.  
  explicit: The owner of the snapshot granted create volume permissions to a specific AWS account.  
  implicit: An AWS account has implicit create volume permissions for all snapshots it owns.   
The list of snapshots returned can be modified by specifying snapshot IDs, snapshot owners, or AWS accounts with create volume permissions. If no options are specified, Amazon EC2 returns all snapshots for which you have create volume permissions. 
If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned. If you specify an invalid snapshot ID, an error is returned. If you specify a snapshot ID for which you do not have access, it is not included in the returned results. 
If you specify one or more snapshot owners using the OwnerIds option, only snapshots from the specified owners and for which you have access are returned. The results can include the AWS account IDs of the specified owners, amazon for snapshots owned by Amazon, or self for snapshots that you own. 
If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned. You can specify AWS account IDs (if you own the snapshots), self for snapshots for which you own or have explicit permissions, or all for public snapshots. 
If you are describing a long list of snapshots, you can paginate the output to make the list more manageable. The MaxResults parameter sets the maximum number of results returned in a single page. If the list of results exceeds your MaxResults value, then that number of results is returned along with a NextToken value that can be passed to a subsequent DescribeSnapshots request to retrieve the remaining results. 
For more information about EBS snapshots, see Amazon EBS Snapshots in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSnapshots.

**Type:** object

```json
{
  "RestorableBy" : [ "string" ],
  "SnapshotId" : [ "string" ],
  "Owner" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_datafeed_subscription

Describes the data feed for Spot Instances. For more information, see Spot Instance Data Feed in the Amazon EC2 User Guide for Linux Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotDatafeedSubscription.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_fleet_instances

Describes the running instances for the specified Spot Fleet.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotFleetInstances.

**Type:** object

```json
{
  "SpotFleetRequestId" : "The ID of the Spot Fleet request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_fleet_request_history

Describes the events for the specified Spot Fleet request during the specified time. 
Spot Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last evaluated time and not miss a recorded event.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotFleetRequestHistory.

**Type:** object

```json
{
  "NextToken" : "The token for the next set of results.",
  "EventType" : "The type of events to describe. By default, all events are described.",
  "SpotFleetRequestId" : "The ID of the Spot Fleet request.",
  "MaxResults" : "The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.",
  "StartTime" : "The starting date and time for the events, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_fleet_requests

Describes your Spot Fleet requests. 
Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotFleetRequests.

**Type:** object

```json
{
  "SpotFleetRequestId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_instance_requests

Describes the specified Spot Instance requests. 
You can use DescribeSpotInstanceRequests to find a running Spot Instance by examining the response. If the status of the Spot Instance is fulfilled, the instance ID appears in the response and contains the identifier of the instance. Alternatively, you can use DescribeInstances with a filter to look for instances where the instance lifecycle is spot. 
Spot Instance requests are deleted four hours after they are canceled and their instances are terminated.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotInstanceRequests.

**Type:** object

```json
{
  "SpotInstanceRequestId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_spot_price_history

Describes the Spot price history. For more information, see Spot Instance Pricing History in the Amazon EC2 User Guide for Linux Instances. 
When you specify a start and end time, this operation returns the prices of the instance types within the time range that you specified and the time when the price changed. The price is valid within the time period that you specified; the response merely indicates the last time that the price changed.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeSpotPriceHistory.

**Type:** object

```json
{
  "EndTime" : "The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "StartTime" : "The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AvailabilityZone" : "Filters the results by the specified Availability Zone.",
  "ProductDescription" : [ "string" ],
  "InstanceType" : [ "string. Possible values: t1.micro | t2.nano | t2.micro | t2.small | t2.medium | t2.large | t2.xlarge | t2.2xlarge | t3.nano | t3.micro | t3.small | t3.medium | t3.large | t3.xlarge | t3.2xlarge | m1.small | m1.medium | m1.large | m1.xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m4.16xlarge | m2.xlarge | m2.2xlarge | m2.4xlarge | cr1.8xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5.metal | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | r5d.metal | x1.16xlarge | x1.32xlarge | x1e.xlarge | x1e.2xlarge | x1e.4xlarge | x1e.8xlarge | x1e.16xlarge | x1e.32xlarge | i2.xlarge | i2.2xlarge | i2.4xlarge | i2.8xlarge | i3.large | i3.xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.16xlarge | i3.metal | hi1.4xlarge | hs1.8xlarge | c1.medium | c1.xlarge | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.18xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.18xlarge | cc1.4xlarge | cc2.8xlarge | g2.2xlarge | g2.8xlarge | g3.4xlarge | g3.8xlarge | g3.16xlarge | g3s.xlarge | cg1.4xlarge | p2.xlarge | p2.8xlarge | p2.16xlarge | p3.2xlarge | p3.8xlarge | p3.16xlarge | d2.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge | f1.2xlarge | f1.4xlarge | f1.16xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.12xlarge | m5.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.12xlarge | m5d.24xlarge | h1.2xlarge | h1.4xlarge | h1.8xlarge | h1.16xlarge | z1d.large | z1d.xlarge | z1d.2xlarge | z1d.3xlarge | z1d.6xlarge | z1d.12xlarge | u-6tb1.metal | u-9tb1.metal | u-12tb1.metal" ]
}
```

</details>

## describe_stale_security_groups

[EC2-VPC only] Describes the stale security group rules for security groups in a specified VPC. Rules are stale when they reference a deleted security group in a peer VPC, or a security group in a peer VPC for which the VPC peering connection has been deleted.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "NextToken" : "The token for the next set of items to return. (You received this token from a prior call.)",
  "MaxResults" : "The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_subnets

Describes one or more of your subnets. 
For more information, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SubnetId" : [ "string" ]
}
```

</details>

## describe_tags

Describes one or more of the tags for your EC2 resources. 
For more information about tags, see Tagging Your Resources in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_volume_attribute

Describes the specified attribute of the specified volume. You can specify only one attribute at a time. 
For more information about EBS volumes, see Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVolumeAttribute.

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "Attribute" : "The attribute of the volume. This parameter is required.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_volume_status

Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volume's underlying host. If the volume's underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event. 
The DescribeVolumeStatus operation provides the following information about the specified volumes: 
 Status: Reflects the current status of the volume. The possible values are ok, impaired , warning, or insufficient-data. If all checks pass, the overall status of the volume is ok. If the check fails, the overall status is impaired. If the status is insufficient-data, then the checks may still be taking place on your volume at the time. We recommend that you retry the request. For more information about volume status, see Monitoring the Status of Your Volumes in the Amazon Elastic Compute Cloud User Guide. 
 Events: Reflect the cause of a volume status and may require you to take action. For example, if your volume returns an impaired status, then the volume event might be potential-data-inconsistency. This means that your volume has been affected by an issue with the underlying host, has all I/O operations disabled, and may have inconsistent data. 
 Actions: Reflect the actions you may have to take in response to an event. For example, if the status of the volume is impaired and the volume event shows potential-data-inconsistency, then the action shows enable-volume-io. This means that you may want to enable the I/O operations for the volume by calling the EnableVolumeIO action and then check the volume for data consistency. 
Volume status is based on the volume status checks, and does not reflect the volume state. Therefore, volume status does not indicate volumes in the error state (for example, when a volume is incapable of accepting I/O.)

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVolumeStatus.

**Type:** object

```json
{
  "VolumeId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_volumes

Describes the specified EBS volumes. 
If you are describing a long list of volumes, you can paginate the output to make the list more manageable. The MaxResults parameter sets the maximum number of results returned in a single page. If the list of results exceeds your MaxResults value, then that number of results is returned along with a NextToken value that can be passed to a subsequent DescribeVolumes request to retrieve the remaining results. 
For more information about EBS volumes, see Amazon EBS Volumes in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVolumes.

**Type:** object

```json
{
  "VolumeId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_volumes_modifications

Reports the current modification status of EBS volumes. 
Current-generation EBS volumes support modification of attributes including type, size, and (for io1 volumes) IOPS provisioning while either attached to or detached from an instance. Following an action from the API or the console to modify a volume, the status of the modification may be modifying, optimizing, completed, or failed. If a volume has never been modified, then certain elements of the returned VolumeModification objects are null.  
 You can also use CloudWatch Events to check the status of a modification to an EBS volume. For information about CloudWatch Events, see the Amazon CloudWatch Events User Guide. For more information, see Monitoring Volume Modifications" in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VolumeId" : [ "string" ],
  "NextToken" : "The nextToken value returned by a previous paginated request.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results (up to a limit of 500) to be returned in a paginated request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_attribute

Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "Attribute" : "The VPC attribute.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_classic_link

Describes the ClassicLink status of one or more VPCs.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_classic_link_dns_support

Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token for the next set of items to return. (You received this token from a prior call.)",
  "VpcIds" : [ "string" ],
  "MaxResults" : "The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results."
}
```

</details>

## describe_vpc_endpoint_connection_notifications

Describes the connection notifications for VPC endpoints and VPC endpoint services.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConnectionNotificationId" : "The ID of the notification.",
  "NextToken" : "The token to request the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the returned NextToken value.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_endpoint_connections

Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_endpoint_service_configurations

Describes the VPC endpoint service configurations in your account (your services).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ServiceId" : [ "string" ]
}
```

</details>

## describe_vpc_endpoint_service_permissions

Describes the principals (service consumers) that are permitted to discover your VPC endpoint service.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token to retrieve the next page of results.",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned NextToken value. This value can be between 5 and 1000; if MaxResults is given a value larger than 1000, only 1000 results are returned.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ServiceId" : "The ID of the service."
}
```

</details>

## describe_vpc_endpoint_services

Describes available services to which you can create a VPC endpoint.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVpcEndpointServices.

**Type:** object

```json
{
  "NextToken" : "The token for the next set of items to return. (You received this token from a prior call.)",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "ServiceName" : [ "string" ],
  "MaxResults" : "The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results. \nConstraint: If the value is greater than 1000, we return only 1000 items.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpc_endpoints

Describes one or more of your VPC endpoints.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVpcEndpoints.

**Type:** object

```json
{
  "NextToken" : "The token for the next set of items to return. (You received this token from a prior call.)",
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "MaxResults" : "The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results. \nConstraint: If the value is greater than 1000, we return only 1000 items.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpcEndpointId" : [ "string" ]
}
```

</details>

## describe_vpc_peering_connections

Describes one or more of your VPC peering connections.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcPeeringConnectionId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpcs

Describes one or more of your VPCs.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## describe_vpn_connections

Describes one or more of your VPN connections. 
For more information about VPN connections, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVpnConnections.

**Type:** object

```json
{
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpnConnectionId" : [ "string" ]
}
```

</details>

## describe_vpn_gateways

Describes one or more of your virtual private gateways. 
For more information about virtual private gateways, see AWS Managed VPN Connections in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DescribeVpnGateways.

**Type:** object

```json
{
  "VpnGatewayId" : [ "string" ],
  "Filter" : [ {
    "Value" : [ "string" ],
    "Name" : "The name of the filter. Filter names are case-sensitive."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## detach_classic_link_vpc

Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is automatically unlinked from a VPC when it's stopped.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC to which the instance is linked.",
  "InstanceId" : "The ID of the instance to unlink from the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## detach_internet_gateway

Detaches an internet gateway from a VPC, disabling connectivity between the internet and the VPC. The VPC must not contain any running instances with Elastic IP addresses or public IPv4 addresses.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InternetGatewayId" : "The ID of the internet gateway.",
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## detach_network_interface

Detaches a network interface from an instance.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DetachNetworkInterface.

**Type:** object

```json
{
  "Force" : "Specifies whether to force a detachment.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AttachmentId" : "The ID of the attachment."
}
```

</details>

## detach_volume

Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becoming stuck in the busy state while detaching. If this happens, detachment can be delayed indefinitely until you unmount the volume, force detachment, reboot the instance, or all three. If an EBS volume is the root device of an instance, it can't be detached while the instance is running. To detach the root volume, stop the instance first. 
When a volume with an AWS Marketplace product code is detached from an instance, the product code is no longer associated with the instance. 
For more information, see Detaching an Amazon EBS Volume in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DetachVolume.

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "InstanceId" : "The ID of the instance.",
  "Force" : "Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.",
  "Device" : "The device name.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## detach_vpn_gateway

Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described). 
You must wait for the attachment's state to switch to detached before you can delete the VPC or attach a different VPC to the virtual private gateway.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DetachVpnGateway.

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "VpnGatewayId" : "The ID of the virtual private gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## disable_vgw_route_propagation

Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DisableVgwRoutePropagation.

**Type:** object

```json
{
  "RouteTableId" : "The ID of the route table.",
  "GatewayId" : "The ID of the virtual private gateway."
}
```

</details>

## disable_vpc_classic_link

Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## disable_vpc_classic_link_dns_support

Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC."
}
```

</details>

## disassociate_address

Disassociates an Elastic IP address from the instance or network interface it's associated with. 
An Elastic IP address is for use in either the EC2-Classic platform or in a VPC. For more information, see Elastic IP Addresses in the Amazon Elastic Compute Cloud User Guide. 
This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error.

<details><summary>Parameters</summary>

### $body

Contains the parameters for DisassociateAddress.

**Type:** object

```json
{
  "PublicIp" : "[EC2-Classic] The Elastic IP address. Required for EC2-Classic.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AssociationId" : "[EC2-VPC] The association ID. Required for EC2-VPC."
}
```

</details>

## disassociate_iam_instance_profile

Disassociates an IAM instance profile from a running or stopped instance. 
Use DescribeIamInstanceProfileAssociations to get the association ID.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AssociationId" : "The ID of the IAM instance profile association."
}
```

</details>

## disassociate_route_table

Disassociates a subnet from a route table. 
After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC's main route table. For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AssociationId" : "The association ID representing the current association between the route table and subnet."
}
```

</details>

## disassociate_subnet_cidr_block

Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AssociationId" : "The association ID for the CIDR block."
}
```

</details>

## disassociate_vpc_cidr_block

Disassociates a CIDR block from a VPC. To disassociate the CIDR block, you must specify its association ID. You can get the association ID by using DescribeVpcs. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.  
You cannot disassociate the CIDR block with which you originally created the VPC (the primary CIDR block).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AssociationId" : "The association ID for the CIDR block."
}
```

</details>

## enable_vgw_route_propagation

Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.

<details><summary>Parameters</summary>

### $body

Contains the parameters for EnableVgwRoutePropagation.

**Type:** object

```json
{
  "RouteTableId" : "The ID of the route table.",
  "GatewayId" : "The ID of the virtual private gateway."
}
```

</details>

## enable_volume_i_o

Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.

<details><summary>Parameters</summary>

### $body

Contains the parameters for EnableVolumeIO.

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## enable_vpc_classic_link

Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable your VPC for ClassicLink if any of your VPC route tables have existing routes for address ranges within the 10.0.0.0/8 IP address range, excluding local routes for VPCs in the 10.0.0.0/16 and 10.1.0.0/16 IP address ranges. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## enable_vpc_classic_link_dns_support

Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC."
}
```

</details>

## get_console_output

Gets the console output for the specified instance. For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. For Windows instances, the instance console output includes the last three system event log errors. 
By default, the console output returns buffered information that was posted shortly after an instance transition state (start, stop, reboot, or terminate). This information is available for at least one hour after the most recent post. Only the most recent 64 KB of console output is available. 
You can optionally retrieve the latest serial console output at any time during the instance lifecycle. This option is supported on instance types that use the Nitro hypervisor. 
For more information, see Instance Console Output in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for GetConsoleOutput.

**Type:** object

```json
{
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Latest" : "When enabled, retrieves the latest console output for the instance. \nDefault: disabled (false)"
}
```

</details>

## get_console_screenshot

Retrieve a JPG-format screenshot of a running instance to help with troubleshooting. 
The returned content is Base64-encoded.

<details><summary>Parameters</summary>

### $body

Contains the parameters for the request.

**Type:** object

```json
{
  "WakeUp" : "When set to true, acts as keystroke input and wakes up an instance that's in standby or \"sleep\" mode.",
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## get_host_reservation_purchase_preview

Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. 
This is a preview of the PurchaseHostReservation action and does not result in the offering being purchased.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "HostIdSet" : [ "string" ],
  "OfferingId" : "The offering ID of the reservation."
}
```

</details>

## get_launch_template_data

Retrieves the configuration data of the specified instance. You can use this data to create a launch template.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## get_password_data

Retrieves the encrypted administrator password for a running Windows instance. 
The Windows password is generated at boot by the EC2Config service or EC2Launch scripts (Windows Server 2016 and later). This usually only happens the first time an instance is launched. For more information, see EC2Config and EC2Launch in the Amazon Elastic Compute Cloud User Guide. 
For the EC2Config service, the password is not generated for rebundled AMIs unless Ec2SetPassword is enabled before bundling. 
The password is encrypted using the key pair that you specified when you launched the instance. You must provide the corresponding key pair file. 
When you launch an instance, password generation and encryption may take a few minutes. If you try to retrieve the password before it's available, the output returns an empty string. We recommend that you wait up to 15 minutes after launching an instance before trying to retrieve the generated password.

<details><summary>Parameters</summary>

### $body

Contains the parameters for GetPasswordData.

**Type:** object

```json
{
  "InstanceId" : "The ID of the Windows instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## get_reserved_instances_exchange_quote

Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use AcceptReservedInstancesExchangeQuote to perform the exchange.

<details><summary>Parameters</summary>

### $body

Contains the parameters for GetReservedInstanceExchangeQuote.

**Type:** object

```json
{
  "TargetConfiguration" : [ {
    "InstanceCount" : "The number of instances the Covertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request",
    "OfferingId" : "The Convertible Reserved Instance offering ID."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ReservedInstanceId" : [ "string" ]
}
```

</details>

## import_image

Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI). For more information, see Importing a VM as an Image Using VM Import/Export in the VM Import/Export User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ImportImage.

**Type:** object

```json
{
  "RoleName" : "The name of the role to use when not using the default role, 'vmimport'.",
  "Description" : "A description string for the import image task.",
  "Platform" : "The operating system of the virtual machine. \nValid values: Windows | Linux ",
  "Architecture" : "The architecture of the virtual machine. \nValid values: i386 | x86_64 ",
  "Hypervisor" : "The target hypervisor platform. \nValid values: xen ",
  "ClientData" : {
    "Comment" : "A user-defined comment about the disk upload.",
    "UploadEnd" : "The time that the disk upload ends.",
    "UploadSize" : "The size of the uploaded disk image, in GiB.",
    "UploadStart" : "The time that the disk upload starts."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DiskContainer" : [ {
    "SnapshotId" : "The ID of the EBS snapshot to be used for importing the snapshot.",
    "Description" : "The description of the disk image.",
    "Format" : "The format of the disk image being imported. \nValid values: VHD | VMDK | OVA ",
    "UserBucket" : {
      "S3Bucket" : "The name of the S3 bucket where the disk image is located.",
      "S3Key" : "The file name of the disk image."
    },
    "Url" : "The URL to the Amazon S3-based disk image being imported. The URL can either be a https URL (https://..) or an Amazon S3 URL (s3://..)",
    "DeviceName" : "The block device mapping for the disk."
  } ],
  "ClientToken" : "The token to enable idempotency for VM import requests.",
  "LicenseType" : "The license type to be used for the Amazon Machine Image (AMI) after importing. \n Note: You may only use BYOL if you have existing licenses with rights to use these licenses in a third party cloud like AWS. For more information, see Prerequisites in the VM Import/Export User Guide. \nValid values: AWS | BYOL "
}
```

</details>

## import_instance

Creates an import instance task using metadata from the specified disk image. ImportInstance only supports single-volume VMs. To import multi-volume VMs, use ImportImage. For more information, see Importing a Virtual Machine Using the Amazon EC2 CLI. 
For information about the import manifest referenced by this API action, see VM Import Manifest.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ImportInstance.

**Type:** object

```json
{
  "Description" : "A description for the instance being imported.",
  "Platform" : "The instance operating system.",
  "LaunchSpecification" : {
    "GroupName" : [ "string" ],
    "subnetId" : "[EC2-VPC] The ID of the subnet in which to launch the instance.",
    "instanceInitiatedShutdownBehavior" : "Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).",
    "userData" : {
      "data" : "The user data. If you are using an AWS SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text."
    },
    "instanceType" : "The instance type. For more information about the instance types that you can import, see Instance Types in the VM Import/Export User Guide.",
    "additionalInfo" : "Reserved.",
    "placement" : {
      "groupName" : "The name of the placement group the instance is in.",
      "tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.",
      "hostId" : "The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the ImportInstance command.",
      "availabilityZone" : "The Availability Zone of the instance.",
      "spreadDomain" : "Reserved for future use.",
      "affinity" : "The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command."
    },
    "monitoring" : "Indicates whether monitoring is enabled.",
    "privateIpAddress" : "[EC2-VPC] An available IP address from the IP address range of the subnet.",
    "architecture" : "The architecture of the instance.",
    "GroupId" : [ "string" ]
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DiskImage" : [ {
    "Description" : "A description of the disk image.",
    "Volume" : {
      "size" : "The size of the volume, in GiB."
    },
    "Image" : {
      "importManifestUrl" : "A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the \"Query String Request Authentication Alternative\" section of the Authenticating REST Requests topic in the Amazon Simple Storage Service Developer Guide. \nFor information about the import manifest referenced by this API action, see VM Import Manifest.",
      "bytes" : "The size of the disk image, in GiB.",
      "format" : "The disk image format."
    }
  } ]
}
```

</details>

## import_key_pair

Imports the public key from an RSA key pair that you created with a third-party tool. Compare this with CreateKeyPair, in which AWS creates the key pair and gives the keys to you (AWS keeps a copy of the public key). With ImportKeyPair, you create the key pair and give AWS just the public key. The private key is never transferred between you and AWS. 
For more information about key pairs, see Key Pairs in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "KeyName" : "A unique name for the key pair.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "PublicKeyMaterial" : "The public key. For API calls, the text must be base64-encoded. For command line tools, base64 encoding is performed for you."
}
```

</details>

## import_snapshot

Imports a disk into an EBS snapshot.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ImportSnapshot.

**Type:** object

```json
{
  "RoleName" : "The name of the role to use when not using the default role, 'vmimport'.",
  "Description" : "The description string for the import snapshot task.",
  "ClientData" : {
    "Comment" : "A user-defined comment about the disk upload.",
    "UploadEnd" : "The time that the disk upload ends.",
    "UploadSize" : "The size of the uploaded disk image, in GiB.",
    "UploadStart" : "The time that the disk upload starts."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DiskContainer" : {
    "Description" : "The description of the disk image being imported.",
    "Format" : "The format of the disk image being imported. \nValid values: VHD | VMDK | OVA ",
    "UserBucket" : {
      "S3Bucket" : "The name of the S3 bucket where the disk image is located.",
      "S3Key" : "The file name of the disk image."
    },
    "Url" : "The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..)."
  },
  "ClientToken" : "Token to enable idempotency for VM import requests."
}
```

</details>

## import_volume

Creates an import volume task using metadata from the specified disk image.For more information, see Importing Disks to Amazon EBS. 
For information about the import manifest referenced by this API action, see VM Import Manifest.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ImportVolume.

**Type:** object

```json
{
  "Description" : "A description of the volume.",
  "Volume" : {
    "size" : "The size of the volume, in GiB."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AvailabilityZone" : "The Availability Zone for the resulting EBS volume.",
  "Image" : {
    "importManifestUrl" : "A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the \"Query String Request Authentication Alternative\" section of the Authenticating REST Requests topic in the Amazon Simple Storage Service Developer Guide. \nFor information about the import manifest referenced by this API action, see VM Import Manifest.",
    "bytes" : "The size of the disk image, in GiB.",
    "format" : "The disk image format."
  }
}
```

</details>

## modify_fleet

Modifies the specified EC2 Fleet. 
While the EC2 Fleet is being modified, it is in the modifying state.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TargetCapacitySpecification" : {
    "DefaultTargetCapacityType" : "The default TotalTargetCapacity, which is either Spot or On-Demand.",
    "TotalTargetCapacity" : "The number of units to request, filled using DefaultTargetCapacityType.",
    "OnDemandTargetCapacity" : "The number of On-Demand units to request.",
    "SpotTargetCapacity" : "The number of Spot units to request."
  },
  "ExcessCapacityTerminationPolicy" : "Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.",
  "FleetId" : "The ID of the EC2 Fleet.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## modify_fpga_image_attribute

Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "LoadPermission" : {
    "Add" : [ {
      "Group" : "The name of the group.",
      "UserId" : "The AWS account ID."
    } ],
    "Remove" : [ {
      "Group" : "The name of the group.",
      "UserId" : "The AWS account ID."
    } ]
  },
  "FpgaImageId" : "The ID of the AFI.",
  "Description" : "A description for the AFI.",
  "ProductCode" : [ "string" ],
  "Attribute" : "The name of the attribute.",
  "UserId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "OperationType" : "The operation type.",
  "Name" : "A name for the AFI.",
  "UserGroup" : [ "string" ]
}
```

</details>

## modify_hosts

Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, any instances that you launch with a tenancy of host but without a specific host ID are placed onto any available Dedicated Host in your account that has auto-placement enabled. When auto-placement is disabled, you need to provide a host ID to have the instance launch onto a specific host. If no host ID is provided, the instance is launched onto a suitable host with auto-placement enabled.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AutoPlacement" : "Specify whether to enable or disable auto-placement.",
  "HostId" : [ "string" ]
}
```

</details>

## modify_id_format

Modifies the ID format for the specified resource on a per-region basis. You can specify that resources should receive longer IDs (17-character IDs) when they are created. 
This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. 
This setting applies to the IAM user who makes the request; it does not apply to the entire AWS account. By default, an IAM user defaults to the same settings as the root user. If you're using this action as the root user, then these settings apply to the entire account, unless an IAM user explicitly overrides these settings for themselves. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide.  
Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.

<details><summary>Parameters</summary>

### $body

Contains the parameters of ModifyIdFormat.

**Type:** object

```json
{
  "Resource" : "The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. \nAlternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.",
  "UseLongIds" : "Indicate whether the resource should use longer IDs (17-character IDs)."
}
```

</details>

## modify_identity_id_format

Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources should receive longer IDs (17-character IDs) when they are created.  
This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway.  
For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide.  
This setting applies to the principal specified in the request; it does not apply to the principal that makes the request.  
Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant Describe command for the resource type.

<details><summary>Parameters</summary>

### $body

Contains the parameters of ModifyIdentityIdFormat.

**Type:** object

```json
{
  "PrincipalArn" : "The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for all IAM users, IAM roles, and the root user of the account.",
  "Resource" : "The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. \nAlternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.",
  "UseLongIds" : "Indicates whether the resource should use longer IDs (17-character IDs)"
}
```

</details>

## modify_image_attribute

Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time. You can use the Attribute parameter to specify the attribute or one of the following parameters: Description, LaunchPermission, or ProductCode. 
AWS Marketplace product codes cannot be modified. Images with an AWS Marketplace product code cannot be made public. 
To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyImageAttribute.

**Type:** object

```json
{
  "Description" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "ProductCode" : [ "string" ],
  "Attribute" : "The name of the attribute to modify. The valid values are description, launchPermission, and productCodes.",
  "UserId" : [ "string" ],
  "Value" : "The value of the attribute being modified. This parameter can be used only when the Attribute parameter is description or productCodes.",
  "ImageId" : "The ID of the AMI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "OperationType" : "The operation type. This parameter can be used only when the Attribute parameter is launchPermission.",
  "LaunchPermission" : {
    "Add" : [ {
      "userId" : "The AWS account ID.",
      "group" : "The name of the group."
    } ],
    "Remove" : [ {
      "userId" : "The AWS account ID.",
      "group" : "The name of the group."
    } ]
  },
  "UserGroup" : [ "string" ]
}
```

</details>

## modify_instance_attribute

Modifies the specified attribute of the specified instance. You can specify only one attribute at a time. 
 Note: Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance in a VPC can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the ModifyNetworkInterfaceAttribute action. 
To modify some attributes, the instance must be stopped. For more information, see Modifying Attributes of a Stopped Instance in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyInstanceAttribute.

**Type:** object

```json
{
  "Attribute" : "The name of the attribute.",
  "InstanceId" : "The ID of the instance.",
  "UserData" : {
    "value" : "blob"
  },
  "InstanceInitiatedShutdownBehavior" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "EnaSupport" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "SriovNetSupport" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "GroupId" : [ "string" ],
  "EbsOptimized" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "Ramdisk" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "DisableApiTermination" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "SourceDestCheck" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "Value" : "A new value for the attribute. Use only with the kernel, ramdisk, userData, disableApiTermination, or instanceInitiatedShutdownBehavior attribute.",
  "BlockDeviceMapping" : [ {
    "noDevice" : "suppress the specified device included in the block device mapping.",
    "ebs" : {
      "volumeId" : "The ID of the EBS volume.",
      "deleteOnTermination" : "Indicates whether the volume is deleted on instance termination."
    },
    "virtualName" : "The virtual device name.",
    "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
  } ],
  "InstanceType" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "Kernel" : {
    "value" : "The attribute value. The value is case-sensitive."
  }
}
```

</details>

## modify_instance_credit_specification

Modifies the credit option for CPU usage on a running or stopped T2 or T3 instance. The credit options are standard and unlimited. 
For more information, see Burstable Performance Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "InstanceCreditSpecification" : [ {
    "InstanceId" : "The ID of the instance.",
    "CpuCredits" : "The credit option for CPU usage of the instance. Valid values are standard and unlimited."
  } ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ClientToken" : "A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see Ensuring Idempotency."
}
```

</details>

## modify_instance_placement

Modifies the placement attributes for a specified instance. You can do the following:  
 Modify the affinity between an instance and a Dedicated Host. When affinity is set to host and the instance is not associated with a specific Dedicated Host, the next time the instance is launched, it is automatically associated with the host on which it lands. If the instance is restarted or rebooted, this relationship persists.  
 Change the Dedicated Host with which an instance is associated.  
 Change the instance tenancy of an instance from host to dedicated, or from dedicated to host.  
 Move an instance to or from a placement group.   
At least one attribute for affinity, host ID, tenancy, or placement group name must be specified in the request. Affinity and tenancy can be modified in the same request. 
To modify the host ID, tenancy, or placement group for an instance, the instance must be in the stopped state.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Tenancy" : "The tenancy for the instance.",
  "GroupName" : "The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of default. For cluster placement groups, the instance must have a tenancy of default or dedicated. \nTo remove an instance from a placement group, specify an empty string (\"\").",
  "InstanceId" : "The ID of the instance that you are modifying.",
  "Affinity" : "The affinity setting for the instance.",
  "HostId" : "The ID of the Dedicated Host with which to associate the instance."
}
```

</details>

## modify_launch_template

Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version is not specified.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "SetDefaultVersion" : "The version number of the launch template to set as the default version.",
  "LaunchTemplateName" : "The name of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "LaunchTemplateId" : "The ID of the launch template. You must specify either the launch template ID or launch template name in the request.",
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency."
}
```

</details>

## modify_network_interface_attribute

Modifies the specified network interface attribute. You can specify only one attribute at a time.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyNetworkInterfaceAttribute.

**Type:** object

```json
{
  "SourceDestCheck" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "Description" : {
    "value" : "The attribute value. The value is case-sensitive."
  },
  "SecurityGroupId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Attachment" : {
    "attachmentId" : "The ID of the network interface attachment.",
    "deleteOnTermination" : "Indicates whether the network interface is deleted when the instance is terminated."
  },
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## modify_reserved_instances

Modifies the Availability Zone, instance count, instance type, or network platform (EC2-Classic or EC2-VPC) of your Reserved Instances. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type. 
For more information, see Modifying Reserved Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyReservedInstances.

**Type:** object

```json
{
  "ReservedInstancesId" : [ "string" ],
  "ReservedInstancesConfigurationSetItemType" : [ {
    "instanceCount" : "The number of modified Reserved Instances.",
    "instanceType" : "The instance type for the modified Reserved Instances.",
    "scope" : "Whether the Reserved Instance is applied to instances in a region or instances in a specific Availability Zone.",
    "availabilityZone" : "The Availability Zone for the modified Reserved Instances.",
    "platform" : "The network platform of the modified Reserved Instances, which is either EC2-Classic or EC2-VPC."
  } ],
  "ClientToken" : "A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see Ensuring Idempotency."
}
```

</details>

## modify_snapshot_attribute

Adds or removes permission settings for the specified snapshot. You may add or remove specified AWS account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single API call. If you need to both add and remove account IDs for a snapshot, you must use multiple API calls. 
Encrypted snapshots and snapshots with AWS Marketplace product codes cannot be made public. Snapshots encrypted with your default CMK cannot be shared with other accounts. 
For more information about modifying snapshot permissions, see Sharing Snapshots in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifySnapshotAttribute.

**Type:** object

```json
{
  "SnapshotId" : "The ID of the snapshot.",
  "CreateVolumePermission" : {
    "Add" : [ {
      "userId" : "The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.",
      "group" : "The specific group that is to be added or removed from a volume's list of create volume permissions."
    } ],
    "Remove" : [ {
      "userId" : "The specific AWS account ID that is to be added or removed from a volume's list of create volume permissions.",
      "group" : "The specific group that is to be added or removed from a volume's list of create volume permissions."
    } ]
  },
  "Attribute" : "The snapshot attribute to modify. Only volume creation permissions can be modified.",
  "UserId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "OperationType" : "The type of operation to perform to the attribute.",
  "UserGroup" : [ "string" ]
}
```

</details>

## modify_spot_fleet_request

Modifies the specified Spot Fleet request. 
While the Spot Fleet request is being modified, it is in the modifying state. 
To scale up your Spot Fleet, increase its target capacity. The Spot Fleet launches the additional Spot Instances according to the allocation strategy for the Spot Fleet request. If the allocation strategy is lowestPrice, the Spot Fleet launches instances using the Spot pool with the lowest price. If the allocation strategy is diversified, the Spot Fleet distributes the instances across the Spot pools. 
To scale down your Spot Fleet, decrease its target capacity. First, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is lowestPrice, the Spot Fleet terminates the instances with the highest price per unit. If the allocation strategy is diversified, the Spot Fleet terminates instances across the Spot pools. Alternatively, you can request that the Spot Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually. 
If you are finished with your Spot Fleet for now, but will use it again later, you can set the target capacity to 0.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifySpotFleetRequest.

**Type:** object

```json
{
  "ExcessCapacityTerminationPolicy" : "Indicates whether running Spot Instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet.",
  "SpotFleetRequestId" : "The ID of the Spot Fleet request.",
  "TargetCapacity" : "The size of the fleet."
}
```

</details>

## modify_subnet_attribute

Modifies a subnet attribute. You can only modify one attribute at a time.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AssignIpv6AddressOnCreation" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "MapPublicIpOnLaunch" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "SubnetId" : "The ID of the subnet."
}
```

</details>

## modify_volume

You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you may be able to apply these changes without stopping the instance or detaching the volume from it. For more information about modifying an EBS volume running Linux, see Modifying the Size, IOPS, or Type of an EBS Volume on Linux. For more information about modifying an EBS volume running Windows, see Modifying the Size, IOPS, or Type of an EBS Volume on Windows.  
 When you complete a resize operation on your volume, you need to extend the volume's file-system size to take advantage of the new storage capacity. For information about extending a Linux file system, see Extending a Linux File System. For information about extending a Windows file system, see Extending a Windows File System.  
 You can use CloudWatch Events to check the status of a modification to an EBS volume. For information about CloudWatch Events, see the Amazon CloudWatch Events User Guide. You can also track the status of a modification using the DescribeVolumesModifications API. For information about tracking status changes using either method, see Monitoring Volume Modifications.  
With previous-generation instance types, resizing an EBS volume may require detaching and reattaching the volume or stopping and restarting the instance. For more information, see Modifying the Size, IOPS, or Type of an EBS Volume on Linux and Modifying the Size, IOPS, or Type of an EBS Volume on Windows. 
If you reach the maximum volume modification rate per volume limit, you will need to wait at least six hours before applying further modifications to the affected EBS volume.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "VolumeType" : "The target EBS volume type of the volume. \nDefault: If no type is specified, the existing type is retained.",
  "Size" : "The target size of the volume, in GiB. The target volume size must be greater than or equal to than the existing size of the volume. For information about available EBS volume sizes, see Amazon EBS Volume Types. \nDefault: If no size is specified, the existing size is retained.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "Iops" : "The target IOPS rate of the volume. \nThis is only valid for Provisioned IOPS SSD (io1) volumes. For more information, see Provisioned IOPS SSD (io1) Volumes. \nDefault: If no IOPS value is specified, the existing value is retained."
}
```

</details>

## modify_volume_attribute

Modifies a volume attribute. 
By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume. 
You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyVolumeAttribute.

**Type:** object

```json
{
  "VolumeId" : "The ID of the volume.",
  "AutoEnableIO" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## modify_vpc_attribute

Modifies the specified attribute of the specified VPC.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "EnableDnsSupport" : {
    "value" : "The attribute value. The valid values are true or false."
  },
  "EnableDnsHostnames" : {
    "value" : "The attribute value. The valid values are true or false."
  }
}
```

</details>

## modify_vpc_endpoint

Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface or gateway). For more information, see VPC Endpoints in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ModifyVpcEndpoint.

**Type:** object

```json
{
  "PrivateDnsEnabled" : "(Interface endpoint) Indicate whether a private hosted zone is associated with the VPC.",
  "AddSecurityGroupId" : [ "string" ],
  "ResetPolicy" : "(Gateway endpoint) Specify true to reset the policy document to the default policy. The default policy allows full access to the service.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AddSubnetId" : [ "string" ],
  "RemoveRouteTableId" : [ "string" ],
  "PolicyDocument" : "(Gateway endpoint) A policy document to attach to the endpoint. The policy must be in valid JSON format.",
  "RemoveSubnetId" : [ "string" ],
  "AddRouteTableId" : [ "string" ],
  "VpcEndpointId" : "The ID of the endpoint.",
  "RemoveSecurityGroupId" : [ "string" ]
}
```

</details>

## modify_vpc_endpoint_connection_notification

Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConnectionEvents" : [ "string" ],
  "ConnectionNotificationId" : "The ID of the notification.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ConnectionNotificationArn" : "The ARN for the SNS topic for the notification."
}
```

</details>

## modify_vpc_endpoint_service_configuration

Modifies the attributes of your VPC endpoint service configuration. You can change the Network Load Balancers for your service, and you can specify whether acceptance is required for requests to connect to your endpoint service through an interface VPC endpoint.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "RemoveNetworkLoadBalancerArn" : [ "string" ],
  "AcceptanceRequired" : "Indicate whether requests to create an endpoint to your service must be accepted.",
  "AddNetworkLoadBalancerArn" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ServiceId" : "The ID of the service."
}
```

</details>

## modify_vpc_endpoint_service_permissions

Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (IAM users, IAM roles, and AWS accounts) to connect to your endpoint service. 
If you grant permissions to all principals, the service is public. Any users who know the name of a public service can send a request to attach an endpoint. If the service does not require manual approval, attachments are automatically approved.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AddAllowedPrincipals" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "RemoveAllowedPrincipals" : [ "string" ],
  "ServiceId" : "The ID of the service."
}
```

</details>

## modify_vpc_peering_connection_options

Modifies the VPC peering connection options on one side of a VPC peering connection. You can do the following:  
 Enable/disable communication over the peering connection between an EC2-Classic instance that's linked to your VPC (using ClassicLink) and instances in the peer VPC.  
 Enable/disable communication over the peering connection between instances in your VPC and an EC2-Classic instance that's linked to the peer VPC.  
 Enable/disable the ability to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.   
If the peered VPCs are in different accounts, each owner must initiate a separate request to modify the peering connection options, depending on whether their VPC was the requester or accepter for the VPC peering connection. If the peered VPCs are in the same account, you can modify the requester and accepter options in the same request. To confirm which VPC is the accepter and requester for a VPC peering connection, use the DescribeVpcPeeringConnections command.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcPeeringConnectionId" : "The ID of the VPC peering connection.",
  "AccepterPeeringConnectionOptions" : {
    "AllowDnsResolutionFromRemoteVpc" : "If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.",
    "AllowEgressFromLocalClassicLinkToRemoteVpc" : "If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC using ClassicLink to instances in a peer VPC.",
    "AllowEgressFromLocalVpcToRemoteClassicLink" : "If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC using ClassicLink."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "RequesterPeeringConnectionOptions" : {
    "AllowDnsResolutionFromRemoteVpc" : "If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.",
    "AllowEgressFromLocalClassicLinkToRemoteVpc" : "If true, enables outbound communication from an EC2-Classic instance that's linked to a local VPC using ClassicLink to instances in a peer VPC.",
    "AllowEgressFromLocalVpcToRemoteClassicLink" : "If true, enables outbound communication from instances in a local VPC to an EC2-Classic instance that's linked to a peer VPC using ClassicLink."
  }
}
```

</details>

## modify_vpc_tenancy

Modifies the instance tenancy attribute of the specified VPC. You can change the instance tenancy attribute of a VPC to default only. You cannot change the instance tenancy attribute to dedicated. 
After you modify the tenancy of the VPC, any new instances that you launch into the VPC have a tenancy of default, unless you specify otherwise during launch. The tenancy of any existing instances in the VPC is not affected. 
For more information, see Dedicated Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcId" : "The ID of the VPC.",
  "InstanceTenancy" : "The instance tenancy attribute for the VPC. ",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## monitor_instances

Enables detailed monitoring for a running instance. Otherwise, basic monitoring is enabled. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide. 
To disable detailed monitoring, see .

<details><summary>Parameters</summary>

### $body

Contains the parameters for MonitorInstances.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## move_address_to_vpc

Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform. The Elastic IP address must be allocated to your account for more than 24 hours, and it must not be associated with an instance. After the Elastic IP address is moved, it is no longer available for use in the EC2-Classic platform, unless you move it back using the RestoreAddressToClassic request. You cannot move an Elastic IP address that was originally allocated for use in the EC2-VPC platform to the EC2-Classic platform. 

<details><summary>Parameters</summary>

### $body

Contains the parameters for MoveAddressToVpc.

**Type:** object

```json
{
  "PublicIp" : "The Elastic IP address.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## purchase_host_reservation

Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "CurrencyCode" : "The currency in which the totalUpfrontPrice, LimitPrice, and totalHourlyPrice amounts are specified. At this time, the only supported currency is USD.",
  "LimitPrice" : "The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request fails. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is USD. For example, to indicate a limit price of USD 100, specify 100.00.",
  "HostIdSet" : [ "string" ],
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide.",
  "OfferingId" : "The ID of the offering."
}
```

</details>

## purchase_reserved_instances_offering

Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing. 
Use DescribeReservedInstancesOfferings to get a list of Reserved Instance offerings that match your specifications. After you've purchased a Reserved Instance, you can check for your new Reserved Instance with DescribeReservedInstances. 
For more information, see Reserved Instances and Reserved Instance Marketplace in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for PurchaseReservedInstancesOffering.

**Type:** object

```json
{
  "InstanceCount" : "The number of Reserved Instances to purchase.",
  "LimitPrice" : {
    "amount" : "Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount * price).",
    "currencyCode" : "The currency in which the limitPrice amount is specified. At this time, the only supported currency is USD."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ReservedInstancesOfferingId" : "The ID of the Reserved Instance offering to purchase."
}
```

</details>

## purchase_scheduled_instances

Purchases one or more Scheduled Instances with the specified schedule. 
Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a one-year term. Before you can purchase a Scheduled Instance, you must call DescribeScheduledInstanceAvailability to check for available schedules and obtain a purchase token. After you purchase a Scheduled Instance, you must call RunScheduledInstances during each scheduled time period. 
After you purchase a Scheduled Instance, you can't cancel, modify, or resell your purchase.

<details><summary>Parameters</summary>

### $body

Contains the parameters for PurchaseScheduledInstances.

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "PurchaseRequest" : [ {
    "InstanceCount" : "The number of instances.",
    "PurchaseToken" : "The purchase token."
  } ],
  "ClientToken" : "Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency."
}
```

</details>

## reboot_instances

Requests a reboot of one or more instances. This operation is asynchronous; it only queues a request to reboot the specified instances. The operation succeeds if the instances are valid and belong to you. Requests to reboot terminated instances are ignored. 
If an instance does not cleanly shut down within four minutes, Amazon EC2 performs a hard reboot. 
For more information about troubleshooting, see Getting Console Output and Rebooting Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RebootInstances.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## register_image

Registers an AMI. When you're creating an AMI, this is the final step you must complete before you can launch an instance from the AMI. For more information about creating AMIs, see Creating Your Own AMIs in the Amazon Elastic Compute Cloud User Guide.  
For Amazon EBS-backed instances, CreateImage creates and registers the AMI in a single request, so you don't have to register the AMI yourself.  
You can also use RegisterImage to create an Amazon EBS-backed Linux AMI from a snapshot of a root device volume. You specify the snapshot using the block device mapping. For more information, see Launching a Linux Instance from a Backup in the Amazon Elastic Compute Cloud User Guide. 
You can't register an image where a secondary (non-root) snapshot has AWS Marketplace product codes. 
Some Linux distributions, such as Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES), use the EC2 billing product code associated with an AMI to verify the subscription status for package updates. Creating an AMI from an EBS snapshot does not maintain this billing code, and instances launched from such an AMI are not able to connect to package update infrastructure. If you purchase a Reserved Instance offering for one of these Linux distributions and launch instances using an AMI that does not contain the required billing code, your Reserved Instance is not applied to these instances. 
To create an AMI for operating systems that require a billing code, see CreateImage. 
If needed, you can deregister an AMI at any time. Any modifications you make to an AMI backed by an instance store volume invalidates its registration. If you make changes to an image, deregister the previous image and register the new image.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RegisterImage.

**Type:** object

```json
{
  "RamdiskId" : "The ID of the RAM disk.",
  "RootDeviceName" : "The device name of the root device volume (for example, /dev/sda1).",
  "Description" : "A description for your AMI.",
  "Architecture" : "The architecture of the AMI. \nDefault: For Amazon EBS-backed AMIs, i386. For instance store-backed AMIs, the architecture specified in the manifest file.",
  "VirtualizationType" : "The type of virtualization (hvm | paravirtual). \nDefault: paravirtual ",
  "EnaSupport" : "Set to true to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI. \nThis option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "BlockDeviceMapping" : [ {
    "noDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
    "virtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nNVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
    "ebs" : {
      "volumeType" : "The volume type: gp2, io1, st1, sc1, or standard. \nDefault: standard ",
      "snapshotId" : "The ID of the snapshot.",
      "encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption.  \nIf you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.",
      "KmsKeyId" : "Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted. \nThis parameter is only supported on BlockDeviceMapping objects called by RunInstances, RequestSpotFleet, and RequestSpotInstances.",
      "iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
      "deleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination.",
      "volumeSize" : "The size of the volume, in GiB. \nConstraints: 1-16384 for General Purpose SSD (gp2), 4-16384 for Provisioned IOPS SSD (io1), 500-16384 for Throughput Optimized HDD (st1), 500-16384 for Cold HDD (sc1), and 1-1024 for Magnetic (standard) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size."
    },
    "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
  } ],
  "SriovNetSupport" : "Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI. \nThere is no way to disable sriovNetSupport at this time. \nThis option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.",
  "BillingProduct" : [ "string" ],
  "KernelId" : "The ID of the kernel.",
  "ImageLocation" : "The full path to your AMI manifest in Amazon S3 storage.",
  "Name" : "A name for your AMI. \nConstraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)"
}
```

</details>

## reject_vpc_endpoint_connections

Rejects one or more VPC endpoint connection requests to your VPC endpoint service.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "VpcEndpointId" : [ "string" ],
  "ServiceId" : "The ID of the service."
}
```

</details>

## reject_vpc_peering_connection

Rejects a VPC peering connection request. The VPC peering connection must be in the pending-acceptance state. Use the DescribeVpcPeeringConnections request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use DeleteVpcPeeringConnection.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "VpcPeeringConnectionId" : "The ID of the VPC peering connection.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## release_address

Releases the specified Elastic IP address. 
[EC2-Classic, default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with. To disassociate an Elastic IP address without releasing it, use DisassociateAddress. 
[Nondefault VPC] You must use DisassociateAddress to disassociate the Elastic IP address before you can release it. Otherwise, Amazon EC2 returns an error (InvalidIPAddress.InUse). 
After releasing an Elastic IP address, it is released to the IP address pool. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you'll get an AuthFailure error if the address is already allocated to another AWS account. 
[EC2-VPC] After you release an Elastic IP address for use in a VPC, you might be able to recover it. For more information, see AllocateAddress.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ReleaseAddress.

**Type:** object

```json
{
  "PublicIp" : "[EC2-Classic] The Elastic IP address. Required for EC2-Classic.",
  "AllocationId" : "[EC2-VPC] The allocation ID. Required for EC2-VPC.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## release_hosts

When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into released state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, for example, to modify the host. You must stop or terminate all instances on a host before it can be released. 
When Dedicated Hosts are released, it may take some time for them to stop counting toward your limit and you may receive capacity errors when trying to allocate new Dedicated Hosts. Wait a few minutes and then try again. 
Released hosts still appear in a DescribeHosts response.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "HostId" : [ "string" ]
}
```

</details>

## replace_iam_instance_profile_association

Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first. 
Use DescribeIamInstanceProfileAssociations to get the association ID.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "IamInstanceProfile" : {
    "name" : "The name of the instance profile.",
    "arn" : "The Amazon Resource Name (ARN) of the instance profile."
  },
  "AssociationId" : "The ID of the existing IAM instance profile association."
}
```

</details>

## replace_network_acl_association

Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide. 
This is an idempotent operation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NetworkAclId" : "The ID of the new network ACL to associate with the subnet.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AssociationId" : "The ID of the current association between the original network ACL and the subnet."
}
```

</details>

## replace_network_acl_entry

Replaces an entry (rule) in a network ACL. For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "PortRange" : {
    "from" : "The first port in the range.",
    "to" : "The last port in the range."
  },
  "NetworkAclId" : "The ID of the ACL.",
  "RuleAction" : "Indicates whether to allow or deny the traffic that matches the rule.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "CidrBlock" : "The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24).",
  "Egress" : "Indicates whether to replace the egress rule. \nDefault: If no value is specified, we replace the ingress rule.",
  "RuleNumber" : "The rule number of the entry to replace.",
  "Ipv6CidrBlock" : "The IPv6 network range to allow or deny, in CIDR notation (for example 2001:bd8:1234:1a00::/64).",
  "Protocol" : "The IP protocol. You can specify all or -1 to mean all protocols. If you specify all, -1, or a protocol number other than tcp, udp, or icmp, traffic on all ports is allowed, regardless of any ports or ICMP types or codes you that specify. If you specify protocol 58 (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol 58 (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.",
  "Icmp" : {
    "code" : "The ICMP code. A value of -1 means all codes for the specified ICMP type.",
    "type" : "The ICMP type. A value of -1 means all types."
  }
}
```

</details>

## replace_route

Replaces an existing route within a route table in a VPC. You must provide only one of the following: internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only internet gateway. 
For more information, see Route Tables in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DestinationIpv6CidrBlock" : "The IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.",
  "VpcPeeringConnectionId" : "The ID of a VPC peering connection.",
  "RouteTableId" : "The ID of the route table.",
  "InstanceId" : "The ID of a NAT instance in your VPC.",
  "EgressOnlyInternetGatewayId" : "[IPv6 traffic only] The ID of an egress-only internet gateway.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "DestinationCidrBlock" : "The IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.",
  "GatewayId" : "The ID of an internet gateway or virtual private gateway.",
  "NetworkInterfaceId" : "The ID of a network interface.",
  "NatGatewayId" : "[IPv4 traffic only] The ID of a NAT gateway."
}
```

</details>

## replace_route_table_association

Changes the route table associated with a given subnet in a VPC. After the operation completes, the subnet uses the routes in the new route table it's associated with. For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide. 
You can also use ReplaceRouteTableAssociation to change which table is the main route table in the VPC. You just specify the main route table's association ID and the route table to be the new main route table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "RouteTableId" : "The ID of the new route table to associate with the subnet.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "AssociationId" : "The association ID."
}
```

</details>

## report_instance_status

Submits feedback about the status of an instance. The instance must be in the running state. If your experience with the instance differs from the instance status returned by DescribeInstanceStatus, use ReportInstanceStatus to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks. 
Use of this action does not change the value returned by DescribeInstanceStatus.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ReportInstanceStatus.

**Type:** object

```json
{
  "Status" : "The status of all instances listed.",
  "Description" : "Descriptive text about the health state of your instance.",
  "EndTime" : "The time at which the reported instance health state ended.",
  "InstanceId" : [ "string" ],
  "StartTime" : "The time at which the reported instance health state began.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ReasonCode" : [ "string. Possible values: instance-stuck-in-state | unresponsive | not-accepting-credentials | password-not-available | performance-network | performance-instance-store | performance-ebs-volume | performance-other | other" ]
}
```

</details>

## request_spot_fleet

Creates a Spot Fleet request. 
The Spot Fleet request specifies the total target capacity and the On-Demand target capacity. Amazon EC2 calculates the difference between the total capacity and On-Demand capacity, and launches the difference as Spot capacity. 
You can submit a single request that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet. 
By default, the Spot Fleet requests Spot Instances in the Spot pool where the price per unit is the lowest. Each launch specification can include its own instance weighting that reflects the value of the instance type to your application workload. 
Alternatively, you can specify that the Spot Fleet distribute the target capacity across the Spot pools included in its launch specifications. By ensuring that the Spot Instances in your Spot Fleet are in different Spot pools, you can improve the availability of your fleet. 
You can specify tags for the Spot Instances. You cannot tag other resource types in a Spot Fleet request because only the instance resource type is supported. 
For more information, see Spot Fleet Requests in the Amazon EC2 User Guide for Linux Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RequestSpotFleet.

**Type:** object

```json
{
  "SpotFleetRequestConfig" : {
    "onDemandFulfilledCapacity" : "The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.",
    "spotPrice" : "The maximum price per unit hour that you are willing to pay for a Spot Instance. The default is the On-Demand price.",
    "targetCapacity" : "The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is maintain, you can specify a target capacity of 0 and add capacity later.",
    "clientToken" : "A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see Ensuring Idempotency.",
    "instancePoolsToUseCount" : "The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot AllocationStrategy is set to lowest-price. Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.",
    "launchTemplateConfigs" : [ {
      "overrides" : [ {
        "subnetId" : "The ID of the subnet in which to launch the instances.",
        "spotPrice" : "The maximum price per unit hour that you are willing to pay for a Spot Instance.",
        "instanceType" : "The instance type.",
        "priority" : "The priority for the launch template override. If OnDemandAllocationStrategy is set to prioritized, Spot Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at 0. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority.",
        "availabilityZone" : "The Availability Zone in which to launch the instances.",
        "weightedCapacity" : "The number of units provided by the specified instance type."
      } ],
      "launchTemplateSpecification" : {
        "launchTemplateId" : "The ID of the launch template. You must specify either a template ID or a template name.",
        "version" : "The version number of the launch template. You must specify a version number.",
        "launchTemplateName" : "The name of the launch template. You must specify either a template name or a template ID."
      }
    } ],
    "onDemandAllocationStrategy" : "The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify lowestPrice, Spot Fleet uses price to determine the order, launching the lowest price first. If you specify prioritized, Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to lowestPrice.",
    "onDemandTargetCapacity" : "The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is maintain, you can specify a target capacity of 0 and add capacity later.",
    "validFrom" : "The start date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.",
    "launchSpecifications" : [ {
      "subnetId" : "The ID of the subnet in which to launch the instances. To specify multiple subnets, separate them using commas; for example, \"subnet-a61dafcf, subnet-65ea5f08\".",
      "addressingType" : "Deprecated.",
      "kernelId" : "The ID of the kernel.",
      "ebsOptimized" : "Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance. \nDefault: false ",
      "ramdiskId" : "The ID of the RAM disk.",
      "imageId" : "The ID of the AMI.",
      "spotPrice" : "The maximum price per unit hour that you are willing to pay for a Spot Instance. If this value is not specified, the default is the Spot price specified for the fleet. To determine the Spot price per unit hour, divide the Spot price by the value of WeightedCapacity.",
      "userData" : "The Base64-encoded user data to make available to the instances.",
      "networkInterfaceSet" : [ {
        "networkInterfaceId" : "The ID of the network interface.",
        "subnetId" : "The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.",
        "ipv6AddressCount" : "A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.",
        "SecurityGroupId" : [ "string" ],
        "ipv6AddressesSet" : [ {
          "ipv6Address" : "The IPv6 address."
        } ],
        "description" : "The description of the network interface. Applies only if creating a network interface when launching an instance.",
        "associatePublicIpAddress" : "Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true.",
        "deleteOnTermination" : "If set to true, the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.",
        "secondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
        "deviceIndex" : "The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.",
        "privateIpAddress" : "The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
        "privateIpAddressesSet" : [ {
          "privateIpAddress" : "The private IPv4 addresses.",
          "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
        } ]
      } ],
      "blockDeviceMapping" : [ {
        "noDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
        "virtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nNVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
        "ebs" : {
          "volumeType" : "The volume type: gp2, io1, st1, sc1, or standard. \nDefault: standard ",
          "snapshotId" : "The ID of the snapshot.",
          "encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption.  \nIf you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.",
          "KmsKeyId" : "Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted. \nThis parameter is only supported on BlockDeviceMapping objects called by RunInstances, RequestSpotFleet, and RequestSpotInstances.",
          "iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
          "deleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination.",
          "volumeSize" : "The size of the volume, in GiB. \nConstraints: 1-16384 for General Purpose SSD (gp2), 4-16384 for Provisioned IOPS SSD (io1), 500-16384 for Throughput Optimized HDD (st1), 500-16384 for Cold HDD (sc1), and 1-1024 for Magnetic (standard) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size."
        },
        "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
      } ],
      "tagSpecificationSet" : [ {
        "tag" : [ {
          "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
          "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
        } ],
        "resourceType" : "The type of resource. Currently, the only resource type that is supported is instance."
      } ],
      "instanceType" : "The instance type.",
      "keyName" : "The name of the key pair.",
      "monitoring" : {
        "enabled" : "Enables monitoring for the instance. \nDefault: false "
      },
      "groupSet" : [ {
        "groupName" : "The name of the security group.",
        "groupId" : "The ID of the security group."
      } ],
      "iamInstanceProfile" : {
        "name" : "The name of the instance profile.",
        "arn" : "The Amazon Resource Name (ARN) of the instance profile."
      },
      "weightedCapacity" : "The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms (instances or a performance characteristic such as vCPUs, memory, or I/O). \nIf the target capacity divided by this value is not a whole number, we round the number of instances to the next whole number. If this value is not specified, the default is 1.",
      "placement" : {
        "groupName" : "The name of the placement group.",
        "tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for Spot Instances.",
        "availabilityZone" : "The Availability Zone. \n[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, \"us-west-2a, us-west-2b\"."
      }
    } ],
    "type" : "The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is request, the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. To maintain a certain target capacity, the Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: maintain.",
    "allocationStrategy" : "Indicates how to allocate the target capacity across the Spot pools specified by the Spot Fleet request. The default is lowestPrice.",
    "fulfilledCapacity" : "The number of units fulfilled by this request compared to the set target capacity.",
    "replaceUnhealthyInstances" : "Indicates whether Spot Fleet should replace unhealthy instances.",
    "loadBalancersConfig" : {
      "targetGroupsConfig" : {
        "targetGroups" : [ {
          "arn" : "The Amazon Resource Name (ARN) of the target group."
        } ]
      },
      "classicLoadBalancersConfig" : {
        "classicLoadBalancers" : [ {
          "name" : "The name of the load balancer."
        } ]
      }
    },
    "terminateInstancesWithExpiration" : "Indicates whether running Spot Instances should be terminated when the Spot Fleet request expires.",
    "iamFleetRole" : "Grants the Spot Fleet permission to terminate Spot Instances on your behalf when you cancel its Spot Fleet request using CancelSpotFleetRequests or when the Spot Fleet request expires, if you set terminateInstancesWithExpiration.",
    "validUntil" : "The end date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot Instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date.",
    "instanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
    "excessCapacityTerminationPolicy" : "Indicates whether running Spot Instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet."
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## request_spot_instances

Creates a Spot Instance request. 
For more information, see Spot Instance Requests in the Amazon EC2 User Guide for Linux Instances.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RequestSpotInstances.

**Type:** object

```json
{
  "InstanceCount" : "The maximum number of Spot Instances to launch. \nDefault: 1",
  "SpotPrice" : "The maximum price per hour that you are willing to pay for a Spot Instance. The default is the On-Demand price.",
  "Type" : "The Spot Instance request type. \nDefault: one-time ",
  "AvailabilityZoneGroup" : "The user-specified name for a logical grouping of requests. \nWhen you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active. \nIf there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group. \nDefault: Instances are launched in any available Availability Zone.",
  "LaunchGroup" : "The instance launch group. Launch groups are Spot Instances that launch together and terminate together. \nDefault: Instances are launched and terminated individually",
  "InstanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
  "LaunchSpecification" : {
    "subnetId" : "The ID of the subnet in which to launch the instance.",
    "addressingType" : "Deprecated.",
    "kernelId" : "The ID of the kernel.",
    "ebsOptimized" : "Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance. \nDefault: false ",
    "ramdiskId" : "The ID of the RAM disk.",
    "imageId" : "The ID of the AMI.",
    "userData" : "The Base64-encoded user data for the instance.",
    "blockDeviceMapping" : [ {
      "noDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
      "virtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nNVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
      "ebs" : {
        "volumeType" : "The volume type: gp2, io1, st1, sc1, or standard. \nDefault: standard ",
        "snapshotId" : "The ID of the snapshot.",
        "encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption.  \nIf you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.",
        "KmsKeyId" : "Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted. \nThis parameter is only supported on BlockDeviceMapping objects called by RunInstances, RequestSpotFleet, and RequestSpotInstances.",
        "iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
        "deleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination.",
        "volumeSize" : "The size of the volume, in GiB. \nConstraints: 1-16384 for General Purpose SSD (gp2), 4-16384 for Provisioned IOPS SSD (io1), 500-16384 for Throughput Optimized HDD (st1), 500-16384 for Cold HDD (sc1), and 1-1024 for Magnetic (standard) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size."
      },
      "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
    } ],
    "SecurityGroupId" : [ "string" ],
    "instanceType" : "The instance type.",
    "keyName" : "The name of the key pair.",
    "NetworkInterface" : [ {
      "networkInterfaceId" : "The ID of the network interface.",
      "subnetId" : "The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.",
      "ipv6AddressCount" : "A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.",
      "SecurityGroupId" : [ "string" ],
      "ipv6AddressesSet" : [ {
        "ipv6Address" : "The IPv6 address."
      } ],
      "description" : "The description of the network interface. Applies only if creating a network interface when launching an instance.",
      "associatePublicIpAddress" : "Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true.",
      "deleteOnTermination" : "If set to true, the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.",
      "secondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
      "deviceIndex" : "The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.",
      "privateIpAddress" : "The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
      "privateIpAddressesSet" : [ {
        "privateIpAddress" : "The private IPv4 addresses.",
        "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
      } ]
    } ],
    "SecurityGroup" : [ "string" ],
    "monitoring" : {
      "enabled" : "Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled."
    },
    "iamInstanceProfile" : {
      "name" : "The name of the instance profile.",
      "arn" : "The Amazon Resource Name (ARN) of the instance profile."
    },
    "placement" : {
      "groupName" : "The name of the placement group.",
      "tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for Spot Instances.",
      "availabilityZone" : "The Availability Zone. \n[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, \"us-west-2a, us-west-2b\"."
    }
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ValidFrom" : "The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.",
  "ClientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon EC2 User Guide for Linux Instances.",
  "ValidUntil" : "The end date of the request. If this is a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date is reached. The default end date is 7 days from the current date.",
  "BlockDurationMinutes" : "The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360). \nThe duration period starts as soon as your Spot Instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates. \nYou can't specify an Availability Zone group or a launch group if you specify a duration."
}
```

</details>

## reset_fpga_image_attribute

Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "FpgaImageId" : "The ID of the AFI.",
  "Attribute" : "The attribute.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## reset_image_attribute

Resets an attribute of an AMI to its default value.  
The productCodes attribute can't be reset.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ResetImageAttribute.

**Type:** object

```json
{
  "Attribute" : "The attribute to reset (currently you can only reset the launch permission attribute).",
  "ImageId" : "The ID of the AMI.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## reset_instance_attribute

Resets an attribute of an instance to its default value. To reset the kernel or ramdisk, the instance must be in a stopped state. To reset the sourceDestCheck, the instance can be either running or stopped. 
The sourceDestCheck attribute controls whether source/destination checking is enabled. The default value is true, which means checking is enabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT Instances in the Amazon Virtual Private Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ResetInstanceAttribute.

**Type:** object

```json
{
  "Attribute" : "The attribute to reset.  \nYou can only reset the following attributes: kernel | ramdisk | sourceDestCheck. To change an instance attribute, use ModifyInstanceAttribute.",
  "InstanceId" : "The ID of the instance.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## reset_network_interface_attribute

Resets a network interface attribute. You can specify only one attribute at a time.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ResetNetworkInterfaceAttribute.

**Type:** object

```json
{
  "SourceDestCheck" : "The source/destination checking attribute. Resets the value to true.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## reset_snapshot_attribute

Resets permission settings for the specified snapshot. 
For more information about modifying snapshot permissions, see Sharing Snapshots in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for ResetSnapshotAttribute.

**Type:** object

```json
{
  "SnapshotId" : "The ID of the snapshot.",
  "Attribute" : "The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## restore_address_to_classic

Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform. You cannot move an Elastic IP address that was originally allocated for use in EC2-VPC. The Elastic IP address must not be associated with an instance or network interface.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RestoreAddressToClassic.

**Type:** object

```json
{
  "PublicIp" : "The Elastic IP address.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## revoke_security_group_egress

[EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC. This action doesn't apply to security groups for use in EC2-Classic. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly. 
Each rule consists of the protocol and the IPv4 or IPv6 CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not have to specify the description to revoke the rule. 
Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "CidrIp" : "Not supported. Use a set of IP permissions to specify the CIDR.",
  "FromPort" : "Not supported. Use a set of IP permissions to specify the port.",
  "ToPort" : "Not supported. Use a set of IP permissions to specify the port.",
  "SourceSecurityGroupName" : "Not supported. Use a set of IP permissions to specify a destination security group.",
  "SourceSecurityGroupOwnerId" : "Not supported. Use a set of IP permissions to specify a destination security group.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpProtocol" : "Not supported. Use a set of IP permissions to specify the protocol name or number.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group."
}
```

</details>

## revoke_security_group_ingress

Removes one or more ingress rules from a security group. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly.  
[EC2-Classic security groups only] If the values you specify do not match the existing rule's values, no error is returned. Use DescribeSecurityGroups to verify that the rule has been removed.  
Each rule consists of the protocol and the CIDR range or source security group. For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not have to specify the description to revoke the rule. 
Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.",
  "CidrIp" : "The CIDR IP address range. You can't specify this parameter when specifying a source security group.",
  "FromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, use -1 to specify all ICMP types.",
  "ToPort" : "The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, use -1 to specify all ICMP codes for the ICMP type.",
  "SourceSecurityGroupName" : "[EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. For EC2-VPC, the source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.",
  "SourceSecurityGroupOwnerId" : "[EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers). Use -1 to specify all.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID."
}
```

</details>

## run_instances

Launches the specified number of instances using an AMI for which you have permissions.  
You can specify a number of options, or leave the default options. The following rules apply:  
 [EC2-VPC] If you don't specify a subnet ID, we choose a default subnet from your default VPC for you. If you don't have a default VPC, you must specify a subnet ID in the request.  
 [EC2-Classic] If don't specify an Availability Zone, we choose one for you.  
 Some instance types must be launched into a VPC. If you do not have a default VPC, or if you do not specify a subnet ID, the request fails. For more information, see Instance Types Available Only in a VPC.  
 [EC2-VPC] All instances have a network interface with a primary private IPv4 address. If you don't specify this address, we choose one from the IPv4 range of your subnet.  
 Not all instance types support IPv6 addresses. For more information, see Instance Types.  
 If you don't specify a security group ID, we use the default security group. For more information, see Security Groups.  
 If any of the AMIs have a product code attached for which the user has not subscribed, the request fails.   
You can create a launch template, which is a resource that contains the parameters to launch an instance. When you launch an instance using RunInstances, you can specify the launch template instead of specifying the launch parameters. 
To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances. 
An instance is ready for you to use when it's in the running state. You can check the state of your instance using DescribeInstances. You can tag instances and EBS volumes during launch, after launch, or both. For more information, see CreateTags and Tagging Your Amazon EC2 Resources. 
Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see Key Pairs in the Amazon Elastic Compute Cloud User Guide. 
For troubleshooting, see What To Do If An Instance Immediately Terminates, and Troubleshooting Connecting to Your Instance in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RunInstances.

**Type:** object

```json
{
  "PrivateIpAddress" : "[EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet. \nOnly one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.",
  "UserData" : "The user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ElasticGpuSpecification" : [ {
    "Type" : "The type of Elastic GPU."
  } ],
  "IamInstanceProfile" : {
    "name" : "The name of the instance profile.",
    "arn" : "The Amazon Resource Name (ARN) of the instance profile."
  },
  "SubnetId" : "[EC2-VPC] The ID of the subnet to launch the instance into.",
  "MaxCount" : "The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above MinCount. \nConstraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 FAQ.",
  "KernelId" : "The ID of the kernel.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see  PV-GRUB in the Amazon Elastic Compute Cloud User Guide.",
  "EbsOptimized" : "Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance. \nDefault: false ",
  "Placement" : {
    "groupName" : "The name of the placement group the instance is in.",
    "tenancy" : "The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.",
    "hostId" : "The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the ImportInstance command.",
    "availabilityZone" : "The Availability Zone of the instance.",
    "spreadDomain" : "Reserved for future use.",
    "affinity" : "The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command."
  },
  "LaunchTemplate" : {
    "LaunchTemplateName" : "The name of the launch template.",
    "Version" : "The version number of the launch template. \nDefault: The default version for the launch template.",
    "LaunchTemplateId" : "The ID of the launch template."
  },
  "Ipv6AddressCount" : "[EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.",
  "ImageId" : "The ID of the AMI, which you can get by calling DescribeImages. An AMI is required to launch an instance and must be specified here or in a launch template.",
  "BlockDeviceMapping" : [ {
    "noDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
    "virtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nNVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
    "ebs" : {
      "volumeType" : "The volume type: gp2, io1, st1, sc1, or standard. \nDefault: standard ",
      "snapshotId" : "The ID of the snapshot.",
      "encrypted" : "Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption.  \nIf you are creating a volume from a snapshot, you cannot specify an encryption value. This is because only blank volumes can be encrypted on creation. If you are creating a snapshot from an existing EBS volume, you cannot specify an encryption value that differs from that of the EBS volume. We recommend that you omit the encryption value from the block device mappings when creating an image from an instance.",
      "KmsKeyId" : "Identifier (key ID, key alias, ID ARN, or alias ARN) for a user-managed CMK under which the EBS volume is encrypted. \nThis parameter is only supported on BlockDeviceMapping objects called by RunInstances, RequestSpotFleet, and RequestSpotInstances.",
      "iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
      "deleteOnTermination" : "Indicates whether the EBS volume is deleted on instance termination.",
      "volumeSize" : "The size of the volume, in GiB. \nConstraints: 1-16384 for General Purpose SSD (gp2), 4-16384 for Provisioned IOPS SSD (io1), 500-16384 for Throughput Optimized HDD (st1), 500-16384 for Cold HDD (sc1), and 1-1024 for Magnetic (standard) volumes. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size."
    },
    "deviceName" : "The device name (for example, /dev/sdh or xvdh)."
  } ],
  "InstanceType" : "The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide. \nDefault: m1.small ",
  "Monitoring" : {
    "enabled" : "Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled."
  },
  "Ipv6Address" : [ {
    "ipv6Address" : "The IPv6 address."
  } ],
  "AdditionalInfo" : "Reserved.",
  "InstanceInitiatedShutdownBehavior" : "Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown). \nDefault: stop ",
  "CpuOptions" : {
    "ThreadsPerCore" : "The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of 1. Otherwise, specify the default value of 2.",
    "CoreCount" : "The number of CPU cores for the instance."
  },
  "SecurityGroupId" : [ "string" ],
  "NetworkInterface" : [ {
    "networkInterfaceId" : "The ID of the network interface.",
    "subnetId" : "The ID of the subnet associated with the network string. Applies only if creating a network interface when launching an instance.",
    "ipv6AddressCount" : "A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.",
    "SecurityGroupId" : [ "string" ],
    "ipv6AddressesSet" : [ {
      "ipv6Address" : "The IPv6 address."
    } ],
    "description" : "The description of the network interface. Applies only if creating a network interface when launching an instance.",
    "associatePublicIpAddress" : "Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true.",
    "deleteOnTermination" : "If set to true, the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.",
    "secondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
    "deviceIndex" : "The index of the device on the instance for the network interface attachment. If you are specifying a network interface in a RunInstances request, you must provide the device index.",
    "privateIpAddress" : "The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.",
    "privateIpAddressesSet" : [ {
      "privateIpAddress" : "The private IPv4 addresses.",
      "primary" : "Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary."
    } ]
  } ],
  "TagSpecification" : [ {
    "Tag" : [ {
      "value" : "The value of the tag. \nConstraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
      "key" : "The key of the tag. \nConstraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:."
    } ],
    "resourceType" : "The type of resource to tag. Currently, the resource types that support tagging on creation are fleet, dedicated-host, instance, snapshot, and volume. To tag a resource after it has been created, see CreateTags."
  } ],
  "SecurityGroup" : [ "string" ],
  "DisableApiTermination" : "If you set this parameter to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to false after launch, use ModifyInstanceAttribute. Alternatively, if you set InstanceInitiatedShutdownBehavior to terminate, you can terminate the instance by running the shutdown command from the instance. \nDefault: false ",
  "RamdiskId" : "The ID of the RAM disk.  \nWe recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see  PV-GRUB in the Amazon Elastic Compute Cloud User Guide.",
  "KeyName" : "The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair.  \nIf you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.",
  "InstanceMarketOptions" : {
    "SpotOptions" : {
      "SpotInstanceType" : "The Spot Instance request type. For RunInstances, persistent Spot Instance requests are only supported when InstanceInterruptionBehavior is set to either hibernate or stop.",
      "InstanceInterruptionBehavior" : "The behavior when a Spot Instance is interrupted. The default is terminate.",
      "MaxPrice" : "The maximum hourly price you're willing to pay for the Spot Instances. The default is the On-Demand price.",
      "BlockDurationMinutes" : "The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).",
      "ValidUntil" : "The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached. The default end date is 7 days from the current date."
    },
    "MarketType" : "The market type."
  },
  "ClientToken" : "Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency. \nConstraints: Maximum 64 ASCII characters",
  "CreditSpecification" : {
    "CpuCredits" : "The credit option for CPU usage of a T2 or T3 instance. Valid values are standard and unlimited."
  },
  "MinCount" : "The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances. \nConstraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 General FAQ."
}
```

</details>

## run_scheduled_instances

Launches the specified Scheduled Instances. 
Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using PurchaseScheduledInstances. 
You must launch a Scheduled Instance during its scheduled time period. You can't stop or reboot a Scheduled Instance, but you can terminate it as needed. If you terminate a Scheduled Instance before the current scheduled time period ends, you can launch it again after a few minutes. For more information, see Scheduled Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for RunScheduledInstances.

**Type:** object

```json
{
  "InstanceCount" : "The number of instances. \nDefault: 1",
  "LaunchSpecification" : {
    "UserData" : "The base64-encoded MIME user data.",
    "SecurityGroupId" : [ "string" ],
    "NetworkInterface" : [ {
      "Group" : [ "string" ],
      "Description" : "The description.",
      "PrivateIpAddress" : "The IPv4 address of the network interface within the subnet.",
      "SecondaryPrivateIpAddressCount" : "The number of secondary private IPv4 addresses.",
      "DeviceIndex" : "The index of the device for the network interface attachment.",
      "Ipv6AddressCount" : "The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.",
      "SubnetId" : "The ID of the subnet.",
      "AssociatePublicIpAddress" : "Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true.",
      "NetworkInterfaceId" : "The ID of the network interface.",
      "Ipv6Address" : [ {
        "Ipv6Address" : "Ipv6Address"
      } ],
      "PrivateIpAddressConfig" : [ {
        "PrivateIpAddress" : "The IPv4 address.",
        "Primary" : "Indicates whether this is a primary IPv4 address. Otherwise, this is a secondary IPv4 address."
      } ],
      "DeleteOnTermination" : "Indicates whether to delete the interface when the instance is terminated."
    } ],
    "IamInstanceProfile" : {
      "Arn" : "The Amazon Resource Name (ARN).",
      "Name" : "The name."
    },
    "KernelId" : "The ID of the kernel.",
    "SubnetId" : "The ID of the subnet in which to launch the instances.",
    "EbsOptimized" : "Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance. \nDefault: false ",
    "KeyName" : "The name of the key pair.",
    "RamdiskId" : "The ID of the RAM disk.",
    "Placement" : {
      "GroupName" : "The name of the placement group.",
      "AvailabilityZone" : "The Availability Zone."
    },
    "ImageId" : "The ID of the Amazon Machine Image (AMI).",
    "BlockDeviceMapping" : [ {
      "Ebs" : {
        "SnapshotId" : "The ID of the snapshot.",
        "VolumeType" : "The volume type. gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, Throughput Optimized HDD for st1, Cold HDD for sc1, or standard for Magnetic. \nDefault: standard ",
        "Encrypted" : "Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.",
        "Iops" : "The number of I/O operations per second (IOPS) that the volume supports. For io1 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about gp2 baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. \nConstraint: Range is 100-20000 IOPS for io1 volumes and 100-10000 IOPS for gp2 volumes. \nCondition: This parameter is required for requests to create io1volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes.",
        "VolumeSize" : "The size of the volume, in GiB. \nDefault: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.",
        "DeleteOnTermination" : "Indicates whether the volume is deleted on instance termination."
      },
      "NoDevice" : "Suppresses the specified device included in the block device mapping of the AMI.",
      "VirtualName" : "The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. \nConstraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.",
      "DeviceName" : "The device name (for example, /dev/sdh or xvdh)."
    } ],
    "InstanceType" : "The instance type.",
    "Monitoring" : {
      "Enabled" : "Indicates whether monitoring is enabled."
    }
  },
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "ScheduledInstanceId" : "The Scheduled Instance ID.",
  "ClientToken" : "Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempotency."
}
```

</details>

## start_instances

Starts an Amazon EBS-backed instance that you've previously stopped. 
Instances that use Amazon EBS volumes as their root devices can be quickly stopped and started. When an instance is stopped, the compute resources are released and you are not billed for instance usage. However, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. You can restart your instance at any time. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage. 
Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM. 
Performing this operation on an instance that uses an instance store as its root device returns an error. 
For more information, see Stopping Instances in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for StartInstances.

**Type:** object

```json
{
  "AdditionalInfo" : "Reserved.",
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## stop_instances

Stops an Amazon EBS-backed instance. 
We don't charge usage for a stopped instance, or data transfer fees; however, your root partition Amazon EBS volume remains and continues to persist your data, and you are charged for Amazon EBS volume usage. Every time you start your Windows instance, Amazon EC2 charges you for a full instance hour. If you stop and restart your Windows instance, a new instance hour begins and Amazon EC2 charges you for another full instance hour even if you are still within the same 60-minute period when it was stopped. Every time you start your Linux instance, Amazon EC2 charges a one-minute minimum for instance usage, and thereafter charges per second for instance usage. 
You can't start or stop Spot Instances, and you can't stop instance store-backed instances. 
When you stop an instance, we shut it down. You can restart your instance at any time. Before stopping an instance, make sure it is in a state from which it can be restarted. Stopping an instance does not preserve data stored in RAM. 
Stopping an instance is different to rebooting or terminating it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, the root device and any other devices attached during the instance launch are automatically deleted. For more information about the differences between rebooting, stopping, and terminating instances, see Instance Lifecycle in the Amazon Elastic Compute Cloud User Guide. 
When you stop an instance, we attempt to shut it down forcibly after a short while. If your instance appears stuck in the stopping state after a period of time, there may be an issue with the underlying host computer. For more information, see Troubleshooting Stopping Your Instance in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for StopInstances.

**Type:** object

```json
{
  "Force" : "Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances. \nDefault: false ",
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## terminate_instances

Shuts down one or more instances. This operation is idempotent; if you terminate an instance more than once, each call succeeds.  
If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated. 
Terminated instances remain visible after termination (for approximately one hour). 
By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running. 
You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop it or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the DeleteOnTermination block device mapping parameter set to true are automatically deleted. For more information about the differences between stopping and terminating instances, see Instance Lifecycle in the Amazon Elastic Compute Cloud User Guide. 
For more information about troubleshooting, see Troubleshooting Terminating Your Instance in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for TerminateInstances.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## unassign_ipv6_addresses

Unassigns one or more IPv6 addresses from a network interface.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Ipv6Addresses" : [ "string" ],
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## unassign_private_ip_addresses

Unassigns one or more secondary private IP addresses from a network interface.

<details><summary>Parameters</summary>

### $body

Contains the parameters for UnassignPrivateIpAddresses.

**Type:** object

```json
{
  "PrivateIpAddress" : [ "string" ],
  "NetworkInterfaceId" : "The ID of the network interface."
}
```

</details>

## unmonitor_instances

Disables detailed monitoring for a running instance. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide.

<details><summary>Parameters</summary>

### $body

Contains the parameters for UnmonitorInstances.

**Type:** object

```json
{
  "InstanceId" : [ "string" ],
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation."
}
```

</details>

## update_security_group_rule_descriptions_egress

[EC2-VPC only] Updates the description of an egress (outbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. 
You specify the description as part of the IP permissions structure. You can remove a description for a security group rule by omitting the description parameter in the request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "[Default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID."
}
```

</details>

## update_security_group_rule_descriptions_ingress

Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. 
You specify the description as part of the IP permissions structure. You can remove a description for a security group rule by omitting the description parameter in the request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GroupName" : "[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.",
  "DryRun" : "Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.",
  "IpPermissions" : [ {
    "ipRanges" : [ {
      "description" : "A description for the security group rule that references this IPv4 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIp" : "The IPv4 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length."
    } ],
    "prefixListIds" : [ {
      "description" : "A description for the security group rule that references this prefix list ID. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "prefixListId" : "The ID of the prefix."
    } ],
    "fromPort" : "The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "toPort" : "The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes for the specified ICMP type. If you specify all ICMP/ICMPv6 types, you must specify all codes.",
    "groups" : [ {
      "groupName" : "The name of the security group. In a request, use this parameter for a security group in EC2-Classic or a default VPC only. For a security group in a nondefault VPC, use the security group ID.  \nFor a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.",
      "groupId" : "The ID of the security group.",
      "vpcId" : "The ID of the VPC for the referenced security group, if applicable.",
      "description" : "A description for the security group rule that references this user ID group pair. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "vpcPeeringConnectionId" : "The ID of the VPC peering connection, if applicable.",
      "peeringStatus" : "The status of a VPC peering connection, if applicable.",
      "userId" : "The ID of an AWS account. \nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned. \n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS account."
    } ],
    "ipProtocol" : "The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).  \n[EC2-VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6) allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed when authorizing rules. ",
    "ipv6Ranges" : [ {
      "description" : "A description for the security group rule that references this IPv6 address range. \nConstraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*",
      "cidrIpv6" : "The IPv6 CIDR range. You can either specify a CIDR range or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length."
    } ]
  } ],
  "GroupId" : "The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID."
}
```

</details>

