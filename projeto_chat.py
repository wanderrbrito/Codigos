###
Criacao de um Chat para uso local
Projeto realizado durante a Jornada Python da Hastag Treinamentos
###
# Criacao de um chat para uso local

# importar o flet

# video em 01


# criar a funcao principal do sistema
def main(pagina):

    # criar o titulo
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    

    titulo_janela = ft.Text("Bem vindo ao Chat da Orion!")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"

        
        pagina.pubsub.send_all(texto)

        texto_mensagem.value = ""

        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar =  ft.ElevatedButton("Enviar", on_click=enviar_mensagem)



    #criar chat
    chat =ft.Column()


    # colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        # tirar o titulo da pagina
        pagina.remove(titulo)

        # tirar o botao iniciar
        pagina.remove(botao_iniciar)

        # fechar o popup
        janela.open = False

        # adcionar o chat
        pagina.add(chat)

        # linha da mensagem
        pagina.add(linha_mensagem)

        # exibir: usuario entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat!"
        #chat.controls.append(ft.Text(texto_entrou_chat))
        pagina.pubsub.send_all(texto_entrou_chat)
        
        #pagina.add(botao_enviar)
        pagina.update()

        # criar o chat

       

        pagina.update()
    botao_entrar = ft.ElevatedButton("Entrar no chat!", on_click=entrar_chat)


    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_nome_usuario, 
        actions=[botao_entrar]
    )



    def abrir_popup(evento):
        pagina.dialog = janela
        #pagina.overlay.append(dialog.janela)
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
        
   
    #botao_iniciar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)



    # exibir na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    

# excecutar o sistema
ft.app(main, view=ft.WEB_BROWSER)
