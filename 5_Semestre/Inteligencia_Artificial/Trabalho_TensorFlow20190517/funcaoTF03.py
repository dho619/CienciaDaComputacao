# 2019-05-17
# @geovanebarbosa
# Formula da Hipotenusa
#https://calculareconverter.com.br/calcular-hipotenusa/
# ---------------------


import tensorflow as tf #Importando Tensor

sess = tf.InteractiveSession() #Criando a Sessao

cateto1 = 9.0
cateto2 = 12.0


#CRIANDO A ESTRUTURA DO TENSORFLOW
valores = tf.constant([cateto1, cateto2], tf.float32)


#DECLARANDO AS OPERACOES
x_quad = tf.add(tf.pow(cateto1,2), tf.pow(cateto2,2))
x = tf.sqrt(x_quad)

#COLOCANDO A SESSAO PARA RODAR
with tf.Session() as sess:
    hipotenusa = sess.run(x)


#RESULTADO
print("\n-----------------------------------------------------------------------\n\n")
print("Hipotenusa = {}".format(hipotenusa))


