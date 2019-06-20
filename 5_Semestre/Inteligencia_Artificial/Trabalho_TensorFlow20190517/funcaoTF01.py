# 2019-05-17
# @geovanebarbosa
# Formula de Bhaskara
#https://pt.khanacademy.org/math/algebra/quadratics/solving-quadratics-using-the-quadratic-formula/a/quadratic-formula-review
# ---------------------


import tensorflow as tf #Importando Tensor

sess = tf.InteractiveSession() #Criando a Sessao

A = -7
B = 2
C = 9

#CRIANDO A ESTRUTURA DO TENSORFLOW
valores = tf.constant([A, B, C], tf.float32)


#DECLARANDO AS OPERACOES
delta = tf.subtract(tf.pow(valores[1],2), tf.multiply(4.0,tf.multiply(valores[0],valores[2])))

x1 = tf.divide(tf.add(tf.negative(valores[1]), tf.sqrt(delta)), tf.multiply(2.0, valores[0]))

x2 = tf.divide(tf.subtract(tf.negative(valores[1]), tf.sqrt(delta)), tf.multiply(2.0, valores[0]))



#COLOCANDO A SESSAO PARA RODAR
with tf.Session() as sess:
    result = sess.run([x1,x2])


#RESULTADO
print("\n-----------------------------------------------------------------------\n\n")
print("x1 = {}\nx2 = {}".format(result[0],result[1]))


