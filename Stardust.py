import json

import requests
import random
import string
import urllib.parse

api_key = None
if api_key is None:
    print("Pl. set the api key")
    exit()
external_wallet_address = "0x1196E3EC27323828d3dd638Fc0de3f78452D1bDD"
api_counter = 1

print(api_counter, '.Check Health API')
url = "https://core-api.stardust.gg/v1/health"

headers = {"accept": "application/json"}
print("URL", url)
print("Method: GET")
print("Headers:")
print(json.dumps(headers, indent=4))
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get Game API')
url = "https://core-api.stardust.gg/v1/game/get"
print("URL", url)
print("Method: GET")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, "A.Create Player ")
url = "https://core-api.stardust.gg/v1/player/create"
print("Method :Post")
print("URL", url)
player_name = "falcon_" + ''.join(random.choices(string.ascii_letters, k=3))
payload = {
    "uniqueId": player_name,
    "userData": {
        "level": 3,
        "username": player_name,
        "premium": False
    },
    "image": "https://pixabay.com/images/id-7713508/"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print("Comments: User_data parameters in Payload can be customized")
print(
    "In place of level,username etc any number(>=0) of other parameters can be defined in string ,integer and boolean "
    "data type.")
print("playerId parameter in response has to be stored for subsequent API calls ")

playerId1 = response.json()['playerId']

print('\n')
print("--------------------------------------------------------------------------------------")
print(api_counter, "B.Create 2nd Player ")
url = "https://core-api.stardust.gg/v1/player/create"
print("Method :Post")
print("URL", url)
player_name = "falcon_" + ''.join(random.choices(string.ascii_letters, k=3))
payload = {
    "uniqueId": player_name,
    "userData": {
        "level": 3,
        "Email": player_name + "@gmail.com",
        "Experience": 500
    },
    "image": "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
playerId2 = response.json()['playerId']

print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
playerId2 = response.json()['playerId']

print('\n')
print("--------------------------------------------------------------------------------------")
print(api_counter, "C.Create 3rd Player ")
url = "https://core-api.stardust.gg/v1/player/create"
print("Method :Post")
print("URL", url)
player_name = "falcon_" + ''.join(random.choices(string.ascii_letters, k=3))
payload = {
    "uniqueId": player_name,
    "userData": {
        "Game_level": 3,
        "Email": player_name + "@gmail.com",
    },
    "image": "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
playerId3 = response.json()['playerId']

print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get Player Id by unique_id(player_name)')
url = "https://core-api.stardust.gg/v1/player/get-id?uniqueId=" + player_name
print("Method: Get")
print("URL", url)
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

playerId_ = response.json()['playerId']

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get Player details by playerId')
url = "https://core-api.stardust.gg/v1/player/get?playerId=" + playerId1
print("URL", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")

print(api_counter, ".Get All Player Ids")
url = "https://core-api.stardust.gg/v1/player/get-ids"
print("URL: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Mutate Player')

url = "https://core-api.stardust.gg/v1/player/mutate"
print("URl ", url)
print("Method: Put")

payload = {
    "playerId": playerId1,
    "props": {
        "exp": 1200,
        "premium": True
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("Comments:Existing Parameter (premium) will be updated , new parameter(exp) will be added")

print('\n')
print("--------------------------------------------------------------------------------------")
print('Get Player details after mutating player')
url = "https://core-api.stardust.gg/v1/player/get?playerId=" + playerId1
print("URL", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Remove player property")
property_to_removed = '["exp","premium"]'
url_encoded_property_to_be_removed = urllib.parse.quote(property_to_removed)

url = "https://core-api.stardust.gg/v1/player/props-remove?playerId=" + playerId1 + "&props=" + url_encoded_property_to_be_removed
print("URL: ", url)
print("Method: delete")
print("Note: props in url is ASCII encoded value of the array -", property_to_removed,
      "containing properties to be removed")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.delete(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
print('Get Player details after removing player property')
url = "https://core-api.stardust.gg/v1/player/get?playerId=" + playerId1
print("URL", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, 'A.Get Player 1 Wallet')

url = "https://core-api.stardust.gg/v1/player/wallet-get?playerId=" + playerId1
print("Url: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
player1_wallet_address = response.json()["wallet"][0]["address"]

print('\n')
print("--------------------------------------------------------------------------------------")
print(api_counter, 'B.Get Player 2 Wallet')

url = "https://core-api.stardust.gg/v1/player/wallet-get?playerId=" + playerId1
print("Url: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
player2_wallet_address = response.json()["wallet"][0]["address"]

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get Player Count')
url = "https://core-api.stardust.gg/v1/player/count"
print("URL: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
count = response.json()['count']

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Get All Player details")
url = "https://core-api.stardust.gg/v1/player/get-all?start=0&limit=" + str(count)
print("Url: ", url)
print("Method: Get")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print("\n")
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Remove a player")
url = "https://core-api.stardust.gg/v1/player/remove?playerId=" + playerId3
print("Url: ", url)
print("Method: delete")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.delete(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Create NFT Token Template")
url = "https://core-api.stardust.gg/v1/template/create"
print("Url: ", url)
print("Method :Post")

template_name = "AK_47_" + ''.join(random.choices(string.ascii_letters, k=3))

payload = {
    "name": template_name,
    "cap": "10000",
    "type": "NFT",
    "props": {
        "immutable": {"itemType": "oneHandedWeapon"},
        "mutable": {"description": "Nice Gun.", "Fire distance": "100 metre"}
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
nft_template_id = response.json()['id']
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Payload Explaination:type can be NFT or FT.")
print("\nProperties defined under props are inherited by tokens minted.")
print(
    "\nImmutable properties cannot be modified after creation of a template.More number of immutable properties can also defined(>=0).Here only 1 property(ItemType) has been defined ")
print(
    "\nMutable properties can be changed even after template creation.More number of mutable properties can be defined(>=0).It  is better to keep the description property as it is,because there is a specific parameter named description for a template which defaults to no description if the parameter description is omitted or spelling is changed")
print("\nIf mutable properties of a template are changed after minting any token, inherited properties of tokens will "
      "also be updated.")
print("\nIf same parameter is provided in mutable and immutable block , mutable parameter will not be inherited in "
      "minted tokens")

print('\n')
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("In response template id is generated which will be used to mint token")

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get Template details by template Id')

url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(nft_template_id)
print("url: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

# Creating Another template
template_name = "AR_15" + ''.join(random.choices(string.ascii_letters, k=3))
payload = {
    "name": template_name,
    "cap": "10000",
    "type": "NFT",
    "props": {
        "immutable": {"itemType": "oneHandedWeapon2"},
        "mutable": {"description": "Nice Gun.", "Fire distance": "200 metre"}
    }
}
url = "https://core-api.stardust.gg/v1/template/create"
response = requests.post(url, json=payload, headers=headers)
nft_template_id2 = response.json()['id']

template_name = "Krig6_" + ''.join(random.choices(string.ascii_letters, k=3))
payload = {
    "name": template_name,
    "cap": "10000",
    "type": "NFT",
    "props": {
        "immutable": {"itemType": "oneHandedWeapon3"},
        "mutable": {"description": "Nice Gun.", "Fire distance": "500 metre"}
    }
}
url = "https://core-api.stardust.gg/v1/template/create"
response = requests.post(url, json=payload, headers=headers)
nft_template_id3 = response.json()['id']

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, 'A.Mutate Template')

url = "https://core-api.stardust.gg/v1/template/mutate"
print("Url :", url)
print("Method: Put")

payload = {
    "templateId": nft_template_id,
    "props": {
        "durability": 10,
        "faction": "legion",
        "Fire distance": "300 metre"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Comments on Payload:Updates existing mutable property and adds new mutable property.")
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
print('Getting the updated Template details')
url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(nft_template_id)
print("Calling API: ", url)
response = requests.get(url, headers=headers)
print("\nUpdated template details")
print(json.dumps(response.json(), indent=4))
print(
    "Note:New mutable property durability and faction has been added ,existing mutable property Fire distance has been updated , ")

print('\n')
print("--------------------------------------------------------------------------------------")
print(api_counter, 'B.Mutate Template: Example 2: trying to update immutable property')

url = "https://core-api.stardust.gg/v1/template/mutate"
print("Url :", url)
print("Method: Put")

payload = {
    "templateId": nft_template_id2,
    "props": {
        "durability": 10,
        "faction": "legion",
        "Fire distance": "400 metre",
        "itemType": "One handed long distance weapon"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print(
    "Existing immutable property (itemType) is attempted to be updated , a new mutable property with same name will be created, but this is not inherited in minted tokens.Only the immutable property is inherited")
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
print('Getting the updated Template details')
url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(nft_template_id2)
print("Calling API: ", url)
response = requests.get(url, headers=headers)
print("\nUpdated template details")
print(json.dumps(response.json(), indent=4))
print(
    "Note:New mutable property durability and faction and itemType has been added ,existing immutable property itemType is unchanged ,existing mutable property Fire distance has been updated , ")
print(
    "itemType is defined both in mutable section and immutable section.The one in immutable section will be inherited in minted token")
print('\n')
print("--------------------------------------------------------------------------------------")
print("Create FT Token Template")
url = "https://core-api.stardust.gg/v1/template/create"
print("Url: ", url)
print("Method :Post")

template_name = "Gold_Coin_" + ''.join(random.choices(string.ascii_letters, k=3))

payload = {
    "name": template_name,
    "cap": "10000",
    "type": "FT",
    "props": {
        "immutable": {"itemType": "Gold_Coin"},
        "mutable": {"description": "Gold Coin", "Usage": "Rejuvination"}
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
ft_template_id = response.json()['id']
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
print('Get FT Template details')

url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(ft_template_id)
print("url: ", url)

response = requests.get(url, headers=headers)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Remove template property")
property_to_removed = '["durability", "faction","itemType"]'
url_encoded_property_to_be_removed = urllib.parse.quote(property_to_removed)
url = "https://core-api.stardust.gg/v1/template/props-remove?templateId=" + str(
    nft_template_id) + "&props=" + url_encoded_property_to_be_removed
print("Url: ", url)
print("Method: delete")
print("\nNote: props in url is ASCII encoded value of the array -", property_to_removed,
      "containing properties to be removed")
print("\nImmutable property(itemtype) cannot be removed even if requested")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.delete(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
print('Getting the updated Template details')
url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(nft_template_id)
print("Calling API: ", url)
response = requests.get(url, headers=headers)
print("Updated template details")
print(json.dumps(response.json(), indent=4))

print("\n")
print("--------------------------------------------------------------------------------------")
api_counter = api_counter + 1
print(api_counter, ".Get Template count")
url = 'https://core-api.stardust.gg/v1/template/count'
print("URl: ", url)
print("Method: Get")
# print("Note:filter in url Filters out templates who's name does not contain the string as a substring")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
template_count = response.json()['count']

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Get All templates')
url = "https://core-api.stardust.gg/v1/template/get-all?start=0&limit=" + str(template_count)
print("URL: ", url)
print("Method: Get")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Mint Token for a player")
url = "https://core-api.stardust.gg/v1/token/mint-bulk"
print("Method: Post")

payload = {
    "tokenObjects": [
        {

            "templateId": nft_template_id,
            "amount": "1",
            "props": {
                "immutable": {"Manufacturer": "LockHead_Martin"},
                "mutable": {"date": "12.08.2022",
                            "Condition": "Excellent"}
            },

        },
        {

            "templateId": nft_template_id,
            "amount": "1",
            "props": {
                "immutable": {"Manufacturer": "LockHead_Martin"},
                "mutable": {
                    "date": "12.08.2022",
                    "Condition": "Damaged",
                    "Advise": "Discard"
                }
            },

        },

        {
            "templateId": ft_template_id,
            "amount": "8"
        },
        {

            "templateId": nft_template_id3,
            "amount": "1",
            "props": {
                "immutable": {"Manufacturer": "LockHead_Martin",
                              "Kill_Ability": "None"},
                "mutable": {
                    "date": "12.08.2022",
                    "Condition": "Damaged",
                    "Advise": "Discard"
                }
            },

        },
    ],
    "playerId": playerId1
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("PayLoad Explaination:")
print(
    "Every NFT is unique,Whenever working with minting, burning, transferring, or trading NFTs, amounts must always be equal to 1.")
print(
    "\nFor example, if you mint 5 NFTs with templateId 123, then the tokenObjects array needs to contain 5 tokens each with an amount set to 1")
print("\nFor a NFT,props block is optional , but should be supplied to differentiate between NFTs.")
print(
    "\nFor NFTs, the template allows for all tokens of a certain template to have some degree of shared commonality. Each individual NFT can have additional specifics defined in props block of the payload of mint api .")
print(
    "\nFor Example,Two pieces of weapons as NFTs could have identical stats(inherited from the template), but one could be in better condition than the other. They share the same base layer , but they each hold specific traits to themselves .")
print(
    "\nFor FT , props block must be omitted,as FTs are identical and not unique,FTs inherit properties only from template.No additional properties can be provided.")
print("\nMore than 1 FT can be minted in a single block , unlike NFTs")
print("\nToken Id for all the FT tokens minted for a player based on a template is same. ")
print('\n')
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("Response contains token ids")
token_ids = response.json()
print("Note: ", token_ids[0], token_ids[1], token_ids[3], "are the token ids for the NFT tokens")
print(token_ids[2], " is token id for the 8 FT tokens")

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Get all tokens minted from a token template")
url = "https://core-api.stardust.gg/v1/template/get-tokens?templateId=" + str(ft_template_id) + "&start=0&limit=10"
print("Url: ", url)
print("Method: Get")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))


print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")

print(api_counter, '.Get Token details')
token_id_array_encoded = urllib.parse.quote(str(token_ids))
url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded
print("\nTokenIds in url is ASCII encoded value of the array containing token ids", token_ids)
print("\nUrl: ", url)
print("Method: Get")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("\n")
print("--------------------------------------------------------------------------------------")

print(
    "Mint Token for a player:Example 2:if same property(itemType) appears in immutable and mutable section of token "
    "template , only the immutable property will be inherited")

print("Getting Token template details:")
url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(nft_template_id2)
print("\nCalling API: ", url)
response = requests.get(url, headers=headers)
print("Template Details:")
print(json.dumps(response.json(), indent=4))
print('\n')
print("Now Minting Token")
url = "https://core-api.stardust.gg/v1/token/mint-bulk"
print("Calling API :", url)

payload = {
    "tokenObjects": [
        {

            "templateId": nft_template_id2,
            "amount": "1",
            "props": {
                "immutable": {"Creator": "Darpa"},
                "mutable": {"date": "12.08.2022"}
            },

        }

    ],
    "playerId": playerId1
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}
print("Payload:")
print(json.dumps(payload, indent=4))

response = requests.post(url, json=payload, headers=headers)

token_id = response.json()

print('\n')

print('Get Token details:')
token_id_array_encoded = urllib.parse.quote(str(token_id))
url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded
print("Calling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}
print("\nToken Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, "Mutate NFT token.")
url = "https://core-api.stardust.gg/v1/token/mutate"
print("Url:", url)
print("Method: Put")
print(
    "\nTo mutate FT token , use mutate template which will update the inherited properties of all minted FT tokens based on the template")
payload = {
    "tokenId": token_ids[0],
    "props": {
        "durability": 10,
        "faction": "legion"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))

print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Remove Token Property")
property_to_removed = '["faction","durability"]'
property_to_removed_encoded = urllib.parse.quote(property_to_removed)

url = "https://core-api.stardust.gg/v1/token/props-remove?tokenId=" + str(
    token_ids[0]) + "&props=" + property_to_removed_encoded
print("Url: ", url)
print("Method: Delete")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.delete(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')

print('Get updated Token details')
token_id_array_encoded = urllib.parse.quote(str([token_ids[0]]))
url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded

print("Calling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Updated Token Details:")
print(json.dumps(response.json(), indent=4))

print("\n")
print("--------------------------------------------------------------------------------------")

print("Mutate NFT token.Example 2: Trying to update immutable property of token\n")

print('Displaying Token details before updating:')
token_id_array_encoded = urllib.parse.quote(str([token_ids[3]]))

url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded

print("Calling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}
print("\nToken Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

print('\n')

print("Mutating token")
url = "https://core-api.stardust.gg/v1/token/mutate"
print("\n Calling API", url)
payload = {
    "tokenId": token_ids[3],
    "props": {
        "durability": 10,
        "faction": "legion",
        "Kill_Ability": "Minor Injury"
    }

}
print("Payload :")
print(json.dumps(payload, indent=4))

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)

print('Displaying Updated Token details:')
token_id_array_encoded = urllib.parse.quote(str([token_ids[3]]))

url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded

print("\nCalling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}
print("Token Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))
print("Trying to mutate immutable property('Kill_Ability') of token will create a new mutable property with same name")


print("\n")
print("--------------------------------------------------------------------------------------")
print("Mutating Template from which token has been already minted")
print('\n')
print("Displaying Token details before mutating template\n")
token_id_array_encoded = urllib.parse.quote(str([token_ids[2]]))

url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded

print("Calling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}
print("\nToken Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

print('\n')

print("Now Mutating Token template")
url = "https://core-api.stardust.gg/v1/template/mutate"
print("Url :", url)
print("\nMethod: Put")

payload = {
    "templateId": ft_template_id,
    "props": {
        "Usage": "boost speed",
        "Value": "1 Gold Coin = 500 Alpha"
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.put(url, json=payload, headers=headers)
print("Payload:")
print(json.dumps(payload, indent=4))

print("Getting updated token template details:")
url = "https://core-api.stardust.gg/v1/template/get?templateId=" + str(ft_template_id)
print("Calling API: ", url)
print("\nTemplate Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))
print('\n')

print("Now displaying token details to show change in template is reflected in tokens minted before changing template ")
print(
    "\nUpdating FT token template is the only way of mutating FT tokens,because all FTs based on a template must have the same properties.Mutating individual FTs is not allowed. ")
print(
    "\nBut individual NFT tokens can be mutated or all NFT token based on a template can be mutated in bulk by updating the template itself")

token_id_array_encoded = urllib.parse.quote(str([token_ids[2]]))
url = "https://core-api.stardust.gg/v1/token/get?tokenIds=" + token_id_array_encoded

print("Calling API: ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}
print("\nToken Details:")
response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

print('\n')
print("--------------------------------------------------------------------------------------")
api_counter = api_counter + 1
print(api_counter, ".Get Player Inventory")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("url: ", url)
print("Method: Get")
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Burn Token')
url = "https://core-api.stardust.gg/v1/token/burn"
print("URl: ", url)
print("Method : Post")

payload = {
    "tokenObjects": [
        {
            "tokenId": token_ids[1],
            "amount": "1"
        }
    ],
    "playerId": playerId1
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("Tokens are sent to null address to burn them")

print("\nDisplaying Player Inventory after burning")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer Inventory:")
print(json.dumps(response.json(), indent=4))

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, ".Transfer Token from player1 to player2")

print("\nDisplaying Player1 Inventory before Transfer")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer1 Inventory:")
print(json.dumps(response.json(), indent=4))

print("\nDisplaying Player2 Inventory before Transfer")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId2
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer2 Inventory:")
print(json.dumps(response.json(), indent=4))

print("\nNow Transferring tokens from player1 to player2")
url = "https://core-api.stardust.gg/v1/token/transfer"
print("URl: ", url)
print("Method : Post")

payload = {
    "tokenObjects": [
        {
            "tokenId": token_ids[2],
            "amount": "5"
        },
        {
            "tokenId": token_ids[0],
            "amount": "1"
        }
    ],
    "fromPlayerId": playerId1,
    "toPlayerId": playerId2
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)

print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print(
    "Payload Explaination:Amount for NFT token id must be 1 ,while for FT token id can be more than 1 if available "
    "with the player")
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print("\nDisplaying Player1 Inventory after Transfer")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer1 Inventory:")
print(json.dumps(response.json(), indent=4))

print("\nDisplaying Player2 Inventory after Transfer")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId2
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer Inventory:")
print(json.dumps(response.json(), indent=4))

print("\n")
print("--------------------------------------------------------------------------------------")
api_counter = api_counter + 1
print(api_counter, ".Remove Template")
# Creating Template
url = "https://core-api.stardust.gg/v1/template/create"

payload = {
    "name": "to_be_removed",
    "cap": "10000",
    "type": "NFT",
    "props": {
        "immutable": {"itemType": "Nil"},
        "mutable": {"description": "Nil"}
    }
}

response = requests.post(url, json=payload, headers=headers)
temp_id = response.json()['id']

url = "https://core-api.stardust.gg/v1/template/remove?templateId=" + str(temp_id)
print("Url : ", url)
print("Method: delete")

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.delete(url, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))
print("Templates from which tokens are minted cannot be removed without burning the tokens")

print('\n')
api_counter = api_counter + 1
print("--------------------------------------------------------------------------------------")
print(api_counter, '.Withdraw tokens from stardust wallet to external wallet')
print("\nDisplaying Player Inventory before withdrawing")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer Inventory:")
print(json.dumps(response.json(), indent=4))

print("\n Now withdrawing tokens from stardust wallet to external wallet")

url = "https://core-api.stardust.gg/v1/player/withdraw"
print("Url: ", url)
print("Method: Post")

payload = {
    "address": external_wallet_address,
    "playerId": playerId1,
    "tokenObjects": [
        {
            "tokenId": token_ids[2],
            "amount": "2"
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": api_key
}

response = requests.post(url, json=payload, headers=headers)
print("Headers:")
print(json.dumps(headers, indent=4))
print("Payload:")
print(json.dumps(payload, indent=4))
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=4))

print("\nDisplaying Player Inventory after withdrawing")
url = "https://core-api.stardust.gg/v1/player/get-inventory?playerId=" + playerId1
print("Calling API ", url)

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

response = requests.get(url, headers=headers)
print("\nPlayer Inventory:")
print(json.dumps(response.json(), indent=4))
