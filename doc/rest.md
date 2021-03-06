# QIIME 2 REST API
- Each resource is either an entity or a collection.
- Every entity has one, and only one, URI (Uniform Resource Identifier), which is its own URL. This URI will always end in an ID.
- The host is a meaningful part of a resource's URI, allowing distributed URIs.
- Every collection contains zero or more entities. The content of a collection is not necessarily exclusive to a URL. The order of a collection is not significant.
- Every response is JSON, minimally containing the URI of the resource (`resource`) and the HTTP method (`action`).
- HTTP response codes are used to indicate status.

# /system

### GET
URI of the host and general health endpoint.

Response:

    version: QIIME server version [string]

# /system/plugins and /system/plugins/all

### GET
Collection of plugins.

Response:

    plugins: plugin URIs [array]

# /system/plugins/:plugin

### GET
Info about the plugin.

Response:

    name: [string]
    version: [string]
    author: [string]
    description: [string]

## /system/plugins/all/methods

### GET
List all methods across all plugins.

## /system/plugins/:plugin/methods

### GET
List of methods in the specified plugin.

## /system/plugins/:plugin/methods/:method

### GET
Information about the method, e.g., name, description, annotations, etc.

## /system/plugins/all/types

### GET
Registered types across all plugins. Query parameter ``format`` will specify the structure of the output format: ``list`` will be a flat list of type URIs and ``tree`` will be a JSON tree indicating the hierarchical relationship among the types.

## /system/plugins/:plugin/types

### GET
Registered types in the specified plugin. Query parameter ``format`` will specify the structure of the output format: ``list`` will be a flat list of type URIs and ``tree`` will be a JSON tree indicating the hierarchical relationship among the types.

## /system/plugins/:plugin/types/:type

### GET
Info about the registered type, e.g., name, description, etc.

## /system/types/primitives

### GET
List of registered primitive types.

## /system/types/primitives/:type

### GET
Info about the registered primitive type.

## /system/types/parameterized

### GET
List of registered parameterized types.

## /system/types/parameterized/:type

### GET
Info about the registered parameterized type.

## /studies

### GET
List studies you have access to.

### POST
Create a new study.

## /studies/:study

### GET
Information about the study, e.g., name, description, creation time, etc.

### PUT
Update an existing study.

### DELETE
Delete an existing study.

## /studies/:study/artifacts

### GET
Provide artifact abstract file system tree.

### POST
Create a new artifact.

### PUT
Link an existing artifact.

## /studies/:study/artifacts/:artifact

### GET
Information about the artifact. Query parameter ``export`` specifies
file type to export artifact as for downloading.

### PUT
Update artifact metadata, e.g., name, description. History, underlying data, and
type cannot be modified.

### DELETE
Delete artifact.

## /studies/:study/jobs

### GET
List all jobs. Query parameter to filter by job status (completed, running,
etc.)

### POST
Create a new job.

## /studies/:study/jobs/:job

### GET
Information about the job, e.g., status. SSE will also happen here via a query
parameter (``subscribe``).

### PUT
Update the job: pause, resume, or update a downstream parameter.

### DELETE
Terminate the job.

## /studies/:study/workflows

### GET
List all workflow templates.

### POST
Create a new workflow template.

## /studies/:study/workflows/:workflow

### GET
Return workflow template and metadata.

### PUT
Update workflow template and metadata.

### DELETE
Delete workfow template and metadata.
