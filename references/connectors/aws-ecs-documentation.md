---
id: aws-ecs-documentation
title: AWS ECS (version v5.*.*)
sidebar_label: AWS ECS
layout: docs.mustache
---

## create_cluster

Creates a new Amazon ECS cluster. By default, your account receives a default cluster when you launch your first container instance. However, you can create your own cluster with a unique name with the CreateCluster action.  
When you call the CreateCluster API operation, Amazon ECS attempts to create the service-linked role for your account so that required resources in other AWS services can be managed on your behalf. However, if the IAM user that makes the call does not have permissions to create the service-linked role, it is not created. For more information, see Using Service-Linked Roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "clusterName" : "The name of your cluster. If you do not specify a name for your cluster, you create a cluster named default. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed."
}
```

</details>

## create_service

Runs and maintains a desired number of tasks from a specified task definition. If the number of tasks running in a service drops below desiredCount, Amazon ECS spawns another copy of the task in the specified cluster. To update an existing service, see UpdateService. 
In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind a load balancer. The load balancer distributes traffic across the tasks that are associated with the service. For more information, see Service Load Balancing in the Amazon Elastic Container Service Developer Guide. 
You can optionally specify a deployment configuration for your service. During a deployment, the service scheduler uses the minimumHealthyPercent and maximumPercent parameters to determine the deployment strategy. The deployment is triggered by changing the task definition or the desired count of a service with an UpdateService operation. 
The minimumHealthyPercent represents a lower limit on the number of your service's tasks that must remain in the RUNNING state during a deployment, as a percentage of the desiredCount (rounded up to the nearest integer). This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desiredCount of four tasks and a minimumHealthyPercent of 50%, the scheduler can stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state. Tasks for services that do use a load balancer are considered healthy if they are in the RUNNING state and the container instance they are hosted on is reported as healthy by the load balancer. The default value for a replica service for minimumHealthyPercent is 50% in the console and 100% for the AWS CLI, the AWS SDKs, and the APIs. The default value for a daemon service for minimumHealthyPercent is 0% for the AWS CLI, the AWS SDKs, and the APIs and 50% for the console. 
The maximumPercent parameter represents an upper limit on the number of your service's tasks that are allowed in the RUNNING or PENDING state during a deployment, as a percentage of the desiredCount (rounded down to the nearest integer). This parameter enables you to define the deployment batch size. For example, if your replica service has a desiredCount of four tasks and a maximumPercent value of 200%, the scheduler can start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for a replica service for maximumPercent is 200%. If you are using a daemon service type, the maximumPercent should remain at 100%, which is the default value. 
When the service scheduler launches new tasks, it determines task placement in your cluster using the following logic:  
 Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes).  
 By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy) with the placementStrategy parameter):   Sort the valid container instances, giving priority to instances that have the fewest number of running tasks for this service in their respective Availability Zone. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.   Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.   

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service. If you do not specify a cluster, the default cluster is assumed.",
  "placementConstraints" : [ {
    "expression" : "A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.",
    "type" : "The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions."
  } ],
  "role" : "The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition does not use the awsvpc network mode. If you specify the role parameter, you must also specify a load balancer object with the loadBalancers parameter.  \nIf your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here. The service-linked role is required if your task definition uses the awsvpc network mode, in which case you should not specify a role here. For more information, see Using Service-Linked Roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide.  \nIf your specified role has a path other than /, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name bar has a path of /foo/ then you would specify /foo/bar as the role name. For more information, see Friendly Names and Paths in the IAM User Guide.",
  "networkConfiguration" : {
    "awsvpcConfiguration" : {
      "assignPublicIp" : "Whether the task's elastic network interface receives a public IP address. The default value is DISABLED.",
      "subnets" : [ "string" ],
      "securityGroups" : [ "string" ]
    }
  },
  "clientToken" : "Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.",
  "desiredCount" : "The number of instantiations of the specified task definition to place and keep running on your cluster.",
  "loadBalancers" : [ {
    "loadBalancerName" : "The name of a load balancer.",
    "containerName" : "The name of the container (as it appears in a container definition) to associate with the load balancer.",
    "targetGroupArn" : "The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group associated with a service.  \nIf your service's task definition uses the awsvpc network mode (which is required for the Fargate launch type), you must choose ip as the target type, not instance, because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance.",
    "containerPort" : "The port on the container to associate with the load balancer. This port must correspond to a containerPort in the service's task definition. Your container instances must allow ingress traffic on the hostPort of the port mapping."
  } ],
  "serviceRegistries" : [ {
    "registryArn" : "The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Amazon Route 53 Auto Naming. For more information, see Service.",
    "port" : "The port value used if your service discovery service specified an SRV record. This field may be used if both the awsvpc network mode and SRV records are used.",
    "containerName" : "The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition that your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both.",
    "containerPort" : "The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the bridge or host network mode, you must specify a containerName and containerPort combination from the task definition. If the task definition your service task specifies uses the awsvpc network mode and a type SRV DNS record is used, you must specify either a containerName and containerPort combination or a port value, but not both."
  } ],
  "serviceName" : "The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.",
  "deploymentConfiguration" : {
    "maximumPercent" : "The upper limit (as a percentage of the service's desiredCount) of the number of tasks that are allowed in the RUNNING or PENDING state in a service during a deployment. The maximum number of tasks during a deployment is the desiredCount multiplied by maximumPercent/100, rounded down to the nearest integer value.",
    "minimumHealthyPercent" : "The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain in the RUNNING state in a service during a deployment. The minimum number of healthy tasks during a deployment is the desiredCount multiplied by minimumHealthyPercent/100, rounded up to the nearest integer value."
  },
  "placementStrategy" : [ {
    "field" : "The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used.",
    "type" : "The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task)."
  } ],
  "schedulingStrategy" : "The scheduling strategy to use for the service. For more information, see Services. \nThere are two service scheduler strategies available:  \n  REPLICA-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions.  \n  DAEMON-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.  Fargate tasks do not support the DAEMON scheduling strategy.  ",
  "platformVersion" : "The platform version on which to run your service. If one is not specified, the latest version is used by default.",
  "taskDefinition" : "The family and revision (family:revision) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used.",
  "launchType" : "The launch type on which to run your service.",
  "healthCheckGracePeriodSeconds" : "The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 7,200 seconds during which the ECS service scheduler ignores health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up."
}
```

</details>

## delete_attributes

Deletes one or more custom attributes from an Amazon ECS resource.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.",
  "attributes" : [ {
    "targetId" : "The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).",
    "name" : "The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.",
    "targetType" : "The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.",
    "value" : "The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed."
  } ]
}
```

</details>

## delete_cluster

Deletes the specified cluster. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with ListContainerInstances and deregister them with DeregisterContainerInstance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster to delete."
}
```

</details>

## delete_service

Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you cannot delete it, and you must update the service to a desired task count of zero. For more information, see UpdateService.  
When you delete a service, if there are still running tasks that require cleanup, the service status moves from ACTIVE to DRAINING, and the service is no longer visible in the console or in ListServices API operations. After the tasks have stopped, then the service status moves from DRAINING to INACTIVE. Services in the DRAINING or INACTIVE status can still be viewed with DescribeServices API operations. However, in the future, INACTIVE services may be cleaned up and purged from Amazon ECS record keeping, and DescribeServices API operations on those services return a ServiceNotFoundException error.   
If you attempt to create a new service with the same name as an existing service in either ACTIVE or DRAINING status, you will receive an error.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.",
  "service" : "The name of the service to delete.",
  "force" : "If true, allows you to delete a service even if it has not been scaled down to zero tasks. It is only necessary to use this if the service is using the REPLICA scheduling strategy."
}
```

</details>

## deregister_container_instance

Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks. 
If you intend to use the container instance for some other purpose after deregistration, you should stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources. 
Deregistering a container instance removes the instance from a cluster, but it does not terminate the EC2 instance; if you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.  
If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents are not automatically deregistered when terminated).

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.",
  "containerInstance" : "The container instance ID or full ARN of the container instance to deregister. The ARN contains the arn:aws:ecs namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the container-instance namespace, and then the container instance ID. For example, arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID .",
  "force" : "Forces the deregistration of the container instance. If you have tasks running on the container instance when you deregister it with the force option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they are orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible.  \nAny containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group."
}
```

</details>

## deregister_task_definition

Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as INACTIVE. Existing tasks and services that reference an INACTIVE task definition continue to run without disruption. Existing services that reference an INACTIVE task definition can still scale up or down by modifying the service's desired count. 
You cannot use an INACTIVE task definition to run new tasks or create new services, and you cannot update an existing service to reference an INACTIVE task definition (although there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect).  
At this time, INACTIVE task definitions remain discoverable in your account indefinitely; however, this behavior is subject to change in the future, so you should not rely on INACTIVE task definitions persisting beyond the lifecycle of any associated tasks and services.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "taskDefinition" : "The family and revision (family:revision) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a revision."
}
```

</details>

## describe_clusters

Describes one or more of your clusters.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "include" : [ "string. Possible values: STATISTICS" ],
  "clusters" : [ "string" ]
}
```

</details>

## describe_container_instances

Describes Amazon Elastic Container Service container instances. Returns metadata about registered and remaining resources on each container instance requested.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed.",
  "containerInstances" : [ "string" ]
}
```

</details>

## describe_services

Describes the specified services running in your cluster.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.",
  "services" : [ "string" ]
}
```

</details>

## describe_task_definition

Describes a task definition. You can specify a family and revision to find information about a specific task definition, or you can simply specify the family to find the latest ACTIVE revision in that family.  
You can only describe INACTIVE task definitions while an active task or service references them.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "taskDefinition" : "The family for the latest ACTIVE revision, family and revision (family:revision) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe."
}
```

</details>

## describe_tasks

Describes a specified task or tasks.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.",
  "tasks" : [ "string" ]
}
```

</details>

## discover_poll_endpoint

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Returns an endpoint for the Amazon ECS agent to poll for updates.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.",
  "containerInstance" : "The container instance ID or full ARN of the container instance. The ARN contains the arn:aws:ecs namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the container-instance namespace, and then the container instance ID. For example, arn:aws:ecs:region:aws_account_id:container-instance/container_instance_ID ."
}
```

</details>

## list_attributes

Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, ListAttributes returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value, for example, to see which container instances in a cluster are running a Linux AMI (ecs.os-type=linux). 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.",
  "attributeValue" : "The value of the attribute with which to filter results. You must also specify an attribute name to use this parameter.",
  "nextToken" : "The nextToken value returned from a previous paginated ListAttributes request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.  \nThis token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.",
  "maxResults" : "The maximum number of cluster results returned by ListAttributes in paginated output. When this parameter is used, ListAttributes only returns maxResults results in a single page along with a nextToken response element. The remaining results of the initial request can be seen by sending another ListAttributes request with the returned nextToken value. This value can be between 1 and 100. If this parameter is not used, then ListAttributes returns up to 100 results and a nextToken value if applicable.",
  "targetType" : "The type of the target with which to list attributes.",
  "attributeName" : "The name of the attribute with which to filter the results. "
}
```

</details>

## list_clusters

Returns a list of existing clusters.

*This operation has no parameters*

## list_container_instances

Returns a list of container instances in a specified cluster. You can filter the results of a ListContainerInstances operation with cluster query language statements inside the filter parameter. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filter" : "You can filter the results of a ListContainerInstances operation with cluster query language statements. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.",
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.",
  "status" : "Filters the container instances by status. For example, if you specify the DRAINING status, the results include only container instances that have been set to DRAINING using UpdateContainerInstancesState. If you do not specify this parameter, the default is to include container instances set to ACTIVE and DRAINING."
}
```

</details>

## list_services

Lists the services that are running in a specified cluster.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.",
  "schedulingStrategy" : "The scheduling strategy for services to list.",
  "launchType" : "The launch type for the services to list."
}
```

</details>

## list_task_definition_families

Returns a list of task definition families that are registered to your account (which may include task definition families that no longer have any ACTIVE task definition revisions). 
You can filter out task definition families that do not contain any ACTIVE task definition revisions by setting the status parameter to ACTIVE. You can also filter the results with the familyPrefix parameter.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "familyPrefix" : "The familyPrefix is a string that is used to filter the results of ListTaskDefinitionFamilies. If you specify a familyPrefix, only task definition family names that begin with the familyPrefix string are returned.",
  "status" : "The task definition family status with which to filter the ListTaskDefinitionFamilies results. By default, both ACTIVE and INACTIVE task definition families are listed. If this parameter is set to ACTIVE, only task definition families that have an ACTIVE task definition revision are returned. If this parameter is set to INACTIVE, only task definition families that do not have any ACTIVE task definition revisions are returned. If you paginate the resulting output, be sure to keep the status value constant in each subsequent request."
}
```

</details>

## list_task_definitions

Returns a list of task definitions that are registered to your account. You can filter the results by family name with the familyPrefix parameter or by status with the status parameter.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "familyPrefix" : "The full family name with which to filter the ListTaskDefinitions results. Specifying a familyPrefix limits the listed task definitions to task definition revisions that belong to that family.",
  "sort" : "The order in which to sort the results. Valid values are ASC and DESC. By default (ASC), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to DESC reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.",
  "status" : "The task definition status with which to filter the ListTaskDefinitions results. By default, only ACTIVE task definitions are listed. By setting this parameter to INACTIVE, you can view task definitions that are INACTIVE as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the status value constant in each subsequent request."
}
```

</details>

## list_tasks

Returns a list of tasks for a specified cluster. You can filter the results by family name, by a particular container instance, or by the desired status of the task with the family, containerInstance, and desiredStatus parameters. 
Recently stopped tasks might appear in the returned results. Currently, stopped tasks appear in the returned results for at least one hour. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.",
  "containerInstance" : "The container instance ID or full ARN of the container instance with which to filter the ListTasks results. Specifying a containerInstance limits the results to tasks that belong to that container instance.",
  "startedBy" : "The startedBy value with which to filter the task results. Specifying a startedBy value limits the results to tasks that were started with that value.",
  "family" : "The name of the family with which to filter the ListTasks results. Specifying a family limits the results to tasks that belong to that family.",
  "serviceName" : "The name of the service with which to filter the ListTasks results. Specifying a serviceName limits the results to tasks that belong to that service.",
  "desiredStatus" : "The task desired status with which to filter the ListTasks results. Specifying a desiredStatus of STOPPED limits the results to tasks that Amazon ECS has set the desired status to STOPPED, which can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is RUNNING, which shows tasks that Amazon ECS has set the desired status to RUNNING.  \nAlthough you can filter results based on a desired status of PENDING, this does not return any results because Amazon ECS never sets the desired status of a task to that value (only a task's lastStatus may have a value of PENDING).",
  "launchType" : "The launch type for services to list."
}
```

</details>

## put_attributes

Create or update an attribute on an Amazon ECS resource. If the attribute does not exist, it is created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use DeleteAttributes. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.",
  "attributes" : [ {
    "targetId" : "The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).",
    "name" : "The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.",
    "targetType" : "The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.",
    "value" : "The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed."
  } ]
}
```

</details>

## register_container_instance

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster with which to register your container instance. If you do not specify a cluster, the default cluster is assumed.",
  "totalResources" : [ {
    "stringSetValue" : [ "string" ],
    "name" : "The name of the resource, such as CPU, MEMORY, PORTS, PORTS_UDP, or a user-defined resource.",
    "integerValue" : "When the integerValue type is set, the value of the resource must be an integer.",
    "doubleValue" : "When the doubleValue type is set, the value of the resource must be a double precision floating-point type.",
    "type" : "The type of the resource, such as INTEGER, DOUBLE, LONG, or STRINGSET.",
    "longValue" : "When the longValue type is set, the value of the resource must be an extended precision floating-point type."
  } ],
  "instanceIdentityDocumentSignature" : "The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: curl http://169.254.169.254/latest/dynamic/instance-identity/signature/ ",
  "instanceIdentityDocument" : "The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: curl http://169.254.169.254/latest/dynamic/instance-identity/document/ ",
  "attributes" : [ {
    "targetId" : "The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).",
    "name" : "The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.",
    "targetType" : "The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.",
    "value" : "The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed."
  } ],
  "versionInfo" : {
    "dockerVersion" : "The Docker version running on the container instance.",
    "agentHash" : "The Git commit hash for the Amazon ECS container agent build on the amazon-ecs-agent  GitHub repository.",
    "agentVersion" : "The version number of the Amazon ECS container agent."
  },
  "containerInstanceArn" : "The ARN of the container instance (if it was previously registered)."
}
```

</details>

## register_task_definition

Registers a new task definition from the supplied family and containerDefinitions. Optionally, you can add data volumes to your containers with the volumes parameter. For more information about task definition parameters and defaults, see Amazon ECS Task Definitions in the Amazon Elastic Container Service Developer Guide. 
You can specify an IAM role for your task with the taskRoleArn parameter. When you specify an IAM role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the IAM policy associated with the role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide. 
You can specify a Docker networking mode for the containers in your task definition with the networkMode parameter. The available network modes correspond to those described in Network settings in the Docker run reference. If you specify the awsvpc network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "networkMode" : "The Docker networking mode to use for the containers in the task. The valid values are none, bridge, awsvpc, and host. The default Docker network mode is bridge. If using the Fargate launch type, the awsvpc network mode is required. If using the EC2 launch type, any network mode can be used. If the network mode is set to none, you can't specify port mappings in your container definitions, and the task's containers do not have external connectivity. The host and awsvpc network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the bridge mode. \nWith the host and awsvpc network modes, exposed container ports are mapped directly to the corresponding host port (for the host network mode) or the attached elastic network interface port (for the awsvpc network mode), so you cannot take advantage of dynamic host port mappings.  \nIf the network mode is awsvpc, the task is allocated an Elastic Network Interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide. \nIf the network mode is host, you can't run multiple instantiations of the same task on a single container instance when port mappings are used. \nDocker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. \nFor more information, see Network settings in the Docker run reference.",
  "placementConstraints" : [ {
    "expression" : "A cluster query language expression to apply to the constraint. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.",
    "type" : "The type of constraint. The DistinctInstance constraint ensures that each task in a particular group is running on a different container instance. The MemberOf constraint restricts selection to be from a group of valid candidates."
  } ],
  "memory" : "The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB, for example 1024, or as a string using GB, for example 1GB or 1 GB, in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.  \nTask-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.  \nIf using the EC2 launch type, this field is optional. \nIf using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the cpu parameter:  \n 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU)  \n 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU)  \n 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU)  \n Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU)  \n Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) ",
  "executionRoleArn" : "The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.",
  "taskRoleArn" : "The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide.",
  "volumes" : [ {
    "dockerVolumeConfiguration" : {
      "driverOpts" : "A map of Docker driver specific options passed through. This parameter maps to DriverOpts in the Create a volume section of the Docker Remote API and the xxopt option to  docker volume create .",
      "autoprovision" : "If this value is true, the Docker volume is created if it does not already exist.  \nThis field is only used if the scope is shared.",
      "driver" : "The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use docker plugin ls to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see Docker plugin discovery. This parameter maps to Driver in the Create a volume section of the Docker Remote API and the xxdriver option to  docker volume create .",
      "scope" : "The scope for the Docker volume which determines it's lifecycle. Docker volumes that are scoped to a task are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as shared persist after the task stops.",
      "labels" : "Custom metadata to add to your Docker volume. This parameter maps to Labels in the Create a volume section of the Docker Remote API and the xxlabel option to  docker volume create ."
    },
    "name" : "The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints.",
    "host" : {
      "sourcePath" : "When the host parameter is used, specify a sourcePath to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported. \nIf you are using the Fargate launch type, the sourcePath parameter is not supported."
    }
  } ],
  "cpu" : "The number of CPU units used by the task. It can be expressed as an integer using CPU units, for example 1024, or as a string using vCPUs, for example 1 vCPU or 1 vcpu, in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.  \nTask-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.  \nIf using the EC2 launch type, this field is optional. Supported values are between 128 CPU units (0.125 vCPUs) and 10240 CPU units (10 vCPUs). \nIf using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the memory parameter:  \n 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)  \n 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)  \n 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)  \n 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)  \n 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) ",
  "family" : "You must specify a family for a task definition, which allows you to track multiple versions of the same task definition. The family is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.",
  "requiresCompatibilities" : [ "string. Possible values: EC2 | FARGATE" ],
  "containerDefinitions" : [ {
    "volumesFrom" : [ {
      "sourceContainer" : "The name of another container within the same task definition to mount volumes from.",
      "readOnly" : "If this value is true, the container has read-only access to the volume. If this value is false, then the container can write to the volume. The default value is false."
    } ],
    "memory" : "The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run. \nIf your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task memory value. \nFor containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of memory or memoryReservation in container definitions. If you specify both, memory must be greater than memoryReservation. If you specify memoryReservation, then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of memory is used. \nThe Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. ",
    "workingDirectory" : "The working directory in which to run commands inside the container. This parameter maps to WorkingDir in the Create a container section of the Docker Remote API and the --workdir option to docker run.",
    "interactive" : "When this parameter is true, this allows you to deploy containerized applications that require stdin or a tty to be allocated. This parameter maps to OpenStdin in the Create a container section of the Docker Remote API and the --interactive option to docker run.",
    "memoryReservation" : "The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit; however, your container can consume more memory when it needs to, up to either the hard limit specified with the memory parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to MemoryReservation in the Create a container section of the Docker Remote API and the --memory-reservation option to docker run. \nYou must specify a non-zero integer for one or both of memory or memoryReservation in container definitions. If you specify both, memory must be greater than memoryReservation. If you specify memoryReservation, then that value is subtracted from the available memory resources for the container instance on which the container is placed; otherwise, the value of memory is used. \nFor example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a memoryReservation of 128 MiB, and a memory hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed. \nThe Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. ",
    "portMappings" : [ {
      "protocol" : "The protocol used for the port mapping. Valid values are tcp and udp. The default is tcp.",
      "containerPort" : "The port number on the container that is bound to the user-specified or automatically assigned host port. \nIf using containers in a task with the awsvpc or host network mode, exposed ports should be specified using containerPort. \nIf using containers in a task with the bridge network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range (for more information, see hostPort). Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.",
      "hostPort" : "The port number on the container instance to reserve for your container. \nIf using containers in a task with the awsvpc or host network mode, the hostPort can either be left blank or set to the same value as the containerPort. \nIf using containers in a task with the bridge network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the hostPort (or set it to 0) while specifying a containerPort and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version. \nThe default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under /proc/sys/net/ipv4/ip_local_port_range; if this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. You should not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.  \nThe default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.  \nThe default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678 and 51679. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the remainingResources of DescribeContainerInstances output, and a container instance may have up to 100 reserved ports at a time, including the default reserved ports (automatically assigned ports do not count toward the 100 reserved ports limit)."
    } ],
    "hostname" : "The hostname to use for your container. This parameter maps to Hostname in the Create a container section of the Docker Remote API and the --hostname option to docker run.  \nThe hostname parameter is not supported if using the awsvpc networkMode.",
    "disableNetworking" : "When this parameter is true, networking is disabled within the container. This parameter maps to NetworkDisabled in the Create a container section of the Docker Remote API.  \nThis parameter is not supported for Windows containers.",
    "readonlyRootFilesystem" : "When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run.  \nThis parameter is not supported for Windows containers.",
    "pseudoTerminal" : "When this parameter is true, a TTY is allocated. This parameter maps to Tty in the Create a container section of the Docker Remote API and the --tty option to docker run.",
    "extraHosts" : [ {
      "hostname" : "The hostname to use in the /etc/hosts entry.",
      "ipAddress" : "The IP address to use in the /etc/hosts entry."
    } ],
    "dockerSecurityOptions" : [ "string" ],
    "links" : [ "string" ],
    "dnsServers" : [ "string" ],
    "linuxParameters" : {
      "tmpfs" : [ {
        "size" : "The size (in MiB) of the tmpfs volume.",
        "mountOptions" : [ "string" ],
        "containerPath" : "The absolute file path where the tmpfs volume is to be mounted."
      } ],
      "capabilities" : {
        "add" : [ "string" ],
        "drop" : [ "string" ]
      },
      "devices" : [ {
        "permissions" : [ "string. Possible values: read | write | mknod" ],
        "containerPath" : "The path inside the container at which to expose the host device.",
        "hostPath" : "The path for the device on the host container instance."
      } ],
      "initProcessEnabled" : "Run an init process inside the container that forwards signals and reaps processes. This parameter maps to the --init option to docker run. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version | grep \"Server API version\" ",
      "sharedMemorySize" : "The value for the size (in MiB) of the /dev/shm volume. This parameter maps to the --shm-size option to docker run.  \nIf you are using tasks that use the Fargate launch type, the sharedMemorySize parameter is not supported."
    },
    "dockerLabels" : "A key/value map of labels to add to the container. This parameter maps to Labels in the Create a container section of the Docker Remote API and the --label option to docker run. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version | grep \"Server API version\" ",
    "image" : "The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either  repository-url/image:tag  or  repository-url/image@digest . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run.  \n When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.  \n Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest. For example, 012345678910.dkr.ecr.&lt;region-name&gt;.amazonaws.com/&lt;repository-name&gt;:latest or 012345678910.dkr.ecr.&lt;region-name&gt;.amazonaws.com/&lt;repository-name&gt;@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE.   \n Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo).  \n Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent).  \n Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu). ",
    "cpu" : "The number of cpu units reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run. \nThis field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level cpu value.  \nYou can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the Amazon EC2 Instances detail page by 1,024.  \nFor example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units. \nLinux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units. \nOn Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see CPU share constraint in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2; however, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:  \n  Agent versions less than or equal to 1.1.0: Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to 2 CPU shares.  \n  Agent versions greater than or equal to 1.2.0: Null, zero, and CPU values of 1 are passed to Docker as 2.   \nOn Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.",
    "logConfiguration" : {
      "logDriver" : "The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default. If using the Fargate launch type, the only supported value is awslogs. For more information about using the awslogs driver, see Using the awslogs Log Driver in the Amazon Elastic Container Service Developer Guide.  \nIf you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is available on GitHub and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.  \nThis parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version | grep \"Server API version\" ",
      "options" : "The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version | grep \"Server API version\" "
    },
    "command" : [ "string" ],
    "systemControls" : [ {
      "namespace" : "The namespaced kernel parameter to set a value for.",
      "value" : "The value for the namespaced kernel parameter specifed in namespace."
    } ],
    "privileged" : "When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run.  \nThis parameter is not supported for Windows containers or tasks using the Fargate launch type.",
    "environment" : [ {
      "name" : "The name of the key value pair. For environment variables, this is the name of the environment variable.",
      "value" : "The value of the key value pair. For environment variables, this is the value of the environment variable."
    } ],
    "ulimits" : [ {
      "name" : "The type of the ulimit.",
      "hardLimit" : "The hard limit for the ulimit type.",
      "softLimit" : "The soft limit for the ulimit type."
    } ],
    "healthCheck" : {
      "retries" : "The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.",
      "startPeriod" : "The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The startPeriod is disabled by default.  \nIf a health check succeeds within the startPeriod, then the container is considered healthy and any subsequent failures count toward the maximum number of retries.",
      "interval" : "The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.",
      "command" : [ "string" ],
      "timeout" : "The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5."
    },
    "name" : "The name of a container. If you are linking multiple containers together in a task definition, the name of one container can be entered in the links of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to name in the Create a container section of the Docker Remote API and the --name option to docker run. ",
    "mountPoints" : [ {
      "readOnly" : "If this value is true, the container has read-only access to the volume. If this value is false, then the container can write to the volume. The default value is false.",
      "containerPath" : "The path on the container to mount the host volume at.",
      "sourceVolume" : "The name of the volume to mount. Must be a volume name referenced in the name parameter of task definition volume."
    } ],
    "entryPoint" : [ "string" ],
    "repositoryCredentials" : {
      "credentialsParameter" : "The Amazon Resource Name (ARN) or name of the secret containing the private repository credentials."
    },
    "user" : "The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run.  \nThis parameter is not supported for Windows containers.",
    "essential" : "If the essential parameter of a container is marked as true, and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the essential parameter of a container is marked as false, then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential. \nAll tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see Application Architecture in the Amazon Elastic Container Service Developer Guide.",
    "dnsSearchDomains" : [ "string" ]
  } ]
}
```

</details>

## run_task

Starts a new task using the specified task definition. 
You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide. 
Alternatively, you can use StartTask to use your own scheduler or place tasks manually on specific container instances. 
The Amazon ECS API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. You should keep this in mind when you carry out an API command that immediately follows a previous API command. 
To manage eventual consistency, you can do the following:  
 Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.  
 Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster on which to run your task. If you do not specify a cluster, the default cluster is assumed.",
  "placementConstraints" : [ {
    "expression" : "A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is distinctInstance. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.",
    "type" : "The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates. The value distinctInstance is not supported in task definitions."
  } ],
  "startedBy" : "An optional tag specified when a task is started. For example if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the startedBy parameter. You can then identify which tasks belong to that job by filtering the results of a ListTasks call with the startedBy value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. \nIf a task is started by an Amazon ECS service, then the startedBy parameter contains the deployment ID of the service that starts it.",
  "placementStrategy" : [ {
    "field" : "The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used.",
    "type" : "The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task)."
  } ],
  "networkConfiguration" : {
    "awsvpcConfiguration" : {
      "assignPublicIp" : "Whether the task's elastic network interface receives a public IP address. The default value is DISABLED.",
      "subnets" : [ "string" ],
      "securityGroups" : [ "string" ]
    }
  },
  "platformVersion" : "The platform version on which to run your task. If one is not specified, the latest version is used by default.",
  "count" : "The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks per call.",
  "taskDefinition" : "The family and revision (family:revision) or full ARN of the task definition to run. If a revision is not specified, the latest ACTIVE revision is used.",
  "overrides" : {
    "containerOverrides" : [ {
      "environment" : [ {
        "name" : "The name of the key value pair. For environment variables, this is the name of the environment variable.",
        "value" : "The value of the key value pair. For environment variables, this is the value of the environment variable."
      } ],
      "memory" : "The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.",
      "name" : "The name of the container that receives the override. This parameter is required if any override is specified.",
      "cpu" : "The number of cpu units reserved for the container, instead of the default value from the task definition. You must also specify a container name.",
      "command" : [ "string" ],
      "memoryReservation" : "The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name."
    } ],
    "executionRoleArn" : "The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.",
    "taskRoleArn" : "The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role."
  },
  "group" : "The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).",
  "launchType" : "The launch type on which to run your task."
}
```

</details>

## start_task

Starts a new task from the specified task definition on the specified container instance or instances. 
Alternatively, you can use RunTask to place tasks for you. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster on which to start your task. If you do not specify a cluster, the default cluster is assumed.",
  "startedBy" : "An optional tag specified when a task is started. For example if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the startedBy parameter. You can then identify which tasks belong to that job by filtering the results of a ListTasks call with the startedBy value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. \nIf a task is started by an Amazon ECS service, then the startedBy parameter contains the deployment ID of the service that starts it.",
  "networkConfiguration" : {
    "awsvpcConfiguration" : {
      "assignPublicIp" : "Whether the task's elastic network interface receives a public IP address. The default value is DISABLED.",
      "subnets" : [ "string" ],
      "securityGroups" : [ "string" ]
    }
  },
  "containerInstances" : [ "string" ],
  "taskDefinition" : "The family and revision (family:revision) or full ARN of the task definition to start. If a revision is not specified, the latest ACTIVE revision is used.",
  "overrides" : {
    "containerOverrides" : [ {
      "environment" : [ {
        "name" : "The name of the key value pair. For environment variables, this is the name of the environment variable.",
        "value" : "The value of the key value pair. For environment variables, this is the value of the environment variable."
      } ],
      "memory" : "The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.",
      "name" : "The name of the container that receives the override. This parameter is required if any override is specified.",
      "cpu" : "The number of cpu units reserved for the container, instead of the default value from the task definition. You must also specify a container name.",
      "command" : [ "string" ],
      "memoryReservation" : "The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name."
    } ],
    "executionRoleArn" : "The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.",
    "taskRoleArn" : "The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role."
  },
  "group" : "The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name)."
}
```

</details>

## stop_task

Stops a running task. 
When StopTask is called on a task, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM and a default 30-second timeout, after which SIGKILL is sent and the containers are forcibly stopped. If the container handles the SIGTERM gracefully and exits within 30 seconds from receiving it, no SIGKILL is sent.  
The default 30-second timeout can be configured on the Amazon ECS container agent with the ECS_CONTAINER_STOP_TIMEOUT variable. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.",
  "reason" : "An optional message specified when a task is stopped. For example, if you are using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent DescribeTasks API operations on this task. Up to 255 characters are allowed in this message.",
  "task" : "The task ID or full ARN entry of the task to stop."
}
```

</details>

## submit_container_state_change

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Sent to acknowledge that a container changed states.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full ARN of the cluster that hosts the container.",
  "reason" : "The reason for the state change request.",
  "task" : "The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.",
  "containerName" : "The name of the container.",
  "exitCode" : "The exit code returned for the state change request.",
  "networkBindings" : [ {
    "bindIP" : "The IP address that the container is bound to on the container instance.",
    "protocol" : "The protocol used for the network binding.",
    "containerPort" : "The port number on the container that is used with the network binding.",
    "hostPort" : "The port number on the host that is used with the network binding."
  } ],
  "status" : "The status of the state change request."
}
```

</details>

## submit_task_state_change

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Sent to acknowledge that a task changed states.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.",
  "reason" : "The reason for the state change request.",
  "executionStoppedAt" : "The Unix time stamp for when the task execution stopped.",
  "task" : "The task ID or full ARN of the task in the state change request.",
  "attachments" : [ {
    "attachmentArn" : "The Amazon Resource Name (ARN) of the attachment.",
    "status" : "The status of the attachment."
  } ],
  "pullStoppedAt" : "The Unix time stamp for when the container image pull completed.",
  "pullStartedAt" : "The Unix time stamp for when the container image pull began.",
  "containers" : [ {
    "reason" : "The reason for the state change.",
    "containerName" : "The name of the container.",
    "exitCode" : "The exit code for the container, if the state change is a result of the container exiting.",
    "networkBindings" : [ {
      "bindIP" : "The IP address that the container is bound to on the container instance.",
      "protocol" : "The protocol used for the network binding.",
      "containerPort" : "The port number on the container that is used with the network binding.",
      "hostPort" : "The port number on the host that is used with the network binding."
    } ],
    "status" : "The status of the container."
  } ],
  "status" : "The status of the state change request."
}
```

</details>

## update_container_agent

Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent does not interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system. 
 UpdateContainerAgent requires the Amazon ECS-optimized AMI or Amazon Linux with the ecs-init service installed and running. For help updating the Amazon ECS container agent on other operating systems, see Manually Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.",
  "containerInstance" : "The container instance ID or full ARN entries for the container instance on which you would like to update the Amazon ECS container agent."
}
```

</details>

## update_container_instances_state

Modifies the status of an Amazon ECS container instance. 
You can change the status of a container instance to DRAINING to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.  
When you set a container instance to DRAINING, Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the PENDING state are stopped immediately. 
Service tasks on the container instance that are in the RUNNING state are stopped and replaced according to the service's deployment configuration parameters, minimumHealthyPercent and maximumPercent. You can change the deployment configuration of your service using UpdateService.  
 If minimumHealthyPercent is below 100%, the scheduler can ignore desiredCount temporarily during task replacement. For example, desiredCount is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state. Tasks for services that use a load balancer are considered healthy if they are in the RUNNING state and the container instance they are hosted on is reported as healthy by the load balancer.  
 The maximumPercent parameter represents an upper limit on the number of running tasks during task replacement, which enables you to define the replacement batch size. For example, if desiredCount of four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained (provided that the cluster resources required to do this are available). If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped.   
Any PENDING or RUNNING tasks that do not belong to a service are not affected; you must wait for them to finish or stop them manually. 
A container instance has completed draining when it has no more RUNNING tasks. You can verify this using ListTasks. 
When you set a container instance to ACTIVE, the Amazon ECS scheduler can begin scheduling tasks on the instance again.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.",
  "containerInstances" : [ "string" ],
  "status" : "The container instance state with which to update the container instance."
}
```

</details>

## update_service

Modifies the desired count, deployment configuration, network configuration, or task definition used in a service. 
You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new desiredCount parameter. 
If you have updated the Docker image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.  
If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, my_image:latest), you do not need to create a new revision of your task definition. You can update the service using the forceNewDeployment option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.  
You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, minimumHealthyPercent and maximumPercent, to determine the deployment strategy.  
 If minimumHealthyPercent is below 100%, the scheduler can ignore desiredCount temporarily during a deployment. For example, if desiredCount is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the RUNNING state. Tasks for services that use a load balancer are considered healthy if they are in the RUNNING state and the container instance they are hosted on is reported as healthy by the load balancer.  
 The maximumPercent parameter represents an upper limit on the number of running tasks during a deployment, which enables you to define the deployment batch size. For example, if desiredCount is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).   
When UpdateService stops a task during a deployment, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM and a 30-second timeout, after which SIGKILL is sent and the containers are forcibly stopped. If the container handles the SIGTERM gracefully and exits within 30 seconds from receiving it, no SIGKILL is sent. 
When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic:  
 Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes).  
 By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy):   Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.   Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.     
When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic:   
 Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.  
 Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "cluster" : "The short name or full Amazon Resource Name (ARN) of the cluster that your service is running on. If you do not specify a cluster, the default cluster is assumed.",
  "deploymentConfiguration" : {
    "maximumPercent" : "The upper limit (as a percentage of the service's desiredCount) of the number of tasks that are allowed in the RUNNING or PENDING state in a service during a deployment. The maximum number of tasks during a deployment is the desiredCount multiplied by maximumPercent/100, rounded down to the nearest integer value.",
    "minimumHealthyPercent" : "The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain in the RUNNING state in a service during a deployment. The minimum number of healthy tasks during a deployment is the desiredCount multiplied by minimumHealthyPercent/100, rounded up to the nearest integer value."
  },
  "networkConfiguration" : {
    "awsvpcConfiguration" : {
      "assignPublicIp" : "Whether the task's elastic network interface receives a public IP address. The default value is DISABLED.",
      "subnets" : [ "string" ],
      "securityGroups" : [ "string" ]
    }
  },
  "service" : "The name of the service to update.",
  "desiredCount" : "The number of instantiations of the task to place and keep running in your service.",
  "platformVersion" : "The platform version that your service should run.",
  "taskDefinition" : "The family and revision (family:revision) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used. If you modify the task definition with UpdateService, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.",
  "forceNewDeployment" : "Whether to force a new deployment of the service. Deployments are not forced by default. You can use this option to trigger a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (my_image:latest) or to roll Fargate tasks onto a newer platform version.",
  "healthCheckGracePeriodSeconds" : "The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 1,800 seconds during which the ECS service scheduler ignores the Elastic Load Balancing health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up."
}
```

</details>

