import requests, json, hashlib

class Cypher():

    def __init__(self, get_url, post_url, filename):
        self.text = None
        self.data = None
        self.filename = filename
        self.get_url = get_url
        self.post_url = post_url
        self.phrase = 'abcdefghijklmnopqrstuvwxyz'
        self.request = requests.get(self.get_url)
        with open(self.filename, 'w') as f:
            json.dump(self.request.json(), f)
    
    def decrypt(self):
        '''
        This function gets the data and deciphers it
        '''
        with open(self.filename, 'r') as f:
            self.data = json.load(f)
            for key in range(len(self.phrase)):   
                deciphered = ''
                for symbol in self.data['cifrado']:
                    if symbol in [' ', '.', ',', '!', '?']:
                        deciphered = deciphered + symbol
                    elif symbol in self.phrase:
                        index_letter = self.phrase.find(symbol) + 1
                        position = index_letter - self.data['numero_casas']
                        if position < 0:
                            new_index_letter = len(self.phrase) + position
                            deciphered = deciphered + self.phrase[new_index_letter - 1]
                        else:
                            deciphered = deciphered + self.phrase[position - 1]
                    else:
                        deciphered = deciphered + symbol
            self.text = deciphered
        return self.text
    
    def update(self):
        '''
        this function updates the file with encrypted data
        '''
        with open(self.filename, 'w') as f:
            self.data['decifrado'] = self.text
            self.data['resumo_criptografico'] = hashlib.sha1(self.text.encode('utf-8')).hexdigest()
            json.dump(self.data, f)
        with open(self.filename, 'r') as f:
            response = requests.post(self.post_url, files={'answer':f})
            print(response.status_code)
        