# Comunicação Serial entre um programa em Python e um microntrolador

## Microntrolador 
Va para src/main.cpp

Esse código vai receber os comandos da serial e passar para outra serial por bluetoth caso seja um ESP32 

Pois para isso funcionar não tem como ver o monitor serial já que o mesmo vai estar ocupado com o programa em python 

Para usar ler o monitor serial do bluetooth a forma mais fácil é baixar o app Serial Bluetooth monitor, conectar o aparelho e assim tudo que vc enviar no terminal do python deve aparecer o que digitou. 


## Python 

### Dependecias 

```bash
pip install pyserial

```

Alterar a porta e a velocidade de acordo com o seu caso 