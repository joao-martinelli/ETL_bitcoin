# ETL_bitcoin

Com a decisção da empresa pelo pentaho, percebi que era melhor focar na ferramenta
Seguindo o diagrama, podemos ver o uso do pentaho
Nela temos o começo em que é declarada a url com a api por onde ira ser consumido
o Rest client onde é chamado
o json input onde as informações são tratadas e espalhadas em campos
o select onde remove-se a url e o response e ficam apenas os campos
o insert, no qual a informação é inserida no banco postgres

![image](https://github.com/joao-martinelli/ETL_bitcoin/assets/139559927/34393bc0-24f8-4295-9988-e213be3f07fb)
