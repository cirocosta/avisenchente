AvisEnchente
===
> Um alerta em tempo real

Problema
---
Há recorrentemente muitos problemas relacionados às enchentes tanto no Brasil quanto em muitos outros lugares do mundo. Raros são os casos em que há efetivamente o combate a tal [dados os gastos]((http://oglobo.globo.com/rio/combate-enchentes-tera-16-bi-5988818)) e outros interesses políticos.


O produto
---
Inspirado em soluções de minimização de dano tomadas por prefeituras de cidades constantemente afetadas por problemas similares tal como a [sirene anti-enchente](http://noticias.r7.com/rio-de-janeiro/noticias/estado-diz-que-sirenes-anti-enchente-serao-instaladas-a-partir-de-novembro-na-regiao-serrana-20110714.html), AvisEnchente pretende amplificar este sistema para as tecnologias recentes e tornar a realização do mesmo totalmente comunitária e sem intervenção do governo. 

Seu princípio é básico: os residentes de uma região cadastram os aparelhos que então entendem o ambiente externo e permite que o sistema possa prever ocorridos.

Há inclusive interação direta por parte do usuário para alertar a ocorrência em casos extremos (bastaria apertar o botão vermelho).

Tal produto poderia também ser extendido para outras áreas, tais como prevenção de queimadas no centro-oeste brasileiro onde isto é recorrente. 


Sdk para consumo de dados do DCA
---
A sdk para python (aqui utilizada) pode ser encontrada [aqui](https://github.com/cirocosta/iot-sdk-python).


Funcionamento
---	
Seu funcionamento pode ser divido em quatro partes:

-	O IoT
-	A aplicação web
-	A aplicação mobile (não implementada)

**O IoT**

Trata-se de uma espécie de microcomputador contendo sensores conectados a ele para obtenção de informações sobre o ambiente externo. Este coletará as seguintes informações:

-	Temperatura
-	Humidade
-   Ruído
-	Luminosidade
-	Inserção de comando (1,0)

Como métricas cruciais ao sistema utiliza-se *temperatura*, *humidade* e *luminosidade*.  


**Aplicação Web**
Agrega toda a informação das redes formadas para o controle da temperatura. Este é o centralizador de toda a informação obtida através do serviço cloud fornecido pela [Telefonica](http://iot.telefonicabeta.com/).

Conta com:

-	interface gráfica para visualização
-	Webservice para fornecimento aberto de toda informação agregada

**Aplicação Mobile**

Permite visualizar em tempo real as informações de uma região e também notifica o usuário em tempo real de uma possível iminência de fortes-chuvas e/ou enchentes.	



Dev
===

Será listado a seguir o necessário para configurar o ambiente de desenvolvimento e subir o necessário.

QuickInstall
---
No shell, execute para instalar as dependências e preparar o ambiente:
```bash
$ ./setup.sh
```

Para iniciar o servidor local nas portas 8080 e 8000:
```
$ ./run_server
``` 	
