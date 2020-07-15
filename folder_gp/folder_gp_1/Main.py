import os
import time

from Cliente import Cliente
from folder_gp_1.clientes import clientes

print("Bem-vindo!")

class Proj:
  def init(self):
    self.cliente = Cliente(clientes)
    while True:
      administracao = False;
      cliente = False;
      movimentacao = False;
      print("Escolha o módulo referente à ação, na qual gostaria de realizar")

      print("1 - Administração")
        
      print("2 - Cliente")
      
      print("3 - Movimentação")

      opcao = int(input("Digite a opção desejada: "))

      if opcao == 1:
        administracao = True
      if opcao == 2:
        cliente = True   
      if opcao == 3:
        movimentacao = True
        
      os.system("cls")
      
      while movimentacao == True:
        time.sleep(2)
        print("1 - Agendar o pagamento de títulos")
        print("2 - Pedir o cancelamento ou a substituição do cartão de crédito em casos de perda, furto ou roubo")
        print("3 - Pedir informações sobre cartão de crédito e débito")
        print("4 - Fazer cópia de documentos")
        print("5 - Comprar créditos para celulares pré-pagos")
        print("6 - Fazer o cadastro ou bloqueio de débito automático")
        print("7 - Depositar dinheiro em conta corrente ou poupança")
        print("8 - Pedir um empréstimo, desde que com o uso de limite pré-aprovado")
        print("9 - Tirar extratos de consulta e retirada")
        print("10 - Pagar benefícios sociais")
        print("11 - Pagar multas, tributos e licenciamento de veículos, assim como contas de consumo de faturas do cartão de crédito")
        print("12 - Receber informações sobre produtos, como ações, câmbio, capitalização, CDB, comércio exterior, consórcios, fundos, vida, previdência e seguros")
        print("13 - Conseguir informações sobre a rede de atendimento")
        print("14 - Consultar saldos")
        print("15 - Fazer saques em conta correntes e poupanças")
        print("16 - Avisar sobre a perda de talão de cheque")
        print("17 - Retirar folhas e talão de cheques")
        print("18 - Consultar a tabela de tarifas do banco")
        print("19 - Realizar transferências entre agências do próprio banco")
        print("20 - Fazer TEDs e DOCs entre bancos")
        print("21 - Cadastrar pessoa física")        
        print (" ")

        selecionado = int(input("Digite a opção desejada: "))

        if selecionado == 21:
          from Banco_crud import carregar_cliente,salvar_cliente,adicionar
        else:
          print("Única opção em funcionamento é a 21")
          
      while cliente == True:
        time.sleep(2)
        print("Menu Cliente - Yan Velho e Júlia Oliveira")
        print("1 - Cadastrar seu banco")
        print("2 - Alterar um banco já cadastrado")
        print("3 - Excluir um banco cadastrado")
        print("4 - Buscar um banco")
        print("5 - Listar os bancos cadastrados")
        print("6 - Defina a forma de reclamações de seu cliente")
        print("7 - Reclamações do nosso sistema")
        print("8 - Sair")

        selecionadoC = int(input("Digite a opção desejada: "))

        if selecionadoC == 1:
          from cliente_gp import carregar_cliente,salvar_cliente,adicionar
        elif selecionadoC == 8:
            print("Fechando o programa...")
            exit()
        else:
            time.sleep(2)
            print("Função ainda não programada... Única função em funcionamento é a 1")

        
      while administracao == True:
        rS = 0
        vss = 0
        rSu = 0
        vssu = 0


        while True:
            time.sleep(2)

            print("Banco Digital - Administrativo")
            print("1 - Sangria")
            print("2 - Suprimento")
            print("3 - Relatórios de Produção")
            print("4 - Sair")

            opcaoSelecionada = input("Digite o opção desejada: \n")
              
            if opcaoSelecionada == '1':
                rSO = rS + 1
                print("Registro: ",rSO,'\n')
                input("Registre a finalidade da sangria: "),
                print("\nForma de Pagamento (Mais opções futuramente)")
                print("1 - Dinheiro")
                print("2 - Crédito")
                print("3 - Débito")
                formaPaga = int(input("Digite o opção desejada: "))
                if formaPaga == 1:
                    valorSangria = int(input("Digite o valor da sangria: "))
                    valorTerciario = vss + valorSangria
                elif formaPaga == 2:
                    valorSangria = int(input("Digite o valor da sangria: "))
                    valorTerciario = vss + valorSangria
                elif formaPaga == 3:
                    valorSangria = int(input("Digite o valor da sangria: "))
                    valorTerciario = vss + valorSangria
                conf = input("Realizar sangria(s/n): ")
                if conf == 'n':
                    print("Sangria cancelada!\n")
                elif conf == 's':
                    print('Sangria feita!\n')
                    rS = rSO
                    vss = valorTerciario
                else:
                    print("\nComando não identificado")

            elif opcaoSelecionada == '2':
                rSup = rSu + 1
                print("Registro do Suprimento: ",rSup)
                valorSuprimento = int(input("Digite o valor da adição: "))
                valorTerciarioo = vssu + valorSuprimento
                input("Digite a finalidade da adição: ")
                confi = input("Salvar suprimento? (s/n)")
                if confi == 'n':
                    print("Suprimento cancelado!\n")
                elif confi == 's':
                    print('Suprimento realizado!\n')
                    rSu = rSup
                    vssu = valorTerciarioo
                else:
                    print("\nComando não identificado")
                         
            elif opcaoSelecionada == '3':
                rSan = str(rS)
                vSan = str(vss)
                rSup = str(rSu)
                vSup = str(vssu)
                print("Relatórios de produção")
                print("Escolha o módulo:")
                print("1 - Relatório da movimentação do dia")
                print("2 - Relatório da movimentação do mês")
                print("3 - Relatório da movimentação do admnistrativo")
                opcao = int(input('Digite a opção: '))
                if opcao == 1:
                    arquivo = open('administracaoDiario.txt', 'w')
                    arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico\n')
                    arquivo.write('A movimentação da sangria de hoje se constituiu em: ')
                    arquivo.write(rSan)
                    arquivo.write('\nO valor da movimentação da sangria de hoje foi: ')
                    arquivo.write(vSan)
                    arquivo.write('\nA movimentação do suprimento de hoje se constituiu em: ')
                    arquivo.write(rSup)
                    arquivo.write('\nO valor da movimentação do suprimento foi: ')
                    arquivo.write(vSup)
                    arquivo.close()
                    
                    arquivo = open('administracaoDiario.txt', 'r')
                    unica_string = arquivo.read()
                    arquivo.close()
                    
                if opcao == 2:
                    arquivo = open('administracaoMensal.txt', 'a+')
                    arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico sobre o mês')
                    arquivo.read()
                    arquivo.close()
                    
                if opcao == 3:
                    arquivo = open('administracaoAdministrativo.txt', 'a+')
                    arquivo.write('Este presente relatório busca fornecer as informações de movimentação deste caixa eletrônico sobre a movimentação do administrativo')
                    arquivo.read()
                    arquivo.close()
            
            elif opcaoSelecionada == '4':
                exit()
        
        pass
          
      
  def saqueCliente(self):
    dinheiro = {
      input("Informe o quanto gostaria de sacar: ")
    }
    pass

  def depositoCliente(self):
    quantidade = {
      input("Informe o quanto gostaria de depositar: "),
      input("Informe a conta para onde o depóstio irá: "),
    }
    pass

  def pagamentoCliente(self):
    pag = {
      input("Informe o quanto será pago: "),
      input("Informe a conta para onde o pagamento irá: "),
    }
    pass

  
  def adicionarCliente(self):
    cliente = {
      'email' : input("Digite o e-mail do usuário: "),
      'nome' : input("Digite o nome do usuário: "),
      'telefone' : input("Digite o telefone do usuário: ")
    }

    if self.cliente.buscarPeloEmail(cliente.get('email')):
      print("O e-mail do cliente já existe.")
      return
      pass

    self.cliente.adicionar(cliente)

    pass

  def alterarCliente(self):
    cliente = {
      'email' : input("Digite o e-mail do cliente: "),
      'nome' : input("Digite o nome do cliente: "),
      'telefone' : input("Digite o telefone do cliente: ")
    }

    cliente_id = int(input("Digite o identificador do usuário: "))
    if self.cliente.alterar(cliente_id, cliente):
      print("Dados do cliente atualizados com sucesso.")
      return
      pass

    print("O Cliente não existe.")
    pass

  def excluirCliente(self):
    cliente_id = int(input("Digite o identificador do cliente: "))

    if self.cliente.excluir(cliente_id):
      print("Cliente excluído.")
      return
      pass

    print("O Cliente não existe.")
    pass

  def buscarClientePeloEmail(self):
    email = input("Digite o e-mail do Cliente: ")

    cliente = self.cliente.buscarPeloEmail(email)
    if cliente:
      print(cliente)
      input("Pressione Enter para continuar...")
      return
      pass

    print("O Cliente não existe.")
    pass

  def buscarClientePeloId(self):
    cliente_id = int(input("Digite o identificador do Cliente: "))

    cliente = self.cliente.buscarPeloId(cliente_id)
    if cliente:
      print(cliente)
      input("Pressione qualquer tecla para continuar...")
      return
      pass

    print("O Cliente não existe.")
    pass

  def listarTodosClientes(self):
    clientes = self.cliente.listarTodos()
    print(clientes)
    input("Pressione qualquer tecla para continuar...")
    pass
    

  


