# -------------------INTRODUÇÃO AO APP--------------------------------------------------
# programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#--------------------PROGRAMA PRINCIPAL----------------------------------------------------------

#--------------------SAUDAÇÃO--------------------------------------------------------------------

print("Boas-vindas ao Simulador de Empréstimos de Alessandro Aguiar")

#--------------------FIM SAUDAÇÃO----------------------------------------------------------------

#--------------------INPUT-----------------------------------------------------------------------

while True: #CONDIÇÃO PARA REPETIÇÃO


    imovel = int(input("Digite o valor do imóvel que deseja adquirir: "))

    salario = int(input("Digite o valor do salário do comprador do imóvel: "))

    anos = int(input("Digite em quantos anos irá quitar o imóvel: "))

#-------------------FIM INPUT---------------------------------------------------------------------

#-------------------CONDIÇÕES PARA GARANTIR A RESPOSTA DO USUÁRIO---------------------------------
    if imovel >= 0 and salario >= 0 and anos >= 1:

        print(f"O imóvel é R${imovel :.2f} de reais e o salário do comprador do imóvel é R${salario :.2f} de reais.")

        break
    
    else:

        print("Valor inválido!")

        continue
#------------------FIM CONDIÇÕES PARA GARANTIR A RESPOSTA DO USUÁRIO------------------------------

#------------------CÁLCULO DAS VARIÁVEIS----------------------------------------------------------

limite = salario / 100 * 30

meses = anos * 12

prestaçao = imovel / meses
#------------------FIM CÁLCULO DAS VARIÁVEIS------------------------------------------------------

#------------------PRINT DAS INFORMAÇÕES DO EMPRÉSTIMO--------------------------------------------

print(f"A prestação do imóvel será de: R${prestaçao :.2f} de reais.")
print(f"O valor limite da sua prestação é: R${limite :.2f} de reais.")
print(f"Voçê quitará o imóvel em: {meses} meses.")

#------------------FIM DAS INFORMAÇÕES DO EMPRÉSTIMO----------------------------------------------

#------------------CONDIÇÕES PARA O CÁLCULO DO EMPRÉSTIMO-----------------------------------------

if prestaçao <= limite:

    print("Parabéns o seu empréstimo foi aprovado!")

else:

    print("Infelismente o seu empréstimo não foi aprovado.")

print("Obrigado por utilizar o Simulador de Empréstimos de Alessandro Aguiar.")

#-----------------FIM DO PROGRAMA-----------------------------------------------------------------