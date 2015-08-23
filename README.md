# dilma-rnn

Repositório com código para gerar o conjunto de treinamento para o Dilma-RNN.

Blog post: http://cesarsalgado.com/dilma_rnn/

Site para gerar novos textos: http://dilma-rnn.appspot.com/ 

## Requisitos:

- Linux
- wget
- Python
- BeautifulSoup (python lib)
- urllib2 (python lib) (opcional)

## Instruções

Para gerar o arquivo input.txt que pode ser usado no char-rnn use o comando: python gen_dilma_dataset.py

Para usar char-rnn no input.txt gerado siga as instruções no site: https://github.com/karpathy/char-rnn

Comando e parâmetros do char-rnn usado para treinar o dilma-rnn:

> th train.lua -data_dir data/dilma_rnn/ -num_layers 3 -rnn_size 400 -dropout 0.25

O arquivo input.txt precisa estar dentro da pasta: data/dilma_rnn/

Para treinar no wikipedia usei os seguinte comando:

> th train.lua -data_dir data/wikipedia/ -num_layers 3 -rnn_size 450 -dropout 0.1 -eval_val_every 10000 -max_epochs 150 -train_frac 0.98 -val_frac 0.02


Caso não queira instalar Lua e Torch (requisitos de char-rnn), você pode fazer tudo em python utilizado a lib Keras: https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py . Obs: Não cheguei a usar o Keras nesse projeto.
