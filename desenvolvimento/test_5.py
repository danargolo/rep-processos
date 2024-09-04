"""Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  """

""" Resolucao: 
Acendo uma lampada e aguardo um período que de diferenca na temperatura da superficie da lâmpada, desligo e ligo outra lâmpada.
Dirijo-me a uma sala e com essas alternativas, identifico um interruptor: 
  - Luz apagada e fria - Interruptor nao utilizado. 
  - Luz apagada e quente - Primeiro interruptor ligado e desligado.
  - Luz ligada - Ultimo interruptor manipulado.
Utilizo a 2 ida para confirmar interruptores restantes.

"""