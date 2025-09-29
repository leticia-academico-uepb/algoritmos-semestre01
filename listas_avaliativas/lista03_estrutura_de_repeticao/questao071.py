contadorSeguranca = 3

usuarioLogin = input("usuario: ")
senhaUsuario = input("senha: ")

while contadorSeguranca >1:

    if (usuarioLogin == "kezia" and senhaUsuario == "123"):
      print("Login concluído!")
      contadorSeguranca = 0
    else:
      contadorSeguranca-=1
      print("Dados de login incorretos. Tentativa (s) restente:", contadorSeguranca)
      usuarioLogin = input("usuario: ")
      senhaUsuario = input("senha: ")

if(contadorSeguranca == 1):
  print("Tentativas excedidas. Por motivos de segurança, você foi impossibilitado de continuar o login")
