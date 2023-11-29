| Name | Alias | Description |
| --- | --- | --- |
| [AddUNSystemTables](./AddUNSystemTables.html) | Create Utility Network System Tables Views | 
          
            This tool generates database views for the utility network system tables for Geodatabases and table views for services.
            Ensure 'Add output datasets to an open map' is checked if you want the results added to your map.
          
         |
| [AdjustDataSources](./AdjustDataSources.html) | Update Data Sources | 
          
            This tool changes the data source of the maps to a new workspace. This will convert between file geodatabase, enterprise geodatabase, and feature services.
            When changing from or to a feature service, the layer alias name in the service (with or without spaces) must match the class name alias.
          
         |
| [AssociationSelection](./AssociationSelection.html) | Select by Association | 
          
            This tool requires at least 1 record be selected.
            The Selection Payload parameter must be specified in JSON as a list of dictionaries with the following keys: |
| [BatchTrace](./BatchTrace.html) | Batch Trace | 
          
            This tool uses a with starting point information to trace the utility network. The starting points are optionally grouped so set of starting points is used in each trace.
            The trace results can be used to select features in a map, calculate values on results, create connectivity and element files or save the aggregated geometry with summary information.
            The starting points layer uses a field to determine if a row is a starting point and/or barrier. A feature as a starting point and filter barrier is useful in a connected trace to determine all the items between the starting points.
            The starting points table requires the following fields:
            
               |
| [BuildStartingPoints](./BuildStartingPoints.html) | Build Starting Points | 
          The Utility Network must be at least Schema Version 5.
         |
| [CalculateTolerances](./CalculateTolerances.html) | Calculate Tolerances and Resolutions | 
          
            Specify the spatial reference and the unit of measure for the M values.
            The tolerances are printed as geoprocessing messages. These values should be entered when defining the spatial reference of the feature dataset.
          
         |
| [ChangeGDBSpatialReference](./ChangeGDBSpatialReference.html) | Change GDB Spatial Reference | 
          Creates a new file geodatabase in the user-specified spatial reference.
         |
| [CompareConfigurations](./CompareConfigurations.html) | Asset Package Configuration Report | 
          Multiple configurations can be selected to compare the results.
         |
| [CompareRenames](./CompareRenames.html) | Asset Package Rename Report | 
          Multiple rename can be selected to compare the results.
         |
| [ConfigureUtilityNetworkLayers](./ConfigureUtilityNetworkLayers.html) | Configure UN Layers | 
          This tool can be run multiple times and existing properties will be updated.
         |
| [ContingentValueWorkbookToCSV](./ContingentValueWorkbookToCSV.html) | Convert Contingent Values Workbook | 
          The CSV files can be imported using Design View or the Import Contingent Values geoprocessing tool.
         |
| [CreateAssociationLines](./CreateAssociationLines.html) | Create Association Lines | 
          For polylines and polygons, the centroid will be used.
         |
| [CreateContingentValueAttributeRules](./CreateContingentValueAttributeRules.html) | Contingent Values to Attribute Rules | 
          
            The target table must have field groups and contingent values set up.
            Restrictive field groups generate Constraint and Non-Restrictive field groups generate Validation Attribute Rules.
          
         |
| [CreateContingentValues](./CreateContingentValues.html) | Create Contingent Values | 
          
            The target table must have at least one field field group.
            Schema mode can create very large CSVs depending on the number of field groups and coded value domains. The result should be edited before importing.
          
         |
| [CreateContingentValuesWorkbook](./CreateContingentValuesWorkbook.html) | Create Contingent Values Workbook | 
          The target table must have at least one field field group.
         |
| [CreateQuadTrees](./CreateQuadTrees.html) | Create Quadtrees | 
          
            Quadtree generation is controlled by specifying Maximum Vertices and/or Maximum depth:
            
               |
| [EnableLRSUPDM](./EnableLRSUPDM.html) | Enable APR on UPDM | 
          Creates the script to enable LRS or enables LRS on a UPDM database with a utility network.
         |
| [EvaluateRulesByPolygon](./EvaluateRulesByPolygon.html) | Evaluate Rules by Polygon | 
          When there is an active map, the Output Class will be added to the map during execution so progress can be monitored.
         |
| [ExportReportingData](./ExportReportingData.html) | Export Reporting Data | 
          
            - For optimal read performance, a database connection is recommended.
            - For optimal write performance, a mobile geodatabase (sqlite) is recommended for the Output Geodatabase.
            - File geodatabases only support a subset of views.
            - If you specify the utility network controller dataset, association and controller views will only be created to the input datasets if the target dataset name matches the class name in the source utility network.
            - You can target the same target dataset with multiple Input Datasets. This allows you to specify the layers with definition queries or subtype group layers for the Input Datasets and load their records to a single target dataset.
            - If the length of the view name exceeds the table name limit, the subtype description will be replaced with its code.
          
         |
| [ExportUtilityNetworkMatrix](./ExportUtilityNetworkMatrix.html) | Export Matrix | 
          
            Use this tool along with ImportUtilityNetworkMatrix to modify properties in bulk.
            For additional information, see the help page on GitHub.
          
         |
| [ExtractFileLogs](./ExtractFileLogs.html) | Extract Logs from Files | 
          
            A series of views are created on top of the log table to look at log entries for particular operations.
            This tool processes log files generated from either ArcGIS Server or ArcGIS Pro.
            For ArcGIS Pro Diagnostic Log files, refer to this technical article.
          
         |
| [ExtractRESTLogs](./ExtractRESTLogs.html) | Extract Logs from REST | 
          
            By default, all logs are extracted. This can be a time intensive process, so consider filtering by time and/or service name.
            When you have access to the directory with the ArcGIS Server logs, it is typically faster to use ExtractFileLogs.
          
         |
| [FilterMap](./FilterMap.html) | Modify Map by Rename and Configure | 
          Applies rename and configuration options to maps based on an asset package.
         |
| [ImportUtilityNetworkMatrix](./ImportUtilityNetworkMatrix.html) | Import Matrix | 
          
            Use this tool along with ExportUtilityNetworkMatrix to modify properties in bulk.
            Rules removed from the worksheet are not removed from the utility network.
            New network categories can be added by adding a new column. Assignments can be removed by deleting 1 from the cell.
            Changing existing terminal assignments are not supported, only setting a terminal configuration from the default of single terminal.
            For additional information, see the help page on GitHub.
          
         |
| [MapLayersToCSV](./MapLayersToCSV.html) | Map Layers to CSV |  |
| [SubnetworkAggregator](./SubnetworkAggregator.html) | Subnetwork Aggregator | 
          Generate output geometry and summary information for the subnetworks in an utility network.  This can be used to generate partial geometry on subnetworks with error features
         |
| [SummarizeUNErrors](./SummarizeUNErrors.html) | Summarize Utility Network Errors | 
          
            For best performance, run this tool with a client-server database connection.
            The Utility Network must be at least Schema Version 4 to extract dirty areas.
            The output geodatabase has a series of tables:
            
               |
| [SummaryByBits](./SummaryByBits.html) | Summary by Bits | 
          The output table containing summary information will have chart(s) associated with it.
         |
| [SwapBits](./SwapBits.html) | Swap Bits | 
          This is used for a phase swap.
         |
| [Trace2Config](./Trace2Config.html) | Trace to Trace Configurations | 
          
            To capture the python code, configure a Utility Network trace and copy the python command.
            If the name of the trace configuration already exists, a number will be appended for uniqueness.
          
         |
| [ValidateByPolygon](./ValidateByPolygon.html) | Validate by Polygon | 
          When there is an active map, the Output Class will be added to the map during execution so progress can be monitored.
         |

`Last built 2023-11-28`
