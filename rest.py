import requests

def consulta():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/')
    print(r.status_code)
    print(r.json())
    for posts in r.json():
        print(posts['userId'], posts['id'], posts['title'], posts['body'])

def insere():
    title = 'Testando service rest'
    body = 'Testando corpo service rest'
    posts = {"title": title, "body": body}
    r = requests.post('https://jsonplaceholder.typicode.com/posts/', json=posts)
    print(r.status_code)
    print(r.json())        

    consulta()