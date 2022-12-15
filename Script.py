# Import required libraries
import boto3
import json
# Set the blockchain network identifier and chain code name
network_id = "my-health-info-network"
chain_code_name = "my-health-info-chaincode"
# Set the Amazon Managed Blockchain client and the Fabric SDK
mbc = boto3.client('managedblockchain')
fabric = boto3.client('fabric-sdk-node')
# Set the Fabric user and channel names
user_name = "Admin"
channel_name = "health-info-channel"
# Set the Fabric invoke and query functions
invoke = fabric.invoke
query = fabric.query
# Set the initial state of the blockchain
state = {
    "Patients": [
        {
            "id": 1,
            "name": "John Doe",
            "dob": "2000-01-01",
            "medical_history": []
        }
    ],
    "Doctors": [
        {
            "id": 1,
            "name": "Dr. Smith",
            "specialty": "Cardiology"
        }
    ]
}
# Set the initial payload for the blockchain
payload = json.dumps(state)
# Invoke the chaincode to set the initial state of the blockchain
invoke_response = invoke(
    NetworkId=network_id,
    ChaincodeName=chain_code_name,
    ChaincodeFunction="init",
    ChaincodeArguments=[payload],
    InvokerUserName=user_name,
    ChannelName=channel_name
)
# Query the blockchain to verify the initial state
query_response = query(
    NetworkId=network_id,
    ChaincodeName=chain_code_name,
    ChaincodeFunction="query",
    ChaincodeArguments=[""],
    InvokerUserName=user_name,
    ChannelName=channel_name
)
# Print the initial state of the blockchain
print(json.loads(query_response["Payload"]["toString"]))
# Add a new patient to the blockchain
new_patient = {
    "id": 2,
    "name": "Jane Smith",
    "dob": "1990-05-01",
    "medical_history": []
}
payload = json.dumps(new_patient)
invoke_response = invoke(
    NetworkId=network_id,
    ChaincodeName=chain_code_name,
    ChaincodeFunction="addPatient",
    ChaincodeArguments=[payload],
    InvokerUserName=user_name,
    ChannelName=channel_name
)
# Query the blockchain to verify the new patient
query_response = query(
    NetworkId=network_id,
    ChaincodeName=chain_code_name,
    ChaincodeFunction="query",
    ChaincodeArguments=[""],
    InvokerUserName=user_name,
    ChannelName=channel_name
)
# Print the updated state of the blockchain
print(json.loads(query_response["Payload"]["toString"]))
