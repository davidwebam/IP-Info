# ===========================================
#     ________     _____   ____________ 	|
#    /  _/ __ \   /  _/ | / / ____/ __ \	|
#    / // /_/ /   / //  |/ / /_  / / / /	|
#  _/ // ____/  _/ // /|  / __/ / /_/ / 	|
# /___/_/      /___/_/ |_/_/    \____/  	|
# 											|
# 											|
# 				   Owner					|
#			  David_Voskanyan				|
# 											|
# ===========================================

# Imports
import requests
from pyfiglet import Figlet

# Preview
preview_text = Figlet(font="slant")
print(preview_text.renderText("IP INFO"))

# Get IP Adress for use 0.0.0.0 or 127.0.0.1
response = requests.get('https://api.ipify.org?format=json')
data = response.json()
external_ip = data['ip']

# Get IP info using IPData
def get_ip_ipdate():
    try:
        print("Use 127.0.0.1 or 0.0.0.0 to find your IP")

        # API Key for IPData
        api_key = input("IP Address: ")
        ip_address = input("IP Address: ")

        # User IP
        if ip_address == "127.0.0.1" or ip_address == "0.0.0.0":
            ip_address = external_ip

        # Response to get info
        response = requests.get(f"https://api.ipdata.co/{ip_address}?api-key={api_key}")

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Get ASN info safely
            asn_info = data.get('asn', {})

            # Get THREAT info safely
            threat_info = data.get('threat', {})

            # Main Info
            info = {
                "[IP]": data.get('ip'),
                "[Europe]": data.get('is_eu'),
                "[City]": data.get('city'),
                "[Region]": data.get('region'),
                "[Country_Code]": data.get('country_code'),
                "[Continent_Name]": data.get('continent_name'),
                "[Continent_Code]": data.get('continent_code'),
                "[Latitude]": data.get('latitude'),
                "[Longitude]": data.get('longitude'),
                "[Postal]": data.get('postal'),
                "[Calling_code]": data.get('calling_code'),
                "[Flag]": data.get('emoji_flag'),
                "[Unicode]": data.get('emoji_unicode'),
                "[ASN]": asn_info.get('asn'),
                "[Name]": asn_info.get('name'),
                "[Domain]": asn_info.get('domain'),
                "[Route]": asn_info.get('route'),
                "[Type]": asn_info.get('type'),
                "[IS_Tor]": threat_info.get('is_tor'),
                "[IS_Icloud_Relay]": threat_info.get('is_icloud_relay'),
                "[IS_Proxy]": threat_info.get('is_proxy'),
                "[IS_Datacenter]": threat_info.get('is_datacenter'),
                "[IS_Anonymous]": threat_info.get('is_anonymous'),
                "[IS_Known_Abuser]": threat_info.get('is_known_abuser'),
                "[IS_Threat]": threat_info.get('is_threat'),
                "[IS_Bogon]": threat_info.get('is_bogon'),
            }

            # Print Info
            for k, v in info.items():
                print(f'{k} : {v}')
        else:
            print(f"[!] Error: Received status code {response.status_code} from the API.")

    except requests.exceptions.ConnectionError:
        print("[!] Connection Error")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

# Start
get_ip_ipdate()
