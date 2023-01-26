import openai

openai.api_key = "SUA API"

conversa = ""

questao = ''

while (questao!='EXIT'):
    if questao != 'EXIT':
        questao = input("Voce: ")
        conversa += f'Você: {questao} \nAI:'
        resposta = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversa,
            temperature=0.9,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        resp = resposta.choices[0].text.strip()
        conversa += resp
        print(f'AI: {resp} \n')
        print(f'Digite EXIT para encerrar a aplicação.')
    else:
        print(f'Até mais!')
        break


