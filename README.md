# HIS_AWS_Blockchain
Implementing a health information system of a hospital on the blockchain on AWS.


Install the necessary Python packages for working with blockchain and AWS. You can do this by running the following commands:

```python
pip install blockchain
pip install boto3

```
Import the necessary modules for working with blockchain and AWS in your Python script. You can do this by adding the following lines of code at the beginning of your script:

```python
import blockchain
import boto3

```
Connect to the AWS blockchain service by creating an instance of the boto3 client and providing your AWS access key and secret key. You can do this by adding the following lines of code to your script:
```python
client = boto3.client('blockchain',
                      aws_access_key_id='YOUR_ACCESS_KEY',
                      aws_secret_access_key='YOUR_SECRET_KEY')

```
Create a blockchain network on AWS by calling the **create_network** method of the client object and providing the necessary parameters such as the ***network name***, **edition**, and **framework**. You can do this by adding the following lines of code to your script:

```python
response = client.create_network(
    Name='my-blockchain-network',
    Edition='STANDARD',
    Framework='HYPERLEDGER_FABRIC',
    Description='My blockchain network for a hospital health information system',
    FrameworkVersion='1.4.8',
    VotingPolicy={
        'ApprovalThresholdPolicy': {
            'ThresholdPercentage': 50,
            'ProposalDurationInHours': 24
        }
    },
    MemberConfiguration={
        'Name': 'HospitalMember',
        'Description': 'A member for the hospital health information system',
        'FrameworkConfiguration': {
            'Fabric': {
                'AdminUsername': 'admin',
                'AdminPassword': 'adminpw'
            }
        }
    }
)

```
Create a blockchain network member on AWS by calling the **create_member** method of the client object and providing the necessary parameters such as the **network id**, ***member name***, and **role**. You can do this by adding the following lines of code to your script:

```python
response = client.create_member(
    NetworkId='my-blockchain-network-id',
    MemberName='my-blockchain-network-member',
    Role='NETWORK_MEMBER',
    Description='A member of my blockchain network for the hospital health information system'
)

```
Create a blockchain network invitation on AWS by calling the **create_invitation** method of the client object and providing the necessary parameters such as the **network id**, **member id**, and **role**. You can do this by adding the following lines of code to your script:

```python
response = client.create_invitation(
    NetworkId='my-blockchain-network-id',
    MemberId='my-blockchain-network-member-id',
    Role='NETWORK_MEMBER'
)

```
Accept the blockchain network invitation on AWS by calling the accept_invitation method of the client object and providing the necessary parameters such as the invitation id and network id.
```python
response = client.accept_invitation(
    NetworkId='my-blockchain-network-id',
    InvitationId='my-blockchain-network-invitation-id',
)
```
