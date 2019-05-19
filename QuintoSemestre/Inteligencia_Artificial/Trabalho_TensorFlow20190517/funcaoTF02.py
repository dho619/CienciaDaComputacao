# 2019-05-17
# @geovanebarbosa
# Formula de IMC
#https://www.minhavida.com.br/alimentacao/tudo-sobre/32159-imc
# ---------------------
import tensorflow as tf #Importando Tensor


sess = tf.InteractiveSession() #Criando a Sessao

peso = 80
altura = 1.80

#CRIANDO A ESTRUTURA DO TENSORFLOW
valores = tf.constant([peso, altura],tf.float32)


#DECLARANDO AS OPERACOES
result = tf.divide(valores[0],tf.pow(valores[1],2))


#COLOCANDO A SESSAO PARA RODAR
with tf.Session() as sess:
    IMC = sess.run(result)


#RESULTADO
print("\n-----------------------------------------------------------------------\n\n")
print("IMC = {:.2f}".format(IMC))

