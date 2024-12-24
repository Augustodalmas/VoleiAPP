<h1 align="center">VoleiAPP</h1>

Sobre o Projeto

Este APP foi desenvolvido para suprir uma necessidade enfrentada por organizadores de partidas de vôlei, que frequentemente lidam com dificuldades para encontrar pessoas e fechar times de 12 jogadores.

Pensando nisso, resolvi criar uma plataforma simples, onde os jogadores possam se reunir de forma rápida e fácil, aliviando o estresse dos organizadores!

A plataforma ainda está em desenvolvimento, mas já foi adicionada ao meu GitHub para compartilhar a iniciativa e acelerar seu progresso. Atualmente, o foco é nas funcionalidades, com pouco cuidado com o design, mas há planos futuros para contratar um designer profissional e melhorar a parte gráfica do aplicativo.

Além disso, tenho como objetivo transformar essa plataforma em um app móvel no futuro.

Tecnologias Utilizadas

allauth: Para autenticação e gestão de contas de usuários.

Stripe: Para integração de pagamentos online.

Django-email: Para envio de emails.

Qrcode: Para gerar códigos QR.

Como Iniciar o Projeto

Para executar o projeto, siga os passos abaixo:

Instalar dependências:
Certifique-se de que todas as dependências estão instaladas usando um ambiente virtual e o arquivo requirements.txt (se aplicável):

'''python -m venv venv'''

"""pip install -r requirements.txt"""

Migrar o banco de dados:
Execute o comando para aplicar as migrações:

```python manage.py migrate```

Iniciar o servidor:
Rode o servidor local para testar o aplicativo:

python manage.py runserver

Importar as cidades:
Acesse a URL /user/cidades para importar as cidades necessárias.

Criar um superusuário:
Para acessar a interface de administração, crie um superusuário:

python manage.py createsuperuser

Planos Futuros

Melhorar o design do app com a ajuda de um designer profissional.

Transformar a plataforma em um aplicativo móvel para facilitar ainda mais o acesso.

Expandir funcionalidades para personalização de partidas e gestão de equipes.

Como Contribuir

Fique à vontade para abrir issues ou enviar pull requests com melhorias e sugestões para o projeto. Toda contribuição é bem-vinda!

Contato

Se tiver alguma dúvida ou sugestão, entre em contato através do meu perfil no GitHub. Vamos construir algo incrível juntos!