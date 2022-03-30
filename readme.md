# Utility-Data-Management-Support-Tools

Here are a set of tools to work with the utility network and the maps to interact with it.

## Features
### Create Utility Network System Tables Views
#### Generate views on the utility network system tables.
<p><p>This tool generates database views for the utility network system tables for Geodatabases and table views for services.</p><p>Ensure 'Add output datasets to an open map' is checked if you want the results added to your map. </p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
network|Input Network|<p>The utility network</p>
tables|Tables|<p>The Utility Network system tables to generate views on.</p>
out_tables|Table Views|<p>The resulting table views</p>
---

### Update Data Sources
#### Use this tool to convert the data source of layers in the maps in the current ArcGIS Pro project to a workspace.
<p><p>This tool changes the data source of the maps to a new workspace. This will convert between file geodatabase, enterprise geodatabase, and feature services.</p><p>When changing from or to a feature service, the layer alias name in the service (with or without spaces) must match the class name alias.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
target_workspace|Target Workspace|<p>The new workspace for the layers.</p>
maps|Maps|<p>The maps in the current ArcGIS Pro project to update the data source in.</p>
update_sr|Update Map Spatial Reference|<p><p>Use the spatial reference from the first feature class to update the maps spatial reference.<p>The error layers are ignored as they are always in 102100.</p></p></p>
---

### Select by Association
#### Expands the current selection in the map based on specified utility network association types and layers.
<p><p>This tool requires at least 1 record be selected.</p><p>The Selection Payload parameter must be specified in JSON as a list of dictionaries with the following keys:<ul><li>fromLayers</li><li>associationTypes</li><li>toLayers</li></ul></p><p>Each key maps to an array of values. If the array is empty, then all valid choices are applied.</p><p>fromLayers and toLayers are the from and to side of the association, respectively. Each entry corresponds to a layer in the map.</p><p>For subtype group layers, specify as "SubtypeGroupLayer/SubtypeLayer".</p><p>associationTypes is the type of association between fromLayers and toLayers. It has the following entries:<ul><li>Junction Junction</li><li>Contained By</li><li>Containing</li><li>Attached To</li><li>Attaching</li><li>Junction Edge From</li><li>Junction Edge Midspan</li><li>Junction Edge To</li></ul></p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
json_payload|Selection Payload|<p>The layers and selection types to apply. For more help, see the tool usage.</p>
---

### Batch Trace
#### Iterate through the starting points to trace the utility network and use the results.
<p><p>This tool uses a with starting point information to trace the utility network. The starting points are optionally grouped so set of starting points is used in each trace.</p><p>The trace results can be used to select features in a map, calculate values on results, create connectivity and element files or save the aggregated geometry with summary information.</p><p>The starting points layer uses a field to determine if a row is a starting point and/or barrier. A feature as a starting point and filter barrier is useful in a connected trace to determine all the items between the starting points.</p><p>The starting points table requires the following fields:<ul><li>FEATUREGLOBALID: GUID</li><li>TERMINALID: Short</li><li>PERCENTALONG: Double</li></ul></p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
in_utility_network|Input Utility Network|<p>The utility network that will be used to trace.</p>
starting_points|Starting Points|<p>The table from which to load starting points for trace.</p>
result_types|Result Types|<p>Specifies the type of results that will be returned by the trace.<ul><li>Selection - The trace results will be returned as a selection set on the appropriate network features.</li><li>Aggregated Geometry - The trace results will be aggregated by geometry type and stored in multipart feature classes displayed in the layers in the active map.</li><li>Connectivity - The trace results will be returned as a connectivity graph in a specified output .json file. This option enables the Output JSON parameter.</li><li>Elements - The trace results will be returned as feature-based information in a specified output .json file. This option enables the Output JSON parameter.</li><li>Calculate - Update a field in the trace results from information on the starting points. If multiple starting points are used, the value from the lowest OID is used.</li></ul></p>
trace_config|Trace Configuration Name or Field|<p>The utility network trace configuration used to define the trace parameters or a field with trace configurations.</p>
expression|Expression|<p>The simple calculation expression used to limit the starting points used in a trace.</p>
output_folder|Output Folder|<p>The location of the output json files and mobile geodatabase with the aggregated geometry. This parameter is only applicable for the Aggregated Geometry, Elements or Connectivity result type.</p>
key_field|Group Field|<p><p>Field used to group starting points and barriers.</p><p>When specified, records with the same value will used for a single trace. By default, a trace is run for every starting point.</p></p>
summary_store_field|Store Summary Information on Starting Points|<p>Optional field used to store summary results on the starting points</p>
fields|Fields to update|<p><p>The mapping of starting points field to network source field.</p><p>This parameter is only applicable for the Calculation result type.</p><p>Mapping components are as follows:<ul><li>From Field - The field from the starting points to propagate.</li><li>Source Name - The name of the utility network source.</li><li>To Field - The field on the source class to update.</li><li>Calculation Mode - How to combine values.</li></ul></p><p>Calculation mode supports:<ul><li>Concatenate with existing - Read existing values and combine with new values.</li><li>Concatenate and overwrite - Combine new values.</li></ul></p></p>
skip_calc_on_start|Calculate on Starting Point Features|<p>If specified, the calculate will also update the features the starting points are placed on.</p>
json_folder|Connectivity and Element file folder|<p>The folder with the files for connectivity and element information.</p>
out_gdb|Aggregated GDB|<p>The mobile geodatabase with the aggregated geometry.</p>
---

### Build Starting Points
#### Creates starting points based on a trace configuration.
Creates starting points based on a trace configuration.

| Parameter | Display | Description |
| --------- | ------- | ----------- |
in_utility_network|Input Utility Network|<p>The utility network that will be used to trace.</p>
trace_config|Trace Configuration Name|<p>The utility network trace configuration used to define the trace parameters.</p>
starting_points|Starting Points or Line Layer|<p><p>The utility network subnetworks table or a table that defines starting points.</p><p>A Line layer can also be used, the center point of the line will be used as the starting point.</p></p>
subnetwork_name|Output Name Field|<p>The name for the trace.Select the Global ID field for a unique name.</p>
expression|Expression|<p>The simple calculation expression used to limit the starting points used in a trace.</p>
results_trace_config|Result Trace Config|<p>The trace configuration to use in the result. If not provided, the trace configuration used to find the results will be used.</p>
trace_results|Trace Results|<p>The results from the trace in the starting points table format. If an existing class is specified and if the row with the Global ID/Terminal ID exists, the ISDIRTY field will be updated. If the row does not exist, it will be inserted.</p>
filter_classes|Filter Classes|<p><p>Do not store features from these classes.</p><p>This is useful when tracing a line layer to build starting points.  The tool loops over all input features and creates a starting point to trace.  If the trace results the features used to trace, they can be skipped to increases preformance.  The this filter allows you to return them and not store them in the result.</p></p>
skip_found|Skip Found Features|<p><p>If a features global id was returned in a trace, do not trace that feature.</p></p>
compare_subnetwork_name|Compare Subnetwork Name|<p><p>On an update, compare the subnetwork names.  When running a batch process, it is best to pick this, but may insert more records instead of updating.</p></p>
---

### Calculate Tolerances and Resolutions
#### Calculate the XY, Z, and M tolerances based on a measure unit for systems that will use a linear referencing system (LRS).
<p>Specify the spatial reference and the unit of measure for the M values. The tolerances are printed as geoprocessing messages. These values should be entered when defining the spatial reference of the feature dataset.</p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
spatial_reference|Spatial Reference|<p>The spatial reference of the dataset.</p>
measure_unit|Measure Unit|<p>Unit of measurement for the M values.</p>
---

### Change GDB Spatial Reference
#### Creates a new file geodatabase in the user-specified spatial reference.
Creates a new file geodatabase in the user-specified spatial reference.

| Parameter | Display | Description |
| --------- | ------- | ----------- |
gdb|Geodatabase|<p>The input gdb that will be copied.</p>
spatial_reference|Output Spatial Reference|<p>The spatial reference of the new geodatabase.</p>
output_folder|Folder Location|<p>The folder location where the asset package will be created.</p>
output_name|Output Name|<p>The name of the output geodatabase.</p>
output_package|Output Package|<p>The result geodatabase with new spatial reference.</p>
---

### Asset Package Configuration Report
#### <p><p>Generate a collection of Excel Workbooks/Sheets to review the what properties are include/removed from the result by selecting 1 or more configurations.</p><p>Multiple configurations can be selected to compare the results.</p></p>
<p><p>Generate a collection of Excel Workbooks/Sheets to review the what properties are include/removed from the result by selecting 1 or more configurations.</p><p>Multiple configurations can be selected to compare the results.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
asset_package|Asset Package|<p>The asset package with configuration tables.</p>
folder|Output Folder|<p>The location to save the output.  A unique folder starting with Configuration will be generated in this location for each run of the tool.</p>
mode|Report Mode|<p><p>The method to generate the report and adjust the UI of this tool.</p><p>Single - The configuration options are present into a list with checkboxes.  Uncheck the configurations to remove those values associated with them.</p><p>Multiple - The configuration options must be defined in a list of list.  The list must include the configurations to include (checked).</p><p>All - All combinations of the configurations will be included.  This is a powerset, so there may be a large number of combinations</p></p>
single_configuration|Single Configuration|<p><p>Select the configuration options you want to apply to your report.</p><p>The D_Configurations table must be present in your asset package.</p><p>More information - https://solutions.arcgis.com/utilities/help/utility-network-automation/asset-package-reference/d-configurations.htm</p></p>
multiple_configurations|Multiple Configurations|<p><p>To compare multiple configurations, you must input a list of list.</p><p>A list of all configurations is predefined.  To create new set of configurations, copy and paste the list and remove the item that you want to 'uncheck'.</p><p>Repeat this process for each combination of configurations you want to compare.</p></p>
rename|Rename Choices|<p><p>Select the rename option you want to apply to your report.</p><p>The D_Rename table must be present in your asset package.</p><p>More information - https://solutions.arcgis.com/utilities/help/utility-network-automation/asset-package-reference/d-rename.htm</p></p>
result_folder|Result Folder|<p>The path the folder generated in the output folder location that contains the reporting Excel files.</p>
---

### Asset Package Rename Report
#### <p><p>Generate a collection of Excel Workbooks/Sheets to review the what properties are renamed by selecting 1 or more rename values.</p><p>Multiple renames can be selected to compare the results.</p></p>
<p><p>Generate a collection of Excel Workbooks/Sheets to review the what properties are renamed by selecting 1 or more rename values.</p><p>Multiple renames can be selected to compare the results.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
asset_package|Asset Package|<p>The asset package with rename table.</p>
rename|Rename Choices|<p><p>Select the rename options you want to apply to your report.</p><p>The D_Rename table must be present in your asset package.</p><p>More information - https://solutions.arcgis.com/utilities/help/utility-network-automation/asset-package-reference/d-rename.htm</p></p>
folder|Output Folder|<p>The location to save the output.  A unique folder starting with Rename will be generated in this location for each run of the tool.</p>
configuration|Configurations|<p><p>Select the configuration options you want to apply to your report.</p><p>The D_Configurations table must be present in your asset package.</p><p>More information - https://solutions.arcgis.com/utilities/help/utility-network-automation/asset-package-reference/d-configurations.htm</p></p>
result_folder|Result Folder|<p>The path the folder generated in the output folder location that contains the reporting Excel files.</p>
---

### Configure UN Layers
#### Configures utility network layers by modifying popups and display filters.
<p><p>Configures utility network layers by modifying popups and display filters.</p><p>This tool can be run multiple times and existing properties will be updated.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
map_name|Map Name|<p>The map name to process.</p>
options|Options|<p>The options to add to the layers.<ul><li>Rule Popup - Adds an entry to the popup listing the valid rules the record can connect to.</li><li>Category Popup - Adds an entry to the popup listing the record's assigned network categories.</li><li>Subnetwork Popup- Adds an entry to the popup listing the record's assigned subnetworks and parent subnetworks. Only valid for partitioned networks.</li><li>Category Display Filter - Adds display filters to show/hide features with the assigned network categories.</li></ul></p>
input_project|Pro Project|<p>The Pro project to read maps from. Leave blank to use the active project.</p>
category_filters|Category Display Filters|<p><p>The display filters to add to the map.</p><p>To specify multiple categories in the same display filter, reuse the Display Filter Name.</p></p>
output_project|Output Project|<p>The updated project.</p>
---

### Create Association Lines
#### Creates lines representing utility network associations.
<p><p>Creates lines representing utility network associations.</p><p>For polylines and polygons, the centroid will be used.</p><p>Both features must intersect the extent to be processed.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
network|Input Network|<p>The utility network or asset package to process.</p>
association_types|Association Types|<p>The association types to generate<ul><li>Junction Junction Connectivity</li><li>Containment</li><li>Structural Attachment</li></ul></p>
output_lines|Output Lines|<p>The output line feature class.</p>
extent|Extent|<p>If specified, only generate lines for features intersecting this extent. By default, the entire network is processed.</p>
completely_within|Completely Within|<p>If specified, both sides of the association must be present in the extent.This option is only valid when specifying an extent.</p>
---

### Enable APR on UPDM
#### Creates the script to enable LRS or enables LRS on a UPDM database with a utility network.
Creates the script to enable LRS or enables LRS on a UPDM database with a utility network.

| Parameter | Display | Description |
| --------- | ------- | ----------- |
in_utility_network|Input Utility Network|<p>The utility network that will be used to create the LRS.</p>
lrs_name|LRS Name|<p>The name of the LRS to create. The name for the LRS cannot already exist in the geodatabase.</p>
write_script|Only Write Script|<p>Option to only write a script to enable LRS and not perform the Geoprocessing calls. This script can be run through python to enable LRS. Selecting this option will enable the output folder parameter.</p>
output_folder|Script Output Folder|<p>Output folder for the LRS script. The script name will start with "updm_lrs" and end with a unique GUID. This parameter is only valid when Write Output Script is true.</p>
---

### Export Matrix
#### Creates Excel workbooks for visualizing and modifying Utility Network rules, categories, and terminal assignments.
Creates Excel workbooks for visualizing and modifying Utility Network rules, categories, and terminal assignments.

| Parameter | Display | Description |
| --------- | ------- | ----------- |
network|Input Network|<p>The utility network or asset package.</p>
workbook|Matrix Workbook|<p>The output workbook to create.</p>
matrix_options|Matrix Options|<p>The properties to create.</p>
---

### Extract Logs from Files
#### <p><p>Generate a Mobile GDB with a record for each entry in a log file.</p><p>A series of views are created on top of the log table to look at log entries for particular operations.</p><p>This tool processes log files generated from either ArcGIS Server or ArcGIS Pro.</p></p>
<p><p>Generate a Mobile GDB with a record for each entry in a log file.</p><p>A series of views are created on top of the log table to look at log entries for particular operations.</p><p>This tool processes log files generated from either ArcGIS Server or ArcGIS Pro.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
diagnostic_files|Diagnostic Files|<p>The ArcGIS Pro Diagnostic Log file.  For more information on how to access it, please refer to this technical article - https://support.esri.com/en/technical-article/000023675</p>
folder|Output Folder|<p>The location to save the output.</p>
logs|Logs|<p>The table with extracted logs.</p>
---

### Extract Logs from REST
#### <p>Extracts logs from ArcGIS Server.</p>
<p>Extracts logs from ArcGIS Server.</p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
site|Server Site|<p>The ArcGIS Server site to query.</p>
folder|Output Folder|<p>The location to save the output.</p>
from_date|From Date|<p><p>The oldest time to include in the result set.</p><p>If not specified, then all logs will be returned.</p></p>
to_date|To Date|<p><p>The most recent time to query.</p><p>If not specified, then the current time will be used.</p></p>
log_level|Log Level|<p><p>Only records with a log level at or more severe than this level are returned.</p><p>If not specified, then WARNING will be used.</p></p>
log_codes|Log Codes|<p><p>Specifies the log codes assigned to server logs.</p><p>If not specified, then all codes will be queried.</p></p>
process_ids|Process IDs|<p><p>Specifies the machine process IDs to query.</p><p>If not specified, then all process IDs will be queried.</p></p>
request_ids|Request IDs|<p><p>Specifies an ID assigned to a specific server request.</p><p>If not specified, then all request IDs will be queried.</p></p>
components|Component|<p><p>Specifies the server components delivering the log message.</p><p>If not specified, then all components will be queried.</p></p>
services|Services|<p><p>Specifies whether to query all, none, or a specific service in your site.</p><p>If not specified, then all services will be queried.</p></p>
machines|Machine Names|<p><p>Specifies whether to query all or a specific machine in your server site.</p><p>If not specified, then all machines will be queried.</p></p>
logs|Logs|<p>The table with extracted logs.</p>
---

### Modify Map by Rename and Configure
#### Applies rename and configuration options to maps based on an asset package.
Applies rename and configuration options to maps based on an asset package.

| Parameter | Display | Description |
| --------- | ------- | ----------- |
maps|Maps|<p>The maps in the current ArcGIS Pro project to modify.</p>
asset_package|Asset Package|<p>The asset package with rename and/or configuration tables.</p>
configurations|Configurations to keep|<p>The configurations to keep. The deselected options will be removed from the map.</p>
rename_field|Rename using|<p>The rename field to apply. Items in the map will have their names changed.</p>
input_project|Pro Project|<p>The Pro project to read maps from. Leave blank to use the active project.</p>
output_project|Output Project|<p>The updated Pro project.</p>
---

### Import Matrix
#### <p>Loads the values from the rule, network category, and terminal assignment workbooks.</p>
<p><p>Loads the values from the rule, network category, and terminal assignment workbooks.</p><p>Rules removed from the worksheet are not removed from the utility network.</p><p>New network categories can be added by adding a new column.  Assignments can be removed by deleting 1 from the cell.</p><p>Changing existing terminal assignments are not supported, only setting a terminal configuration from the default of single terminal.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
network|Input Network|<p>The utility network or asset package to modify.</p>
workbook|Matrix Workbook|<p>The workbook to import.</p>
matrix_options|Matrix Options|<p>The properties to create.</p>
---

### Summarize Errors
#### Generates a Mobile GDB with features for each error in the Utility Network and summary views
<p><p>A new Mobile GDB with features for each error in the Utility Network.  The features geometry is a buffered union of the features.</p><p>A series of views that provide summaries of errors are also included to provide quick metrics on the types and number of errors.</p><p>The Utility Network must be version 4+</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
network|Input Network|<p>The utility network</p>
folder|Output folder|<p>The folder where the results will be saved.</p>
output_gdb|Output Geodatabase|<p>The geodatabase with results.</p>
---

### Summary By Bits
#### Summarizes records containing a bitwise coded value domain.
<p><p>Summarizes records containing a bitwise coded value domain.</p><p>The output table containing summary information will have chart(s) associated with it.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
input_records|Input Records|<p>The table to summarize.</p>
bit_field|Bitwise Field|<p>The field containing bit values. This field must have a coded value domain assigned of type short or long.</p>
output|Table|<p>The table to write the summarized results to.</p>
summary_field|Summary Fields|<p>The numeric fields to summarize in addition to counting the bits. For each summary field, an additional chart will be created.</p>
---

### Trace to Trace Configurations
#### Converts arcpy.un.Trace to arcpy.un.AddTraceConfiguration
<p><p>Converts arcpy.un.Trace to arcpy.un.AddTraceConfiguration</p><p>To capture the python code, configure a Utility Network trace and copy the python command.</p></p>

| Parameter | Display | Description |
| --------- | ------- | ----------- |
trace_configuration_name|Trace Configuration Name|<p>The name of the trace configuration to create. If the name already exists, a number will be appended to make it unique.</p>
trace_results|Trace python calls|<p>The python code for Trace.</p>
execute|Create trace configurations|<p>Option to immediately add the configurations<ul><li>Checked - Add the trace configurations.</li><li>Unchecked - Do nothing. This is the default.</li></ul></p>
output_script|Save python calls to script|<p>Create a python script with the call to arcpy.un.AddTraceConfiguration.</p>
---


## Instructions

1. Download the  [UtilityDataManagementSupport.atbx](/UtilityDataManagementSupport.atbx)
2. Add to an ArcGIS Pro project

## Requirements

* ArcGIS Pro 2.9

## Resources

* [What is the Utility Network](https://pro.arcgis.com/en/pro-app/latest/help/data/utility-network/what-is-a-utility-network-.htm)
* [ArcGIS Blog](http://blogs.esri.com/esri/arcgis/)
* [twitter@esri](http://twitter.com/esri)

## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone. Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing
Copyright 2021 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [license.txt](/license.txt) file.
