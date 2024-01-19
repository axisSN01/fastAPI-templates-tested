import requests
import argparse
import json
import pdb
### requests SAMPLE 
#python .\Requests-tester.py -type GET -url http://127.0.0.1:8000/instagram/post/ -headers '[{"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiJBbGV4aXNAZXhhbXBsZS5jb20iLCJleHBpcmVzIjoxMDcwNTY2NDU3Ny44MjEwNzd9.L42XYDySmgGwIVYmaVCRzrXLSfzlRK6gMFwndz9zuEY"}, {"Accept":"application/json"}]'

def list_of_dicts_to_headers(list_of_dicts):
    headers = {}
    for header_dict in list_of_dicts:
        headers.update(header_dict)
    return headers


def make_get_request(url, headers):
    if headers:
        headers = list_of_dicts_to_headers(headers)
    
    response = requests.get(url, headers=headers)
    return response

def make_post_request(url, headers, body):
    headers = list_of_dicts_to_headers(headers)
    response = requests.post(url, headers=headers, json=body)
    return response

def main():
    parser = argparse.ArgumentParser(description="Script para hacer solicitudes HTTP (GET/POST)")
    parser.add_argument("-type", choices=["GET", "POST"], help="Tipo de solicitud HTTP (GET o POST)", required=True)
    parser.add_argument("-url", help="URL de la solicitud", required=True)
    parser.add_argument("-headers", help="Encabezados de la solicitud en formato JSON", type=json.loads)
    parser.add_argument("-body", help="Cuerpo de la solicitud en formato JSON", type=json.loads)

    args = parser.parse_args()

    if args.type == "GET":
        response = make_get_request(args.url, args.headers)
    elif args.type == "POST":
        response = make_post_request(args.url, args.headers, args.body)
    else:
        print("Tipo de solicitud no válido. Use 'GET' o 'POST'.")
        return

    print("Respuesta:")
    print("Status Code:", response.status_code)
    print("Contenido:", response.text)

if __name__ == "__main__":
    main()
