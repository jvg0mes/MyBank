import inspect
from models.Cliente import Cliente

msg = {
    'login_main': "\n########\nMyBank\n########\n\n" + \
             "Please login in your account. " \
             "Type signin in username field to create an account.\n"
    ,'login_username': "Username: "
    ,'login_password': "Password: "
    ,'cadastrar_cliente': "-"*50 + 'Cadastrar Cliente' + "-"*50 + "\n"
    ,'cadastrar_cliente_campos': list(map(lambda x: '\n' + x + ': ',
    inspect.getfullargspec(Cliente)[0][1:]))
    ,'cadastrar_usuario_senha': ['\nSenha: ', '\nConfirmacao da Senha: ']
}
