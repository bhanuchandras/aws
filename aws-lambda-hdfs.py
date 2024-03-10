import pyarrow.hdfs as hdfs

def lambda_handler(event, context):
    # Specify the HDFS namenode host and port
    namenode_host = 'namenode_hostname'
    namenode_port = 8020  # Default port
    
    # Specify the path to the keytab file and principal
    keytab_path = '/path/to/your/keytab.keytab'
    principal = 'your_service_principal@REALM'
    
    # Initialize PyArrow HDFS client with keytab authentication
    hdfs_client = hdfs.connect(host=namenode_host, port=namenode_port,
                               user=principal, kerb_ticket=keytab_path)
    
    # Specify the HDFS path
    hdfs_path = '/your/hdfs/path'
    
    # List files in the specified HDFS path
    file_list = hdfs_client.ls(hdfs_path)
    
    # Return the list of files
    return {
        'statusCode': 200,
        'body': file_list
    }
