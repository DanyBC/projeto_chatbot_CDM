from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Rota para verificar se o Flask está rodando (opcional)
@app.route("/", methods=["GET"])
def home():
    return "Hello, Flask with ngrok!"

# Rota para o webhook do Twilio (essa é a rota para receber as mensagens do WhatsApp)
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Pega a mensagem recebida pelo WhatsApp
    incoming_msg = request.values.get("Body", "").strip()

    # Cria uma resposta para o Twilio
    resp = MessagingResponse()
    msg = resp.message()

    # Boas-vindas e opções iniciais
    if incoming_msg.lower() in ['oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']:
        msg.body("Olá! Seja bem-vindo(a) ao nosso atendimento. Por favor, escolha uma das opções abaixo:\n\n"
            "1 - Assinatura\n"
            "2 - Cardápio\n"
            "3 - Loja Virtual\n"
            "4 - Falar com uma pessoa (assim que pudermos, você será atendido/a).")
    
    # Opção 1 - Assinatura
    elif incoming_msg == '1':
        msg.body("Nosso sistema de assinatura oferece planos flexíveis de marmitas vegetarianas. "
            "Você pode escolher as opções semanais ou mensais. "
            "Entre em contato com a nossa equipe para mais detalhes ou acesse a nossa página.")
    
    # Opção 2 - Cardápio
    elif incoming_msg == '2':
        msg.body("Aqui está o cardápio da semana:\n\n- Segunda-feira: Quinoa com legumes\n"
            "- Terça-feira: Feijoada vegetariana\n"
            "- Quarta-feira: Macarrão integral com cogumelos\n"
            "... (adicionar mais itens conforme necessário)")
    
    # Opção 3 - Loja Virtual
    elif incoming_msg == '3':
        msg.body("Você pode acessar a nossa loja virtual no seguinte link: [link para a loja]. Lá você pode ver todos os produtos e fazer seus pedidos!")
    
    # Opção 4 - Falar com uma pessoa
    elif incoming_msg == '4': 
        msg.body("Obrigado por escolher falar com um de nossos atendentes. Em breve, alguém da equipe entrará em contato para te ajudar!")

    # Resposta padrão para mensagens não reconhecidas
    else:
        msg.body("Desculpe, não entendi sua resposta. Por favor, escolha uma das opções enviando o número correspondente:\n"
            "1 - Assinatura\n"
            "2 - Cardápio\n"
            "3 - Loja Virtual\n"
            "4 - Falar com uma pessoa.")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
