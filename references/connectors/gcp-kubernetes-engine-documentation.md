---
id: gcp-kubernetes-engine-documentation
title: GCP Kubernetes Engine (version v1.*.*)
sidebar_label: GCP Kubernetes Engine
layout: docs.mustache
---

## container.projects.locations.clusters.completeIpRotation

Completes master IP rotation.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to complete IP
rotation. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

CompleteIPRotationRequest moves the cluster master back into single-IP mode.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to complete IP\nrotation. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.create

Creates a cluster, consisting of the specified number and type of Google
Compute Engine instances.

By default, the cluster is created in the project's
[default network](/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation,
the cluster creates routes for each node to allow the containers
on that node to communicate with all other instances in the
cluster.

Finally, an entry is added to the project's global metadata indicating
which CIDR range is being used by the cluster.

<details><summary>Parameters</summary>

### parent (required)

The parent (project and location) where the cluster will be created.
Specified in the format 'projects/*/locations/*'.

**Type:** string

### $body

CreateClusterRequest creates a cluster.

**Type:** object

```json
{
  "cluster" : {
    "addonsConfig" : {
      "kubernetesDashboard" : {
        "disabled" : "Whether the Kubernetes Dashboard is enabled for this cluster."
      },
      "httpLoadBalancing" : {
        "disabled" : "Whether the HTTP Load Balancing controller is enabled in the cluster.\nWhen enabled, it runs a small pod in the cluster that manages the load\nbalancers."
      },
      "networkPolicyConfig" : {
        "disabled" : "Whether NetworkPolicy is enabled for this cluster."
      },
      "horizontalPodAutoscaling" : {
        "disabled" : "Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.\nWhen enabled, it ensures that a Heapster pod is running in the cluster,\nwhich is also used by the Cloud Monitoring service."
      }
    },
    "masterAuth" : {
      "clientCertificateConfig" : {
        "issueClientCertificate" : "Issue a client certificate."
      },
      "clientCertificate" : "[Output only] Base64-encoded public certificate used by clients to\nauthenticate to the cluster endpoint.",
      "password" : "The password to use for HTTP basic authentication to the master endpoint.\nBecause the master endpoint is open to the Internet, you should create a\nstrong password.  If a password is provided for cluster creation, username\nmust be non-empty.",
      "clientKey" : "[Output only] Base64-encoded private key used by clients to authenticate\nto the cluster endpoint.",
      "clusterCaCertificate" : "[Output only] Base64-encoded public certificate that is the root of\ntrust for the cluster.",
      "username" : "The username to use for HTTP basic authentication to the master endpoint.\nFor clusters v1.6.0 and later, basic authentication can be disabled by\nleaving username unspecified (or setting it to the empty string)."
    },
    "masterAuthorizedNetworksConfig" : {
      "cidrBlocks" : [ {
        "displayName" : "display_name is an optional field for users to identify CIDR blocks.",
        "cidrBlock" : "cidr_block must be specified in CIDR notation."
      } ],
      "enabled" : "Whether or not master authorized networks is enabled."
    },
    "description" : "An optional description of this cluster.",
    "labelFingerprint" : "The fingerprint of the set of labels for this cluster.",
    "currentMasterVersion" : "[Output only] The current software version of the master endpoint.",
    "ipAllocationPolicy" : {
      "clusterIpv4CidrBlock" : "The IP address range for the cluster pod IPs. If this field is set, then\n`cluster.cluster_ipv4_cidr` must be left blank.\n\nThis field is only applicable when `use_ip_aliases` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "createSubnetwork" : "Whether a new subnetwork will be created automatically for the cluster.\n\nThis field is only applicable when `use_ip_aliases` is true.",
      "useIpAliases" : "Whether alias IPs will be used for pod IPs in the cluster.",
      "clusterIpv4Cidr" : "This field is deprecated, use cluster_ipv4_cidr_block.",
      "servicesIpv4CidrBlock" : "The IP address range of the services IPs in this cluster. If blank, a range\nwill be automatically chosen with the default size.\n\nThis field is only applicable when `use_ip_aliases` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "servicesIpv4Cidr" : "This field is deprecated, use services_ipv4_cidr_block.",
      "clusterSecondaryRangeName" : "The name of the secondary range to be used for the cluster CIDR\nblock.  The secondary range will be used for pod IP\naddresses. This must be an existing secondary range associated\nwith the cluster subnetwork.\n\nThis field is only applicable with use_ip_aliases is true and\ncreate_subnetwork is false.",
      "servicesSecondaryRangeName" : "The name of the secondary range to be used as for the services\nCIDR block.  The secondary range will be used for service\nClusterIPs. This must be an existing secondary range associated\nwith the cluster subnetwork.\n\nThis field is only applicable with use_ip_aliases is true and\ncreate_subnetwork is false.",
      "nodeIpv4CidrBlock" : "The IP address range of the instance IPs in this cluster.\n\nThis is applicable only if `create_subnetwork` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "nodeIpv4Cidr" : "This field is deprecated, use node_ipv4_cidr_block.",
      "subnetworkName" : "A custom subnetwork name to be used if `create_subnetwork` is true.  If\nthis field is empty, then an automatic name will be chosen for the new\nsubnetwork."
    },
    "nodeConfig" : {
      "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
      "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
      "oauthScopes" : [ "string" ],
      "taints" : [ {
        "effect" : "Effect for taint.",
        "value" : "Value for taint.",
        "key" : "Key for taint."
      } ],
      "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
      "tags" : [ "string" ],
      "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
      "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
      "accelerators" : [ {
        "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
        "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
      } ],
      "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
      "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
      "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
      "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
      "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
    },
    "network" : "The name of the Google Compute Engine\n[network](/compute/docs/networks-and-firewalls#networks) to which the\ncluster is connected. If left unspecified, the `default` network\nwill be used.",
    "endpoint" : "[Output only] The IP address of this cluster's master endpoint.\nThe endpoint can be accessed from the internet at\n`https://username:password@endpoint/`.\n\nSee the `masterAuth` property of this resource for username and\npassword information.",
    "initialNodeCount" : "The number of nodes to create in this cluster. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.\nFor requests, this field should only be used in lieu of a\n\"node_pool\" object, since this configuration (along with the\n\"node_config\") will be used to create a \"NodePool\" object with an\nauto-generated name. Do not use this and a node_pool at the same time.",
    "zone" : "[Output only] The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field is deprecated, use location instead.",
    "enableKubernetesAlpha" : "Kubernetes alpha features are enabled on this cluster. This includes alpha\nAPI groups (e.g. v1alpha1) and features that may not be production ready in\nthe kubernetes version of the master and nodes.\nThe cluster has no SLA for uptime and master/node upgrades are disabled.\nAlpha enabled clusters are automatically deleted thirty days after\ncreation.",
    "nodePools" : [ {
      "initialNodeCount" : "The initial node count for the pool. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.",
      "instanceGroupUrls" : [ "string" ],
      "management" : {
        "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
        "upgradeOptions" : {
          "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
          "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
        },
        "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
      },
      "name" : "The name of the node pool.",
      "autoscaling" : {
        "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
        "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
        "enabled" : "Is autoscaling enabled for this node pool."
      },
      "conditions" : [ {
        "code" : "Machine-friendly representation of the condition",
        "message" : "Human-friendly representation of the condition"
      } ],
      "config" : {
        "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
        "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
        "oauthScopes" : [ "string" ],
        "taints" : [ {
          "effect" : "Effect for taint.",
          "value" : "Value for taint.",
          "key" : "Key for taint."
        } ],
        "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
        "tags" : [ "string" ],
        "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
        "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
        "accelerators" : [ {
          "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
          "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
        } ],
        "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
        "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
        "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
        "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
        "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
      },
      "version" : "The version of the Kubernetes of this node.",
      "statusMessage" : "[Output only] Additional information about the current status of this\nnode pool instance, if available.",
      "selfLink" : "[Output only] Server-defined URL for the resource.",
      "status" : "[Output only] The status of the nodes in this pool instance."
    } ],
    "initialClusterVersion" : "The initial Kubernetes version for this cluster.  Valid versions are those\nfound in validMasterVersions returned by getServerConfig.  The version can\nbe upgraded over time; such upgrades are reflected in\ncurrentMasterVersion and currentNodeVersion.\n\nUsers may specify either explicit versions offered by\nKubernetes Engine or version aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"\",\"-\": picks the default Kubernetes version",
    "privateClusterConfig" : {
      "enablePrivateEndpoint" : "Whether the master's internal IP address is used as the cluster endpoint.",
      "publicEndpoint" : "Output only. The external IP address of this cluster's master endpoint.",
      "enablePrivateNodes" : "Whether nodes have internal IP addresses only. If enabled, all nodes are\ngiven only RFC 1918 private addresses and communicate with the master via\nprivate networking.",
      "privateEndpoint" : "Output only. The internal IP address of this cluster's master endpoint.",
      "masterIpv4CidrBlock" : "The IP range in CIDR notation to use for the hosted master network. This\nrange will be used for assigning internal IP addresses to the master or\nset of masters, as well as the ILB VIP. This range must not overlap with\nany other ranges in use within the cluster's network."
    },
    "legacyAbac" : {
      "enabled" : "Whether the ABAC authorizer is enabled for this cluster. When enabled,\nidentities in the system, including service accounts, nodes, and\ncontrollers, will have statically granted permissions beyond those\nprovided by the RBAC configuration or IAM."
    },
    "clusterIpv4Cidr" : "The IP address range of the container pods in this cluster, in\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`). Leave blank to have\none automatically chosen or specify a `/14` block in `10.0.0.0/8`.",
    "monitoringService" : "The monitoring service the cluster should use to write metrics.\nCurrently available options:\n\n* `monitoring.googleapis.com` - the Google Cloud Monitoring service.\n* `none` - no metrics will be exported from the cluster.\n* if left as an empty string, `monitoring.googleapis.com` will be used.",
    "networkPolicy" : {
      "provider" : "The selected network policy provider.",
      "enabled" : "Whether network policy is enabled on the cluster."
    },
    "networkConfig" : {
      "subnetwork" : "Output only. The relative name of the Google Compute Engine\n[subnetwork](/compute/docs/vpc) to which the cluster is connected.\nExample: projects/my-project/regions/us-central1/subnetworks/my-subnet",
      "network" : "Output only. The relative name of the Google Compute Engine\nnetwork(/compute/docs/networks-and-firewalls#networks) to which\nthe cluster is connected.\nExample: projects/my-project/global/networks/my-network"
    },
    "currentNodeCount" : "[Output only]  The number of nodes currently in the cluster. Deprecated.\nCall Kubernetes API directly to retrieve node information.",
    "loggingService" : "The logging service the cluster should use to write logs.\nCurrently available options:\n\n* `logging.googleapis.com` - the Google Cloud Logging service.\n* `none` - no logs will be exported from the cluster.\n* if left as an empty string,`logging.googleapis.com` will be used.",
    "statusMessage" : "[Output only] Additional information about the current status of this\ncluster, if available.",
    "selfLink" : "[Output only] Server-defined URL for the resource.",
    "maintenancePolicy" : {
      "window" : {
        "dailyMaintenanceWindow" : {
          "duration" : "[Output only] Duration of the time window, automatically chosen to be\nsmallest possible in the given scenario.\nDuration will be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"PTnHnMnS\".",
          "startTime" : "Time within the maintenance window to start the maintenance operations.\nTime format should be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"HH:MM”, where HH : [00-23] and MM : [00-59] GMT."
        }
      }
    },
    "instanceGroupUrls" : [ "string" ],
    "expireTime" : "[Output only] The time the cluster will be automatically\ndeleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
    "currentNodeVersion" : "[Output only] Deprecated, use\n[NodePool.version](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePool)\ninstead. The current version of the node software components. If they are\ncurrently at multiple versions because they're in the process of being\nupgraded, this reflects the minimum version of all nodes.",
    "createTime" : "[Output only] The time the cluster was created, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
    "nodeIpv4CidrSize" : "[Output only] The size of the address space on each node for hosting\ncontainers. This is provisioned from within the `container_ipv4_cidr`\nrange.",
    "subnetwork" : "The name of the Google Compute Engine\n[subnetwork](/compute/docs/subnetworks) to which the\ncluster is connected.",
    "name" : "The name of this cluster. The name must be unique within this project\nand zone, and can be up to 40 characters with the following restrictions:\n\n* Lowercase letters, numbers, and hyphens only.\n* Must start with a letter.\n* Must end with a number or a letter.",
    "resourceLabels" : "The resource labels for the cluster to use to annotate any related\nGoogle Compute Engine resources.",
    "servicesIpv4Cidr" : "[Output only] The IP address range of the Kubernetes services in\nthis cluster, in\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `1.2.3.4/29`). Service addresses are\ntypically put in the last `/16` from the container CIDR.",
    "location" : "[Output only] The name of the Google Compute Engine\n[zone](/compute/docs/regions-zones/regions-zones#available) or\n[region](/compute/docs/regions-zones/regions-zones#available) in which\nthe cluster resides.",
    "locations" : [ "string" ],
    "conditions" : [ {
      "code" : "Machine-friendly representation of the condition",
      "message" : "Human-friendly representation of the condition"
    } ],
    "status" : "[Output only] The current status of this cluster."
  },
  "parent" : "The parent (project and location) where the cluster will be created.\nSpecified in the format 'projects/*/locations/*'.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the parent field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the parent field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.getJwks

GetJSONWebKeys gets the public component of the cluster signing keys in
JSON Web Key format.
This API is not yet intended for general use, and is not available for all
clusters.

<details><summary>Parameters</summary>

### parent (required)

The cluster (project, location, cluster id) to get keys for. Specified in
the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.list

Lists all clusters owned by a project in either the specified zone or all
zones.

<details><summary>Parameters</summary>

### parent (required)

The parent (project and location) where the clusters will be listed.
Specified in the format 'projects/*/locations/*'.
Location "-" matches all zones and all regions.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the parent field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides, or "-" for all zones.
This field has been deprecated and replaced by the parent field.

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.create

Creates a node pool for a cluster.

<details><summary>Parameters</summary>

### parent (required)

The parent (project, location, cluster id) where the node pool will be
created. Specified in the format
'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

CreateNodePoolRequest creates a node pool for a cluster.

**Type:** object

```json
{
  "nodePool" : {
    "initialNodeCount" : "The initial node count for the pool. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.",
    "instanceGroupUrls" : [ "string" ],
    "management" : {
      "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
      "upgradeOptions" : {
        "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
        "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
      },
      "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
    },
    "name" : "The name of the node pool.",
    "autoscaling" : {
      "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
      "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
      "enabled" : "Is autoscaling enabled for this node pool."
    },
    "conditions" : [ {
      "code" : "Machine-friendly representation of the condition",
      "message" : "Human-friendly representation of the condition"
    } ],
    "config" : {
      "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
      "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
      "oauthScopes" : [ "string" ],
      "taints" : [ {
        "effect" : "Effect for taint.",
        "value" : "Value for taint.",
        "key" : "Key for taint."
      } ],
      "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
      "tags" : [ "string" ],
      "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
      "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
      "accelerators" : [ {
        "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
        "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
      } ],
      "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
      "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
      "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
      "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
      "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
    },
    "version" : "The version of the Kubernetes of this node.",
    "statusMessage" : "[Output only] Additional information about the current status of this\nnode pool instance, if available.",
    "selfLink" : "[Output only] Server-defined URL for the resource.",
    "status" : "[Output only] The status of the nodes in this pool instance."
  },
  "parent" : "The parent (project, location, cluster id) where the node pool will be\ncreated. Specified in the format\n'projects/*/locations/*/clusters/*'.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the parent field.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the parent field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the parent field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.delete

Deletes a node pool from a cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool id) of the node pool to
delete. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### clusterId

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### nodePoolId

Deprecated. The name of the node pool to delete.
This field has been deprecated and replaced by the name field.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.get

Retrieves the node pool requested.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool id) of the node pool to
get. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### clusterId

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### nodePoolId

Deprecated. The name of the node pool.
This field has been deprecated and replaced by the name field.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.list

Lists the node pools for a cluster.

<details><summary>Parameters</summary>

### parent (required)

The parent (project, location, cluster id) where the node pools will be
listed. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### clusterId

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the parent field.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the parent field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the parent field.

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.rollback

Roll back the previously Aborted or Failed NodePool upgrade.
This will be an no-op if the last upgrade successfully completed.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool id) of the node poll to
rollback upgrade.
Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### $body

RollbackNodePoolUpgradeRequest rollbacks the previously Aborted or Failed
NodePool upgrade. This will be an no-op if the last upgrade successfully
completed.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to rollback.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node poll to\nrollback upgrade.\nSpecified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.",
  "clusterId" : "Deprecated. The name of the cluster to rollback.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.setAutoscaling

Sets the autoscaling settings for a specific node pool.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool) of the node pool to set
autoscaler settings. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### $body

SetNodePoolAutoscalingRequest sets the autoscaler settings of a node pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool) of the node pool to set\nautoscaler settings. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "autoscaling" : {
    "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
    "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
    "enabled" : "Is autoscaling enabled for this node pool."
  },
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.setManagement

Sets the NodeManagement options for a node pool.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool id) of the node pool to set
management properties. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### $body

SetNodePoolManagementRequest sets the node management properties of a node
pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to update.\nThis field has been deprecated and replaced by the name field.",
  "management" : {
    "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
    "upgradeOptions" : {
      "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
      "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
    },
    "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
  },
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node pool to set\nmanagement properties. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.setSize

Sets the size for a specific node pool.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool id) of the node pool to set
size.
Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### $body

SetNodePoolSizeRequest sets the size a node
pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to update.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node pool to set\nsize.\nSpecified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.",
  "nodeCount" : "The desired node count for the pool.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.nodePools.update

Updates the version and/or image type for a specific node pool.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster, node pool) of the node pool to
update. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### $body

UpdateNodePoolRequests update a node pool's image and/or version.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool) of the node pool to\nupdate. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "nodeVersion" : "The Kubernetes version to change the nodes to (typically an\nupgrade).\n\nUsers may specify either explicit versions offered by Kubernetes Engine or\nversion aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the Kubernetes master version",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "imageType" : "The desired image type for the node pool.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setAddons

Sets the addons for a specific cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to set addons.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetAddonsConfigRequest sets the addons associated with the cluster.

**Type:** object

```json
{
  "addonsConfig" : {
    "kubernetesDashboard" : {
      "disabled" : "Whether the Kubernetes Dashboard is enabled for this cluster."
    },
    "httpLoadBalancing" : {
      "disabled" : "Whether the HTTP Load Balancing controller is enabled in the cluster.\nWhen enabled, it runs a small pod in the cluster that manages the load\nbalancers."
    },
    "networkPolicyConfig" : {
      "disabled" : "Whether NetworkPolicy is enabled for this cluster."
    },
    "horizontalPodAutoscaling" : {
      "disabled" : "Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.\nWhen enabled, it ensures that a Heapster pod is running in the cluster,\nwhich is also used by the Cloud Monitoring service."
    }
  },
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set addons.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setLegacyAbac

Enables or disables the ABAC authorization mechanism on a cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to set legacy abac.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetLegacyAbacRequest enables or disables the ABAC authorization mechanism for
a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to set legacy abac.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field.",
  "enabled" : "Whether ABAC authorization will be enabled in the cluster."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setLocations

Sets the locations for a specific cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to set locations.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetLocationsRequest sets the locations of the cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set locations.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "locations" : [ "string" ],
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setLogging

Sets the logging service for a specific cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to set logging.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetLoggingServiceRequest sets the logging service of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set logging.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "loggingService" : "The logging service the cluster should use to write metrics.\nCurrently available options:\n\n* \"logging.googleapis.com\" - the Google Cloud Logging service\n* \"none\" - no metrics will be exported from the cluster",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setMaintenancePolicy

Sets the maintenance policy for a cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to set maintenance
policy.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetMaintenancePolicyRequest sets the maintenance policy for a cluster.

**Type:** object

```json
{
  "maintenancePolicy" : {
    "window" : {
      "dailyMaintenanceWindow" : {
        "duration" : "[Output only] Duration of the time window, automatically chosen to be\nsmallest possible in the given scenario.\nDuration will be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"PTnHnMnS\".",
        "startTime" : "Time within the maintenance window to start the maintenance operations.\nTime format should be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"HH:MM”, where HH : [00-23] and MM : [00-59] GMT."
      }
    }
  },
  "zone" : "The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.",
  "name" : "The name (project, location, cluster id) of the cluster to set maintenance\npolicy.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "The name of the cluster to update.",
  "projectId" : "The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840)."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setMasterAuth

Used to set master auth materials. Currently supports :-
Changing the admin password for a specific cluster.
This can be either via password generation or explicitly set the password.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to set auth.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetMasterAuthRequest updates the admin password of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set auth.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "action" : "The exact form of action to be taken on the master auth.",
  "update" : {
    "clientCertificateConfig" : {
      "issueClientCertificate" : "Issue a client certificate."
    },
    "clientCertificate" : "[Output only] Base64-encoded public certificate used by clients to\nauthenticate to the cluster endpoint.",
    "password" : "The password to use for HTTP basic authentication to the master endpoint.\nBecause the master endpoint is open to the Internet, you should create a\nstrong password.  If a password is provided for cluster creation, username\nmust be non-empty.",
    "clientKey" : "[Output only] Base64-encoded private key used by clients to authenticate\nto the cluster endpoint.",
    "clusterCaCertificate" : "[Output only] Base64-encoded public certificate that is the root of\ntrust for the cluster.",
    "username" : "The username to use for HTTP basic authentication to the master endpoint.\nFor clusters v1.6.0 and later, basic authentication can be disabled by\nleaving username unspecified (or setting it to the empty string)."
  },
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setMonitoring

Sets the monitoring service for a specific cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to set monitoring.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetMonitoringServiceRequest sets the monitoring service of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "monitoringService" : "The monitoring service the cluster should use to write metrics.\nCurrently available options:\n\n* \"monitoring.googleapis.com\" - the Google Cloud Monitoring service\n* \"none\" - no metrics will be exported from the cluster",
  "name" : "The name (project, location, cluster) of the cluster to set monitoring.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setNetworkPolicy

Enables/Disables Network Policy for a cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to set networking
policy. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetNetworkPolicyRequest enables/disables network policy for a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "networkPolicy" : {
    "provider" : "The selected network policy provider.",
    "enabled" : "Whether network policy is enabled on the cluster."
  },
  "name" : "The name (project, location, cluster id) of the cluster to set networking\npolicy. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.setResourceLabels

Sets labels on a cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to set labels.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

SetLabelsRequest sets the Google Cloud Platform labels on a Google Container
Engine cluster, which will in turn set them for Google Compute Engine
resources used by that cluster

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to set labels.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "resourceLabels" : "The labels to set for that cluster.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "labelFingerprint" : "The fingerprint of the previous set of labels for this resource,\nused to detect conflicts. The fingerprint is initially generated by\nKubernetes Engine and changes after every request to modify or update\nlabels. You must always provide an up-to-date fingerprint hash when\nupdating or changing labels. Make a get() request to the\nresource to get the latest fingerprint.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.startIpRotation

Start master IP rotation.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster id) of the cluster to start IP
rotation. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

StartIPRotationRequest creates a new IP for the cluster and then performs
a node upgrade on each node pool to point to the new IP.

**Type:** object

```json
{
  "rotateCredentials" : "Whether to rotate credentials during IP rotation.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to start IP\nrotation. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.updateMaster

Updates the master for a specific cluster.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, cluster) of the cluster to update.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### $body

UpdateMasterRequest updates the master of the cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "masterVersion" : "The Kubernetes version to change the master to.\n\nUsers may specify either explicit versions offered by Kubernetes Engine or\nversion aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the default Kubernetes version",
  "name" : "The name (project, location, cluster) of the cluster to update.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.clusters.well-known.getOpenid-configuration

GetOpenIDConfig gets the OIDC discovery document for the cluster.
See the OpenID Connect Discovery 1.0 specification for details.
https://openid.net/specs/openid-connect-discovery-1_0.html
This API is not yet intended for general use, and is not available for all
clusters.

<details><summary>Parameters</summary>

### parent (required)

The cluster (project, location, cluster id) to get the discovery document
for. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.getServerConfig

Returns configuration info about the Kubernetes Engine service.

<details><summary>Parameters</summary>

### name (required)

The name (project and location) of the server config to get,
specified in the format 'projects/*/locations/*'.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) to return operations for.
This field has been deprecated and replaced by the name field.

**Type:** string

</details>

## container.projects.locations.operations.cancel

Cancels the specified operation.

<details><summary>Parameters</summary>

### name (required)

The name (project, location, operation id) of the operation to cancel.
Specified in the format 'projects/*/locations/*/operations/*'.

**Type:** string

### $body

CancelOperationRequest cancels a single operation.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the operation resides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, operation id) of the operation to cancel.\nSpecified in the format 'projects/*/locations/*/operations/*'.",
  "operationId" : "Deprecated. The server-assigned `name` of the operation.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.locations.operations.list

Lists all operations in a project in a specific zone or all zones.

<details><summary>Parameters</summary>

### parent (required)

The parent (project and location) where the operations will be listed.
Specified in the format 'projects/*/locations/*'.
Location "-" matches all zones and all regions.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projectId

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the parent field.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### zone

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) to return operations for, or `-` for
all zones. This field has been deprecated and replaced by the parent field.

**Type:** string

</details>

## container.projects.zones.clusters.addons

Sets the addons for a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetAddonsConfigRequest sets the addons associated with the cluster.

**Type:** object

```json
{
  "addonsConfig" : {
    "kubernetesDashboard" : {
      "disabled" : "Whether the Kubernetes Dashboard is enabled for this cluster."
    },
    "httpLoadBalancing" : {
      "disabled" : "Whether the HTTP Load Balancing controller is enabled in the cluster.\nWhen enabled, it runs a small pod in the cluster that manages the load\nbalancers."
    },
    "networkPolicyConfig" : {
      "disabled" : "Whether NetworkPolicy is enabled for this cluster."
    },
    "horizontalPodAutoscaling" : {
      "disabled" : "Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.\nWhen enabled, it ensures that a Heapster pod is running in the cluster,\nwhich is also used by the Cloud Monitoring service."
    }
  },
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set addons.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.completeIpRotation

Completes master IP rotation.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

CompleteIPRotationRequest moves the cluster master back into single-IP mode.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to complete IP\nrotation. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.create

Creates a cluster, consisting of the specified number and type of Google
Compute Engine instances.

By default, the cluster is created in the project's
[default network](/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation,
the cluster creates routes for each node to allow the containers
on that node to communicate with all other instances in the
cluster.

Finally, an entry is added to the project's global metadata indicating
which CIDR range is being used by the cluster.

<details><summary>Parameters</summary>

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the parent field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the parent field.

**Type:** string

### $body

CreateClusterRequest creates a cluster.

**Type:** object

```json
{
  "cluster" : {
    "addonsConfig" : {
      "kubernetesDashboard" : {
        "disabled" : "Whether the Kubernetes Dashboard is enabled for this cluster."
      },
      "httpLoadBalancing" : {
        "disabled" : "Whether the HTTP Load Balancing controller is enabled in the cluster.\nWhen enabled, it runs a small pod in the cluster that manages the load\nbalancers."
      },
      "networkPolicyConfig" : {
        "disabled" : "Whether NetworkPolicy is enabled for this cluster."
      },
      "horizontalPodAutoscaling" : {
        "disabled" : "Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.\nWhen enabled, it ensures that a Heapster pod is running in the cluster,\nwhich is also used by the Cloud Monitoring service."
      }
    },
    "masterAuth" : {
      "clientCertificateConfig" : {
        "issueClientCertificate" : "Issue a client certificate."
      },
      "clientCertificate" : "[Output only] Base64-encoded public certificate used by clients to\nauthenticate to the cluster endpoint.",
      "password" : "The password to use for HTTP basic authentication to the master endpoint.\nBecause the master endpoint is open to the Internet, you should create a\nstrong password.  If a password is provided for cluster creation, username\nmust be non-empty.",
      "clientKey" : "[Output only] Base64-encoded private key used by clients to authenticate\nto the cluster endpoint.",
      "clusterCaCertificate" : "[Output only] Base64-encoded public certificate that is the root of\ntrust for the cluster.",
      "username" : "The username to use for HTTP basic authentication to the master endpoint.\nFor clusters v1.6.0 and later, basic authentication can be disabled by\nleaving username unspecified (or setting it to the empty string)."
    },
    "masterAuthorizedNetworksConfig" : {
      "cidrBlocks" : [ {
        "displayName" : "display_name is an optional field for users to identify CIDR blocks.",
        "cidrBlock" : "cidr_block must be specified in CIDR notation."
      } ],
      "enabled" : "Whether or not master authorized networks is enabled."
    },
    "description" : "An optional description of this cluster.",
    "labelFingerprint" : "The fingerprint of the set of labels for this cluster.",
    "currentMasterVersion" : "[Output only] The current software version of the master endpoint.",
    "ipAllocationPolicy" : {
      "clusterIpv4CidrBlock" : "The IP address range for the cluster pod IPs. If this field is set, then\n`cluster.cluster_ipv4_cidr` must be left blank.\n\nThis field is only applicable when `use_ip_aliases` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "createSubnetwork" : "Whether a new subnetwork will be created automatically for the cluster.\n\nThis field is only applicable when `use_ip_aliases` is true.",
      "useIpAliases" : "Whether alias IPs will be used for pod IPs in the cluster.",
      "clusterIpv4Cidr" : "This field is deprecated, use cluster_ipv4_cidr_block.",
      "servicesIpv4CidrBlock" : "The IP address range of the services IPs in this cluster. If blank, a range\nwill be automatically chosen with the default size.\n\nThis field is only applicable when `use_ip_aliases` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "servicesIpv4Cidr" : "This field is deprecated, use services_ipv4_cidr_block.",
      "clusterSecondaryRangeName" : "The name of the secondary range to be used for the cluster CIDR\nblock.  The secondary range will be used for pod IP\naddresses. This must be an existing secondary range associated\nwith the cluster subnetwork.\n\nThis field is only applicable with use_ip_aliases is true and\ncreate_subnetwork is false.",
      "servicesSecondaryRangeName" : "The name of the secondary range to be used as for the services\nCIDR block.  The secondary range will be used for service\nClusterIPs. This must be an existing secondary range associated\nwith the cluster subnetwork.\n\nThis field is only applicable with use_ip_aliases is true and\ncreate_subnetwork is false.",
      "nodeIpv4CidrBlock" : "The IP address range of the instance IPs in this cluster.\n\nThis is applicable only if `create_subnetwork` is true.\n\nSet to blank to have a range chosen with the default size.\n\nSet to /netmask (e.g. `/14`) to have a range chosen with a specific\nnetmask.\n\nSet to a\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g.\n`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range\nto use.",
      "nodeIpv4Cidr" : "This field is deprecated, use node_ipv4_cidr_block.",
      "subnetworkName" : "A custom subnetwork name to be used if `create_subnetwork` is true.  If\nthis field is empty, then an automatic name will be chosen for the new\nsubnetwork."
    },
    "nodeConfig" : {
      "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
      "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
      "oauthScopes" : [ "string" ],
      "taints" : [ {
        "effect" : "Effect for taint.",
        "value" : "Value for taint.",
        "key" : "Key for taint."
      } ],
      "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
      "tags" : [ "string" ],
      "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
      "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
      "accelerators" : [ {
        "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
        "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
      } ],
      "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
      "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
      "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
      "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
      "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
    },
    "network" : "The name of the Google Compute Engine\n[network](/compute/docs/networks-and-firewalls#networks) to which the\ncluster is connected. If left unspecified, the `default` network\nwill be used.",
    "endpoint" : "[Output only] The IP address of this cluster's master endpoint.\nThe endpoint can be accessed from the internet at\n`https://username:password@endpoint/`.\n\nSee the `masterAuth` property of this resource for username and\npassword information.",
    "initialNodeCount" : "The number of nodes to create in this cluster. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.\nFor requests, this field should only be used in lieu of a\n\"node_pool\" object, since this configuration (along with the\n\"node_config\") will be used to create a \"NodePool\" object with an\nauto-generated name. Do not use this and a node_pool at the same time.",
    "zone" : "[Output only] The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field is deprecated, use location instead.",
    "enableKubernetesAlpha" : "Kubernetes alpha features are enabled on this cluster. This includes alpha\nAPI groups (e.g. v1alpha1) and features that may not be production ready in\nthe kubernetes version of the master and nodes.\nThe cluster has no SLA for uptime and master/node upgrades are disabled.\nAlpha enabled clusters are automatically deleted thirty days after\ncreation.",
    "nodePools" : [ {
      "initialNodeCount" : "The initial node count for the pool. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.",
      "instanceGroupUrls" : [ "string" ],
      "management" : {
        "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
        "upgradeOptions" : {
          "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
          "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
        },
        "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
      },
      "name" : "The name of the node pool.",
      "autoscaling" : {
        "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
        "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
        "enabled" : "Is autoscaling enabled for this node pool."
      },
      "conditions" : [ {
        "code" : "Machine-friendly representation of the condition",
        "message" : "Human-friendly representation of the condition"
      } ],
      "config" : {
        "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
        "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
        "oauthScopes" : [ "string" ],
        "taints" : [ {
          "effect" : "Effect for taint.",
          "value" : "Value for taint.",
          "key" : "Key for taint."
        } ],
        "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
        "tags" : [ "string" ],
        "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
        "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
        "accelerators" : [ {
          "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
          "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
        } ],
        "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
        "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
        "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
        "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
        "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
      },
      "version" : "The version of the Kubernetes of this node.",
      "statusMessage" : "[Output only] Additional information about the current status of this\nnode pool instance, if available.",
      "selfLink" : "[Output only] Server-defined URL for the resource.",
      "status" : "[Output only] The status of the nodes in this pool instance."
    } ],
    "initialClusterVersion" : "The initial Kubernetes version for this cluster.  Valid versions are those\nfound in validMasterVersions returned by getServerConfig.  The version can\nbe upgraded over time; such upgrades are reflected in\ncurrentMasterVersion and currentNodeVersion.\n\nUsers may specify either explicit versions offered by\nKubernetes Engine or version aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"\",\"-\": picks the default Kubernetes version",
    "privateClusterConfig" : {
      "enablePrivateEndpoint" : "Whether the master's internal IP address is used as the cluster endpoint.",
      "publicEndpoint" : "Output only. The external IP address of this cluster's master endpoint.",
      "enablePrivateNodes" : "Whether nodes have internal IP addresses only. If enabled, all nodes are\ngiven only RFC 1918 private addresses and communicate with the master via\nprivate networking.",
      "privateEndpoint" : "Output only. The internal IP address of this cluster's master endpoint.",
      "masterIpv4CidrBlock" : "The IP range in CIDR notation to use for the hosted master network. This\nrange will be used for assigning internal IP addresses to the master or\nset of masters, as well as the ILB VIP. This range must not overlap with\nany other ranges in use within the cluster's network."
    },
    "legacyAbac" : {
      "enabled" : "Whether the ABAC authorizer is enabled for this cluster. When enabled,\nidentities in the system, including service accounts, nodes, and\ncontrollers, will have statically granted permissions beyond those\nprovided by the RBAC configuration or IAM."
    },
    "clusterIpv4Cidr" : "The IP address range of the container pods in this cluster, in\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `10.96.0.0/14`). Leave blank to have\none automatically chosen or specify a `/14` block in `10.0.0.0/8`.",
    "monitoringService" : "The monitoring service the cluster should use to write metrics.\nCurrently available options:\n\n* `monitoring.googleapis.com` - the Google Cloud Monitoring service.\n* `none` - no metrics will be exported from the cluster.\n* if left as an empty string, `monitoring.googleapis.com` will be used.",
    "networkPolicy" : {
      "provider" : "The selected network policy provider.",
      "enabled" : "Whether network policy is enabled on the cluster."
    },
    "networkConfig" : {
      "subnetwork" : "Output only. The relative name of the Google Compute Engine\n[subnetwork](/compute/docs/vpc) to which the cluster is connected.\nExample: projects/my-project/regions/us-central1/subnetworks/my-subnet",
      "network" : "Output only. The relative name of the Google Compute Engine\nnetwork(/compute/docs/networks-and-firewalls#networks) to which\nthe cluster is connected.\nExample: projects/my-project/global/networks/my-network"
    },
    "currentNodeCount" : "[Output only]  The number of nodes currently in the cluster. Deprecated.\nCall Kubernetes API directly to retrieve node information.",
    "loggingService" : "The logging service the cluster should use to write logs.\nCurrently available options:\n\n* `logging.googleapis.com` - the Google Cloud Logging service.\n* `none` - no logs will be exported from the cluster.\n* if left as an empty string,`logging.googleapis.com` will be used.",
    "statusMessage" : "[Output only] Additional information about the current status of this\ncluster, if available.",
    "selfLink" : "[Output only] Server-defined URL for the resource.",
    "maintenancePolicy" : {
      "window" : {
        "dailyMaintenanceWindow" : {
          "duration" : "[Output only] Duration of the time window, automatically chosen to be\nsmallest possible in the given scenario.\nDuration will be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"PTnHnMnS\".",
          "startTime" : "Time within the maintenance window to start the maintenance operations.\nTime format should be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"HH:MM”, where HH : [00-23] and MM : [00-59] GMT."
        }
      }
    },
    "instanceGroupUrls" : [ "string" ],
    "expireTime" : "[Output only] The time the cluster will be automatically\ndeleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
    "currentNodeVersion" : "[Output only] Deprecated, use\n[NodePool.version](/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePool)\ninstead. The current version of the node software components. If they are\ncurrently at multiple versions because they're in the process of being\nupgraded, this reflects the minimum version of all nodes.",
    "createTime" : "[Output only] The time the cluster was created, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
    "nodeIpv4CidrSize" : "[Output only] The size of the address space on each node for hosting\ncontainers. This is provisioned from within the `container_ipv4_cidr`\nrange.",
    "subnetwork" : "The name of the Google Compute Engine\n[subnetwork](/compute/docs/subnetworks) to which the\ncluster is connected.",
    "name" : "The name of this cluster. The name must be unique within this project\nand zone, and can be up to 40 characters with the following restrictions:\n\n* Lowercase letters, numbers, and hyphens only.\n* Must start with a letter.\n* Must end with a number or a letter.",
    "resourceLabels" : "The resource labels for the cluster to use to annotate any related\nGoogle Compute Engine resources.",
    "servicesIpv4Cidr" : "[Output only] The IP address range of the Kubernetes services in\nthis cluster, in\n[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)\nnotation (e.g. `1.2.3.4/29`). Service addresses are\ntypically put in the last `/16` from the container CIDR.",
    "location" : "[Output only] The name of the Google Compute Engine\n[zone](/compute/docs/regions-zones/regions-zones#available) or\n[region](/compute/docs/regions-zones/regions-zones#available) in which\nthe cluster resides.",
    "locations" : [ "string" ],
    "conditions" : [ {
      "code" : "Machine-friendly representation of the condition",
      "message" : "Human-friendly representation of the condition"
    } ],
    "status" : "[Output only] The current status of this cluster."
  },
  "parent" : "The parent (project and location) where the cluster will be created.\nSpecified in the format 'projects/*/locations/*'.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the parent field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the parent field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.delete

Deletes the cluster, including the Kubernetes endpoint and all worker
nodes.

Firewalls and routes that were configured during cluster creation
are also deleted.

Other Google Compute Engine resources that might be in use by the cluster
(e.g. load balancer resources) will not be deleted if they weren't present
at the initial create time.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to delete.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project, location, cluster) of the cluster to delete.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.get

Gets the details of a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to retrieve.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project, location, cluster) of the cluster to retrieve.
Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.legacyAbac

Enables or disables the ABAC authorization mechanism on a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to update.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetLegacyAbacRequest enables or disables the ABAC authorization mechanism for
a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to set legacy abac.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field.",
  "enabled" : "Whether ABAC authorization will be enabled in the cluster."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.list

Lists all clusters owned by a project in either the specified zone or all
zones.

<details><summary>Parameters</summary>

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the parent field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides, or "-" for all zones.
This field has been deprecated and replaced by the parent field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### parent

The parent (project and location) where the clusters will be listed.
Specified in the format 'projects/*/locations/*'.
Location "-" matches all zones and all regions.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.locations

Sets the locations for a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetLocationsRequest sets the locations of the cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set locations.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "locations" : [ "string" ],
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.logging

Sets the logging service for a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetLoggingServiceRequest sets the logging service of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set logging.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "loggingService" : "The logging service the cluster should use to write metrics.\nCurrently available options:\n\n* \"logging.googleapis.com\" - the Google Cloud Logging service\n* \"none\" - no metrics will be exported from the cluster",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.master

Updates the master for a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

UpdateMasterRequest updates the master of the cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "masterVersion" : "The Kubernetes version to change the master to.\n\nUsers may specify either explicit versions offered by Kubernetes Engine or\nversion aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the default Kubernetes version",
  "name" : "The name (project, location, cluster) of the cluster to update.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.monitoring

Sets the monitoring service for a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetMonitoringServiceRequest sets the monitoring service of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "monitoringService" : "The monitoring service the cluster should use to write metrics.\nCurrently available options:\n\n* \"monitoring.googleapis.com\" - the Google Cloud Monitoring service\n* \"none\" - no metrics will be exported from the cluster",
  "name" : "The name (project, location, cluster) of the cluster to set monitoring.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.autoscaling

Sets the autoscaling settings for a specific node pool.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetNodePoolAutoscalingRequest sets the autoscaler settings of a node pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool) of the node pool to set\nautoscaler settings. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "autoscaling" : {
    "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
    "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
    "enabled" : "Is autoscaling enabled for this node pool."
  },
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.create

Creates a node pool for a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the parent field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the parent field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the parent field.

**Type:** string

### $body

CreateNodePoolRequest creates a node pool for a cluster.

**Type:** object

```json
{
  "nodePool" : {
    "initialNodeCount" : "The initial node count for the pool. You must ensure that your\nCompute Engine resource quota\nis sufficient for this number of instances. You must also have available\nfirewall and routes quota.",
    "instanceGroupUrls" : [ "string" ],
    "management" : {
      "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
      "upgradeOptions" : {
        "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
        "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
      },
      "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
    },
    "name" : "The name of the node pool.",
    "autoscaling" : {
      "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
      "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
      "enabled" : "Is autoscaling enabled for this node pool."
    },
    "conditions" : [ {
      "code" : "Machine-friendly representation of the condition",
      "message" : "Human-friendly representation of the condition"
    } ],
    "config" : {
      "metadata" : "The metadata key/value pairs assigned to instances in the cluster.\n\nKeys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes\nin length. These are reflected as part of a URL in the metadata server.\nAdditionally, to avoid ambiguity, keys must not conflict with any other\nmetadata keys for the project or be one of the reserved keys:\n \"cluster-location\"\n \"cluster-name\"\n \"cluster-uid\"\n \"configure-sh\"\n \"containerd-configure-sh\"\n \"enable-os-login\"\n \"gci-update-strategy\"\n \"gci-ensure-gke-docker\"\n \"instance-template\"\n \"kube-env\"\n \"startup-script\"\n \"user-data\"\n\nValues are free-form strings, and only have meaning as interpreted by\nthe image running in the instance. The only restriction placed on them is\nthat each value's size must be less than or equal to 32 KB.\n\nThe total size of all keys and values must be less than 512 KB.",
      "serviceAccount" : "The Google Cloud Platform Service Account to be used by the node VMs. If\nno Service Account is specified, the \"default\" service account is used.",
      "oauthScopes" : [ "string" ],
      "taints" : [ {
        "effect" : "Effect for taint.",
        "value" : "Value for taint.",
        "key" : "Key for taint."
      } ],
      "labels" : "The map of Kubernetes labels (key/value pairs) to be applied to each node.\nThese will added in addition to any default label(s) that\nKubernetes may apply to the node.\nIn case of conflict in label keys, the applied set may differ depending on\nthe Kubernetes version -- it's best to assume the behavior is undefined\nand conflicts should be avoided.\nFor more information, including usage and the valid values, see:\nhttps://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
      "tags" : [ "string" ],
      "preemptible" : "Whether the nodes are created as preemptible VM instances. See:\nhttps://cloud.google.com/compute/docs/instances/preemptible for more\ninformation about preemptible VM instances.",
      "minCpuPlatform" : "Minimum CPU platform to be used by this instance. The instance may be\nscheduled on the specified or newer CPU platform. Applicable values are the\nfriendly names of CPU platforms, such as\nminCpuPlatform: \"Intel Haswell\" or\nminCpuPlatform: \"Intel Sandy Bridge\". For more\ninformation, read [how to specify min CPU\nplatform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)",
      "accelerators" : [ {
        "acceleratorType" : "The accelerator type resource name. List of supported accelerators\n[here](/compute/docs/gpus/#Introduction)",
        "acceleratorCount" : "The number of the accelerator cards exposed to an instance."
      } ],
      "diskType" : "Type of the disk attached to each node (e.g. 'pd-standard' or 'pd-ssd')\n\nIf unspecified, the default disk type is 'pd-standard'",
      "imageType" : "The image type to use for this node. Note that for a given image type,\nthe latest version of it will be used.",
      "localSsdCount" : "The number of local SSD disks to be attached to the node.\n\nThe limit for this value is dependant upon the maximum number of\ndisks available on a machine per zone. See:\nhttps://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits\nfor more information.",
      "machineType" : "The name of a Google Compute Engine [machine\ntype](/compute/docs/machine-types) (e.g.\n`n1-standard-1`).\n\nIf unspecified, the default machine type is\n`n1-standard-1`.",
      "diskSizeGb" : "Size of the disk attached to each node, specified in GB.\nThe smallest allowed disk size is 10GB.\n\nIf unspecified, the default disk size is 100GB."
    },
    "version" : "The version of the Kubernetes of this node.",
    "statusMessage" : "[Output only] Additional information about the current status of this\nnode pool instance, if available.",
    "selfLink" : "[Output only] Server-defined URL for the resource.",
    "status" : "[Output only] The status of the nodes in this pool instance."
  },
  "parent" : "The parent (project, location, cluster id) where the node pool will be\ncreated. Specified in the format\n'projects/*/locations/*/clusters/*'.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the parent field.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the parent field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the parent field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.delete

Deletes a node pool from a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to delete.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project, location, cluster, node pool id) of the node pool to
delete. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.get

Retrieves the node pool requested.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project, location, cluster, node pool id) of the node pool to
get. Specified in the format
'projects/*/locations/*/clusters/*/nodePools/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.list

Lists the node pools for a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the parent field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the parent field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the parent field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### parent

The parent (project, location, cluster id) where the node pools will be
listed. Specified in the format 'projects/*/locations/*/clusters/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.rollback

Roll back the previously Aborted or Failed NodePool upgrade.
This will be an no-op if the last upgrade successfully completed.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to rollback.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to rollback.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

RollbackNodePoolUpgradeRequest rollbacks the previously Aborted or Failed
NodePool upgrade. This will be an no-op if the last upgrade successfully
completed.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to rollback.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node poll to\nrollback upgrade.\nSpecified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.",
  "clusterId" : "Deprecated. The name of the cluster to rollback.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.setManagement

Sets the NodeManagement options for a node pool.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to update.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to update.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetNodePoolManagementRequest sets the node management properties of a node
pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to update.\nThis field has been deprecated and replaced by the name field.",
  "management" : {
    "autoUpgrade" : "A flag that specifies whether node auto-upgrade is enabled for the node\npool. If enabled, node auto-upgrade helps keep the nodes in your node pool\nup to date with the latest release version of Kubernetes.",
    "upgradeOptions" : {
      "autoUpgradeStartTime" : "[Output only] This field is set when upgrades are about to commence\nwith the approximate start time for the upgrades, in\n[RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.",
      "description" : "[Output only] This field is set when upgrades are about to commence\nwith the description of the upgrade."
    },
    "autoRepair" : "A flag that specifies whether the node auto-repair is enabled for the node\npool. If enabled, the nodes in this node pool will be monitored and, if\nthey fail health checks too many times, an automatic repair action will be\ntriggered."
  },
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node pool to set\nmanagement properties. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.setSize

Sets the size for a specific node pool.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to update.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to update.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetNodePoolSizeRequest sets the size a node
pool.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to update.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool id) of the node pool to set\nsize.\nSpecified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.",
  "nodeCount" : "The desired node count for the pool.",
  "clusterId" : "Deprecated. The name of the cluster to update.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.nodePools.update

Updates the version and/or image type for a specific node pool.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### nodePoolId (required)

Deprecated. The name of the node pool to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

UpdateNodePoolRequests update a node pool's image and/or version.

**Type:** object

```json
{
  "nodePoolId" : "Deprecated. The name of the node pool to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster, node pool) of the node pool to\nupdate. Specified in the format\n'projects/*/locations/*/clusters/*/nodePools/*'.",
  "nodeVersion" : "The Kubernetes version to change the nodes to (typically an\nupgrade).\n\nUsers may specify either explicit versions offered by Kubernetes Engine or\nversion aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the Kubernetes master version",
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "imageType" : "The desired image type for the node pool.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.resourceLabels

Sets labels on a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetLabelsRequest sets the Google Cloud Platform labels on a Google Container
Engine cluster, which will in turn set them for Google Compute Engine
resources used by that cluster

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to set labels.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "resourceLabels" : "The labels to set for that cluster.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "labelFingerprint" : "The fingerprint of the previous set of labels for this resource,\nused to detect conflicts. The fingerprint is initially generated by\nKubernetes Engine and changes after every request to modify or update\nlabels. You must always provide an up-to-date fingerprint hash when\nupdating or changing labels. Make a get() request to the\nresource to get the latest fingerprint.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.setMaintenancePolicy

Sets the maintenance policy for a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

The name of the cluster to update.

**Type:** string

### projectId (required)

The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).

**Type:** string

### zone (required)

The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.

**Type:** string

### $body

SetMaintenancePolicyRequest sets the maintenance policy for a cluster.

**Type:** object

```json
{
  "maintenancePolicy" : {
    "window" : {
      "dailyMaintenanceWindow" : {
        "duration" : "[Output only] Duration of the time window, automatically chosen to be\nsmallest possible in the given scenario.\nDuration will be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"PTnHnMnS\".",
        "startTime" : "Time within the maintenance window to start the maintenance operations.\nTime format should be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)\nformat \"HH:MM”, where HH : [00-23] and MM : [00-59] GMT."
      }
    }
  },
  "zone" : "The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.",
  "name" : "The name (project, location, cluster id) of the cluster to set maintenance\npolicy.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "The name of the cluster to update.",
  "projectId" : "The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840)."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.setMasterAuth

Used to set master auth materials. Currently supports :-
Changing the admin password for a specific cluster.
This can be either via password generation or explicitly set the password.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetMasterAuthRequest updates the admin password of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to set auth.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "action" : "The exact form of action to be taken on the master auth.",
  "update" : {
    "clientCertificateConfig" : {
      "issueClientCertificate" : "Issue a client certificate."
    },
    "clientCertificate" : "[Output only] Base64-encoded public certificate used by clients to\nauthenticate to the cluster endpoint.",
    "password" : "The password to use for HTTP basic authentication to the master endpoint.\nBecause the master endpoint is open to the Internet, you should create a\nstrong password.  If a password is provided for cluster creation, username\nmust be non-empty.",
    "clientKey" : "[Output only] Base64-encoded private key used by clients to authenticate\nto the cluster endpoint.",
    "clusterCaCertificate" : "[Output only] Base64-encoded public certificate that is the root of\ntrust for the cluster.",
    "username" : "The username to use for HTTP basic authentication to the master endpoint.\nFor clusters v1.6.0 and later, basic authentication can be disabled by\nleaving username unspecified (or setting it to the empty string)."
  },
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.setNetworkPolicy

Enables/Disables Network Policy for a cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

SetNetworkPolicyRequest enables/disables network policy for a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "networkPolicy" : {
    "provider" : "The selected network policy provider.",
    "enabled" : "Whether network policy is enabled on the cluster."
  },
  "name" : "The name (project, location, cluster id) of the cluster to set networking\npolicy. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.startIpRotation

Start master IP rotation.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://developers.google.com/console/help/new/#projectnumber).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

StartIPRotationRequest creates a new IP for the cluster and then performs
a node upgrade on each node pool to point to the new IP.

**Type:** object

```json
{
  "rotateCredentials" : "Whether to rotate credentials during IP rotation.",
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster id) of the cluster to start IP\nrotation. Specified in the format 'projects/*/locations/*/clusters/*'.",
  "clusterId" : "Deprecated. The name of the cluster.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://developers.google.com/console/help/new/#projectnumber).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.clusters.update

Updates the settings of a specific cluster.

<details><summary>Parameters</summary>

### clusterId (required)

Deprecated. The name of the cluster to upgrade.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

UpdateClusterRequest updates the settings of a cluster.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the cluster\nresides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, cluster) of the cluster to update.\nSpecified in the format 'projects/*/locations/*/clusters/*'.",
  "update" : {
    "desiredImageType" : "The desired image type for the node pool.\nNOTE: Set the \"desired_node_pool\" field as well.",
    "desiredMonitoringService" : "The monitoring service the cluster should use to write metrics.\nCurrently available options:\n\n* \"monitoring.googleapis.com\" - the Google Cloud Monitoring service\n* \"none\" - no metrics will be exported from the cluster",
    "desiredMasterVersion" : "The Kubernetes version to change the master to.\n\nUsers may specify either explicit versions offered by\nKubernetes Engine or version aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the default Kubernetes version",
    "desiredMasterAuthorizedNetworksConfig" : {
      "cidrBlocks" : [ {
        "displayName" : "display_name is an optional field for users to identify CIDR blocks.",
        "cidrBlock" : "cidr_block must be specified in CIDR notation."
      } ],
      "enabled" : "Whether or not master authorized networks is enabled."
    },
    "desiredLocations" : [ "string" ],
    "desiredNodePoolId" : "The node pool to be upgraded. This field is mandatory if\n\"desired_node_version\", \"desired_image_family\" or\n\"desired_node_pool_autoscaling\" is specified and there is more than one\nnode pool on the cluster.",
    "desiredNodePoolAutoscaling" : {
      "minNodeCount" : "Minimum number of nodes in the NodePool. Must be &gt;= 1 and &lt;=\nmax_node_count.",
      "maxNodeCount" : "Maximum number of nodes in the NodePool. Must be &gt;= min_node_count. There\nhas to enough quota to scale up the cluster.",
      "enabled" : "Is autoscaling enabled for this node pool."
    },
    "desiredNodeVersion" : "The Kubernetes version to change the nodes to (typically an\nupgrade).\n\nUsers may specify either explicit versions offered by\nKubernetes Engine or version aliases, which have the following behavior:\n\n- \"latest\": picks the highest valid Kubernetes version\n- \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version\n- \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version\n- \"1.X.Y-gke.N\": picks an explicit Kubernetes version\n- \"-\": picks the Kubernetes master version",
    "desiredAddonsConfig" : {
      "kubernetesDashboard" : {
        "disabled" : "Whether the Kubernetes Dashboard is enabled for this cluster."
      },
      "httpLoadBalancing" : {
        "disabled" : "Whether the HTTP Load Balancing controller is enabled in the cluster.\nWhen enabled, it runs a small pod in the cluster that manages the load\nbalancers."
      },
      "networkPolicyConfig" : {
        "disabled" : "Whether NetworkPolicy is enabled for this cluster."
      },
      "horizontalPodAutoscaling" : {
        "disabled" : "Whether the Horizontal Pod Autoscaling feature is enabled in the cluster.\nWhen enabled, it ensures that a Heapster pod is running in the cluster,\nwhich is also used by the Cloud Monitoring service."
      }
    }
  },
  "clusterId" : "Deprecated. The name of the cluster to upgrade.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.getServerconfig

Returns configuration info about the Kubernetes Engine service.

<details><summary>Parameters</summary>

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) to return operations for.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project and location) of the server config to get,
specified in the format 'projects/*/locations/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.operations.cancel

Cancels the specified operation.

<details><summary>Parameters</summary>

### operationId (required)

Deprecated. The server-assigned `name` of the operation.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the operation resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### $body

CancelOperationRequest cancels a single operation.

**Type:** object

```json
{
  "zone" : "Deprecated. The name of the Google Compute Engine\n[zone](/compute/docs/zones#available) in which the operation resides.\nThis field has been deprecated and replaced by the name field.",
  "name" : "The name (project, location, operation id) of the operation to cancel.\nSpecified in the format 'projects/*/locations/*/operations/*'.",
  "operationId" : "Deprecated. The server-assigned `name` of the operation.\nThis field has been deprecated and replaced by the name field.",
  "projectId" : "Deprecated. The Google Developers Console [project ID or project\nnumber](https://support.google.com/cloud/answer/6158840).\nThis field has been deprecated and replaced by the name field."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.operations.get

Gets the specified operation.

<details><summary>Parameters</summary>

### operationId (required)

Deprecated. The server-assigned `name` of the operation.
This field has been deprecated and replaced by the name field.

**Type:** string

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the name field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) in which the cluster
resides.
This field has been deprecated and replaced by the name field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### name

The name (project, location, operation id) of the operation to get.
Specified in the format 'projects/*/locations/*/operations/*'.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## container.projects.zones.operations.list

Lists all operations in a project in a specific zone or all zones.

<details><summary>Parameters</summary>

### projectId (required)

Deprecated. The Google Developers Console [project ID or project
number](https://support.google.com/cloud/answer/6158840).
This field has been deprecated and replaced by the parent field.

**Type:** string

### zone (required)

Deprecated. The name of the Google Compute Engine
[zone](/compute/docs/zones#available) to return operations for, or `-` for
all zones. This field has been deprecated and replaced by the parent field.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### parent

The parent (project and location) where the operations will be listed.
Specified in the format 'projects/*/locations/*'.
Location "-" matches all zones and all regions.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

