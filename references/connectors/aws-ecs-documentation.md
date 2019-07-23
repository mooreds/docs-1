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

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

## delete_attributes

Deletes one or more custom attributes from an Amazon ECS resource.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_cluster

Deletes the specified cluster. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with ListContainerInstances and deregister them with DeregisterContainerInstance.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_service

Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you cannot delete it, and you must update the service to a desired task count of zero. For more information, see UpdateService.  
When you delete a service, if there are still running tasks that require cleanup, the service status moves from ACTIVE to DRAINING, and the service is no longer visible in the console or in ListServices API operations. After the tasks have stopped, then the service status moves from DRAINING to INACTIVE. Services in the DRAINING or INACTIVE status can still be viewed with DescribeServices API operations. However, in the future, INACTIVE services may be cleaned up and purged from Amazon ECS record keeping, and DescribeServices API operations on those services return a ServiceNotFoundException error.   
If you attempt to create a new service with the same name as an existing service in either ACTIVE or DRAINING status, you will receive an error.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## deregister_container_instance

Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks. 
If you intend to use the container instance for some other purpose after deregistration, you should stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources. 
Deregistering a container instance removes the instance from a cluster, but it does not terminate the EC2 instance; if you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.  
If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents are not automatically deregistered when terminated).

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## deregister_task_definition

Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as INACTIVE. Existing tasks and services that reference an INACTIVE task definition continue to run without disruption. Existing services that reference an INACTIVE task definition can still scale up or down by modifying the service's desired count. 
You cannot use an INACTIVE task definition to run new tasks or create new services, and you cannot update an existing service to reference an INACTIVE task definition (although there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect).  
At this time, INACTIVE task definitions remain discoverable in your account indefinitely; however, this behavior is subject to change in the future, so you should not rely on INACTIVE task definitions persisting beyond the lifecycle of any associated tasks and services.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_clusters

Describes one or more of your clusters.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_container_instances

Describes Amazon Elastic Container Service container instances. Returns metadata about registered and remaining resources on each container instance requested.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_services

Describes the specified services running in your cluster.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_task_definition

Describes a task definition. You can specify a family and revision to find information about a specific task definition, or you can simply specify the family to find the latest ACTIVE revision in that family.  
You can only describe INACTIVE task definitions while an active task or service references them.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_tasks

Describes a specified task or tasks.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## discover_poll_endpoint

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Returns an endpoint for the Amazon ECS agent to poll for updates.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_attributes

Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, ListAttributes returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value, for example, to see which container instances in a cluster are running a Linux AMI (ecs.os-type=linux). 

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_clusters

Returns a list of existing clusters.

*This operation has no parameters*

## list_container_instances

Returns a list of container instances in a specified cluster. You can filter the results of a ListContainerInstances operation with cluster query language statements inside the filter parameter. For more information, see Cluster Query Language in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_services

Lists the services that are running in a specified cluster.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_task_definition_families

Returns a list of task definition families that are registered to your account (which may include task definition families that no longer have any ACTIVE task definition revisions). 
You can filter out task definition families that do not contain any ACTIVE task definition revisions by setting the status parameter to ACTIVE. You can also filter the results with the familyPrefix parameter.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_task_definitions

Returns a list of task definitions that are registered to your account. You can filter the results by family name with the familyPrefix parameter or by status with the status parameter.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_tasks

Returns a list of tasks for a specified cluster. You can filter the results by family name, by a particular container instance, or by the desired status of the task with the family, containerInstance, and desiredStatus parameters. 
Recently stopped tasks might appear in the returned results. Currently, stopped tasks appear in the returned results for at least one hour. 

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## put_attributes

Create or update an attribute on an Amazon ECS resource. If the attribute does not exist, it is created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use DeleteAttributes. For more information, see Attributes in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## register_container_instance

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## register_task_definition

Registers a new task definition from the supplied family and containerDefinitions. Optionally, you can add data volumes to your containers with the volumes parameter. For more information about task definition parameters and defaults, see Amazon ECS Task Definitions in the Amazon Elastic Container Service Developer Guide. 
You can specify an IAM role for your task with the taskRoleArn parameter. When you specify an IAM role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the IAM policy associated with the role. For more information, see IAM Roles for Tasks in the Amazon Elastic Container Service Developer Guide. 
You can specify a Docker networking mode for the containers in your task definition with the networkMode parameter. The available network modes correspond to those described in Network settings in the Docker run reference. If you specify the awsvpc network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see Task Networking in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

## start_task

Starts a new task from the specified task definition on the specified container instance or instances. 
Alternatively, you can use RunTask to place tasks for you. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## stop_task

Stops a running task. 
When StopTask is called on a task, the equivalent of docker stop is issued to the containers running in the task. This results in a SIGTERM and a default 30-second timeout, after which SIGKILL is sent and the containers are forcibly stopped. If the container handles the SIGTERM gracefully and exits within 30 seconds from receiving it, no SIGKILL is sent.  
The default 30-second timeout can be configured on the Amazon ECS container agent with the ECS_CONTAINER_STOP_TIMEOUT variable. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## submit_container_state_change

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Sent to acknowledge that a container changed states.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## submit_task_state_change

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.  
Sent to acknowledge that a task changed states.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_container_agent

Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent does not interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system. 
 UpdateContainerAgent requires the Amazon ECS-optimized AMI or Amazon Linux with the ecs-init service installed and running. For help updating the Amazon ECS container agent on other operating systems, see Manually Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

