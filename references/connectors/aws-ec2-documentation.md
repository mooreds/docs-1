---
id: aws-ec2-documentation
title: AWS EC2 (version v1.*.*)
sidebar_label: AWS EC2
layout: docs.mustache
---

## accept_reserved_instances_exchange_quote

Accepts the Convertible Reserved Instance exchange quote described in the GetReservedInstancesExchangeQuote call.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptReservedInstancesExchangeQuote.html

<details><summary>Parameters</summary>

#### ReservedInstanceId (required)

The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or higher value.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TargetConfiguration

The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.

**Type:** ARRAY

</details>

## accept_transit_gateway_vpc_attachment

Accepts a request to attach a VPC to a transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptTransitGatewayVpcAttachment.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## accept_vpc_endpoint_connections

Accepts one or more interface VPC endpoint connection requests to your VPC endpoint service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcEndpointConnections.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The ID of the endpoint service.

**Type:** STRING

#### VpcEndpointId (required)

The IDs of one or more interface VPC endpoints.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## accept_vpc_peering_connection

Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the pending-acceptance state, and you must be the owner of the peer VPC. Use DescribeVpcPeeringConnections to view your outstanding VPC peering connection requests.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcPeeringConnection.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### VpcPeeringConnectionId

The ID of the VPC peering connection. You must specify this parameter in the request.

**Type:** STRING

</details>

## advertise_byoip_cidr

Advertises an IPv4 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP).  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html

<details><summary>Parameters</summary>

#### Cidr (required)

The IPv4 address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## allocate_address

Allocates an Elastic IP address to your AWS account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different AWS account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateAddress.html

<details><summary>Parameters</summary>

#### Address

[EC2-VPC] The Elastic IP address to recover or an IPv4 address from an address pool.

**Type:** STRING

#### Domain

Set to vpc to allocate the address for use with instances in a VPC. Default: The address is for use with instances in EC2-Classic.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PublicIpv4Pool

The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To specify a specific address from the address pool, use the Address parameter instead.

**Type:** STRING

</details>

## allocate_hosts

Allocates a Dedicated Host to your account. At a minimum, specify the instance size type, Availability Zone, and quantity of hosts to allocate.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateHosts.html

<details><summary>Parameters</summary>

#### AvailabilityZone (required)

The Availability Zone for the Dedicated Hosts.

**Type:** STRING

#### InstanceType (required)

Specify the instance type for which to configure your Dedicated Hosts. When you specify the instance type, that is the only instance type that you can launch onto that host.

**Type:** STRING

#### Quantity (required)

The number of Dedicated Hosts to allocate to your account with these parameters.

**Type:** INTEGER

#### AutoPlacement

This is enabled by default. This property allows instances to be automatically placed onto available Dedicated Hosts, when you are launching instances without specifying a host ID. Default: Enabled

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### TagSpecification

The tags to apply to the Dedicated Host during creation.

**Type:** ARRAY

</details>

## apply_security_groups_to_client_vpn_target_network

Applies a security group to the association between the target network and the Client VPN endpoint. This action replaces the existing security groups with the specified security groups.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplySecurityGroupsToClientVpnTargetNetwork.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### SecurityGroupId (required)

The IDs of the security groups to apply to the associated target network. Up to 5 security groups can  be applied to an associated target network.

**Type:** ARRAY

#### VpcId (required)

The ID of the VPC in which the associated target network is located.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## assign_private_ip_addresses

Assigns one or more secondary private IP addresses to the specified network interface. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### AllowReassignment

Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.

**Type:** BOOLEAN

#### PrivateIpAddress

One or more IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses. If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.

**Type:** ARRAY

#### SecondaryPrivateIpAddressCount

The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.

**Type:** INTEGER

</details>

## associate_address

Associates an Elastic IP address with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateAddress.html

<details><summary>Parameters</summary>

#### AllocationId

[EC2-VPC] The allocation ID. This is required for EC2-VPC.

**Type:** STRING

#### AllowReassociation

[EC2-VPC] For a VPC in an EC2-Classic account, specify true to allow an Elastic IP address that is already associated with an instance or network interface to be reassociated with the specified instance or network interface. Otherwise, the operation fails. In a VPC in an EC2-VPC-only account, reassociation is automatic, therefore you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### InstanceId

The ID of the instance. This is required for EC2-Classic. For EC2-VPC, you can specify either the instance ID or the network interface ID, but not both. The operation fails if you specify an instance ID unless exactly one network interface is attached.

**Type:** STRING

#### NetworkInterfaceId

[EC2-VPC] The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.

**Type:** STRING

#### PrivateIpAddress

[EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.

**Type:** STRING

#### PublicIp

The Elastic IP address. This is required for EC2-Classic.

**Type:** STRING

</details>

## associate_client_vpn_target_network

Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateClientVpnTargetNetwork.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### SubnetId (required)

The ID of the subnet to associate with the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## associate_dhcp_options

Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateDhcpOptions.html

<details><summary>Parameters</summary>

#### DhcpOptionsId (required)

The ID of the DHCP options set, or default to associate  no DHCP options with the VPC.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## associate_iam_instance_profile

Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html

<details><summary>Parameters</summary>

#### IamInstanceProfile (required)

The IAM instance profile.

**Type:** OBJECT

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

</details>

## associate_route_table

Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table from the subnet later. A route table can be associated with multiple subnets.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateRouteTable.html

<details><summary>Parameters</summary>

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

#### SubnetId (required)

The ID of the subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## associate_subnet_cidr_block

Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet. An IPv6 CIDR block must have a prefix length of /64.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSubnetCidrBlock.html

<details><summary>Parameters</summary>

#### Ipv6CidrBlock (required)

The IPv6 CIDR block for your subnet. The subnet must have a /64 prefix length.

**Type:** STRING

#### SubnetId (required)

The ID of your subnet.

**Type:** STRING

</details>

## associate_transit_gateway_route_table

Associates the specified attachment with the specified transit gateway route table. You can associate only one route table with an attachment.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayRouteTable.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## associate_vpc_cidr_block

Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, or you can associate an Amazon-provided IPv6 CIDR block. The IPv6 CIDR block size is fixed at /56.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateVpcCidrBlock.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### AmazonProvidedIpv6CidrBlock

Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.

**Type:** BOOLEAN

#### CidrBlock

An IPv4 CIDR block to associate with the VPC.

**Type:** STRING

</details>

## attach_classic_link_vpc

Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the running state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachClassicLinkVpc.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of an EC2-Classic instance to link to the ClassicLink-enabled VPC.

**Type:** STRING

#### SecurityGroupId (required)

The ID of one or more of the VPC's security groups. You cannot specify security groups from a different VPC.

**Type:** ARRAY

#### VpcId (required)

The ID of a ClassicLink-enabled VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## attach_internet_gateway

Attaches an internet gateway to a VPC, enabling connectivity between the internet and the VPC. For more information about your VPC and internet gateway, see the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachInternetGateway.html

<details><summary>Parameters</summary>

#### InternetGatewayId (required)

The ID of the internet gateway.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## attach_network_interface

Attaches a network interface to an instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachNetworkInterface.html

<details><summary>Parameters</summary>

#### DeviceIndex (required)

The index of the device for the network interface attachment.

**Type:** INTEGER

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## attach_volume

Attaches an EBS volume to a running or stopped instance and exposes it to the instance with the specified device name.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVolume.html

<details><summary>Parameters</summary>

#### Device (required)

The device name (for example, /dev/sdh or xvdh).

**Type:** STRING

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### VolumeId (required)

The ID of the EBS volume. The volume and instance must be within the same Availability Zone.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## attach_vpn_gateway

Attaches a virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVpnGateway.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### VpnGatewayId (required)

The ID of the virtual private gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## authorize_client_vpn_ingress

Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in AWS or on-premises networks.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeClientVpnIngress.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### TargetNetworkCidr (required)

The IPv4 address range, in CIDR notation, of the network for which access is being authorized.

**Type:** STRING

#### AccessGroupId

The ID of the Active Directory group to grant access.

**Type:** STRING

#### AuthorizeAllGroups

Indicates whether to grant access to all clients. Use true to grant all clients who successfully establish a VPN connection access to the network.

**Type:** BOOLEAN

#### Description

A brief description of the authorization rule.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## authorize_security_group_egress

[EC2-VPC only] Adds the specified egress rules to a security group for use with a VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html

<details><summary>Parameters</summary>

#### GroupId (required)

The ID of the security group.

**Type:** STRING

#### CidrIp

Not supported. Use a set of IP permissions to specify the CIDR.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### FromPort

Not supported. Use a set of IP permissions to specify the port.

**Type:** INTEGER

#### IpPermissions

The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set of permissions.

**Type:** ARRAY

#### IpProtocol

Not supported. Use a set of IP permissions to specify the protocol name or number.

**Type:** STRING

#### SourceSecurityGroupName

Not supported. Use a set of IP permissions to specify a destination security group.

**Type:** STRING

#### SourceSecurityGroupOwnerId

Not supported. Use a set of IP permissions to specify a destination security group.

**Type:** STRING

#### ToPort

Not supported. Use a set of IP permissions to specify the port.

**Type:** INTEGER

</details>

## authorize_security_group_ingress

Adds the specified ingress rules to a security group. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html

<details><summary>Parameters</summary>

#### CidrIp

The CIDR IPv4 address range. You can't specify this parameter when specifying a source security group. Alternatively, use a set of IP permissions to specify multiple rules and a description for the rule.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### FromPort

The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. For the ICMP/ICMPv6 type number, use -1 to specify all types. If you specify all ICMP/ICMPv6 types, you must specify all codes. Alternatively, use a set of IP permissions to specify multiple rules and a description for the rule.

**Type:** INTEGER

#### GroupId

The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.

**Type:** STRING

#### GroupName

[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.

**Type:** STRING

#### IpPermissions

The sets of IP permissions.

**Type:** ARRAY

#### IpProtocol

The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers). (VPC only) Use -1 to specify all protocols. If you specify -1, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For tcp, udp, and icmp, you must specify a port range. For protocol 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed. Alternatively, use a set of IP permissions to specify multiple rules and a description for the rule.

**Type:** STRING

#### SourceSecurityGroupName

[EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter  in combination with the following parameters: the CIDR IP address range, the start of the port range,  the IP protocol, and the end of the port range. Creates rules that grant full ICMP, UDP, and TCP access.  To create a rule with a specific IP protocol and port range, use a set of IP permissions instead. For  EC2-VPC, the source security group must be in the same VPC.

**Type:** STRING

#### SourceSecurityGroupOwnerId

[nondefault VPC] The AWS account ID for the source security group, if the source security group is  in a different account. You can't specify this parameter in combination with the following parameters:  the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range.  Creates rules that grant full ICMP, UDP, and TCP access. To create a rule with a specific IP protocol  and port range, use a set of IP permissions instead.

**Type:** STRING

#### ToPort

The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number. For the ICMP/ICMPv6 code number, use -1 to specify all codes. If you specify all ICMP/ICMPv6 types, you must specify all codes. Alternatively, use a set of IP permissions to specify multiple rules and a description for the rule.

**Type:** INTEGER

</details>

## bundle_instance

Bundles an Amazon instance store-backed Windows instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleInstance.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance to bundle. Type: String Default: None Required: Yes

**Type:** STRING

#### Storage (required)

The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## cancel_bundle_task

Cancels a bundling operation for an instance store-backed Windows instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelBundleTask.html

<details><summary>Parameters</summary>

#### BundleId (required)

The ID of the bundle task.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## cancel_capacity_reservation

Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to cancelled.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelCapacityReservation.html

<details><summary>Parameters</summary>

#### CapacityReservationId (required)

The ID of the Capacity Reservation to be cancelled.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides  an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise,  it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## cancel_conversion_task

Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelConversionTask.html

<details><summary>Parameters</summary>

#### ConversionTaskId (required)

The ID of the conversion task.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ReasonMessage

The reason for canceling the conversion task.

**Type:** STRING

</details>

## cancel_export_task

Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelExportTask.html

<details><summary>Parameters</summary>

#### ExportTaskId (required)

The ID of the export task. This is the ID returned by CreateInstanceExportTask.

**Type:** STRING

</details>

## cancel_import_task

Cancels an in-process import virtual machine or import snapshot task. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelImportTask.html

<details><summary>Parameters</summary>

#### CancelReason

The reason for canceling the task.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ImportTaskId

The ID of the import image or import snapshot task to be canceled.

**Type:** STRING

</details>

## cancel_reserved_instances_listing

Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelReservedInstancesListing.html

<details><summary>Parameters</summary>

#### ReservedInstancesListingId (required)

The ID of the Reserved Instance listing.

**Type:** STRING

</details>

## cancel_spot_fleet_requests

Cancels the specified Spot Fleet requests. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests.html

<details><summary>Parameters</summary>

#### SpotFleetRequestId (required)

The IDs of the Spot Fleet requests.

**Type:** ARRAY

#### TerminateInstances (required)

Indicates whether to terminate instances for a Spot Fleet request if it is canceled successfully.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## cancel_spot_instance_requests

Cancels one or more Spot Instance requests. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotInstanceRequests.html

<details><summary>Parameters</summary>

#### SpotInstanceRequestId (required)

One or more Spot Instance request IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## confirm_product_instance

Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user's instance is eligible for support.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConfirmProductInstance.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### ProductCode (required)

The product code. This must be a product code that you own.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## copy_fpga_image

Copies the specified Amazon FPGA Image (AFI) to the current region. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyFpgaImage.html

<details><summary>Parameters</summary>

#### SourceFpgaImageId (required)

The ID of the source AFI.

**Type:** STRING

#### SourceRegion (required)

The region that contains the source AFI.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  For more information, see Ensuring Idempotency.

**Type:** STRING

#### Description

The description for the new AFI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Name

The name for the new AFI. The default is the name of the source AFI.

**Type:** STRING

</details>

## copy_image

Initiates the copy of an AMI from the specified source region to the current region. You specify the destination region by using its endpoint when making the request.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyImage.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the new AMI in the destination region.

**Type:** STRING

#### SourceImageId (required)

The ID of the AMI to copy.

**Type:** STRING

#### SourceRegion (required)

The name of the region that contains the AMI to copy.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the  Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### Description

A description for the new AMI in the destination region.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Encrypted

Specifies whether the destination snapshots of the copied image should be encrypted. You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default CMK for EBS is used unless you specify a non-default  AWS Key Management Service (AWS KMS) CMK using KmsKeyId. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.

**Type:** BOOLEAN

#### KmsKeyId

An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  The CMK identifier may be provided in any of the following formats:  Key ID Key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.  ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.  AWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.  The specified CMK must exist in the region that the snapshot is being copied to.

**Type:** STRING

</details>

## copy_snapshot

Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3. You can copy the snapshot within the same Region or from one Region to another. You can use the snapshot to create EBS volumes or Amazon Machine Images (AMIs). The snapshot is copied to the regional endpoint that you send the HTTP request to.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopySnapshot.html

<details><summary>Parameters</summary>

#### SourceRegion (required)

The ID of the Region that contains the snapshot to be copied.

**Type:** STRING

#### SourceSnapshotId (required)

The ID of the EBS snapshot to copy.

**Type:** STRING

#### Description

A description for the EBS snapshot.

**Type:** STRING

#### DestinationRegion

The destination Region to use in the PresignedUrl parameter of a snapshot copy operation. This parameter is only valid for specifying the destination Region in a PresignedUrl parameter, where it is required. The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, ec2.us-east-1.amazonaws.com).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Encrypted

Specifies whether the destination snapshot should be encrypted. You can encrypt a copy of an unencrypted snapshot, but you cannot use it to create an unencrypted copy of an encrypted  snapshot. Your default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK  using KmsKeyId. For more information, see Amazon EBS Encryption in the  Amazon Elastic Compute Cloud User Guide.

**Type:** BOOLEAN

#### KmsKeyId

An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  The CMK identifier may be provided in any of the following formats:  Key ID Key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.  ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.  AWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail.

**Type:** STRING

#### PresignedUrl

When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see Query Requests. The PresignedUrl should use the snapshot source endpoint, the CopySnapshot action, and include the SourceRegion, SourceSnapshotId, and DestinationRegion parameters. The PresignedUrl must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in Authenticating Requests by Using Query Parameters (AWS Signature Version 4) in the Amazon Simple Storage Service API Reference. An invalid or improperly signed PresignedUrl will cause the copy operation to fail asynchronously, and the snapshot will move to an error state.

**Type:** STRING

</details>

## create_capacity_reservation

Creates a new Capacity Reservation with the specified attributes. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservation.html

<details><summary>Parameters</summary>

#### AvailabilityZone (required)

The Availability Zone in which to create the Capacity Reservation.

**Type:** STRING

#### InstanceCount (required)

The number of instances for which to reserve capacity.

**Type:** INTEGER

#### InstancePlatform (required)

The type of operating system for which to reserve capacity.

**Type:** STRING

#### InstanceType (required)

The instance type for which to reserve capacity. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency. Constraint: Maximum 64 ASCII characters.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides  an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise,  it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EbsOptimized

Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.

**Type:** BOOLEAN

#### EndDate

The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to expired when it reaches its end date and time. You must provide an EndDate value if EndDateType is limited. Omit EndDate if EndDateType is unlimited. If the EndDateType is limited, the Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify  5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.

**Type:** STRING

#### EndDateType

Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types: unlimited - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an EndDate if the EndDateType is unlimited. limited - The Capacity Reservation expires automatically at a specified date and time. You must provide an EndDate value if the EndDateType value is limited.

**Type:** STRING

#### EphemeralStorage

Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.

**Type:** BOOLEAN

#### InstanceMatchCriteria

Indicates the type of instance launches that the Capacity Reservation accepts. The options include: open - The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform,  and Availability Zone). Instances that have matching attributes run in the Capacity Reservation automatically without specifying  any additional parameters. targeted - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.  Default: open

**Type:** STRING

#### TagSpecifications

The tags to apply to the Capacity Reservation during launch.

**Type:** ARRAY

#### Tenancy

Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings: default - The Capacity Reservation is created on hardware that is shared with other AWS accounts. dedicated - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account.

**Type:** STRING

</details>

## create_client_vpn_endpoint

Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnEndpoint.html

<details><summary>Parameters</summary>

#### Authentication (required)

Information about the authentication method to be used to authenticate clients.

**Type:** ARRAY

#### ClientCidrBlock (required)

The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.

**Type:** STRING

#### ConnectionLogOptions (required)

Information about the client connection logging options. If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged: Client connection requests Client connection results (successful and unsuccessful) Reasons for unsuccessful client connection requests Client connection termination time

**Type:** OBJECT

#### ServerCertificateArn (required)

The ARN of the server certificate. For more information, see  the AWS Certificate Manager User Guide.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more  information, see  How to Ensure Idempotency.

**Type:** STRING

#### Description

A brief description of the Client VPN endpoint.

**Type:** STRING

#### DnsServers

Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TagSpecification

The tags to apply to the Client VPN endpoint during creation.

**Type:** ARRAY

#### TransportProtocol

The transport protocol to be used by the VPN session. Default value: udp

**Type:** STRING

</details>

## create_client_vpn_route

Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnRoute.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint to which to add the route.

**Type:** STRING

#### DestinationCidrBlock (required)

The IPv4 address range, in CIDR notation, of the route destination. For example: To add a route for Internet access, enter 0.0.0.0/0 To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range To add a route for an on-premises network, enter the AWS Site-to-Site VPN connection's IPv4 CIDR range Route address ranges cannot overlap with the CIDR range specified for client allocation.

**Type:** STRING

#### TargetVpcSubnetId (required)

The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of the Client VPN endpoint.

**Type:** STRING

#### Description

A brief description of the route.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_customer_gateway

Provides information to AWS about your VPN customer gateway device. The customer gateway is the appliance at your end of the VPN connection. (The device on the AWS side of the VPN connection is the virtual private gateway.) You must provide the Internet-routable IP address of the customer gateway's external interface. The IP address must be static and may be behind a device performing network address translation (NAT).  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCustomerGateway.html

<details><summary>Parameters</summary>

#### BgpAsn (required)

For devices that support BGP, the customer gateway's BGP ASN. Default: 65000

**Type:** INTEGER

#### IpAddress (required)

The Internet-routable IP address for the customer gateway's outside interface. The address must be static.

**Type:** STRING

#### Type (required)

The type of VPN connection that this customer gateway supports (ipsec.1).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_default_subnet

Creates a default subnet with a size /20 IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see Creating a Default Subnet in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultSubnet.html

<details><summary>Parameters</summary>

#### AvailabilityZone (required)

The Availability Zone in which to create the default subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_default_vpc

Creates a default VPC with a size /16 IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see Default VPC and Default Subnets in the Amazon Virtual Private Cloud User Guide. You cannot specify the components of the default VPC yourself.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultVpc.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_dhcp_options

Creates a set of DHCP options for your VPC. After creating the set, you must associate it with the VPC, causing all existing and new instances that you launch in the VPC to use this set of DHCP options. The following are the individual DHCP options you can specify. For more information about the options, see RFC 2132.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html

<details><summary>Parameters</summary>

#### DhcpConfiguration (required)

A DHCP configuration option.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_egress_only_internet_gateway

[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateEgressOnlyInternetGateway.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC for which to create the egress-only internet gateway.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_fleet

Launches an EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html

<details><summary>Parameters</summary>

#### LaunchTemplateConfigs (required)

The configuration for the EC2 Fleet.

**Type:** ARRAY

#### TargetCapacitySpecification (required)

The TotalTargetCapacity, OnDemandTargetCapacity, SpotTargetCapacity, and DefaultCapacityType structure.

**Type:** OBJECT

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ExcessCapacityTerminationPolicy

Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.

**Type:** STRING

#### OnDemandOptions

The allocation strategy of On-Demand Instances in an EC2 Fleet.

**Type:** OBJECT

#### ReplaceUnhealthyInstances

Indicates whether EC2 Fleet should replace unhealthy instances.

**Type:** BOOLEAN

#### SpotOptions

Describes the configuration of Spot Instances in an EC2 Fleet.

**Type:** OBJECT

#### TagSpecification

The key-value pair for tagging the EC2 Fleet request on creation. The value for ResourceType must be fleet, otherwise the fleet request fails. To tag instances at launch, specify the tags in the launch template. For information about tagging after launch, see Tagging Your Resources.

**Type:** ARRAY

#### TerminateInstancesWithExpiration

Indicates whether running instances should be terminated when the EC2 Fleet expires.

**Type:** BOOLEAN

#### Type

The type of the request. By default, the EC2 Fleet places an asynchronous request for your desired capacity, and maintains it by replenishing interrupted Spot Instances (maintain). A value of instant places a synchronous one-time request, and returns errors for any instances that could not be launched. A value of request places an asynchronous one-time request without maintaining capacity or submitting requests in alternative capacity pools if capacity is unavailable. For more information, see EC2 Fleet Request Types in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### ValidFrom

The start date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

**Type:** STRING

#### ValidUntil

The end date and time of the request, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.

**Type:** STRING

</details>

## create_flow_logs

Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFlowLogs.html

<details><summary>Parameters</summary>

#### ResourceId (required)

One or more subnet, network interface, or VPC IDs. Constraints: Maximum of 1000 resources

**Type:** ARRAY

#### ResourceType (required)

The type of resource on which to create the flow log.

**Type:** STRING

#### TrafficType (required)

The type of traffic to log.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.

**Type:** STRING

#### DeliverLogsPermissionArn

The ARN for the IAM role that's used to post flow logs to a log group.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LogDestination

Specifies the destination to which the flow log data is to be published. Flow log data can be published  to an CloudWatch Logs log group or an Amazon S3 bucket. The value specified for this parameter depends on the value specified for LogDestinationType. If LogDestinationType is not specified or cloud-watch-logs, specify the Amazon Resource Name  (ARN) of the CloudWatch Logs log group. If LogDestinationType is s3, specify the ARN of the Amazon S3 bucket. You can also specify a  subfolder in the bucket. To specify a subfolder in the bucket, use the following ARN format:  bucket_ARN/subfolder_name/. For example, to specify a subfolder named my-logs in a  bucket named my-bucket, use the following ARN: arn:aws:s3:::my-bucket/my-logs/. You  cannot use AWSLogs as a subfolder name. This is a reserved term.

**Type:** STRING

#### LogDestinationType

Specifies the type of destination to which the flow log data is to be published. Flow log data can be  published to CloudWatch Logs or Amazon S3. To publish flow log data to CloudWatch Logs, specify cloud-watch-logs. To  publish flow log data to Amazon S3, specify s3. Default: cloud-watch-logs

**Type:** STRING

#### LogGroupName

The name of the log group.

**Type:** STRING

</details>

## create_fpga_image

Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP). https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFpgaImage.html

<details><summary>Parameters</summary>

#### InputStorageLocation (required)

The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball.

**Type:** OBJECT

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  For more information, see Ensuring Idempotency.

**Type:** STRING

#### Description

A description for the AFI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LogsStorageLocation

The location in Amazon S3 for the output logs.

**Type:** OBJECT

#### Name

A name for the AFI.

**Type:** STRING

</details>

## create_image

Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### Name (required)

A name for the new image. Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)

**Type:** STRING

#### BlockDeviceMapping

Tthe block device mappings. This parameter cannot be used to modify the encryption status of existing volumes or snapshots. To create an AMI with encrypted snapshots, use the CopyImage action.

**Type:** ARRAY

#### Description

A description for the new image.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### NoReboot

By default, Amazon EC2 attempts to shut down and reboot the instance before creating the image. If the 'No Reboot' option is set, Amazon EC2 doesn't shut down the instance before creating the image. When this option is used, file system integrity on the created image can't be guaranteed.

**Type:** BOOLEAN

</details>

## create_instance_export_task

Exports a running or stopped instance to an S3 bucket. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceExportTask.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### Description

A description for the conversion task or the resource being exported. The maximum length is 255 bytes.

**Type:** STRING

#### ExportToS3

The format and location for an instance export task.

**Type:** OBJECT

#### TargetEnvironment

The target virtualization environment.

**Type:** STRING

</details>

## create_internet_gateway

Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using AttachInternetGateway.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInternetGateway.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_key_pair

Creates a 2048-bit RSA key pair with the specified name. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#1 private key. If a key with the specified name already exists, Amazon EC2 returns an error.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html

<details><summary>Parameters</summary>

#### KeyName (required)

A unique name for the key pair. Constraints: Up to 255 ASCII characters

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_launch_template

Creates a launch template. A launch template contains the parameters to launch an instance. When you launch an instance using RunInstances, you can specify a launch template instead of providing the launch parameters in the request.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html

<details><summary>Parameters</summary>

#### LaunchTemplateData (required)

The information for the launch template.

**Type:** OBJECT

#### LaunchTemplateName (required)

A name for the launch template.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency. Constraint: Maximum 128 ASCII characters.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### VersionDescription

A description for the first version of the launch template.

**Type:** STRING

</details>

## create_launch_template_version

Creates a new version for a launch template. You can specify an existing version of launch template from which to base the new version.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html

<details><summary>Parameters</summary>

#### LaunchTemplateData (required)

The information for the launch template.

**Type:** OBJECT

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency. Constraint: Maximum 128 ASCII characters.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchTemplateId

The ID of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateName

The name of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### SourceVersion

The version number of the launch template version on which to base the new version. The new version inherits the same launch parameters as the source version, except for parameters that you specify in LaunchTemplateData.

**Type:** STRING

#### VersionDescription

A description for the version of the launch template.

**Type:** STRING

</details>

## create_nat_gateway

Creates a NAT gateway in the specified public subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. Internet-bound traffic from a private subnet can be routed to the NAT gateway, therefore enabling instances in the private subnet to connect to the internet. For more information, see NAT Gateways in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNatGateway.html

<details><summary>Parameters</summary>

#### AllocationId (required)

The allocation ID of an Elastic IP address to associate with the NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it.

**Type:** STRING

#### SubnetId (required)

The subnet in which to create the NAT gateway.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency. Constraint: Maximum 64 ASCII characters.

**Type:** STRING

</details>

## create_network_acl

Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAcl.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_network_acl_entry

Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAclEntry.html

<details><summary>Parameters</summary>

#### Egress (required)

Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).

**Type:** BOOLEAN

#### NetworkAclId (required)

The ID of the network ACL.

**Type:** STRING

#### Protocol (required)

The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), "17" (UDP), or "1" (ICMP), traffic on all ports is  allowed, regardless of any ports or ICMP types or codes that you specify. If you specify  protocol "58" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and  codes allowed, regardless of any that you specify. If you specify protocol "58" (ICMPv6)  and specify an IPv6 CIDR block, you must specify an ICMP type and code.

**Type:** STRING

#### RuleAction (required)

Indicates whether to allow or deny the traffic that matches the rule.

**Type:** STRING

#### RuleNumber (required)

The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number. Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.

**Type:** INTEGER

#### CidrBlock

The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Icmp

ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol  1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.

**Type:** OBJECT

#### Ipv6CidrBlock

The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64).

**Type:** STRING

#### PortRange

TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).

**Type:** OBJECT

</details>

## create_network_interface

Creates a network interface in the specified subnet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html

<details><summary>Parameters</summary>

#### SubnetId (required)

The ID of the subnet to associate with the network interface.

**Type:** STRING

#### Description

A description for the network interface.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Ipv6AddressCount

The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses. If your subnet has the AssignIpv6AddressOnCreation attribute set to true, you can specify 0 to override this setting.

**Type:** INTEGER

#### Ipv6Addresses

One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying a number of IPv6 addresses.

**Type:** ARRAY

#### PrivateIpAddress

The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in privateIpAddresses as primary (only one IP address can be designated as primary).

**Type:** STRING

#### PrivateIpAddresses

One or more private IPv4 addresses.

**Type:** ARRAY

#### SecondaryPrivateIpAddressCount

The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses. The number of IP addresses you can assign to a network interface varies by instance type. For more information, see IP Addresses Per ENI Per Instance Type in the Amazon Virtual Private Cloud User Guide.

**Type:** INTEGER

#### SecurityGroupId

The IDs of one or more security groups.

**Type:** ARRAY

</details>

## create_network_interface_permission

Grants an AWS-authorized account permission to attach the specified network interface to an instance in their account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterfacePermission.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### Permission (required)

The type of permission to grant.

**Type:** STRING

#### AwsAccountId

The AWS account ID.

**Type:** STRING

#### AwsService

The AWS service. Currently not supported.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_placement_group

Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePlacementGroup.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### GroupName

A name for the placement group. Must be unique within the scope of your account for the Region. Constraints: Up to 255 ASCII characters

**Type:** STRING

#### PartitionCount

The number of partitions. Valid only when Strategy is set to partition.

**Type:** INTEGER

#### Strategy

The placement strategy.

**Type:** STRING

</details>

## create_reserved_instances_listing

Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the DescribeReservedInstances operation.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReservedInstancesListing.html

<details><summary>Parameters</summary>

#### ClientToken (required)

Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see  Ensuring Idempotency.

**Type:** STRING

#### InstanceCount (required)

The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.

**Type:** INTEGER

#### PriceSchedules (required)

A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.

**Type:** ARRAY

#### ReservedInstancesId (required)

The ID of the active Standard Reserved Instance.

**Type:** STRING

</details>

## create_route

Creates a route in a route table within a VPC. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html

<details><summary>Parameters</summary>

#### RouteTableId (required)

The ID of the route table for the route.

**Type:** STRING

#### DestinationCidrBlock

The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match.

**Type:** STRING

#### DestinationIpv6CidrBlock

The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EgressOnlyInternetGatewayId

[IPv6 traffic only] The ID of an egress-only internet gateway.

**Type:** STRING

#### GatewayId

The ID of an internet gateway or virtual private gateway attached to your VPC.

**Type:** STRING

#### InstanceId

The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.

**Type:** STRING

#### NatGatewayId

[IPv4 traffic only] The ID of a NAT gateway.

**Type:** STRING

#### NetworkInterfaceId

The ID of a network interface.

**Type:** STRING

#### TransitGatewayId

The ID of a transit gateway.

**Type:** STRING

#### VpcPeeringConnectionId

The ID of a VPC peering connection.

**Type:** STRING

</details>

## create_route_table

Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteTable.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_security_group

Creates a security group. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html

<details><summary>Parameters</summary>

#### GroupDescription (required)

A description for the security group. This is informational only. Constraints: Up to 255 characters in length Constraints for EC2-Classic: ASCII characters Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

**Type:** STRING

#### GroupName (required)

The name of the security group. Constraints: Up to 255 characters in length. Cannot start with sg-. Constraints for EC2-Classic: ASCII characters Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### VpcId

[EC2-VPC] The ID of the VPC. Required for EC2-VPC.

**Type:** STRING

</details>

## create_snapshot

Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use snapshots for backups, to make copies of EBS volumes, and to save data before shutting down an instance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the EBS volume.

**Type:** STRING

#### Description

A description for the snapshot.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TagSpecification

The tags to apply to the snapshot during creation.

**Type:** ARRAY

</details>

## create_spot_datafeed_subscription

Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per AWS account. For more information, see Spot Instance Data Feed in the Amazon EC2 User Guide for Linux Instances.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSpotDatafeedSubscription.html

<details><summary>Parameters</summary>

#### Bucket (required)

The Amazon S3 bucket in which to store the Spot Instance data feed.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Prefix

A prefix for the data feed file names.

**Type:** STRING

</details>

## create_subnet

Creates a subnet in an existing VPC. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnet.html

<details><summary>Parameters</summary>

#### CidrBlock (required)

The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### AvailabilityZone

The Availability Zone for the subnet. Default: AWS selects one for you. If you create more than one subnet in your VPC, we may not necessarily select a different zone for each subnet.

**Type:** STRING

#### AvailabilityZoneId

The AZ ID of the subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Ipv6CidrBlock

The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.

**Type:** STRING

</details>

## create_tags

Adds or overwrites the specified tags for the specified Amazon EC2 resource or resources. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html

<details><summary>Parameters</summary>

#### ResourceId (required)

The IDs of the resources, separated by spaces. Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.

**Type:** ARRAY

#### Tag (required)

The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_transit_gateway

Creates a transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGateway.html

<details><summary>Parameters</summary>

#### Description

A description of the transit gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Options

The transit gateway options.

**Type:** OBJECT

#### TagSpecification

The tags to apply to the transit gateway.

**Type:** ARRAY

</details>

## create_transit_gateway_route

Creates a static route for the specified transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRoute.html

<details><summary>Parameters</summary>

#### DestinationCidrBlock (required)

The CIDR range used for destination matches. Routing decisions are based on the most specific match.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### Blackhole

Indicates whether traffic matching this route is to be dropped.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TransitGatewayAttachmentId

The ID of the attachment.

**Type:** STRING

</details>

## create_transit_gateway_route_table

Creates a route table for the specified transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRouteTable.html

<details><summary>Parameters</summary>

#### TransitGatewayId (required)

The ID of the transit gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TagSpecifications

The tags to apply to the transit gateway route table.

**Type:** ARRAY

</details>

## create_transit_gateway_vpc_attachment

Attaches the specified VPC to the specified transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayVpcAttachment.html

<details><summary>Parameters</summary>

#### SubnetIds (required)

The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.

**Type:** ARRAY

#### TransitGatewayId (required)

The ID of the transit gateway.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Options

The VPC attachment options.

**Type:** OBJECT

#### TagSpecifications

The tags to apply to the VPC attachment.

**Type:** ARRAY

</details>

## create_volume

Creates an EBS volume that can be attached to an instance in the same Availability Zone. The volume is created in the regional endpoint that you send the HTTP request to. For more information see Regions and Endpoints.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html

<details><summary>Parameters</summary>

#### AvailabilityZone (required)

The Availability Zone in which to create the volume. Use DescribeAvailabilityZones to list the Availability Zones that are currently available to you.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Encrypted

Specifies whether the volume should be encrypted. Encrypted Amazon EBS volumes may only be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or vice versa. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide.

**Type:** BOOLEAN

#### Iops

The number of I/O operations per second (IOPS) to provision for the volume, with a maximum ratio of 50 IOPS/GiB. Range is 100 to 64,000 IOPS for volumes in most Regions. Maximum IOPS of 64,000 is guaranteed only on Nitro-based instances. Other instance families guarantee performance up to 32,000  IOPS. For more information, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide. This parameter is valid only for Provisioned IOPS SSD (io1) volumes.

**Type:** INTEGER

#### KmsKeyId

An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  The CMK identifier may be provided in any of the following formats:  Key ID Key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.  ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.  AWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. The action will eventually fail.

**Type:** STRING

#### Size

The size of the volume, in GiBs. Constraints: 1-16,384 for gp2, 4-16,384 for io1, 500-16,384 for st1, 500-16,384 for sc1, and 1-1,024 for standard. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size. Note At least one of Size or SnapshotId are required.

**Type:** INTEGER

#### SnapshotId

The snapshot from which to create the volume. Note At least one of Size or SnapshotId are required.

**Type:** STRING

#### TagSpecification

The tags to apply to the volume during creation.

**Type:** ARRAY

#### VolumeType

The volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes. Defaults: If no volume type is specified, the default is standard in us-east-1, eu-west-1, eu-central-1, us-west-2, us-west-1, sa-east-1, ap-northeast-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-south-1, us-gov-west-1, and cn-north-1. In all other Regions, EBS defaults to gp2.

**Type:** STRING

</details>

## create_vpc

Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). For more information about how large to make your VPC, see Your VPC and Subnets in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpc.html

<details><summary>Parameters</summary>

#### CidrBlock (required)

The IPv4 network range for the VPC, in CIDR notation. For example, 10.0.0.0/16.

**Type:** STRING

#### AmazonProvidedIpv6CidrBlock

Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### InstanceTenancy

The tenancy options for instances launched into the VPC. For default, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For dedicated, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.  Important: The host value cannot be used with this parameter. Use the default or dedicated values only. Default: default

**Type:** STRING

</details>

## create_vpc_endpoint

Creates a VPC endpoint for a specified service. An endpoint enables you to create a private connection between your VPC and the service. The service may be provided by AWS, an AWS Marketplace partner, or another AWS account. For more information, see VPC Endpoints in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpoint.html

<details><summary>Parameters</summary>

#### ServiceName (required)

The service name. To get a list of available services, use the DescribeVpcEndpointServices request, or get the name from the service provider.

**Type:** STRING

#### VpcId (required)

The ID of the VPC in which the endpoint will be used.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PolicyDocument

A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format. If this parameter is not specified, we attach a default policy that allows full access to the service.

**Type:** STRING

#### PrivateDnsEnabled

(Interface endpoint) Indicate whether to associate a private hosted zone with the specified VPC. The private hosted zone contains a record set for the default public DNS name for the service for the region (for example, kinesis.us-east-1.amazonaws.com) which resolves to the private IP addresses of the endpoint network interfaces in the VPC. This enables you to make requests to the default public DNS name for the service instead of the public DNS names that are automatically generated by the VPC endpoint service. To use a private hosted zone, you must set the following VPC attributes to true: enableDnsHostnames and enableDnsSupport. Use ModifyVpcAttribute to set the VPC attributes. Default: false

**Type:** BOOLEAN

#### RouteTableId

(Gateway endpoint) One or more route table IDs.

**Type:** ARRAY

#### SecurityGroupId

(Interface endpoint) The ID of one or more security groups to associate with the endpoint network interface.

**Type:** ARRAY

#### SubnetId

(Interface endpoint) The ID of one or more subnets in which to create an endpoint network interface.

**Type:** ARRAY

#### VpcEndpointType

The type of endpoint. Default: Gateway

**Type:** STRING

</details>

## create_vpc_endpoint_connection_notification

Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see Create a Topic in the Amazon Simple Notification Service Developer Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html

<details><summary>Parameters</summary>

#### ConnectionEvents (required)

One or more endpoint events for which to receive notifications. Valid values are Accept, Connect, Delete, and Reject.

**Type:** ARRAY

#### ConnectionNotificationArn (required)

The ARN of the SNS topic for the notifications.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ServiceId

The ID of the endpoint service.

**Type:** STRING

#### VpcEndpointId

The ID of the endpoint.

**Type:** STRING

</details>

## create_vpc_endpoint_service_configuration

Creates a VPC endpoint service configuration to which service consumers (AWS accounts, IAM users, and IAM roles) can connect. Service consumers can create an interface VPC endpoint to connect to your service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointServiceConfiguration.html

<details><summary>Parameters</summary>

#### NetworkLoadBalancerArn (required)

The Amazon Resource Names (ARNs) of one or more Network Load Balancers for your service.

**Type:** ARRAY

#### AcceptanceRequired

Indicate whether requests from service consumers to create an endpoint to your service must be accepted. To accept a request, use AcceptVpcEndpointConnections.

**Type:** BOOLEAN

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see How to Ensure Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## create_vpc_peering_connection

Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another AWS account and can be in a different Region to the requester VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcPeeringConnection.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PeerOwnerId

The AWS account ID of the owner of the accepter VPC. Default: Your AWS account ID

**Type:** STRING

#### PeerRegion

The region code for the accepter VPC, if the accepter VPC is located in a region other than the region in which you make the request. Default: The region in which you make the request.

**Type:** STRING

#### PeerVpcId

The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.

**Type:** STRING

#### VpcId

The ID of the requester VPC. You must specify this parameter in the request.

**Type:** STRING

</details>

## create_vpn_connection

Creates a VPN connection between an existing virtual private gateway and a VPN customer gateway. The only supported connection type is ipsec.1.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnection.html

<details><summary>Parameters</summary>

#### CustomerGatewayId (required)

The ID of the customer gateway.

**Type:** STRING

#### Type (required)

The type of VPN connection (ipsec.1).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Options

The options for the VPN connection.

**Type:** OBJECT

#### TransitGatewayId

The ID of the transit gateway. If you specify a transit gateway, you cannot specify a virtual private gateway.

**Type:** STRING

#### VpnGatewayId

The ID of the virtual private gateway. If you specify a virtual private gateway, you cannot specify a transit gateway.

**Type:** STRING

</details>

## create_vpn_connection_route

Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.html

<details><summary>Parameters</summary>

#### DestinationCidrBlock (required)

The CIDR block associated with the local subnet of the customer network.

**Type:** STRING

#### VpnConnectionId (required)

The ID of the VPN connection.

**Type:** STRING

</details>

## create_vpn_gateway

Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnGateway.html

<details><summary>Parameters</summary>

#### Type (required)

The type of VPN connection this virtual private gateway supports.

**Type:** STRING

#### AmazonSideAsn

A private Autonomous System Number (ASN) for the Amazon side of a BGP session. If you're using a 16-bit ASN, it must be in the 64512 to 65534 range. If you're using a 32-bit ASN, it must be in the 4200000000 to 4294967294 range. Default: 64512

**Type:** OBJECT

#### AvailabilityZone

The Availability Zone for the virtual private gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_client_vpn_endpoint

Deletes the specified Client VPN endpoint. You must disassociate all target networks before you can delete a Client VPN endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnEndpoint.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN to be deleted.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_client_vpn_route

Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the CreateClientVpnRoute action. You cannot delete routes that were automatically added when associating a subnet. To remove routes that have been automatically added, disassociate the target subnet from the Client VPN endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnRoute.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint from which the route is to be deleted.

**Type:** STRING

#### DestinationCidrBlock (required)

The IPv4 address range, in CIDR notation, of the route to be deleted.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TargetVpcSubnetId

The ID of the target subnet used by the route.

**Type:** STRING

</details>

## delete_customer_gateway

Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCustomerGateway.html

<details><summary>Parameters</summary>

#### CustomerGatewayId (required)

The ID of the customer gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_dhcp_options

Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteDhcpOptions.html

<details><summary>Parameters</summary>

#### DhcpOptionsId (required)

The ID of the DHCP options set.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_egress_only_internet_gateway

Deletes an egress-only internet gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteEgressOnlyInternetGateway.html

<details><summary>Parameters</summary>

#### EgressOnlyInternetGatewayId (required)

The ID of the egress-only internet gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_fleets

Deletes the specified EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFleets.html

<details><summary>Parameters</summary>

#### FleetId (required)

The IDs of the EC2 Fleets.

**Type:** ARRAY

#### TerminateInstances (required)

Indicates whether to terminate instances for an EC2 Fleet if it is deleted successfully.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_flow_logs

Deletes one or more flow logs. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html

<details><summary>Parameters</summary>

#### FlowLogId (required)

One or more flow log IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_fpga_image

Deletes the specified Amazon FPGA Image (AFI). https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFpgaImage.html

<details><summary>Parameters</summary>

#### FpgaImageId (required)

The ID of the AFI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_internet_gateway

Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteInternetGateway.html

<details><summary>Parameters</summary>

#### InternetGatewayId (required)

The ID of the internet gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_key_pair

Deletes the specified key pair, by removing the public key from Amazon EC2. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteKeyPair.html

<details><summary>Parameters</summary>

#### KeyName (required)

The name of the key pair.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_launch_template

Deletes a launch template. Deleting a launch template deletes all of its versions. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplate.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchTemplateId

The ID of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateName

The name of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

</details>

## delete_launch_template_versions

Deletes one or more versions of a launch template. You cannot delete the default version of a launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must delete the entire launch template using DeleteLaunchTemplate.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplateVersions.html

<details><summary>Parameters</summary>

#### LaunchTemplateVersion (required)

The version numbers of one or more launch template versions to delete.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchTemplateId

The ID of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateName

The name of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

</details>

## delete_nat_gateway

Deletes the specified NAT gateway. Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNatGateway.html

<details><summary>Parameters</summary>

#### NatGatewayId (required)

The ID of the NAT gateway.

**Type:** STRING

</details>

## delete_network_acl

Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAcl.html

<details><summary>Parameters</summary>

#### NetworkAclId (required)

The ID of the network ACL.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_network_acl_entry

Deletes the specified ingress or egress entry (rule) from the specified network ACL. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAclEntry.html

<details><summary>Parameters</summary>

#### Egress (required)

Indicates whether the rule is an egress rule.

**Type:** BOOLEAN

#### NetworkAclId (required)

The ID of the network ACL.

**Type:** STRING

#### RuleNumber (required)

The rule number of the entry to delete.

**Type:** INTEGER

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_network_interface

Deletes the specified network interface. You must detach the network interface before you can delete it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_network_interface_permission

Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. However, you can force delete the permission, regardless of any attachment.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterfacePermission.html

<details><summary>Parameters</summary>

#### NetworkInterfacePermissionId (required)

The ID of the network interface permission.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Force

Specify true to remove the permission even if the network interface is attached to an instance.

**Type:** BOOLEAN

</details>

## delete_placement_group

Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeletePlacementGroup.html

<details><summary>Parameters</summary>

#### GroupName (required)

The name of the placement group.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_route

Deletes the specified route from the specified route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html

<details><summary>Parameters</summary>

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

#### DestinationCidrBlock

The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

**Type:** STRING

#### DestinationIpv6CidrBlock

The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_route_table

Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRouteTable.html

<details><summary>Parameters</summary>

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_security_group

Deletes a security group. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### GroupId

The ID of the security group. Required for a nondefault VPC.

**Type:** STRING

#### GroupName

[EC2-Classic, default VPC] The name of the security group. You can specify either the security group name or the security group ID.

**Type:** STRING

</details>

## delete_snapshot

Deletes the specified snapshot. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html

<details><summary>Parameters</summary>

#### SnapshotId (required)

The ID of the EBS snapshot.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_spot_datafeed_subscription

Deletes the data feed for Spot Instances. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSpotDatafeedSubscription.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_subnet

Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSubnet.html

<details><summary>Parameters</summary>

#### SubnetId (required)

The ID of the subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_tags

Deletes the specified set of tags from the specified set of resources. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTags.html

<details><summary>Parameters</summary>

#### ResourceId (required)

The IDs of the resources, separated by spaces. Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Tag

The tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key without a tag value, we delete any tag with this key regardless of its value. If you specify a tag key with an empty string as the tag value, we delete the tag only if its value is an empty string. If you omit this parameter, we delete all user-defined tags for the specified resources. We do not delete AWS-generated tags (tags that have the aws: prefix).

**Type:** ARRAY

</details>

## delete_transit_gateway

Deletes the specified transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGateway.html

<details><summary>Parameters</summary>

#### TransitGatewayId (required)

The ID of the transit gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_transit_gateway_route

Deletes the specified route from the specified transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRoute.html

<details><summary>Parameters</summary>

#### DestinationCidrBlock (required)

The CIDR range for the route. This must match the CIDR for the route exactly.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_transit_gateway_route_table

Deletes the specified transit gateway route table. You must disassociate the route table from any transit gateway route tables before you can delete it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRouteTable.html

<details><summary>Parameters</summary>

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_transit_gateway_vpc_attachment

Deletes the specified VPC attachment. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayVpcAttachment.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_volume

Deletes the specified EBS volume. The volume must be in the available state (not attached to an instance).  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVolume.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpc

Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except the default one), and so on.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpc.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpc_endpoint_connection_notifications

Deletes one or more VPC endpoint connection notifications. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointConnectionNotifications.html

<details><summary>Parameters</summary>

#### ConnectionNotificationId (required)

One or more notification IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpc_endpoint_service_configurations

Deletes one or more VPC endpoint service configurations in your account. Before you delete the endpoint service configuration, you must reject any Available or PendingAcceptance interface endpoint connections that are attached to the service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointServiceConfigurations.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The IDs of one or more services.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpc_endpoints

Deletes one or more specified VPC endpoints. Deleting a gateway endpoint also deletes the endpoint routes in the route tables that were associated with the endpoint. Deleting an interface endpoint deletes the endpoint network interfaces.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpoints.html

<details><summary>Parameters</summary>

#### VpcEndpointId (required)

One or more VPC endpoint IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpc_peering_connection

Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the accepter VPC can delete the VPC peering connection if it's in the active state. The owner of the requester VPC can delete a VPC peering connection in the pending-acceptance state. You cannot delete a VPC peering connection that's in the failed state.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcPeeringConnection.html

<details><summary>Parameters</summary>

#### VpcPeeringConnectionId (required)

The ID of the VPC peering connection.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpn_connection

Deletes the specified VPN connection. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnection.html

<details><summary>Parameters</summary>

#### VpnConnectionId (required)

The ID of the VPN connection.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## delete_vpn_connection_route

Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.html

<details><summary>Parameters</summary>

#### DestinationCidrBlock (required)

The CIDR block associated with the local subnet of the customer network.

**Type:** STRING

#### VpnConnectionId (required)

The ID of the VPN connection.

**Type:** STRING

</details>

## delete_vpn_gateway

Deletes the specified virtual private gateway. We recommend that before you delete a virtual private gateway, you detach it from the VPC and delete the VPN connection. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnGateway.html

<details><summary>Parameters</summary>

#### VpnGatewayId (required)

The ID of the virtual private gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## deprovision_byoip_cidr

Releases the specified address range that you provisioned for use with your AWS resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionByoipCidr.html

<details><summary>Parameters</summary>

#### Cidr (required)

The public IPv4 address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## deregister_image

Deregisters the specified AMI. After you deregister an AMI, it can't be used to launch new instances; however, it doesn't affect any instances that you've already launched from the AMI. You'll continue to incur usage costs for those instances until you terminate them.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterImage.html

<details><summary>Parameters</summary>

#### ImageId (required)

The ID of the AMI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_account_attributes

Describes attributes of your AWS account. The following are the supported account attributes:  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAccountAttributes.html

<details><summary>Parameters</summary>

#### AttributeName

The account attribute names.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_addresses

Describes the specified Elastic IP addresses or all of your Elastic IP addresses. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html

<details><summary>Parameters</summary>

#### AllocationId

[EC2-VPC] Information about the allocation IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive. allocation-id - [EC2-VPC] The allocation ID for the address. association-id - [EC2-VPC] The association ID for the address. domain - Indicates whether the address is for use in EC2-Classic (standard)  or in a VPC (vpc). instance-id - The ID of the instance the address is associated with, if any. network-interface-id - [EC2-VPC] The ID of the network interface that the address is associated with, if any. network-interface-owner-id - The AWS account ID of the owner. private-ip-address - [EC2-VPC] The private IP address associated with the Elastic IP address. public-ip - The Elastic IP address. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### PublicIp

One or more Elastic IP addresses. Default: Describes all your Elastic IP addresses.

**Type:** ARRAY

</details>

## describe_aggregate_id_format

Describes the longer ID format settings for all resource types in a specific region. This request is useful for performing a quick audit to determine whether a specific region is fully opted in for longer IDs (17-character IDs).  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAggregateIdFormat.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_availability_zones

Describes the Availability Zones that are available to you. The results include zones only for the region you're currently using. If there is an event impacting an Availability Zone, you can use this request to view the state and any provided message for that Availability Zone.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. message - Information about the Availability Zone. region-name - The name of the region for the Availability Zone (for example, us-east-1). state - The state of the Availability Zone (available | information | impaired | unavailable). zone-id - The ID of the Availability Zone (for example, use1-az1). zone-name - The name of the Availability Zone (for example, us-east-1a).

**Type:** ARRAY

#### ZoneId

The IDs of the Availability Zones.

**Type:** ARRAY

#### ZoneName

The names of the Availability Zones.

**Type:** ARRAY

</details>

## describe_bundle_tasks

Describes the specified bundle tasks or all of your bundle tasks. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeBundleTasks.html

<details><summary>Parameters</summary>

#### BundleId

The bundle task IDs. Default: Describes all your bundle tasks.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. bundle-id - The ID of the bundle task. error-code - If the task failed, the error code returned. error-message - If the task failed, the error message returned. instance-id - The ID of the instance. progress - The level of task completion, as a percentage (for example, 20%). s3-bucket - The Amazon S3 bucket to store the AMI. s3-prefix - The beginning of the AMI name. start-time - The time the task started (for example, 2013-09-15T17:15:20.000Z). state - The state of the task (pending | waiting-for-shutdown | bundling | storing | cancelling | complete | failed). update-time - The time of the most recent update for the task.

**Type:** ARRAY

</details>

## describe_byoip_cidrs

Describes the IP address ranges that were specified in calls to ProvisionByoipCidr.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeByoipCidrs.html

<details><summary>Parameters</summary>

#### MaxResults (required)

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### NextToken

The token for the next page of results.

**Type:** STRING

</details>

## describe_capacity_reservations

Describes one or more of your Capacity Reservations. The results describe only the Capacity Reservations in the AWS Region that you're currently using.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html

<details><summary>Parameters</summary>

#### CapacityReservationId

The ID of the Capacity Reservation.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides  an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise,  it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return for the request in a single page. The remaining results can be seen by  sending another request with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token to retrieve the next page of results.

**Type:** STRING

</details>

## describe_classic_link_instances

Describes one or more of your linked EC2-Classic instances. This request only returns information about EC2-Classic instances linked to a VPC through ClassicLink. You cannot use this request to return information about other instances.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. group-id - The ID of a VPC security group that's associated with the instance. instance-id - The ID of the instance. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC to which the instance is linked. vpc-id - The ID of the VPC that the instance is linked to.

**Type:** ARRAY

#### InstanceId

One or more instance IDs. Must be instances linked to a VPC through ClassicLink.

**Type:** ARRAY

</details>

## describe_client_vpn_authorization_rules

Describes the authorization rules for a specified Client VPN endpoint. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnAuthorizationRules.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive.

**Type:** ARRAY

</details>

## describe_client_vpn_connections

Describes active client connections and connections that have been terminated within the last 60 minutes for the specified Client VPN endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnConnections.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive.

**Type:** ARRAY

</details>

## describe_client_vpn_endpoints

Describes one or more Client VPN endpoints in the account. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnEndpoints.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId

The ID of the Client VPN endpoint.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive.

**Type:** ARRAY

</details>

## describe_client_vpn_routes

Describes the routes for the specified Client VPN endpoint. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnRoutes.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive.

**Type:** ARRAY

</details>

## describe_client_vpn_target_networks

Describes the target networks associated with the specified Client VPN endpoint. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnTargetNetworks.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### AssociationIds

The IDs of the target network associations.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. Filter names and values are case-sensitive.

**Type:** ARRAY

</details>

## describe_conversion_tasks

Describes the specified conversion tasks or all your conversion tasks. For more information, see the VM Import/Export User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeConversionTasks.html

<details><summary>Parameters</summary>

#### ConversionTaskId

The conversion task IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_customer_gateways

Describes one or more of your VPN customer gateways. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html

<details><summary>Parameters</summary>

#### CustomerGatewayId

One or more customer gateway IDs. Default: Describes all your customer gateways.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. bgp-asn - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN). customer-gateway-id - The ID of the customer gateway. ip-address - The IP address of the customer gateway's Internet-routable external interface. state - The state of the customer gateway (pending | available | deleting | deleted). type - The type of customer gateway. Currently, the only supported type is ipsec.1. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

</details>

## describe_dhcp_options

Describes one or more of your DHCP options sets. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDhcpOptions.html

<details><summary>Parameters</summary>

#### DhcpOptionsId

The IDs of one or more DHCP options sets. Default: Describes all your DHCP options sets.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. dhcp-options-id - The ID of a DHCP options set. key - The key for one of the options (for example, domain-name). value - The value for one of the options. owner-id - The ID of the AWS account that owns the DHCP options set. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

</details>

## describe_egress_only_internet_gateways

Describes one or more of your egress-only internet gateways. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeEgressOnlyInternetGateways.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EgressOnlyInternetGatewayId

One or more egress-only internet gateway IDs.

**Type:** ARRAY

</details>

## describe_elastic_gpus

Describes the Elastic Graphics accelerator associated with your instances. For more information about Elastic Graphics, see Amazon Elastic Graphics.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeElasticGpus.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ElasticGpuId

The Elastic Graphics accelerator IDs.

**Type:** ARRAY

#### Filter

The filters. availability-zone - The Availability Zone in which the Elastic Graphics accelerator resides. elastic-gpu-health - The status of the Elastic Graphics accelerator (OK | IMPAIRED). elastic-gpu-state - The state of the Elastic Graphics accelerator (ATTACHED). elastic-gpu-type - The type of Elastic Graphics accelerator; for example, eg1.medium. instance-id - The ID of the instance to which the Elastic Graphics accelerator is associated.

**Type:** ARRAY

</details>

## describe_export_tasks

Describes the specified export tasks or all your export tasks. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportTasks.html

<details><summary>Parameters</summary>

#### ExportTaskId

The export task IDs.

**Type:** ARRAY

</details>

## describe_fleet_history

Describes the events for the specified EC2 Fleet during the specified time. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetHistory.html

<details><summary>Parameters</summary>

#### FleetId (required)

The ID of the EC2 Fleet.

**Type:** STRING

#### StartTime (required)

The start date and time for the events, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EventType

The type of events to describe. By default, all events are described.

**Type:** STRING

#### MaxResults

The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

The token for the next set of results.

**Type:** STRING

</details>

## describe_fleet_instances

Describes the running instances for the specified EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetInstances.html

<details><summary>Parameters</summary>

#### FleetId (required)

The ID of the EC2 Fleet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. instance-type - The instance type.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

The token for the next set of results.

**Type:** STRING

</details>

## describe_fleets

Describes the specified EC2 Fleets or all your EC2 Fleets. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleets.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. activity-status - The progress of the EC2 Fleet ( error | pending-fulfillment | pending-termination | fulfilled). excess-capacity-termination-policy - Indicates whether to terminate running instances if the target capacity is decreased below the current EC2 Fleet size (true | false). fleet-state - The state of the EC2 Fleet (submitted | active | deleted | failed | deleted-running | deleted-terminating | modifying). replace-unhealthy-instances - Indicates whether EC2 Fleet should replace unhealthy instances (true | false). type - The type of request (instant | request | maintain).

**Type:** ARRAY

#### FleetId

The ID of the EC2 Fleets.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call. Specify a value between 1 and 1000. The default value is 1000. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

The token for the next set of results.

**Type:** STRING

</details>

## describe_flow_logs

Describes one or more flow logs. To view the information in your flow logs (the log streams for the network interfaces), you must use the CloudWatch Logs console or the CloudWatch Logs API.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. deliver-log-status - The status of the logs delivery (SUCCESS | FAILED). log-destination-type - The type of destination to which the flow log publishes data. Possible destination types include cloud-watch-logs and S3. flow-log-id - The ID of the flow log. log-group-name - The name of the log group. resource-id - The ID of the VPC, subnet, or network interface. traffic-type - The type of traffic (ACCEPT | REJECT | ALL).

**Type:** ARRAY

#### FlowLogId

One or more flow log IDs.

**Type:** ARRAY

</details>

## describe_fpga_image_attribute

Describes the specified attribute of the specified Amazon FPGA Image (AFI). https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImageAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The AFI attribute.

**Type:** STRING

#### FpgaImageId (required)

The ID of the AFI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_fpga_images

Describes the Amazon FPGA Images (AFIs) available to you. These include public AFIs, private AFIs that you own, and AFIs owned by other AWS accounts for which you have load permissions.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImages.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. create-time - The creation time of the AFI. fpga-image-id - The FPGA image identifier (AFI ID). fpga-image-global-id - The global FPGA image identifier (AGFI ID). name - The name of the AFI. owner-id - The AWS account ID of the AFI owner. product-code - The product code. shell-version - The version of the AWS Shell that was used to create the bitstream. state - The state of the AFI (pending | failed | available | unavailable). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. update-time - The time of the most recent update.

**Type:** ARRAY

#### FpgaImageId

The AFI IDs.

**Type:** ARRAY

#### Owner

Filters the AFI by owner. Specify an AWS account ID, self (owner is the sender of the request), or an AWS owner alias (valid values are amazon | aws-marketplace).

**Type:** ARRAY

</details>

## describe_host_reservation_offerings

Describes the Dedicated Host reservations that are available to purchase. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservationOfferings.html

<details><summary>Parameters</summary>

#### Filter

The filters. instance-family - The instance family of the offering (for example, m4). payment-option - The payment option (NoUpfront | PartialUpfront | AllUpfront).

**Type:** ARRAY

#### MaxDuration

This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.

**Type:** INTEGER

#### MinDuration

This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.

**Type:** INTEGER

#### OfferingId

The ID of the reservation offering.

**Type:** STRING

</details>

## describe_host_reservations

Describes reservations that are associated with Dedicated Hosts in your account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservations.html

<details><summary>Parameters</summary>

#### Filter

The filters. instance-family - The instance family (for example, m4). payment-option - The payment option (NoUpfront | PartialUpfront | AllUpfront). state - The state of the reservation (payment-pending | payment-failed | active | retired). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### HostReservationIdSet

The host reservation IDs.

**Type:** ARRAY

</details>

## describe_hosts

Describes the specified Dedicated Hosts or all your Dedicated Hosts. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHosts.html

<details><summary>Parameters</summary>

#### Filter

The filters. auto-placement - Whether auto-placement is enabled or disabled (on | off). availability-zone - The Availability Zone of the host. client-token - The idempotency token that you provided when you allocated the host. host-reservation-id - The ID of the reservation assigned to this host. instance-type - The instance type size that the Dedicated Host is configured to support. state - The allocation state of the Dedicated Host (available | under-assessment | permanent-failure | released | released-permanent-failure). tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### HostId

The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.

**Type:** ARRAY

#### NextToken

The token to retrieve the next page of results.

**Type:** STRING

</details>

## describe_iam_instance_profile_associations

Describes your IAM instance profile associations. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.html

<details><summary>Parameters</summary>

#### AssociationId

The IAM instance profile associations.

**Type:** ARRAY

#### Filter

The filters. instance-id - The ID of the instance. state - The state of the association (associating | associated | disassociating | disassociated).

**Type:** ARRAY

</details>

## describe_id_format

Describes the ID format settings for your resources on a per-region basis, for example, to view which resource types are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdFormat.html

<details><summary>Parameters</summary>

#### Resource

The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway

**Type:** STRING

</details>

## describe_identity_id_format

Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see Resource IDs in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdentityIdFormat.html

<details><summary>Parameters</summary>

#### PrincipalArn (required)

The ARN of the principal, which can be an IAM role, IAM user, or the root user.

**Type:** STRING

#### Resource

The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway

**Type:** STRING

</details>

## describe_image_attribute

Describes the specified attribute of the specified AMI. You can specify only one attribute at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The AMI attribute. Note: Depending on your account privileges, the blockDeviceMapping attribute may return a Client.AuthFailure error. If this happens, use DescribeImages to get information about the block device mapping for the AMI.

**Type:** STRING

#### ImageId (required)

The ID of the AMI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_images

Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of the images available to you.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ExecutableBy

Scopes the images by users with explicit launch permissions.  Specify an AWS account ID, self (the sender of the request), or all (public AMIs).

**Type:** ARRAY

#### Filter

The filters. architecture - The image architecture (i386 | x86_64). block-device-mapping.delete-on-termination - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination. block-device-mapping.device-name - The device name specified in the block device mapping (for example, /dev/sdh or xvdh). block-device-mapping.snapshot-id - The ID of the snapshot used for the EBS volume. block-device-mapping.volume-size - The volume size of the EBS volume, in GiB. block-device-mapping.volume-type - The volume type of the EBS volume (gp2 | io1 | st1 | sc1 | standard). block-device-mapping.encrypted - A Boolean that indicates whether the EBS volume is encrypted. description - The description of the image (provided during image creation). ena-support - A Boolean that indicates whether enhanced networking with ENA is enabled. hypervisor - The hypervisor type (ovm | xen). image-id - The ID of the image. image-type - The image type (machine | kernel | ramdisk). is-public - A Boolean that indicates whether the image is public. kernel-id - The kernel ID. manifest-location - The location of the image manifest. name - The name of the AMI (provided during image creation). owner-alias - String value from an Amazon-maintained list (amazon | aws-marketplace | microsoft) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. owner-id - The AWS account ID of the image owner. platform - The platform. To only list Windows-based AMIs, use windows. product-code - The product code. product-code.type - The type of the product code (devpay | marketplace). ramdisk-id - The RAM disk ID. root-device-name - The device name of the root device volume (for example, /dev/sda1). root-device-type - The type of the root device volume (ebs | instance-store). state - The state of the image (available | pending | failed). state-reason-code - The reason code for the state change. state-reason-message - The message for the state change. sriov-net-support - A value of simple indicates that enhanced networking with the Intel 82599 VF interface is enabled. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. virtualization-type - The virtualization type (paravirtual | hvm).

**Type:** ARRAY

#### ImageId

The image IDs. Default: Describes all images available to you.

**Type:** ARRAY

#### Owner

Filters the images by the owner. Specify an AWS account ID, self (owner is the sender of the request), or an AWS owner alias (valid values are amazon | aws-marketplace | microsoft). Omitting this option returns all images for which you have launch permissions, regardless of ownership.

**Type:** ARRAY

</details>

## describe_import_image_tasks

Displays details about an import virtual machine or import snapshot tasks that are already created.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportImageTasks.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filters

Filter tasks using the task-state filter and one of the following values: active, completed, deleting, deleted.

**Type:** ARRAY

#### ImportTaskId

A list of import image task IDs.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

A token that indicates the next page of results.

**Type:** STRING

</details>

## describe_import_snapshot_tasks

Describes your import snapshot tasks. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filters

The filters.

**Type:** ARRAY

#### ImportTaskId

A list of import snapshot task IDs.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

A token that indicates the next page of results.

**Type:** STRING

</details>

## describe_instance_attribute

Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Valid attribute values are: instanceType | kernel | ramdisk | userData | disableApiTermination | instanceInitiatedShutdownBehavior | rootDeviceName | blockDeviceMapping | productCodes | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The instance attribute. Note: The enaSupport attribute is not supported at this time.

**Type:** STRING

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_instance_credit_specifications

Describes the credit option for CPU usage of the specified T2 or T3 instances. The credit options are standard and unlimited.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceCreditSpecifications.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. instance-id - The ID of the instance.

**Type:** ARRAY

#### InstanceId

The instance IDs. Default: Describes all your instances. Constraints: Maximum 1000 explicitly specified instance IDs.

**Type:** ARRAY

</details>

## describe_instance_status

Describes the status of the specified instances or all of your instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. availability-zone - The Availability Zone of the instance. event.code - The code for the scheduled event (instance-reboot | system-reboot | system-maintenance | instance-retirement | instance-stop). event.description - A description of the event. event.instance-event-id - The ID of the event whose date and time you are modifying. event.not-after - The latest end time for the scheduled event (for example, 2014-09-15T17:15:20.000Z). event.not-before - The earliest start time for the scheduled event (for example, 2014-09-15T17:15:20.000Z). event.not-before-deadline - The deadline for starting the event (for example, 2014-09-15T17:15:20.000Z). instance-state-code - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). instance-state-name - The state of the instance (pending | running | shutting-down | terminated | stopping | stopped). instance-status.reachability - Filters on instance status where the name is reachability (passed | failed | initializing | insufficient-data). instance-status.status - The status of the instance (ok | impaired | initializing | insufficient-data | not-applicable). system-status.reachability - Filters on system status where the name is reachability (passed | failed | initializing | insufficient-data). system-status.status - The system status of the instance (ok | impaired | initializing | insufficient-data | not-applicable).

**Type:** ARRAY

#### IncludeAllInstances

When true, includes the health status for all instances. When false, includes the health status for running instances only. Default: false

**Type:** BOOLEAN

#### InstanceId

The instance IDs. Default: Describes all your instances. Constraints: Maximum 100 explicitly specified instance IDs.

**Type:** ARRAY

</details>

## describe_instances

Describes the specified instances or all of your instances. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. affinity - The affinity setting for an instance running on a Dedicated Host (default | host). architecture - The instance architecture (i386 | x86_64). availability-zone - The Availability Zone of the instance. block-device-mapping.attach-time - The attach time for an EBS volume mapped to the instance, for example, 2010-09-15T17:15:20.000Z. block-device-mapping.delete-on-termination - A Boolean that indicates whether the EBS volume is deleted on instance termination. block-device-mapping.device-name - The device name specified in the block device mapping (for example, /dev/sdh or xvdh). block-device-mapping.status - The status for the EBS volume (attaching | attached | detaching | detached). block-device-mapping.volume-id - The volume ID of the EBS volume. client-token - The idempotency token you provided when you launched the instance. dns-name - The public DNS name of the instance. group-id - The ID of the security group for the instance. EC2-Classic only. group-name - The name of the security group for the instance. EC2-Classic only. hibernation-options.configured - A Boolean that indicates whether the instance is enabled for hibernation. A value of true means that the instance is enabled for hibernation.  host-id - The ID of the Dedicated Host on which the instance is running, if applicable. hypervisor - The hypervisor type of the instance (ovm | xen). iam-instance-profile.arn - The instance profile associated with the instance. Specified as an ARN. image-id - The ID of the image used to launch the instance. instance-id - The ID of the instance. instance-lifecycle - Indicates whether this is a Spot Instance or a Scheduled Instance (spot | scheduled). instance-state-code - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). instance-state-name - The state of the instance (pending | running | shutting-down | terminated | stopping | stopped). instance-type - The type of instance (for example, t2.micro). instance.group-id - The ID of the security group for the instance. instance.group-name - The name of the security group for the instance.  ip-address - The public IPv4 address of the instance. kernel-id - The kernel ID. key-name - The name of the key pair used when the instance was launched. launch-index - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on). launch-time - The time when the instance was launched. monitoring-state - Indicates whether detailed monitoring is enabled (disabled | enabled). network-interface.addresses.private-ip-address - The private IPv4 address associated with the network interface. network-interface.addresses.primary - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. network-interface.addresses.association.public-ip - The ID of the association of an Elastic IP address (IPv4) with a network interface. network-interface.addresses.association.ip-owner-id - The owner ID of the private IPv4 address associated with the network interface. network-interface.association.public-ip - The address of the Elastic IP address (IPv4) bound to the network interface. network-interface.association.ip-owner-id - The owner of the Elastic IP address (IPv4) associated with the network interface. network-interface.association.allocation-id - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. network-interface.association.association-id - The association ID returned when the network interface was associated with an IPv4 address. network-interface.attachment.attachment-id - The ID of the interface attachment. network-interface.attachment.instance-id - The ID of the instance to which the network interface is attached. network-interface.attachment.instance-owner-id - The owner ID of the instance to which the network interface is attached. network-interface.attachment.device-index - The device index to which the network interface is attached. network-interface.attachment.status - The status of the attachment (attaching | attached | detaching | detached). network-interface.attachment.attach-time - The time that the network interface was attached to an instance. network-interface.attachment.delete-on-termination - Specifies whether the attachment is deleted when an instance is terminated. network-interface.availability-zone - The Availability Zone for the network interface. network-interface.description - The description of the network interface. network-interface.group-id - The ID of a security group associated with the network interface. network-interface.group-name - The name of a security group associated with the network interface. network-interface.ipv6-addresses.ipv6-address - The IPv6 address associated with the network interface. network-interface.mac-address - The MAC address of the network interface. network-interface.network-interface-id - The ID of the network interface. network-interface.owner-id - The ID of the owner of the network interface. network-interface.private-dns-name - The private DNS name of the network interface. network-interface.requester-id - The requester ID for the network interface. network-interface.requester-managed - Indicates whether the network interface is being managed by AWS. network-interface.status - The status of the network interface (available) | in-use). network-interface.source-dest-check - Whether the network interface performs source/destination checking. A value of true means that checking is enabled, and false means that checking is disabled. The value must be false for the network interface to perform network address translation (NAT) in your VPC. network-interface.subnet-id - The ID of the subnet for the network interface. network-interface.vpc-id - The ID of the VPC for the network interface. owner-id - The AWS account ID of the instance owner. placement-group-name - The name of the placement group for the instance. placement-partition-number - The partition in which the instance is located. platform - The platform. To list only Windows instances, use windows. private-dns-name - The private IPv4 DNS name of the instance. private-ip-address - The private IPv4 address of the instance. product-code - The product code associated with the AMI used to launch the instance. product-code.type - The type of product code (devpay | marketplace). ramdisk-id - The RAM disk ID. reason - The reason for the current state of the instance (for example, shows "User Initiated [date]" when you stop or terminate the instance). Similar to the state-reason-code filter. requester-id - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). reservation-id - The ID of the instance's reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. root-device-name - The device name of the root device volume (for example, /dev/sda1). root-device-type - The type of the root device volume (ebs | instance-store). source-dest-check - Indicates whether the instance performs source/destination checking. A value of true means that checking is enabled, and false means that checking is disabled. The value must be false for the instance to perform network address translation (NAT) in your VPC.  spot-instance-request-id - The ID of the Spot Instance request. state-reason-code - The reason code for the state change. state-reason-message - A message that describes the state change. subnet-id - The ID of the subnet for the instance. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. tenancy - The tenancy of an instance (dedicated | default | host). virtualization-type - The virtualization type of the instance (paravirtual | hvm). vpc-id - The ID of the VPC that the instance is running in.

**Type:** ARRAY

#### InstanceId

The instance IDs. Default: Describes all your instances.

**Type:** ARRAY

</details>

## describe_internet_gateways

Describes one or more of your internet gateways. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInternetGateways.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. attachment.state - The current state of the attachment between the gateway and the VPC (available). Present only if a VPC is attached. attachment.vpc-id - The ID of an attached VPC. internet-gateway-id - The ID of the Internet gateway. owner-id - The ID of the AWS account that owns the internet gateway. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### InternetGatewayId

One or more internet gateway IDs. Default: Describes all your internet gateways.

**Type:** ARRAY

</details>

## describe_key_pairs

Describes the specified key pairs or all of your key pairs. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeKeyPairs.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. fingerprint - The fingerprint of the key pair. key-name - The name of the key pair.

**Type:** ARRAY

#### KeyName

The key pair names. Default: Describes all your key pairs.

**Type:** ARRAY

</details>

## describe_launch_template_versions

Describes one or more versions of a specified launch template. You can describe all versions, individual versions, or a range of versions.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. create-time - The time the launch template version was created. ebs-optimized - A boolean that indicates whether the instance is optimized for Amazon EBS I/O. iam-instance-profile - The ARN of the IAM instance profile. image-id - The ID of the AMI. instance-type - The instance type. is-default-version - A boolean that indicates whether the launch template version is the default version. kernel-id - The kernel ID. ram-disk-id - The RAM disk ID.

**Type:** ARRAY

#### LaunchTemplateId

The ID of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateName

The name of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateVersion

One or more versions of the launch template.

**Type:** ARRAY

#### MaxVersion

The version number up to which to describe launch template versions.

**Type:** STRING

#### MinVersion

The version number after which to describe launch template versions.

**Type:** STRING

</details>

## describe_launch_templates

Describes one or more launch templates. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. create-time - The time the launch template was created. launch-template-name - The name of the launch template. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### LaunchTemplateId

One or more launch template IDs.

**Type:** ARRAY

#### LaunchTemplateName

One or more launch template names.

**Type:** ARRAY

</details>

## describe_moving_addresses

Describes your Elastic IP addresses that are being moved to the EC2-VPC platform, or that are being restored to the EC2-Classic platform. This request does not return information about any other Elastic IP addresses in your account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMovingAddresses.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. moving-status - The status of the Elastic IP address (MovingToVpc | RestoringToClassic).

**Type:** ARRAY

#### PublicIp

One or more Elastic IP addresses.

**Type:** ARRAY

</details>

## describe_nat_gateways

Describes one or more of your NAT gateways. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html

<details><summary>Parameters</summary>

#### Filter

One or more filters. nat-gateway-id - The ID of the NAT gateway. state - The state of the NAT gateway (pending | failed | available | deleting | deleted). subnet-id - The ID of the subnet in which the NAT gateway resides. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC in which the NAT gateway resides.

**Type:** ARRAY

#### NatGatewayId

One or more NAT gateway IDs.

**Type:** ARRAY

</details>

## describe_network_acls

Describes one or more of your network ACLs. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkAcls.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. association.association-id - The ID of an association ID for the ACL. association.network-acl-id - The ID of the network ACL involved in the association. association.subnet-id - The ID of the subnet involved in the association. default - Indicates whether the ACL is the default network ACL for the VPC. entry.cidr - The IPv4 CIDR range specified in the entry. entry.icmp.code - The ICMP code specified in the entry, if any. entry.icmp.type - The ICMP type specified in the entry, if any. entry.ipv6-cidr - The IPv6 CIDR range specified in the entry. entry.port-range.from - The start of the port range specified in the entry.  entry.port-range.to - The end of the port range specified in the entry.  entry.protocol - The protocol specified in the entry (tcp | udp | icmp or a protocol number). entry.rule-action - Allows or denies the matching traffic (allow | deny). entry.rule-number - The number of an entry (in other words, rule) in the set of ACL entries. network-acl-id - The ID of the network ACL. owner-id - The ID of the AWS account that owns the network ACL. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC for the network ACL.

**Type:** ARRAY

#### NetworkAclId

One or more network ACL IDs. Default: Describes all your network ACLs.

**Type:** ARRAY

</details>

## describe_network_interface_attribute

Describes a network interface attribute. You can specify only one attribute at a time. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaceAttribute.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### Attribute

The attribute of the network interface. This parameter is required.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_network_interface_permissions

Describes the permissions for your network interfaces.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfacePermissions.html

<details><summary>Parameters</summary>

#### Filter

One or more filters. network-interface-permission.network-interface-permission-id - The ID of the permission. network-interface-permission.network-interface-id - The ID of the network interface. network-interface-permission.aws-account-id - The AWS account ID. network-interface-permission.aws-service - The AWS service. network-interface-permission.permission - The type of permission (INSTANCE-ATTACH | EIP-ASSOCIATE).

**Type:** ARRAY

#### NetworkInterfacePermissionId

One or more network interface permission IDs.

**Type:** ARRAY

</details>

## describe_network_interfaces

Describes one or more of your network interfaces. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. addresses.private-ip-address - The private IPv4 addresses associated with the network interface. addresses.primary - Whether the private IPv4 address is the primary IP address associated with the network interface.  addresses.association.public-ip - The association ID returned when the network interface was associated with the Elastic IP address (IPv4). addresses.association.owner-id - The owner ID of the addresses associated with the network interface. association.association-id - The association ID returned when the network interface was associated with an IPv4 address. association.allocation-id - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. association.ip-owner-id - The owner of the Elastic IP address (IPv4) associated with the network interface. association.public-ip - The address of the Elastic IP address (IPv4) bound to the network interface. association.public-dns-name - The public DNS name for the network interface (IPv4). attachment.attachment-id - The ID of the interface attachment. attachment.attach.time - The time that the network interface was attached to an instance. attachment.delete-on-termination - Indicates whether the attachment is deleted when an instance is terminated. attachment.device-index - The device index to which the network interface is attached. attachment.instance-id - The ID of the instance to which the network interface is attached. attachment.instance-owner-id - The owner ID of the instance to which the network interface is attached. attachment.nat-gateway-id - The ID of the NAT gateway to which the network interface is attached. attachment.status - The status of the attachment (attaching | attached | detaching | detached). availability-zone - The Availability Zone of the network interface. description - The description of the network interface. group-id - The ID of a security group associated with the network interface. group-name - The name of a security group associated with the network interface. ipv6-addresses.ipv6-address - An IPv6 address associated with the network interface. mac-address - The MAC address of the network interface. network-interface-id - The ID of the network interface. owner-id - The AWS account ID of the network interface owner. private-ip-address - The private IPv4 address or addresses of the network interface. private-dns-name - The private DNS name of the network interface (IPv4). requester-id - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). requester-managed - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on). source-desk-check - Indicates whether the network interface performs source/destination checking.  A value of true means checking is enabled, and false means checking is disabled.  The value must be false for the network interface to perform network address translation (NAT) in your VPC. status - The status of the network interface. If the network interface is not attached to an instance, the status is available;  if a network interface is attached to an instance the status is in-use. subnet-id - The ID of the subnet for the network interface. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC for the network interface.

**Type:** ARRAY

#### NetworkInterfaceId

One or more network interface IDs. Default: Describes all your network interfaces.

**Type:** ARRAY

</details>

## describe_placement_groups

Describes the specified placement groups or all of your placement groups. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePlacementGroups.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. group-name - The name of the placement group. state - The state of the placement group (pending | available | deleting | deleted). strategy - The strategy of the placement group (cluster | spread | partition).

**Type:** ARRAY

#### GroupName

The names of the placement groups. Default: Describes all your placement groups, or only those otherwise specified.

**Type:** ARRAY

</details>

## describe_prefix_lists

Describes available AWS services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service. A prefix list ID is required for creating an outbound security group rule that allows traffic from a VPC to access an AWS service through a gateway VPC endpoint. Currently, the services that support this action are Amazon S3 and Amazon DynamoDB.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. prefix-list-id: The ID of a prefix list. prefix-list-name: The name of a prefix list.

**Type:** ARRAY

#### PrefixListId

One or more prefix list IDs.

**Type:** ARRAY

</details>

## describe_principal_id_format

Describes the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrincipalIdFormat.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Resource

The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway

**Type:** ARRAY

</details>

## describe_regions

Describes the regions that are currently available to you. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. endpoint - The endpoint of the region (for example, ec2.us-east-1.amazonaws.com). region-name - The name of the region (for example, us-east-1).

**Type:** ARRAY

#### RegionName

The names of the regions.

**Type:** ARRAY

</details>

## describe_reserved_instances

Describes one or more of the Reserved Instances that you purchased. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstances.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. availability-zone - The Availability Zone where the Reserved Instance can be used. duration - The duration of the Reserved Instance (one year or three years), in seconds (31536000 | 94608000). end - The time when the Reserved Instance expires (for example, 2015-08-07T11:54:42.000Z). fixed-price - The purchase price of the Reserved Instance (for example, 9800.0). instance-type - The instance type that is covered by the reservation. scope - The scope of the Reserved Instance (Region or Availability Zone). product-description - The Reserved Instance product platform description. Instances that include (Amazon VPC) in the product platform description will only be displayed to EC2-Classic account holders and are for use with Amazon VPC (Linux/UNIX | Linux/UNIX (Amazon VPC) | SUSE Linux | SUSE Linux (Amazon VPC) | Red Hat Enterprise Linux | Red Hat Enterprise Linux (Amazon VPC) | Windows | Windows (Amazon VPC) | Windows with SQL Server Standard | Windows with SQL Server Standard (Amazon VPC) | Windows with SQL Server Web | Windows with SQL Server Web (Amazon VPC) | Windows with SQL Server Enterprise | Windows with SQL Server Enterprise (Amazon VPC)). reserved-instances-id - The ID of the Reserved Instance. start - The time at which the Reserved Instance purchase request was placed (for example, 2014-08-07T11:54:42.000Z). state - The state of the Reserved Instance (payment-pending | active | payment-failed | retired). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. usage-price - The usage price of the Reserved Instance, per hour (for example, 0.84).

**Type:** ARRAY

#### OfferingClass

Describes whether the Reserved Instance is Standard or Convertible.

**Type:** STRING

#### OfferingType

The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.

**Type:** STRING

#### ReservedInstancesId

One or more Reserved Instance IDs. Default: Describes all your Reserved Instances, or only those otherwise specified.

**Type:** ARRAY

</details>

## describe_reserved_instances_listings

Describes your account's Reserved Instance listings in the Reserved Instance Marketplace. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesListings.html

<details><summary>Parameters</summary>

#### Filter

One or more filters. reserved-instances-id - The ID of the Reserved Instances. reserved-instances-listing-id - The ID of the Reserved Instances listing. status - The status of the Reserved Instance listing (pending | active | cancelled | closed). status-message - The reason for the status.

**Type:** ARRAY

#### ReservedInstancesId

One or more Reserved Instance IDs.

**Type:** STRING

#### ReservedInstancesListingId

One or more Reserved Instance listing IDs.

**Type:** STRING

</details>

## describe_reserved_instances_modifications

Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is specified, only information about the specific modification is returned.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesModifications.html

<details><summary>Parameters</summary>

#### Filter

One or more filters. client-token - The idempotency token for the modification request. create-date - The time when the modification request was created. effective-date - The time when the modification becomes effective. modification-result.reserved-instances-id - The ID for the Reserved Instances created as part of the modification request. This ID is only available when the status of the modification is fulfilled. modification-result.target-configuration.availability-zone - The Availability Zone for the new Reserved Instances. modification-result.target-configuration.instance-count  - The number of new Reserved Instances. modification-result.target-configuration.instance-type - The instance type of the new Reserved Instances. modification-result.target-configuration.platform - The network platform of the new Reserved Instances (EC2-Classic | EC2-VPC). reserved-instances-id - The ID of the Reserved Instances modified. reserved-instances-modification-id - The ID of the modification request. status - The status of the Reserved Instances modification request (processing | fulfilled | failed). status-message - The reason for the status. update-date - The time when the modification request was last updated.

**Type:** ARRAY

#### NextToken

The token to retrieve the next page of results.

**Type:** STRING

#### ReservedInstancesModificationId

IDs for the submitted modification request.

**Type:** ARRAY

</details>

## describe_reserved_instances_offerings

Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not receive insufficient capacity errors, and you pay a lower usage rate than the rate charged for On-Demand instances for the actual time used.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html

<details><summary>Parameters</summary>

#### AvailabilityZone

The Availability Zone in which the Reserved Instance can be used.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. availability-zone - The Availability Zone where the Reserved Instance can be used. duration - The duration of the Reserved Instance (for example, one year or three years), in seconds (31536000 | 94608000). fixed-price - The purchase price of the Reserved Instance (for example, 9800.0). instance-type - The instance type that is covered by the reservation. marketplace - Set to true to show only Reserved Instance Marketplace offerings. When this filter is not used, which is the default behavior, all offerings from both AWS and the Reserved Instance Marketplace are listed. product-description - The Reserved Instance product platform description. Instances that include (Amazon VPC) in the product platform description will only be displayed to EC2-Classic account holders and are for use with Amazon VPC. (Linux/UNIX | Linux/UNIX (Amazon VPC) | SUSE Linux | SUSE Linux (Amazon VPC) | Red Hat Enterprise Linux | Red Hat Enterprise Linux (Amazon VPC) | Windows | Windows (Amazon VPC) | Windows with SQL Server Standard | Windows with SQL Server Standard (Amazon VPC) | Windows with SQL Server Web |  Windows with SQL Server Web (Amazon VPC) | Windows with SQL Server Enterprise | Windows with SQL Server Enterprise (Amazon VPC))  reserved-instances-offering-id - The Reserved Instances offering ID. scope - The scope of the Reserved Instance (Availability Zone or Region). usage-price - The usage price of the Reserved Instance, per hour (for example, 0.84).

**Type:** ARRAY

#### IncludeMarketplace

Include Reserved Instance Marketplace offerings in the response.

**Type:** BOOLEAN

#### InstanceTenancy

The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of dedicated is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances). Important: The host value cannot be used with this parameter. Use the default or dedicated values only. Default: default

**Type:** STRING

#### InstanceType

The instance type that the reservation will cover (for example, m1.small). For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### MaxDuration

The maximum duration (in seconds) to filter when searching for offerings. Default: 94608000 (3 years)

**Type:** NUMBER

#### MaxInstanceCount

The maximum number of instances to filter when searching for offerings. Default: 20

**Type:** INTEGER

#### MinDuration

The minimum duration (in seconds) to filter when searching for offerings. Default: 2592000 (1 month)

**Type:** NUMBER

#### OfferingClass

The offering class of the Reserved Instance. Can be standard or convertible.

**Type:** STRING

#### OfferingType

The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the Medium Utilization Reserved Instance offering type.

**Type:** STRING

#### ProductDescription

The Reserved Instance product platform description. Instances that include (Amazon VPC) in the description are for use with Amazon VPC.

**Type:** STRING

#### ReservedInstancesOfferingId

One or more Reserved Instances offering IDs.

**Type:** ARRAY

</details>

## describe_route_tables

Describes one or more of your route tables. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. association.route-table-association-id - The ID of an association ID for the route table. association.route-table-id - The ID of the route table involved in the association. association.subnet-id - The ID of the subnet involved in the association. association.main - Indicates whether the route table is the main route table for the VPC (true | false). Route tables that do not have an association ID are not returned in the response. owner-id - The ID of the AWS account that owns the route table. route-table-id - The ID of the route table. route.destination-cidr-block - The IPv4 CIDR range specified in a route in the table. route.destination-ipv6-cidr-block - The IPv6 CIDR range specified in a route in the route table. route.destination-prefix-list-id - The ID (prefix) of the AWS service specified in a route in the table. route.egress-only-internet-gateway-id - The ID of an egress-only Internet gateway specified in a route in the route table. route.gateway-id - The ID of a gateway specified in a route in the table. route.instance-id - The ID of an instance specified in a route in the table. route.nat-gateway-id - The ID of a NAT gateway. route.transit-gateway-id - The ID of a transit gateway. route.origin - Describes how the route was created.  CreateRouteTable indicates that the route was automatically created when the route table was created; CreateRoute indicates that the route was manually added to the route table; EnableVgwRoutePropagation indicates that the route was propagated by route propagation. route.state - The state of a route in the route table (active | blackhole). The blackhole state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, the specified NAT instance has been terminated, and so on). route.vpc-peering-connection-id - The ID of a VPC peering connection specified in a route in the table. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. transit-gateway-id - The ID of a transit gateway. vpc-id - The ID of the VPC for the route table.

**Type:** ARRAY

#### RouteTableId

One or more route table IDs. Default: Describes all your route tables.

**Type:** ARRAY

</details>

## describe_scheduled_instance_availability

Finds available schedules that meet the specified criteria. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstanceAvailability.html

<details><summary>Parameters</summary>

#### FirstSlotStartTimeRange (required)

The time period for the first schedule to start.

**Type:** OBJECT

#### Recurrence (required)

The schedule recurrence.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. availability-zone - The Availability Zone (for example, us-west-2a). instance-type - The instance type (for example, c4.large). network-platform - The network platform (EC2-Classic or EC2-VPC). platform - The platform (Linux/UNIX or Windows).

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call.  This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### MaxSlotDurationInHours

The maximum available duration, in hours. This value must be greater than MinSlotDurationInHours and less than 1,720.

**Type:** INTEGER

#### MinSlotDurationInHours

The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.

**Type:** INTEGER

#### NextToken

The token for the next set of results.

**Type:** STRING

</details>

## describe_scheduled_instances

Describes the specified Scheduled Instances or all your Scheduled Instances. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstances.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. availability-zone - The Availability Zone (for example, us-west-2a). instance-type - The instance type (for example, c4.large). network-platform - The network platform (EC2-Classic or EC2-VPC). platform - The platform (Linux/UNIX or Windows).

**Type:** ARRAY

#### MaxResults

The maximum number of results to return in a single call.  This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned NextToken value.

**Type:** INTEGER

#### NextToken

The token for the next set of results.

**Type:** STRING

#### ScheduledInstanceId

The Scheduled Instance IDs.

**Type:** ARRAY

#### SlotStartTimeRange

The time period for the first schedule to start.

**Type:** OBJECT

</details>

## describe_security_group_references

[EC2-VPC only] Describes the VPCs on the other side of a VPC peering connection that are referencing the security groups you've specified in this request.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupReferences.html

<details><summary>Parameters</summary>

#### GroupId (required)

The IDs of the security groups in your account.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_security_groups

Describes the specified security groups or all of your security groups. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters. description - The description of the security group. egress.ip-permission.cidr - An IPv4 CIDR block for an outbound security group rule. egress.ip-permission.from-port - For an outbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number. egress.ip-permission.group-id - The ID of a security group that has been referenced in an outbound security group rule. egress.ip-permission.group-name - The name of a security group that has been referenced in an outbound security group rule. egress.ip-permission.ipv6-cidr - An IPv6 CIDR block for an outbound security group rule. egress.ip-permission.prefix-list-id - The ID (prefix) of the AWS service to which a security group rule allows outbound access. egress.ip-permission.protocol - The IP protocol for an outbound security group rule (tcp | udp | icmp or a protocol number). egress.ip-permission.to-port - For an outbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code. egress.ip-permission.user-id - The ID of an AWS account that has been referenced in an outbound security group rule. group-id - The ID of the security group.  group-name - The name of the security group. ip-permission.cidr - An IPv4 CIDR block for an inbound security group rule. ip-permission.from-port - For an inbound rule, the start of port range for the TCP and UDP protocols, or an ICMP type number. ip-permission.group-id - The ID of a security group that has been referenced in an inbound security group rule. ip-permission.group-name - The name of a security group that has been referenced in an inbound security group rule. ip-permission.ipv6-cidr - An IPv6 CIDR block for an inbound security group rule. ip-permission.prefix-list-id - The ID (prefix) of the AWS service from which a security group rule allows inbound access. ip-permission.protocol - The IP protocol for an inbound security group rule (tcp | udp | icmp or a protocol number). ip-permission.to-port - For an inbound rule, the end of port range for the TCP and UDP protocols, or an ICMP code. ip-permission.user-id - The ID of an AWS account that has been referenced in an inbound security group rule. owner-id - The AWS account ID of the owner of the security group. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC specified when the security group was created.

**Type:** ARRAY

#### GroupId

The IDs of the security groups. Required for security groups in a nondefault VPC. Default: Describes all your security groups.

**Type:** ARRAY

#### GroupName

[EC2-Classic and default VPC only] The names of the security groups. You can specify either the security group name or the security group ID. For security groups in a nondefault VPC, use the group-name filter to describe security groups by name. Default: Describes all your security groups.

**Type:** ARRAY

</details>

## describe_snapshot_attribute

Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshotAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The snapshot attribute you would like to view.

**Type:** STRING

#### SnapshotId (required)

The ID of the EBS snapshot.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_snapshots

Describes the specified EBS snapshots available to you or all of the EBS snapshots available to you.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. description - A description of the snapshot. encrypted - Indicates whether the snapshot is encrypted (true  | false) owner-alias - Value from an Amazon-maintained list (amazon | self | all | aws-marketplace | microsoft) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. owner-id - The ID of the AWS account that owns the snapshot. progress - The progress of the snapshot, as a percentage (for example, 80%). snapshot-id - The snapshot ID. start-time - The time stamp when the snapshot was initiated. status - The status of the snapshot (pending | completed | error). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. volume-id - The ID of the volume the snapshot is for. volume-size - The size of the volume, in GiB.

**Type:** ARRAY

#### Owner

Describes the snapshots owned by these owners.

**Type:** ARRAY

#### RestorableBy

The IDs of the AWS accounts that can create volumes from the snapshot.

**Type:** ARRAY

#### SnapshotId

The snapshot IDs. Default: Describes the snapshots for which you have create volume permissions.

**Type:** ARRAY

</details>

## describe_spot_datafeed_subscription

Describes the data feed for Spot Instances. For more information, see Spot Instance Data Feed in the Amazon EC2 User Guide for Linux Instances.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotDatafeedSubscription.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_spot_fleet_instances

Describes the running instances for the specified Spot Fleet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetInstances.html

<details><summary>Parameters</summary>

#### SpotFleetRequestId (required)

The ID of the Spot Fleet request.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_spot_fleet_request_history

Describes the events for the specified Spot Fleet request during the specified time. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequestHistory.html

<details><summary>Parameters</summary>

#### SpotFleetRequestId (required)

The ID of the Spot Fleet request.

**Type:** STRING

#### StartTime (required)

The starting date and time for the events, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EventType

The type of events to describe. By default, all events are described.

**Type:** STRING

</details>

## describe_spot_fleet_requests

Describes your Spot Fleet requests. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### SpotFleetRequestId

The IDs of the Spot Fleet requests.

**Type:** ARRAY

</details>

## describe_spot_instance_requests

Describes the specified Spot Instance requests. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. availability-zone-group - The Availability Zone group. create-time - The time stamp when the Spot Instance request was created. fault-code - The fault code related to the request. fault-message - The fault message related to the request. instance-id - The ID of the instance that fulfilled the request. launch-group - The Spot Instance launch group. launch.block-device-mapping.delete-on-termination - Indicates whether the EBS volume is deleted on instance termination. launch.block-device-mapping.device-name - The device name for the volume in the block device mapping (for example, /dev/sdh or xvdh). launch.block-device-mapping.snapshot-id - The ID of the snapshot for the EBS volume. launch.block-device-mapping.volume-size - The size of the EBS volume, in GiB. launch.block-device-mapping.volume-type - The type of EBS volume: gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1for Cold HDD, or standard for Magnetic. launch.group-id - The ID of the security group for the instance. launch.group-name - The name of the security group for the instance. launch.image-id - The ID of the AMI. launch.instance-type - The type of instance (for example, m3.medium). launch.kernel-id - The kernel ID. launch.key-name - The name of the key pair the instance launched with. launch.monitoring-enabled - Whether detailed monitoring is enabled for the Spot Instance. launch.ramdisk-id - The RAM disk ID. launched-availability-zone - The Availability Zone in which the request is launched. network-interface.addresses.primary - Indicates whether the IP address is the primary private IP address. network-interface.delete-on-termination - Indicates whether the network interface is deleted when the instance is terminated. network-interface.description - A description of the network interface. network-interface.device-index - The index of the device for the network interface attachment on the instance. network-interface.group-id - The ID of the security group associated with the network interface. network-interface.network-interface-id - The ID of the network interface. network-interface.private-ip-address - The primary private IP address of the network interface. network-interface.subnet-id - The ID of the subnet for the instance. product-description - The product description associated with the instance (Linux/UNIX | Windows). spot-instance-request-id - The Spot Instance request ID. spot-price - The maximum hourly price for any Spot Instance launched to fulfill the request. state - The state of the Spot Instance request (open | active | closed | cancelled | failed). Spot request status information can help you track your Amazon EC2 Spot Instance requests. For more information, see Spot Request Status in the Amazon EC2 User Guide for Linux Instances. status-code - The short code describing the most recent evaluation of your Spot Instance request. status-message - The message explaining the status of the Spot Instance request. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. type - The type of Spot Instance request (one-time | persistent). valid-from - The start date of the request. valid-until - The end date of the request.

**Type:** ARRAY

#### SpotInstanceRequestId

One or more Spot Instance request IDs.

**Type:** ARRAY

</details>

## describe_spot_price_history

Describes the Spot price history. For more information, see Spot Instance Pricing History in the Amazon EC2 User Guide for Linux Instances.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html

<details><summary>Parameters</summary>

#### AvailabilityZone

Filters the results by the specified Availability Zone.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EndTime

The date and time, up to the current date, from which to stop retrieving the price history data,  in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).

**Type:** STRING

#### Filter

One or more filters. availability-zone - The Availability Zone for which prices should be returned. instance-type - The type of instance (for example, m3.medium). product-description - The product description for the Spot price (Linux/UNIX | SUSE Linux | Windows | Linux/UNIX (Amazon VPC) | SUSE Linux (Amazon VPC) | Windows (Amazon VPC)). spot-price - The Spot price. The value must match exactly (or use wildcards; greater than or less than comparison is not supported). timestamp - The time stamp of the Spot price history, in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ). You can use wildcards (* and ?). Greater than or less than comparison is not supported.

**Type:** ARRAY

#### InstanceType

Filters the results by the specified instance types.

**Type:** ARRAY

#### ProductDescription

Filters the results by the specified basic product descriptions.

**Type:** ARRAY

#### StartTime

The date and time, up to the past 90 days, from which to start retrieving the price history data,  in UTC format (for example, YYYY-MM-DDTHH:MM:SSZ).

**Type:** STRING

</details>

## describe_stale_security_groups

[EC2-VPC only] Describes the stale security group rules for security groups in a specified VPC. Rules are stale when they reference a deleted security group in a peer VPC, or a security group in a peer VPC for which the VPC peering connection has been deleted.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeStaleSecurityGroups.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_subnets

Describes one or more of your subnets. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. availability-zone - The Availability Zone for the subnet. You can also use availabilityZone as the filter name. availability-zone-id - The ID of the Availability Zone for the subnet. You can also use availabilityZoneId as the filter name. available-ip-address-count - The number of IPv4 addresses in the subnet that are available. cidr-block - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet's CIDR block for information to be returned for the subnet. You can also use cidr or cidrBlock as the filter names. default-for-az - Indicates whether this is the default subnet for the Availability Zone. You can also use defaultForAz as the filter name. ipv6-cidr-block-association.ipv6-cidr-block - An IPv6 CIDR block associated with the subnet. ipv6-cidr-block-association.association-id - An association ID for an IPv6 CIDR block associated with the subnet. ipv6-cidr-block-association.state - The state of an IPv6 CIDR block associated with the subnet. owner-id - The ID of the AWS account that owns the subnet. state - The state of the subnet (pending | available). subnet-arn - The Amazon Resource Name (ARN) of the subnet. subnet-id - The ID of the subnet. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC for the subnet.

**Type:** ARRAY

#### SubnetId

One or more subnet IDs. Default: Describes all your subnets.

**Type:** ARRAY

</details>

## describe_tags

Describes the specified tags for your EC2 resources. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTags.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. key - The tag key. resource-id - The ID of the resource. resource-type - The resource type (customer-gateway | dedicated-host | dhcp-options | elastic-ip | fleet | fpga-image | image | instance | host-reservation | internet-gateway | launch-template | natgateway | network-acl | network-interface | reserved-instances | route-table | security-group | snapshot | spot-instances-request | subnet | volume | vpc | vpc-peering-connection | vpn-connection | vpn-gateway). tag:<key> - The key/value combination of the tag. For example, specify "tag:Owner" for the filter name and "TeamA" for the filter value to find resources with the tag "Owner=TeamA". value - The tag value.

**Type:** ARRAY

</details>

## describe_transit_gateway_attachments

Describes one or more attachments between resources and transit gateways. By default, all attachments are described. Alternatively, you can filter the results by attachment ID, attachment state, resource ID, or resource owner.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: association.state - The state of the association (associating | associated | disassociating). association.transit-gateway-route-table-id - The ID of the route table for the transit gateway. resource-id - The ID of the resource. resource-owner-id - The ID of the AWS account that owns the resource. resource-type - The resource type (vpc | vpn). state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). transit-gateway-attachment-id - The ID of the attachment. transit-gateway-id - The ID of the transit gateway. transit-gateway-owner-id - The ID of the AWS account that owns the transit gateway.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

#### TransitGatewayAttachmentIds

The IDs of the attachments.

**Type:** ARRAY

</details>

## describe_transit_gateway_route_tables

Describes one or more transit gateway route tables. By default, all transit gateway route tables are described. Alternatively, you can filter the results.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayRouteTables.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: default-association-route-table - Indicates whether this is the default association route table for the transit gateway (true | false). default-propagation-route-table - Indicates whether this is the default propagation route table for the transit gateway (true | false). state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). transit-gateway-id - The ID of the transit gateway. transit-gateway-route-table-id - The ID of the transit gateway route table.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

#### TransitGatewayRouteTableIds

The IDs of the transit gateway route tables.

**Type:** ARRAY

</details>

## describe_transit_gateway_vpc_attachments

Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayVpcAttachments.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). transit-gateway-attachment-id - The ID of the attachment. transit-gateway-id - The ID of the transit gateway. vpc-id - The ID of the VPC.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

#### TransitGatewayAttachmentIds

The IDs of the attachments.

**Type:** ARRAY

</details>

## describe_transit_gateways

Describes one or more transit gateways. By default, all transit gateways are described. Alternatively, you can filter the results.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: options.propagation-default-route-table-id - The ID of the default propagation route table. options.amazon-side-asn - The private ASN for the Amazon side of a BGP session. options.association-default-route-table-id - The ID of the default association route table. options.auto-accept-shared-attachments - Indicates whether there is automatic acceptance of attachment requests (enable | disable). options.default-route-table-association - Indicates whether resource attachments are automatically  associated with the default association route table (enable | disable). options.default-route-table-propagation - Indicates whether resource attachments automatically propagate  routes to the default propagation route table (enable | disable). options.dns-support - Indicates whether DNS support is enabled (enable | disable). options.vpn-ecmp-support - Indicates whether Equal Cost Multipath Protocol support is enabled  (enable | disable). owner-id - The ID of the AWS account that owns the transit gateway. state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). transit-gateway-id - The ID of the transit gateway.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

#### TransitGatewayIds

The IDs of the transit gateways.

**Type:** ARRAY

</details>

## describe_volume_attribute

Describes the specified attribute of the specified volume. You can specify only one attribute at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The attribute of the volume. This parameter is required.

**Type:** STRING

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_volume_status

Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volume's underlying host. If the volume's underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeStatus.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. action.code - The action code for the event (for example, enable-volume-io). action.description - A description of the action. action.event-id - The event ID associated with the action. availability-zone - The Availability Zone of the instance. event.description - A description of the event. event.event-id - The event ID. event.event-type - The event type (for io-enabled: passed | failed; for io-performance: io-performance:degraded | io-performance:severely-degraded | io-performance:stalled). event.not-after - The latest end time for the event. event.not-before - The earliest start time for the event. volume-status.details-name - The cause for volume-status.status (io-enabled | io-performance). volume-status.details-status - The status of volume-status.details-name (for io-enabled: passed | failed; for io-performance: normal | degraded | severely-degraded | stalled). volume-status.status - The status of the volume (ok | impaired | warning | insufficient-data).

**Type:** ARRAY

#### VolumeId

The IDs of the volumes. Default: Describes all your volumes.

**Type:** ARRAY

</details>

## describe_volumes

Describes the specified EBS volumes or all of your EBS volumes. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. attachment.attach-time - The time stamp when the attachment initiated. attachment.delete-on-termination - Whether the volume is deleted on instance termination. attachment.device - The device name specified in the block device mapping (for example, /dev/sda1). attachment.instance-id - The ID of the instance the volume is attached to. attachment.status - The attachment state (attaching | attached | detaching). availability-zone - The Availability Zone in which the volume was created. create-time - The time stamp when the volume was created. encrypted - Indicates whether the volume is encrypted (true  | false) size - The size of the volume, in GiB. snapshot-id - The snapshot from which the volume was created. status - The status of the volume (creating | available | in-use | deleting | deleted | error). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. volume-id - The volume ID. volume-type - The Amazon EBS volume type. This can be gp2 for General Purpose SSD, io1 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.

**Type:** ARRAY

#### VolumeId

The volume IDs.

**Type:** ARRAY

</details>

## describe_volumes_modifications

Reports the current modification status of EBS volumes. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumesModifications.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

The filters. Supported filters: volume-id, modification-state, target-size, target-iops, target-volume-type, original-size, original-iops, original-volume-type, start-time.

**Type:** ARRAY

#### VolumeId

The IDs of the volumes for which in-progress modifications will be described.

**Type:** ARRAY

</details>

## describe_vpc_attribute

Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The VPC attribute.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## describe_vpc_classic_link

Describes the ClassicLink status of one or more VPCs. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLink.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. is-classic-link-enabled - Whether the VPC is enabled for ClassicLink (true | false). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.

**Type:** ARRAY

#### VpcId

One or more VPCs for which you want to describe the ClassicLink status.

**Type:** ARRAY

</details>

## describe_vpc_classic_link_dns_support

Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLinkDnsSupport.html

<details><summary>Parameters</summary>

#### VpcIds

One or more VPC IDs.

**Type:** ARRAY

</details>

## describe_vpc_endpoint_connection_notifications

Describes the connection notifications for VPC endpoints and VPC endpoint services.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnectionNotifications.html

<details><summary>Parameters</summary>

#### ConnectionNotificationId

The ID of the notification.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. connection-notification-arn - The ARN of SNS topic for the notification. connection-notification-id - The ID of the notification. connection-notification-state - The state of the notification (Enabled | Disabled). connection-notification-type - The type of notification (Topic). service-id - The ID of the endpoint service. vpc-endpoint-id - The ID of the VPC endpoint.

**Type:** ARRAY

</details>

## describe_vpc_endpoint_connections

Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnections.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. service-id - The ID of the service. vpc-endpoint-owner - The AWS account number of the owner of the endpoint. vpc-endpoint-state - The state of the endpoint (pendingAcceptance | pending | available | deleting | deleted | rejected | failed). vpc-endpoint-id - The ID of the endpoint.

**Type:** ARRAY

</details>

## describe_vpc_endpoint_service_configurations

Describes the VPC endpoint service configurations in your account (your services). https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. service-name - The name of the service. service-id - The ID of the service. service-state - The state of the service (Pending | Available | Deleting | Deleted | Failed).

**Type:** ARRAY

#### ServiceId

The IDs of one or more services.

**Type:** ARRAY

</details>

## describe_vpc_endpoint_service_permissions

Describes the principals (service consumers) that are permitted to discover your VPC endpoint service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServicePermissions.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The ID of the service.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. principal - The ARN of the principal. principal-type - The principal type (All | Service | OrganizationUnit | Account | User | Role).

**Type:** ARRAY

</details>

## describe_vpc_endpoint_services

Describes available services to which you can create a VPC endpoint. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. service-name: The name of the service.

**Type:** ARRAY

#### MaxResults

The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results. Constraint: If the value is greater than 1000, we return only 1000 items.

**Type:** INTEGER

#### NextToken

The token for the next set of items to return. (You received this token from a prior call.)

**Type:** STRING

#### ServiceName

One or more service names.

**Type:** ARRAY

</details>

## describe_vpc_endpoints

Describes one or more of your VPC endpoints. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. service-name: The name of the service. vpc-id: The ID of the VPC in which the endpoint resides. vpc-endpoint-id: The ID of the endpoint. vpc-endpoint-state: The state of the endpoint. (pending | available | deleting | deleted)

**Type:** ARRAY

#### VpcEndpointId

One or more endpoint IDs.

**Type:** ARRAY

</details>

## describe_vpc_peering_connections

Describes one or more of your VPC peering connections. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcPeeringConnections.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. accepter-vpc-info.cidr-block - The IPv4 CIDR block of the accepter VPC. accepter-vpc-info.owner-id - The AWS account ID of the owner of the accepter VPC. accepter-vpc-info.vpc-id - The ID of the accepter VPC. expiration-time - The expiration date and time for the VPC peering connection. requester-vpc-info.cidr-block - The IPv4 CIDR block of the requester's VPC. requester-vpc-info.owner-id - The AWS account ID of the owner of the requester VPC. requester-vpc-info.vpc-id - The ID of the requester VPC. status-code - The status of the VPC peering connection (pending-acceptance | failed | expired | provisioning | active | deleting | deleted | rejected). status-message - A message that provides more information about the status of the VPC peering connection, if applicable. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-peering-connection-id - The ID of the VPC peering connection.

**Type:** ARRAY

#### VpcPeeringConnectionId

One or more VPC peering connection IDs. Default: Describes all your VPC peering connections.

**Type:** ARRAY

</details>

## describe_vpcs

Describes one or more of your VPCs. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. cidr - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC's CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, /28). cidr-block-association.cidr-block - An IPv4 CIDR block associated with the VPC. cidr-block-association.association-id - The association ID for an IPv4 CIDR block associated with the VPC. cidr-block-association.state - The state of an IPv4 CIDR block associated with the VPC. dhcp-options-id - The ID of a set of DHCP options. ipv6-cidr-block-association.ipv6-cidr-block - An IPv6 CIDR block associated with the VPC. ipv6-cidr-block-association.association-id - The association ID for an IPv6 CIDR block associated with the VPC. ipv6-cidr-block-association.state - The state of an IPv6 CIDR block associated with the VPC. isDefault - Indicates whether the VPC is the default VPC. owner-id - The ID of the AWS account that owns the VPC. state - The state of the VPC (pending | available). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. vpc-id - The ID of the VPC.

**Type:** ARRAY

#### VpcId

One or more VPC IDs. Default: Describes all your VPCs.

**Type:** ARRAY

</details>

## describe_vpn_connections

Describes one or more of your VPN connections. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. customer-gateway-configuration - The configuration information for the customer gateway. customer-gateway-id - The ID of a customer gateway associated with the VPN connection. state - The state of the VPN connection (pending | available | deleting | deleted). option.static-routes-only - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP). route.destination-cidr-block - The destination CIDR block. This corresponds to the subnet used in a customer data center. bgp-asn - The BGP Autonomous System Number (ASN) associated with a BGP device. tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. type - The type of VPN connection. Currently the only supported type is ipsec.1. vpn-connection-id - The ID of the VPN connection. vpn-gateway-id - The ID of a virtual private gateway associated with the VPN connection.

**Type:** ARRAY

#### VpnConnectionId

One or more VPN connection IDs. Default: Describes your VPN connections.

**Type:** ARRAY

</details>

## describe_vpn_gateways

Describes one or more of your virtual private gateways. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html

<details><summary>Parameters</summary>

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. amazon-side-asn - The Autonomous System Number (ASN) for the Amazon side of the gateway. attachment.state - The current state of the attachment between the gateway and the VPC (attaching | attached | detaching | detached). attachment.vpc-id - The ID of an attached VPC. availability-zone - The Availability Zone for the virtual private gateway (if applicable). state - The state of the virtual private gateway (pending | available | deleting | deleted). tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify tag:Owner for the filter name and TeamA for the filter value. tag-key - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. type - The type of virtual private gateway. Currently the only supported type is ipsec.1. vpn-gateway-id - The ID of the virtual private gateway.

**Type:** ARRAY

#### VpnGatewayId

One or more virtual private gateway IDs. Default: Describes all your virtual private gateways.

**Type:** ARRAY

</details>

## detach_classic_link_vpc

Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is automatically unlinked from a VPC when it's stopped.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachClassicLinkVpc.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance to unlink from the VPC.

**Type:** STRING

#### VpcId (required)

The ID of the VPC to which the instance is linked.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## detach_internet_gateway

Detaches an internet gateway from a VPC, disabling connectivity between the internet and the VPC. The VPC must not contain any running instances with Elastic IP addresses or public IPv4 addresses.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachInternetGateway.html

<details><summary>Parameters</summary>

#### InternetGatewayId (required)

The ID of the internet gateway.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## detach_network_interface

Detaches a network interface from an instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachNetworkInterface.html

<details><summary>Parameters</summary>

#### AttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Force

Specifies whether to force a detachment.

**Type:** BOOLEAN

</details>

## detach_volume

Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becoming stuck in the busy state while detaching. If this happens, detachment can be delayed indefinitely until you unmount the volume, force detachment, reboot the instance, or all three. If an EBS volume is the root device of an instance, it can't be detached while the instance is running. To detach the root volume, stop the instance first.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVolume.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### Device

The device name.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Force

Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.

**Type:** BOOLEAN

#### InstanceId

The ID of the instance.

**Type:** STRING

</details>

## detach_vpn_gateway

Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described).  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVpnGateway.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### VpnGatewayId (required)

The ID of the virtual private gateway.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disable_transit_gateway_route_table_propagation

Disables the specified resource attachment from propagating routes to the specified propagation route table.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableTransitGatewayRouteTablePropagation.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the propagation route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disable_vgw_route_propagation

Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.html

<details><summary>Parameters</summary>

#### GatewayId (required)

The ID of the virtual private gateway.

**Type:** STRING

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

</details>

## disable_vpc_classic_link

Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLink.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disable_vpc_classic_link_dns_support

Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLinkDnsSupport.html

<details><summary>Parameters</summary>

#### VpcId

The ID of the VPC.

**Type:** STRING

</details>

## disassociate_address

Disassociates an Elastic IP address from the instance or network interface it's associated with.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateAddress.html

<details><summary>Parameters</summary>

#### AssociationId

[EC2-VPC] The association ID. Required for EC2-VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PublicIp

[EC2-Classic] The Elastic IP address. Required for EC2-Classic.

**Type:** STRING

</details>

## disassociate_client_vpn_target_network

Disassociates a target network from the specified Client VPN endpoint. When you disassociate the last target network from a Client VPN, the following happens:  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateClientVpnTargetNetwork.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The ID of the target network association.

**Type:** STRING

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint from which to disassociate the target network.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disassociate_iam_instance_profile

Disassociates an IAM instance profile from a running or stopped instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The ID of the IAM instance profile association.

**Type:** STRING

</details>

## disassociate_route_table

Disassociates a subnet from a route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateRouteTable.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The association ID representing the current association between the route table and subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disassociate_subnet_cidr_block

Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateSubnetCidrBlock.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The association ID for the CIDR block.

**Type:** STRING

</details>

## disassociate_transit_gateway_route_table

Disassociates a resource attachment from a transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayRouteTable.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## disassociate_vpc_cidr_block

Disassociates a CIDR block from a VPC. To disassociate the CIDR block, you must specify its association ID. You can get the association ID by using DescribeVpcs. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateVpcCidrBlock.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The association ID for the CIDR block.

**Type:** STRING

</details>

## enable_transit_gateway_route_table_propagation

Enables the specified attachment to propagate routes to the specified propagation route table.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableTransitGatewayRouteTablePropagation.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the propagation route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## enable_vgw_route_propagation

Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.html

<details><summary>Parameters</summary>

#### GatewayId (required)

The ID of the virtual private gateway.

**Type:** STRING

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

</details>

## enable_volume_i_o

Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVolumeIO.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## enable_vpc_classic_link

Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable your VPC for ClassicLink if any of your VPC route tables have existing routes for address ranges within the 10.0.0.0/8 IP address range, excluding local routes for VPCs in the 10.0.0.0/16 and 10.1.0.0/16 IP address ranges. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLink.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## enable_vpc_classic_link_dns_support

Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLinkDnsSupport.html

<details><summary>Parameters</summary>

#### VpcId

The ID of the VPC.

**Type:** STRING

</details>

## export_client_vpn_client_certificate_revocation_list

Downloads the client certificate revocation list for the specified Client VPN endpoint. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientCertificateRevocationList.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## export_client_vpn_client_configuration

Downloads the contents of the Client VPN endpoint configuration file for the specified Client VPN endpoint. The Client VPN endpoint configuration file includes the Client VPN endpoint and certificate information clients need to establish a connection with the Client VPN endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientConfiguration.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## export_transit_gateway_routes

Exports routes from the specified transit gateway route table to the specified S3 bucket. By default, all routes are exported. Alternatively, you can filter by CIDR range.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportTransitGatewayRoutes.html

<details><summary>Parameters</summary>

#### S3Bucket (required)

The name of the S3 bucket.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: attachment.transit-gateway-attachment-id- The id of the transit gateway attachment. attachment.resource-id - The resource id of the transit gateway attachment. route-search.exact-match - The exact match of the specified filter. route-search.longest-prefix-match - The longest prefix that matches the route. route-search.subnet-of-match - The routes with a subnet that match the specified CIDR filter. route-search.supernet-of-match - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29. state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). transit-gateway-route-destination-cidr-block - The CIDR range. type - The type of roue (active | blackhole).

**Type:** ARRAY

</details>

## get_console_output

Gets the console output for the specified instance. For Linux instances, the instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. For Windows instances, the instance console output includes the last three system event log errors.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Latest

When enabled, retrieves the latest console output for the instance. Default: disabled (false)

**Type:** BOOLEAN

</details>

## get_console_screenshot

Retrieve a JPG-format screenshot of a running instance to help with troubleshooting.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleScreenshot.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### WakeUp

When set to true, acts as keystroke input and wakes up an instance that's in standby or "sleep" mode.

**Type:** BOOLEAN

</details>

## get_host_reservation_purchase_preview

Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetHostReservationPurchasePreview.html

<details><summary>Parameters</summary>

#### HostIdSet (required)

The IDs of the Dedicated Hosts with which the reservation is associated.

**Type:** ARRAY

#### OfferingId (required)

The offering ID of the reservation.

**Type:** STRING

</details>

## get_launch_template_data

Retrieves the configuration data of the specified instance. You can use this data to create a launch template.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetLaunchTemplateData.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## get_password_data

Retrieves the encrypted administrator password for a running Windows instance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the Windows instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## get_reserved_instances_exchange_quote

Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use AcceptReservedInstancesExchangeQuote to perform the exchange.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetReservedInstancesExchangeQuote.html

<details><summary>Parameters</summary>

#### ReservedInstanceId (required)

The IDs of the Convertible Reserved Instances to exchange.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TargetConfiguration

The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.

**Type:** ARRAY

</details>

## get_transit_gateway_attachment_propagations

Lists the route tables to which the specified resource attachment propagates routes. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayAttachmentPropagations.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: transit-gateway-route-table-id - The ID of the transit gateway route table.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

</details>

## get_transit_gateway_route_table_associations

Gets information about the associations for the specified transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTableAssociations.html

<details><summary>Parameters</summary>

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: resource-id - The ID of the resource. resource-type - The resource type (vpc | vpn). transit-gateway-attachment-id - The ID of the attachment.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

</details>

## get_transit_gateway_route_table_propagations

Gets information about the route table propagations for the specified transit gateway route table.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTablePropagations.html

<details><summary>Parameters</summary>

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Filter

One or more filters. The possible values are: resource-id - The ID of the resource. resource-type - The resource type (vpc | vpn). transit-gateway-attachment-id - The ID of the attachment.

**Type:** ARRAY

#### MaxResults

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

**Type:** INTEGER

#### NextToken

The token for the next page of results.

**Type:** STRING

</details>

## import_client_vpn_client_certificate_revocation_list

Uploads a client certificate revocation list to the specified Client VPN endpoint. Uploading a client certificate revocation list overwrites the existing client certificate revocation list.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportClientVpnClientCertificateRevocationList.html

<details><summary>Parameters</summary>

#### CertificateRevocationList (required)

The client certificate revocation list file. For more information, see Generate a Client Certificate Revocation List in the AWS Client VPN Administrator Guide.

**Type:** STRING

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint to which the client certificate revocation list applies.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## import_image

Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI). For more information, see Importing a VM as an Image Using VM Import/Export in the VM Import/Export User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html

<details><summary>Parameters</summary>

#### Architecture

The architecture of the virtual machine. Valid values: i386 | x86_64

**Type:** STRING

#### ClientData

The client-specific data.

**Type:** OBJECT

#### ClientToken

The token to enable idempotency for VM import requests.

**Type:** STRING

#### Description

A description string for the import image task.

**Type:** STRING

#### DiskContainer

Information about the disk containers.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Encrypted

Specifies whether the destination AMI of the imported image should be encrypted.  The default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK using  KmsKeyId. For more information, see Amazon EBS Encryption in the  Amazon Elastic Compute Cloud User Guide.

**Type:** BOOLEAN

#### Hypervisor

The target hypervisor platform. Valid values: xen

**Type:** STRING

#### KmsKeyId

An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted AMI. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  The CMK identifier may be provided in any of the following formats:  Key ID Key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.  AWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.  The specified CMK must exist in the region that the AMI is being copied to.

**Type:** STRING

#### LicenseType

The license type to be used for the Amazon Machine Image (AMI) after importing. Note: You may only use BYOL if you have existing licenses with rights to  use these licenses in a third party cloud like AWS. For more information, see Prerequisites in the VM Import/Export User Guide. Valid values include: Auto - Detects the source-system operating system (OS) and applies the appropriate license. AWS - Replaces the source-system license with an AWS license, if appropriate. BYOL - Retains the source-system license, if appropriate. Default value: Auto

**Type:** STRING

#### Platform

The operating system of the virtual machine. Valid values: Windows | Linux

**Type:** STRING

#### RoleName

The name of the role to use when not using the default role, 'vmimport'.

**Type:** STRING

</details>

## import_instance

Creates an import instance task using metadata from the specified disk image. ImportInstance only supports single-volume VMs. To import multi-volume VMs, use ImportImage. For more information, see Importing a Virtual Machine Using the Amazon EC2 CLI.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html

<details><summary>Parameters</summary>

#### Platform (required)

The instance operating system.

**Type:** STRING

#### Description

A description for the instance being imported.

**Type:** STRING

#### DiskImage

The disk image.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchSpecification

The launch specification.

**Type:** OBJECT

</details>

## import_key_pair

Imports the public key from an RSA key pair that you created with a third-party tool. Compare this with CreateKeyPair, in which AWS creates the key pair and gives the keys to you (AWS keeps a copy of the public key). With ImportKeyPair, you create the key pair and give AWS just the public key. The private key is never transferred between you and AWS.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html

<details><summary>Parameters</summary>

#### KeyName (required)

A unique name for the key pair.

**Type:** STRING

#### PublicKeyMaterial (required)

The public key. For API calls, the text must be base64-encoded. For command line tools, base64 encoding is performed for you.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## import_snapshot

Imports a disk into an EBS snapshot. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportSnapshot.html

<details><summary>Parameters</summary>

#### ClientData

The client-specific data.

**Type:** OBJECT

#### ClientToken

Token to enable idempotency for VM import requests.

**Type:** STRING

#### Description

The description string for the import snapshot task.

**Type:** STRING

#### DiskContainer

Information about the disk container.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Encrypted

Specifies whether the destination snapshot of the imported image should be encrypted. The default CMK for EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) CMK using  KmsKeyId. For more information, see Amazon EBS Encryption in the  Amazon Elastic Compute Cloud User Guide.

**Type:** BOOLEAN

#### KmsKeyId

An identifier for the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted snapshot. This parameter is only required if you want to use a non-default CMK; if this parameter is not specified, the default CMK for EBS is used. If a KmsKeyId is specified, the Encrypted flag must also be set.  The CMK identifier may be provided in any of the following formats:  Key ID Key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias. ARN using key ID. The ID ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the key namespace, and then the CMK ID. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. ARN using key alias. The alias ARN contains the arn:aws:kms namespace, followed by the region of the CMK, the AWS account ID of the CMK owner, the alias namespace, and then the CMK alias. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.  AWS parses KmsKeyId asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.  The specified CMK must exist in the region that the snapshot is being copied to.

**Type:** STRING

#### RoleName

The name of the role to use when not using the default role, 'vmimport'.

**Type:** STRING

</details>

## import_volume

Creates an import volume task using metadata from the specified disk image.For more information, see Importing Disks to Amazon EBS.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportVolume.html

<details><summary>Parameters</summary>

#### AvailabilityZone (required)

The Availability Zone for the resulting EBS volume.

**Type:** STRING

#### Image (required)

The disk image.

**Type:** OBJECT

#### Volume (required)

The volume size.

**Type:** OBJECT

#### Description

A description of the volume.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_capacity_reservation

Modifies a Capacity Reservation's capacity and the conditions under which it is to be released. You cannot change a Capacity Reservation's instance type, EBS optimization, instance store settings, platform, Availability Zone, or instance eligibility. If you need to modify any of these attributes, we recommend that you cancel the Capacity Reservation, and then create a new one with the required attributes.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyCapacityReservation.html

<details><summary>Parameters</summary>

#### CapacityReservationId (required)

The ID of the Capacity Reservation.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides  an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise,  it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EndDate

The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to expired when it reaches its end date and time. The Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify  5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019. You must provide an EndDate value if EndDateType is limited. Omit EndDate if EndDateType is unlimited.

**Type:** STRING

#### EndDateType

Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types: unlimited - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an EndDate value if EndDateType is unlimited. limited - The Capacity Reservation expires automatically at a specified date and time. You must provide an EndDate value if EndDateType is limited.

**Type:** STRING

#### InstanceCount

The number of instances for which to reserve capacity.

**Type:** INTEGER

</details>

## modify_client_vpn_endpoint

Modifies the specified Client VPN endpoint. You can only modify an endpoint's server certificate information, client connection logging information, DNS server, and description. Modifying the DNS server resets existing client connections.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyClientVpnEndpoint.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint to modify.

**Type:** STRING

#### ConnectionLogOptions

Information about the client connection logging options. If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged: Client connection requests Client connection results (successful and unsuccessful) Reasons for unsuccessful client connection requests Client connection termination time

**Type:** OBJECT

#### Description

A brief description of the Client VPN endpoint.

**Type:** STRING

#### DnsServers

Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have  up to two DNS servers.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ServerCertificateArn

The ARN of the server certificate to be used. The server certificate must be provisioned in AWS Certificate Manager (ACM).

**Type:** STRING

</details>

## modify_fleet

Modifies the specified EC2 Fleet. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet.html

<details><summary>Parameters</summary>

#### FleetId (required)

The ID of the EC2 Fleet.

**Type:** STRING

#### TargetCapacitySpecification (required)

The size of the EC2 Fleet.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### ExcessCapacityTerminationPolicy

Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.

**Type:** STRING

</details>

## modify_fpga_image_attribute

Modifies the specified attribute of the specified Amazon FPGA Image (AFI). https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFpgaImageAttribute.html

<details><summary>Parameters</summary>

#### FpgaImageId (required)

The ID of the AFI.

**Type:** STRING

#### Attribute

The name of the attribute.

**Type:** STRING

#### Description

A description for the AFI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LoadPermission

The load permission for the AFI.

**Type:** OBJECT

#### Name

A name for the AFI.

**Type:** STRING

#### OperationType

The operation type.

**Type:** STRING

#### ProductCode

The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modifying the productCodes attribute.

**Type:** ARRAY

#### UserGroup

The user groups. This parameter is valid only when modifying the loadPermission attribute.

**Type:** ARRAY

#### UserId

The AWS account IDs. This parameter is valid only when modifying the loadPermission attribute.

**Type:** ARRAY

</details>

## modify_hosts

Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, any instances that you launch with a tenancy of host but without a specific host ID are placed onto any available Dedicated Host in your account that has auto-placement enabled. When auto-placement is disabled, you need to provide a host ID to have the instance launch onto a specific host. If no host ID is provided, the instance is launched onto a suitable host with auto-placement enabled.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyHosts.html

<details><summary>Parameters</summary>

#### AutoPlacement (required)

Specify whether to enable or disable auto-placement.

**Type:** STRING

#### HostId (required)

The IDs of the Dedicated Hosts to modify.

**Type:** ARRAY

</details>

## modify_id_format

Modifies the ID format for the specified resource on a per-region basis. You can specify that resources should receive longer IDs (17-character IDs) when they are created.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdFormat.html

<details><summary>Parameters</summary>

#### Resource (required)

The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. Alternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.

**Type:** STRING

#### UseLongIds (required)

Indicate whether the resource should use longer IDs (17-character IDs).

**Type:** BOOLEAN

</details>

## modify_identity_id_format

Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources should receive longer IDs (17-character IDs) when they are created.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdentityIdFormat.html

<details><summary>Parameters</summary>

#### PrincipalArn (required)

The ARN of the principal, which can be an IAM user, IAM role, or the root user. Specify all to modify the ID format for all IAM users, IAM roles, and the root user of the account.

**Type:** STRING

#### Resource (required)

The type of resource: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | route-table | route-table-association | security-group | subnet | subnet-cidr-block-association | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway. Alternatively, use the all-current option to include all resource types that are currently within their opt-in period for longer IDs.

**Type:** STRING

#### UseLongIds (required)

Indicates whether the resource should use longer IDs (17-character IDs)

**Type:** BOOLEAN

</details>

## modify_image_attribute

Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time. You can use the Attribute parameter to specify the attribute or one of the following parameters: Description, LaunchPermission, or ProductCode.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html

<details><summary>Parameters</summary>

#### ImageId (required)

The ID of the AMI.

**Type:** STRING

#### Attribute

The name of the attribute to modify.  The valid values are description, launchPermission, and productCodes.

**Type:** STRING

#### Description

A new description for the AMI.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchPermission

A new launch permission for the AMI.

**Type:** OBJECT

#### OperationType

The operation type.  This parameter can be used only when the Attribute parameter is launchPermission.

**Type:** STRING

#### ProductCode

The DevPay product codes. After you add a product code to an AMI, it can't be removed.

**Type:** ARRAY

#### UserGroup

The user groups.  This parameter can be used only when the Attribute parameter is launchPermission.

**Type:** ARRAY

#### UserId

The AWS account IDs.  This parameter can be used only when the Attribute parameter is launchPermission.

**Type:** ARRAY

#### Value

The value of the attribute being modified.  This parameter can be used only when the Attribute parameter is description or productCodes.

**Type:** STRING

</details>

## modify_instance_attribute

Modifies the specified attribute of the specified instance. You can specify only one attribute at a time.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### Attribute

The name of the attribute.

**Type:** STRING

#### BlockDeviceMapping

Modifies the DeleteOnTermination attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for DeleteOnTermination, the default is true and the volume is deleted when the instance is terminated. To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see Updating the Block Device Mapping when Launching an Instance in the Amazon Elastic Compute Cloud User Guide.

**Type:** ARRAY

#### DisableApiTermination

If the value is true, you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. You cannot use this parameter for Spot Instances.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EbsOptimized

Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

**Type:** BOOLEAN

#### EnaSupport

Set to true to enable enhanced networking with ENA for the instance. This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.

**Type:** BOOLEAN

#### GroupId

[EC2-VPC] Changes the security groups of the instance. You must specify at least one security group, even if it's just the default security group for the VPC. You must specify the security group ID, not the security group name.

**Type:** ARRAY

#### InstanceInitiatedShutdownBehavior

Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).

**Type:** BOOLEAN

#### InstanceType

Changes the instance type to the specified value. For more information, see Instance Types. If the instance type is not valid, the error returned is InvalidInstanceAttributeValue.

**Type:** OBJECT

#### Kernel

Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB.

**Type:** OBJECT

#### Ramdisk

Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-GRUB.

**Type:** OBJECT

#### SourceDestCheck

Specifies whether source/destination checking is enabled. A value of true means that checking is enabled, and false means that checking is disabled. This value must be false for a NAT instance to perform NAT.

**Type:** OBJECT

#### SriovNetSupport

Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance. There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time. This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.

**Type:** OBJECT

#### UserData

Changes the instance's user data to the specified value. If you are using an AWS SDK or command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text.

**Type:** OBJECT

#### Value

A new value for the attribute. Use only with the kernel, ramdisk, userData, disableApiTermination, or instanceInitiatedShutdownBehavior attribute.

**Type:** STRING

</details>

## modify_instance_capacity_reservation_attributes

Modifies the Capacity Reservation settings for a stopped instance. Use this action to configure an instance to target a specific Capacity Reservation, run in any open Capacity Reservation with matching attributes, or run On-Demand Instance capacity.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCapacityReservationAttributes.html

<details><summary>Parameters</summary>

#### CapacityReservationSpecification (required)

Information about the Capacity Reservation targeting option.

**Type:** OBJECT

#### InstanceId (required)

The ID of the instance to be modified.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides  an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise,  it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_instance_credit_specification

Modifies the credit option for CPU usage on a running or stopped T2 or T3 instance. The credit options are standard and unlimited.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html

<details><summary>Parameters</summary>

#### InstanceCreditSpecification (required)

Information about the credit option for CPU usage.

**Type:** ARRAY

#### ClientToken

A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see Ensuring Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_instance_event_start_time

Modifies the start time for a scheduled Amazon EC2 instance event. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceEventStartTime.html

<details><summary>Parameters</summary>

#### InstanceEventId (required)

The ID of the event whose date and time you are modifying.

**Type:** STRING

#### InstanceId (required)

The ID of the instance with the scheduled event.

**Type:** STRING

#### NotBefore (required)

The new date and time when the event will take place.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_instance_placement

Modifies the placement attributes for a specified instance. You can do the following:  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstancePlacement.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The ID of the instance that you are modifying.

**Type:** STRING

#### Affinity

The affinity setting for the instance.

**Type:** STRING

#### GroupName

The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of default. For cluster and partition placement groups, the instance must have a tenancy of default or dedicated. To remove an instance from a placement group, specify an empty string ("").

**Type:** STRING

#### HostId

The ID of the Dedicated Host with which to associate the instance.

**Type:** STRING

#### PartitionNumber

Reserved for future use.

**Type:** INTEGER

#### Tenancy

The tenancy for the instance.

**Type:** STRING

</details>

## modify_launch_template

Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version is not specified.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyLaunchTemplate.html

<details><summary>Parameters</summary>

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency. Constraint: Maximum 128 ASCII characters.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LaunchTemplateId

The ID of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### LaunchTemplateName

The name of the launch template. You must specify either the launch template ID or launch template name in the request.

**Type:** STRING

#### SetDefaultVersion

The version number of the launch template to set as the default version.

**Type:** STRING

</details>

## modify_network_interface_attribute

Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### Attachment

Information about the interface attachment. If modifying the 'delete on termination' attribute, you must specify the ID of the interface attachment.

**Type:** OBJECT

#### Description

A description for the network interface.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### SecurityGroupId

Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.

**Type:** ARRAY

#### SourceDestCheck

Indicates whether source/destination checking is enabled. A value of true means checking is enabled, and false means checking is disabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT Instances in the Amazon Virtual Private Cloud User Guide.

**Type:** BOOLEAN

</details>

## modify_reserved_instances

Modifies the Availability Zone, instance count, instance type, or network platform (EC2-Classic or EC2-VPC) of your Reserved Instances. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyReservedInstances.html

<details><summary>Parameters</summary>

#### ReservedInstancesConfigurationSetItemType (required)

The configuration settings for the Reserved Instances to modify.

**Type:** ARRAY

#### ReservedInstancesId (required)

The IDs of the Reserved Instances to modify.

**Type:** ARRAY

#### ClientToken

A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see  Ensuring Idempotency.

**Type:** STRING

</details>

## modify_snapshot_attribute

Adds or removes permission settings for the specified snapshot. You may add or remove specified AWS account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single API call. If you need to both add and remove account IDs for a snapshot, you must use multiple API calls.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html

<details><summary>Parameters</summary>

#### SnapshotId (required)

The ID of the snapshot.

**Type:** STRING

#### Attribute

The snapshot attribute to modify. Only volume creation permissions can be modified.

**Type:** STRING

#### CreateVolumePermission

A JSON representation of the snapshot attribute modification.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### OperationType

The type of operation to perform to the attribute.

**Type:** STRING

#### UserGroup

The group to modify for the snapshot.

**Type:** ARRAY

#### UserId

The account ID to modify for the snapshot.

**Type:** ARRAY

</details>

## modify_spot_fleet_request

Modifies the specified Spot Fleet request. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html

<details><summary>Parameters</summary>

#### SpotFleetRequestId (required)

The ID of the Spot Fleet request.

**Type:** STRING

#### ExcessCapacityTerminationPolicy

Indicates whether running Spot Instances should be terminated if the target capacity of the Spot Fleet request is decreased below the current size of the Spot Fleet.

**Type:** STRING

#### TargetCapacity

The size of the fleet.

**Type:** INTEGER

</details>

## modify_subnet_attribute

Modifies a subnet attribute. You can only modify one attribute at a time. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySubnetAttribute.html

<details><summary>Parameters</summary>

#### SubnetId (required)

The ID of the subnet.

**Type:** STRING

#### AssignIpv6AddressOnCreation

Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives an IPv6 address).  If you enable the IPv6 addressing feature for your subnet, your network interface or instance only receives an IPv6 address if it's created using version 2016-11-15 or later of the Amazon EC2 API.

**Type:** BOOLEAN

#### MapPublicIpOnLaunch

Specify true to indicate that network interfaces created in the specified subnet should be assigned a public IPv4 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives a public IPv4 address).

**Type:** BOOLEAN

</details>

## modify_transit_gateway_vpc_attachment

Modifies the specified VPC attachment. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayVpcAttachment.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### AddSubnetIds

The IDs of one or more subnets to add. You can specify at most one subnet per Availability Zone.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Options

The new VPC attachment options.

**Type:** OBJECT

#### RemoveSubnetIds

The IDs of one or more subnets to remove.

**Type:** ARRAY

</details>

## modify_volume

You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you may be able to apply these changes without stopping the instance or detaching the volume from it. For more information about modifying an EBS volume running Linux, see Modifying the Size, IOPS, or Type of an EBS Volume on Linux. For more information about modifying an EBS volume running Windows, see Modifying the Size, IOPS, or Type of an EBS Volume on Windows.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Iops

The target IOPS rate of the volume. This is only valid for Provisioned IOPS SSD (io1) volumes. For more information, see Provisioned IOPS SSD (io1) Volumes. Default: If no IOPS value is specified, the existing value is retained.

**Type:** INTEGER

#### Size

The target size of the volume, in GiB. The target volume size must be greater than or equal to than the existing size of the volume. For information about available EBS volume sizes, see Amazon EBS Volume Types. Default: If no size is specified, the existing size is retained.

**Type:** INTEGER

#### VolumeType

The target EBS volume type of the volume. Default: If no type is specified, the existing type is retained.

**Type:** STRING

</details>

## modify_volume_attribute

Modifies a volume attribute. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolumeAttribute.html

<details><summary>Parameters</summary>

#### VolumeId (required)

The ID of the volume.

**Type:** STRING

#### AutoEnableIO

Indicates whether the volume should be auto-enabled for I/O operations.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_vpc_attribute

Modifies the specified attribute of the specified VPC. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcAttribute.html

<details><summary>Parameters</summary>

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### EnableDnsHostnames

Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.

**Type:** BOOLEAN

#### EnableDnsSupport

Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.

**Type:** BOOLEAN

</details>

## modify_vpc_endpoint

Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface or gateway). For more information, see VPC Endpoints in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html

<details><summary>Parameters</summary>

#### VpcEndpointId (required)

The ID of the endpoint.

**Type:** STRING

#### AddRouteTableId

(Gateway endpoint) One or more route tables IDs to associate with the endpoint.

**Type:** ARRAY

#### AddSecurityGroupId

(Interface endpoint) One or more security group IDs to associate with the network interface.

**Type:** ARRAY

#### AddSubnetId

(Interface endpoint) One or more subnet IDs in which to serve the endpoint.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PolicyDocument

A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format. If this parameter is not specified, we attach a default policy that allows full access to the service.

**Type:** STRING

#### PrivateDnsEnabled

(Interface endpoint) Indicate whether a private hosted zone is associated with the VPC.

**Type:** BOOLEAN

#### RemoveRouteTableId

(Gateway endpoint) One or more route table IDs to disassociate from the endpoint.

**Type:** ARRAY

#### RemoveSecurityGroupId

(Interface endpoint) One or more security group IDs to disassociate from the network interface.

**Type:** ARRAY

#### RemoveSubnetId

(Interface endpoint) One or more subnets IDs in which to remove the endpoint.

**Type:** ARRAY

#### ResetPolicy

(Gateway endpoint) Specify true to reset the policy document to the default policy. The default policy allows full access to the service.

**Type:** BOOLEAN

</details>

## modify_vpc_endpoint_connection_notification

Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointConnectionNotification.html

<details><summary>Parameters</summary>

#### ConnectionNotificationId (required)

The ID of the notification.

**Type:** STRING

#### ConnectionEvents

One or more events for the endpoint. Valid values are Accept, Connect, Delete, and Reject.

**Type:** ARRAY

#### ConnectionNotificationArn

The ARN for the SNS topic for the notification.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## modify_vpc_endpoint_service_configuration

Modifies the attributes of your VPC endpoint service configuration. You can change the Network Load Balancers for your service, and you can specify whether acceptance is required for requests to connect to your endpoint service through an interface VPC endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServiceConfiguration.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The ID of the service.

**Type:** STRING

#### AcceptanceRequired

Indicate whether requests to create an endpoint to your service must be accepted.

**Type:** BOOLEAN

#### AddNetworkLoadBalancerArn

The Amazon Resource Names (ARNs) of Network Load Balancers to add to your service configuration.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### RemoveNetworkLoadBalancerArn

The Amazon Resource Names (ARNs) of Network Load Balancers to remove from your service configuration.

**Type:** ARRAY

</details>

## modify_vpc_endpoint_service_permissions

Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (IAM users, IAM roles, and AWS accounts) to connect to your endpoint service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServicePermissions.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The ID of the service.

**Type:** STRING

#### AddAllowedPrincipals

The Amazon Resource Names (ARN) of one or more principals. Permissions are granted to the principals in this list. To grant permissions to all principals, specify an asterisk (*).

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### RemoveAllowedPrincipals

The Amazon Resource Names (ARN) of one or more principals. Permissions are revoked for principals in this list.

**Type:** ARRAY

</details>

## modify_vpc_peering_connection_options

Modifies the VPC peering connection options on one side of a VPC peering connection. You can do the following:  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcPeeringConnectionOptions.html

<details><summary>Parameters</summary>

#### VpcPeeringConnectionId (required)

The ID of the VPC peering connection.

**Type:** STRING

#### AccepterPeeringConnectionOptions

The VPC peering connection options for the accepter VPC.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### RequesterPeeringConnectionOptions

The VPC peering connection options for the requester VPC.

**Type:** OBJECT

</details>

## modify_vpc_tenancy

Modifies the instance tenancy attribute of the specified VPC. You can change the instance tenancy attribute of a VPC to default only. You cannot change the instance tenancy attribute to dedicated.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcTenancy.html

<details><summary>Parameters</summary>

#### InstanceTenancy (required)

The instance tenancy attribute for the VPC.

**Type:** STRING

#### VpcId (required)

The ID of the VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## monitor_instances

Enables detailed monitoring for a running instance. Otherwise, basic monitoring is enabled. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The IDs of the instances.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## move_address_to_vpc

Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform. The Elastic IP address must be allocated to your account for more than 24 hours, and it must not be associated with an instance. After the Elastic IP address is moved, it is no longer available for use in the EC2-Classic platform, unless you move it back using the RestoreAddressToClassic request. You cannot move an Elastic IP address that was originally allocated for use in the EC2-VPC platform to the EC2-Classic platform.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveAddressToVpc.html

<details><summary>Parameters</summary>

#### PublicIp (required)

The Elastic IP address.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## provision_byoip_cidr

Provisions an address range for use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using AdvertiseByoipCidr.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionByoipCidr.html

<details><summary>Parameters</summary>

#### Cidr (required)

The public IPv4 address range, in CIDR notation. The most specific prefix that you can  specify is /24. The address range cannot overlap with another address range that you've brought to this or another region.

**Type:** STRING

#### CidrAuthorizationContext

A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.

**Type:** OBJECT

#### Description

A description for the address range and the address pool.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## purchase_host_reservation

Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseHostReservation.html

<details><summary>Parameters</summary>

#### HostIdSet (required)

The IDs of the Dedicated Hosts with which the reservation will be associated.

**Type:** ARRAY

#### OfferingId (required)

The ID of the offering.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see How to Ensure Idempotency in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### CurrencyCode

The currency in which the totalUpfrontPrice, LimitPrice, and totalHourlyPrice amounts are specified. At this time, the only supported currency is USD.

**Type:** STRING

#### LimitPrice

The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request fails. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is USD. For example, to indicate a limit price of USD 100, specify 100.00.

**Type:** STRING

</details>

## purchase_reserved_instances_offering

Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html

<details><summary>Parameters</summary>

#### InstanceCount (required)

The number of Reserved Instances to purchase.

**Type:** INTEGER

#### ReservedInstancesOfferingId (required)

The ID of the Reserved Instance offering to purchase.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### LimitPrice

Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.

**Type:** BOOLEAN

</details>

## purchase_scheduled_instances

Purchases the Scheduled Instances with the specified schedule. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseScheduledInstances.html

<details><summary>Parameters</summary>

#### PurchaseRequest (required)

The purchase requests.

**Type:** ARRAY

#### ClientToken

Unique, case-sensitive identifier that ensures the idempotency of the request.  For more information, see Ensuring Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reboot_instances

Requests a reboot of the specified instances. This operation is asynchronous; it only queues a request to reboot the specified instances. The operation succeeds if the instances are valid and belong to you. Requests to reboot terminated instances are ignored.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The instance IDs.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## register_image

Registers an AMI. When you're creating an AMI, this is the final step you must complete before you can launch an instance from the AMI. For more information about creating AMIs, see Creating Your Own AMIs in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html

<details><summary>Parameters</summary>

#### Name (required)

A name for your AMI. Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)

**Type:** STRING

#### Architecture

The architecture of the AMI. Default: For Amazon EBS-backed AMIs, i386. For instance store-backed AMIs, the architecture specified in the manifest file.

**Type:** STRING

#### BillingProduct

The billing product codes. Your account must be authorized to specify billing product codes. Otherwise, you can use the AWS Marketplace to bill for the use of an AMI.

**Type:** ARRAY

#### BlockDeviceMapping

The block device mapping entries.

**Type:** ARRAY

#### Description

A description for your AMI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EnaSupport

Set to true to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI. This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.

**Type:** BOOLEAN

#### ImageLocation

The full path to your AMI manifest in Amazon S3 storage.

**Type:** STRING

#### KernelId

The ID of the kernel.

**Type:** STRING

#### RamdiskId

The ID of the RAM disk.

**Type:** STRING

#### RootDeviceName

The device name of the root device volume (for example, /dev/sda1).

**Type:** STRING

#### SriovNetSupport

Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI. There is no way to disable sriovNetSupport at this time. This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.

**Type:** STRING

#### VirtualizationType

The type of virtualization (hvm | paravirtual). Default: paravirtual

**Type:** STRING

</details>

## reject_transit_gateway_vpc_attachment

Rejects a request to attach a VPC to a transit gateway. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayVpcAttachment.html

<details><summary>Parameters</summary>

#### TransitGatewayAttachmentId (required)

The ID of the attachment.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reject_vpc_endpoint_connections

Rejects one or more VPC endpoint connection requests to your VPC endpoint service.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcEndpointConnections.html

<details><summary>Parameters</summary>

#### ServiceId (required)

The ID of the service.

**Type:** STRING

#### VpcEndpointId (required)

The IDs of one or more VPC endpoints.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reject_vpc_peering_connection

Rejects a VPC peering connection request. The VPC peering connection must be in the pending-acceptance state. Use the DescribeVpcPeeringConnections request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use DeleteVpcPeeringConnection.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcPeeringConnection.html

<details><summary>Parameters</summary>

#### VpcPeeringConnectionId (required)

The ID of the VPC peering connection.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## release_address

Releases the specified Elastic IP address. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseAddress.html

<details><summary>Parameters</summary>

#### AllocationId

[EC2-VPC] The allocation ID. Required for EC2-VPC.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### PublicIp

[EC2-Classic] The Elastic IP address. Required for EC2-Classic.

**Type:** STRING

</details>

## release_hosts

When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into released state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, for example, to modify the host. You must stop or terminate all instances on a host before it can be released.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseHosts.html

<details><summary>Parameters</summary>

#### HostId (required)

The IDs of the Dedicated Hosts to release.

**Type:** ARRAY

</details>

## replace_iam_instance_profile_association

Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceIamInstanceProfileAssociation.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The ID of the existing IAM instance profile association.

**Type:** STRING

#### IamInstanceProfile (required)

The IAM instance profile.

**Type:** OBJECT

</details>

## replace_network_acl_association

Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclAssociation.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The ID of the current association between the original network ACL and the subnet.

**Type:** STRING

#### NetworkAclId (required)

The ID of the new network ACL to associate with the subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## replace_network_acl_entry

Replaces an entry (rule) in a network ACL. For more information, see Network ACLs in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclEntry.html

<details><summary>Parameters</summary>

#### Egress (required)

Indicates whether to replace the egress rule. Default: If no value is specified, we replace the ingress rule.

**Type:** BOOLEAN

#### NetworkAclId (required)

The ID of the ACL.

**Type:** STRING

#### Protocol (required)

The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), "17" (UDP), or "1" (ICMP), traffic on all ports is  allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and  codes allowed, regardless of any that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.

**Type:** STRING

#### RuleAction (required)

Indicates whether to allow or deny the traffic that matches the rule.

**Type:** STRING

#### RuleNumber (required)

The rule number of the entry to replace.

**Type:** INTEGER

#### CidrBlock

The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24).

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Icmp

ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.

**Type:** OBJECT

#### Ipv6CidrBlock

The IPv6 network range to allow or deny, in CIDR notation (for example 2001:bd8:1234:1a00::/64).

**Type:** STRING

#### PortRange

TCP or UDP protocols: The range of ports the rule applies to.  Required if specifying protocol 6 (TCP) or 17 (UDP).

**Type:** OBJECT

</details>

## replace_route

Replaces an existing route within a route table in a VPC. You must provide only one of the following: internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, or egress-only internet gateway.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRoute.html

<details><summary>Parameters</summary>

#### RouteTableId (required)

The ID of the route table.

**Type:** STRING

#### DestinationCidrBlock

The IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.

**Type:** STRING

#### DestinationIpv6CidrBlock

The IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EgressOnlyInternetGatewayId

[IPv6 traffic only] The ID of an egress-only internet gateway.

**Type:** STRING

#### GatewayId

The ID of an internet gateway or virtual private gateway.

**Type:** STRING

#### InstanceId

The ID of a NAT instance in your VPC.

**Type:** STRING

#### NatGatewayId

[IPv4 traffic only] The ID of a NAT gateway.

**Type:** STRING

#### NetworkInterfaceId

The ID of a network interface.

**Type:** STRING

#### TransitGatewayId

The ID of a transit gateway.

**Type:** STRING

#### VpcPeeringConnectionId

The ID of a VPC peering connection.

**Type:** STRING

</details>

## replace_route_table_association

Changes the route table associated with a given subnet in a VPC. After the operation completes, the subnet uses the routes in the new route table it's associated with. For more information about route tables, see Route Tables in the Amazon Virtual Private Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRouteTableAssociation.html

<details><summary>Parameters</summary>

#### AssociationId (required)

The association ID.

**Type:** STRING

#### RouteTableId (required)

The ID of the new route table to associate with the subnet.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## replace_transit_gateway_route

Replaces the specified route in the specified transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceTransitGatewayRoute.html

<details><summary>Parameters</summary>

#### DestinationCidrBlock (required)

The CIDR range used for the destination match. Routing decisions are based on the most specific match.

**Type:** STRING

#### TransitGatewayRouteTableId (required)

The ID of the route table.

**Type:** STRING

#### Blackhole

Indicates whether traffic matching this route is to be dropped.

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### TransitGatewayAttachmentId

The ID of the attachment.

**Type:** STRING

</details>

## report_instance_status

Submits feedback about the status of an instance. The instance must be in the running state. If your experience with the instance differs from the instance status returned by DescribeInstanceStatus, use ReportInstanceStatus to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReportInstanceStatus.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The instances.

**Type:** ARRAY

#### ReasonCode (required)

The reason codes that describe the health state of your instance. instance-stuck-in-state: My instance is stuck in a state. unresponsive: My instance is unresponsive. not-accepting-credentials: My instance is not accepting my credentials. password-not-available: A password is not available for my instance. performance-network: My instance is experiencing performance problems that I believe are network related. performance-instance-store: My instance is experiencing performance problems that I believe are related to the instance stores. performance-ebs-volume: My instance is experiencing performance problems that I believe are related to an EBS volume. performance-other: My instance is experiencing performance problems. other: [explain using the description parameter]

**Type:** ARRAY

#### Status (required)

The status of all instances listed.

**Type:** STRING

#### Description

Descriptive text about the health state of your instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EndTime

The time at which the reported instance health state ended.

**Type:** STRING

#### StartTime

The time at which the reported instance health state began.

**Type:** STRING

</details>

## request_spot_fleet

Creates a Spot Fleet request. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html

<details><summary>Parameters</summary>

#### SpotFleetRequestConfig (required)

The configuration for the Spot Fleet request.

**Type:** OBJECT

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## request_spot_instances

Creates a Spot Instance request. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html

<details><summary>Parameters</summary>

#### AvailabilityZoneGroup

The user-specified name for a logical grouping of requests. When you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active. If there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group. Default: Instances are launched in any available Availability Zone.

**Type:** STRING

#### BlockDurationMinutes

The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360). The duration period starts as soon as your Spot Instance receives its instance ID. At the end of the duration period, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates. You can't specify an Availability Zone group or a launch group if you specify a duration.

**Type:** INTEGER

#### ClientToken

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  For more information, see How to Ensure Idempotency  in the Amazon EC2 User Guide for Linux Instances.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### InstanceCount

The maximum number of Spot Instances to launch. Default: 1

**Type:** INTEGER

#### InstanceInterruptionBehavior

The behavior when a Spot Instance is interrupted. The default is terminate.

**Type:** STRING

#### LaunchGroup

The instance launch group. Launch groups are Spot Instances that launch together and terminate together. Default: Instances are launched and terminated individually

**Type:** STRING

#### LaunchSpecification

The launch specification.

**Type:** OBJECT

#### SpotPrice

The maximum price per hour that you are willing to pay for a Spot Instance. The default is the On-Demand price.

**Type:** STRING

#### Type

The Spot Instance request type. Default: one-time

**Type:** STRING

#### ValidFrom

The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.

**Type:** STRING

#### ValidUntil

The end date of the request. If this is a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached.  If the request is persistent, it remains active until it is canceled or this date is reached. The default end date is 7 days from the current date.

**Type:** STRING

</details>

## reset_fpga_image_attribute

Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetFpgaImageAttribute.html

<details><summary>Parameters</summary>

#### FpgaImageId (required)

The ID of the AFI.

**Type:** STRING

#### Attribute

The attribute.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reset_image_attribute

Resets an attribute of an AMI to its default value. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetImageAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The attribute to reset (currently you can only reset the launch permission attribute).

**Type:** STRING

#### ImageId (required)

The ID of the AMI.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reset_instance_attribute

Resets an attribute of an instance to its default value. To reset the kernel or ramdisk, the instance must be in a stopped state. To reset the sourceDestCheck, the instance can be either running or stopped.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetInstanceAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The attribute to reset. Important You can only reset the following attributes: kernel | ramdisk | sourceDestCheck. To change an instance attribute, use ModifyInstanceAttribute.

**Type:** STRING

#### InstanceId (required)

The ID of the instance.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## reset_network_interface_attribute

Resets a network interface attribute. You can specify only one attribute at a time. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetNetworkInterfaceAttribute.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### SourceDestCheck

The source/destination checking attribute. Resets the value to true.

**Type:** STRING

</details>

## reset_snapshot_attribute

Resets permission settings for the specified snapshot. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetSnapshotAttribute.html

<details><summary>Parameters</summary>

#### Attribute (required)

The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.

**Type:** STRING

#### SnapshotId (required)

The ID of the snapshot.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## restore_address_to_classic

Restores an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform. You cannot move an Elastic IP address that was originally allocated for use in EC2-VPC. The Elastic IP address must not be associated with an instance or network interface.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreAddressToClassic.html

<details><summary>Parameters</summary>

#### PublicIp (required)

The Elastic IP address.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## revoke_client_vpn_ingress

Removes an ingress authorization rule from a Client VPN endpoint.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeClientVpnIngress.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint with which the authorization rule is associated.

**Type:** STRING

#### TargetNetworkCidr (required)

The IPv4 address range, in CIDR notation, of the network for which access is being removed.

**Type:** STRING

#### AccessGroupId

The ID of the Active Directory group for which to revoke access.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### RevokeAllGroups

Indicates whether access should be revoked for all clients.

**Type:** BOOLEAN

</details>

## revoke_security_group_egress

[EC2-VPC only] Removes the specified egress rules from a security group for EC2-VPC. This action doesn't apply to security groups for use in EC2-Classic. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html

<details><summary>Parameters</summary>

#### GroupId (required)

The ID of the security group.

**Type:** STRING

#### CidrIp

Not supported. Use a set of IP permissions to specify the CIDR.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### FromPort

Not supported. Use a set of IP permissions to specify the port.

**Type:** INTEGER

#### IpPermissions

The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set of permissions.

**Type:** ARRAY

#### IpProtocol

Not supported. Use a set of IP permissions to specify the protocol name or number.

**Type:** STRING

#### SourceSecurityGroupName

Not supported. Use a set of IP permissions to specify a destination security group.

**Type:** STRING

#### SourceSecurityGroupOwnerId

Not supported. Use a set of IP permissions to specify a destination security group.

**Type:** STRING

#### ToPort

Not supported. Use a set of IP permissions to specify the port.

**Type:** INTEGER

</details>

## revoke_security_group_ingress

Removes the specified ingress rules from a security group. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html

<details><summary>Parameters</summary>

#### CidrIp

The CIDR IP address range. You can't specify this parameter when specifying a source security group.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### FromPort

The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number,  use -1 to specify all ICMP types.

**Type:** INTEGER

#### GroupId

The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.

**Type:** STRING

#### GroupName

[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.

**Type:** STRING

#### IpPermissions

The sets of IP permissions. You can't specify a source security group and a CIDR IP address range in the same set of permissions.

**Type:** ARRAY

#### IpProtocol

The IP protocol name (tcp, udp, icmp) or number  (see Protocol Numbers).  Use -1 to specify all.

**Type:** STRING

#### SourceSecurityGroupName

[EC2-Classic, default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. For EC2-VPC, the source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.

**Type:** STRING

#### SourceSecurityGroupOwnerId

[EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the IP protocol, the start of the port range, and the end of the port range. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.

**Type:** STRING

#### ToPort

The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number,  use -1 to specify all ICMP codes for the ICMP type.

**Type:** INTEGER

</details>

## run_instances

Launches the specified number of instances using an AMI for which you have permissions.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html

<details><summary>Parameters</summary>

#### MaxCount (required)

The maximum number of instances to launch. If you specify more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above MinCount. Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 FAQ.

**Type:** INTEGER

#### MinCount (required)

The minimum number of instances to launch. If you specify a minimum that is more instances than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches no instances. Constraints: Between 1 and the maximum number you're allowed for the specified instance type. For more information about the default limits, and how to request an increase, see How many instances can I run in Amazon EC2 in the Amazon EC2 General FAQ.

**Type:** INTEGER

#### AdditionalInfo

Reserved.

**Type:** STRING

#### BlockDeviceMapping

The block device mapping entries. You can't specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.

**Type:** ARRAY

#### CapacityReservationSpecification

Information about the Capacity Reservation targeting option. If you do not specify this parameter, the  instance's Capacity Reservation preference defaults to open, which enables it to run in any open Capacity Reservation that has matching attributes (instance type,  platform, Availability Zone).

**Type:** OBJECT

#### ClientToken

Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see Ensuring Idempotency. Constraints: Maximum 64 ASCII characters

**Type:** STRING

#### CpuOptions

The CPU options for the instance. For more information, see Optimizing CPU Options in the Amazon Elastic Compute Cloud User Guide.

**Type:** OBJECT

#### CreditSpecification

The credit option for CPU usage of the instance. Valid values are standard and unlimited. To change this attribute after launch,  use ModifyInstanceCreditSpecification. For more information, see Burstable Performance Instances in the Amazon Elastic Compute Cloud User Guide. Default: standard (T2 instances) or unlimited (T3 instances)

**Type:** OBJECT

#### DisableApiTermination

If you set this parameter to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can. To change this attribute to false after launch, use ModifyInstanceAttribute. Alternatively, if you set InstanceInitiatedShutdownBehavior to terminate, you can terminate the instance by running the shutdown command from the instance. Default: false

**Type:** BOOLEAN

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### EbsOptimized

Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance. Default: false

**Type:** BOOLEAN

#### ElasticGpuSpecification

An elastic GPU to associate with the instance.

**Type:** ARRAY

#### ElasticInferenceAccelerator

An elastic inference accelerator.

**Type:** ARRAY

#### HibernationOptions

Indicates whether an instance is enabled for hibernation. For more information, see Hibernate Your Instance in the Amazon Elastic Compute Cloud User Guide.

**Type:** OBJECT

#### IamInstanceProfile

The IAM instance profile.

**Type:** OBJECT

#### ImageId

The ID of the AMI, which you can get by calling DescribeImages. An AMI is required to launch an instance and must be specified here or in a launch template.

**Type:** STRING

#### InstanceInitiatedShutdownBehavior

Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown). Default: stop

**Type:** STRING

#### InstanceMarketOptions

The market (purchasing) option for the instances.

**Type:** OBJECT

#### InstanceType

The instance type. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide. Default: m1.small

**Type:** STRING

#### Ipv6Address

[EC2-VPC] The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch. You cannot specify this option and the network interfaces option in the same request.

**Type:** ARRAY

#### Ipv6AddressCount

[EC2-VPC] A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch. You cannot specify this option and the network interfaces option in the same request.

**Type:** INTEGER

#### KernelId

The ID of the kernel. Important We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see  PV-GRUB in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### KeyName

The name of the key pair. You can create a key pair using CreateKeyPair or ImportKeyPair. Important If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.

**Type:** STRING

#### LaunchTemplate

The launch template to use to launch the instances. Any parameters that you specify in RunInstances override the same parameters in the launch template. You can specify either the name or ID of a launch template, but not both.

**Type:** OBJECT

#### LicenseSpecification

The license configurations.

**Type:** ARRAY

#### Monitoring

The monitoring for the instance.

**Type:** OBJECT

#### NetworkInterface

The network interfaces. You cannot specify this option and the network interfaces option in the same request.

**Type:** ARRAY

#### Placement

The placement for the instance.

**Type:** OBJECT

#### PrivateIpAddress

[EC2-VPC] The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet. Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request. You cannot specify this option and the network interfaces option in the same request.

**Type:** STRING

#### RamdiskId

The ID of the RAM disk. Important We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see  PV-GRUB in the Amazon Elastic Compute Cloud User Guide.

**Type:** STRING

#### SecurityGroup

[EC2-Classic, default VPC] The names of the security groups. For a nondefault VPC, you must use security group IDs instead. You cannot specify this option and the network interfaces option in the same request. Default: Amazon EC2 uses the default security group.

**Type:** ARRAY

#### SecurityGroupId

The IDs of the security groups. You can create a security group using CreateSecurityGroup. Default: Amazon EC2 uses the default security group. You cannot specify this option and the network interfaces option in the same request.

**Type:** ARRAY

#### SubnetId

[EC2-VPC] The ID of the subnet to launch the instance into. You cannot specify this option and the network interfaces option in the same request.

**Type:** STRING

#### TagSpecification

The tags to apply to the resources during launch. You can only tag instances and volumes on launch. The specified tags are applied to all instances or volumes that are created during launch. To tag a resource after it has been created, see CreateTags.

**Type:** ARRAY

#### UserData

The user data to make available to the instance. For more information, see Running Commands on Your Linux Instance at Launch (Linux) and Adding User Data (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text. User data is limited to 16 KB.

**Type:** STRING

</details>

## run_scheduled_instances

Launches the specified Scheduled Instances. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunScheduledInstances.html

<details><summary>Parameters</summary>

#### LaunchSpecification (required)

The launch specification. You must match the instance type, Availability Zone,  network, and platform of the schedule that you purchased.

**Type:** OBJECT

#### ScheduledInstanceId (required)

The Scheduled Instance ID.

**Type:** STRING

#### ClientToken

Unique, case-sensitive identifier that ensures the idempotency of the request.  For more information, see Ensuring Idempotency.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### InstanceCount

The number of instances. Default: 1

**Type:** INTEGER

</details>

## search_transit_gateway_routes

Searches for routes in the specified transit gateway route table. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayRoutes.html

<details><summary>Parameters</summary>

#### Filter (required)

One or more filters. The possible values are: attachment.transit-gateway-attachment-id- The id of the transit gateway attachment. attachment.resource-id - The resource id of the transit gateway attachment. attachment.resource-type - The attachment resource type (vpc | vpn). route-search.exact-match - The exact match of the specified filter. route-search.longest-prefix-match - The longest prefix that matches the route. route-search.subnet-of-match - The routes with a subnet that match the specified CIDR filter. route-search.supernet-of-match - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29. state - The state of the attachment (available | deleted | deleting | failed |  modifying | pendingAcceptance | pending | rollingBack | rejected | rejecting). type - The type of roue (active | blackhole).

**Type:** ARRAY

#### TransitGatewayRouteTableId (required)

The ID of the transit gateway route table.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### MaxResults

The maximum number of routes to return.

**Type:** INTEGER

</details>

## start_instances

Starts an Amazon EBS-backed instance that you've previously stopped. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The IDs of the instances.

**Type:** ARRAY

#### AdditionalInfo

Reserved.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## stop_instances

Stops an Amazon EBS-backed instance. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The IDs of the instances.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Force

Forces the instances to stop. The instances do not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances. Default: false

**Type:** BOOLEAN

#### Hibernate

Hibernates the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successfully, a normal shutdown occurs. For more information, see  Hibernate Your Instance in the Amazon Elastic Compute Cloud User Guide. Default: false

**Type:** BOOLEAN

</details>

## terminate_client_vpn_connections

Terminates active Client VPN endpoint connections. This action can be used to terminate a specific client connection, or up to five connections established by a specific user.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateClientVpnConnections.html

<details><summary>Parameters</summary>

#### ClientVpnEndpointId (required)

The ID of the Client VPN endpoint to which the client is connected.

**Type:** STRING

#### ConnectionId

The ID of the client connection to be terminated.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is DryRunOperation. Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### Username

The name of the user who initiated the connection. Use this option to terminate all active connections for  the specified user. This option can only be used if the user has established up to five connections.

**Type:** STRING

</details>

## terminate_instances

Shuts down the specified instances. This operation is idempotent; if you terminate an instance more than once, each call succeeds.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The IDs of the instances. Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## unassign_private_ip_addresses

Unassigns one or more secondary private IP addresses from a network interface. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html

<details><summary>Parameters</summary>

#### NetworkInterfaceId (required)

The ID of the network interface.

**Type:** STRING

#### PrivateIpAddress (required)

The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.

**Type:** ARRAY

</details>

## unmonitor_instances

Disables detailed monitoring for a running instance. For more information, see Monitoring Your Instances and Volumes in the Amazon Elastic Compute Cloud User Guide.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html

<details><summary>Parameters</summary>

#### InstanceId (required)

The IDs of the instances.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

## update_security_group_rule_descriptions_egress

[EC2-VPC only] Updates the description of an egress (outbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html

<details><summary>Parameters</summary>

#### IpPermissions (required)

The IP permissions for the security group rule.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### GroupId

The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.

**Type:** STRING

#### GroupName

[Default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.

**Type:** STRING

</details>

## update_security_group_rule_descriptions_ingress

Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously.  https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html

<details><summary>Parameters</summary>

#### IpPermissions (required)

The IP permissions for the security group rule.

**Type:** ARRAY

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

#### GroupId

The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.

**Type:** STRING

#### GroupName

[EC2-Classic, default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request.

**Type:** STRING

</details>

## withdraw_byoip_cidr

Stops advertising an IPv4 address range that is provisioned as an address pool. https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_WithdrawByoipCidr.html

<details><summary>Parameters</summary>

#### Cidr (required)

The public IPv4 address range, in CIDR notation.

**Type:** STRING

#### DryRun

Checks whether you have the required permissions for the action, without actually making the request,  and provides an error response. If you have the required permissions, the error response is DryRunOperation.  Otherwise, it is UnauthorizedOperation.

**Type:** BOOLEAN

</details>

