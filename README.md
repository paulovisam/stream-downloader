
# Telegram Stream Downloader

-1002442764497


## Aviso LEGAL / DISCLAIMER

## Contribuições

Contribuições são muito bem-vindas! Se você deseja contribuir com este projeto, sinta-se à vontade para abrir pull requests ou issues.
Agradecemos antecipadamente pelo seu interesse e contribuição.

## Repositórios Derivados / Projetos que reproduzem este repositório de forma total ou parcial

Você está autorizado a criar repositórios derivados (forks), e reproduzir total ou parcial partes deste projeto.
No entanto, ao fazer isso, pedimos gentilmente que você forneça os devidos créditos ao repositório original. Isso pode ser feito das seguintes maneiras :

- Incluir um link para este repositório no seu README.

- Mencionar explicitamente o repositório original em qualquer documentação associada ao seu projeto derivado ou projeto que reproduz parte desse projeto.

## O que pode acontecer se eu não cumprir os termos da licença?

Caso o desenvolvedor desse repositório ['viniped/stream-downloader'](https://github.com/viniped/stream-downloader) encontre um repositório que não está cumprindo os termos da licença como reprodução total ou parcial desse repositorio ['viniped/stream-downloader'](https://github.com/viniped/stream-downloader)  
o desenvolvedor e detenteor de direitos autorais do repositório ['viniped/stream-downloader'](https://github.com/viniped/stream-downloader) irá em primeira mão procurar uma solução amigável entrando em contato direto e solicitando a atribução de créditos,
caso a via amigável seja ignorada ou não atendida o desenvolvedor, ciente dos termos de uso da plataforma doravante denominada [GitHub](https://github.com/) irá abrir uma reclamação formal 
através do formulário de suporte da plataforma ou através de um aviso de DMCA (Digital Millennium Copyright Act).

Ao utilizar, contribuir, reproduzir parte total ou parcial deste repositório, você concorda com os termos acima.

## Funcionalidades

- Baixa vídeos em ordem cronológica (da primeira à última mensagem).
- Organiza os vídeos em pastas baseadas no sumário fixado no canal.
- Salva o progresso de download em um arquivo JSON para permitir retomar de onde parou.


## Requisitos


Antes de começar, você precisa dos seguintes requisitos:

- **Python 3.10+**
- Conta no Telegram e credenciais da API (ID e hash)
- As bibliotecas listadas no `requirements.txt` (veja como instalar abaixo)

- **Ferramentas de Build do Microsoft C++**

Necessárias para compilar bibliotecas escritas nas linguagens C ou C ++

## Instalação do Python

1. Vá para o [Site do Python](https://www.python.org/)
2. Na tela inicial clique no botão download, e logo após no botão " Download for Windows " conforme na imagem abaixo :

![site python](https://github.com/user-attachments/assets/1a729329-4311-4b3d-974e-68715a2d7215)

3. Após fazer o download do executável do python , abra-o com privilégios de administrador, você deve se deparar com uma janela como essa:

![add python to path](https://github.com/user-attachments/assets/69df84b3-6250-47cf-a544-04ee61e1debf)

Marque as caixas " Use admin privileges when instaling py.exe" e "Add python.exe to PATH" e por fim clique em "Install Now"

# Ferramentas de Build do Microsoft C++

As Ferramentas de Build do Microsoft C++ (Microsoft C++ Build Tools) são um conjunto de ferramentas e bibliotecas que incluem compiladores, vinculadores e outras ferramentas necessárias para compilar código C++ no Windows. Embora sejam projetadas principalmente para desenvolvimento em C++, elas também são frequentemente necessárias ao instalar e usar pacotes Python que contêm extensões em C ou C++.

#### Por que são necessárias para Python?

1. **Compilação de Extensões em C/C++:**
   - Muitos pacotes Python, especialmente aqueles voltados para desempenho ou integração com bibliotecas de baixo nível, incluem componentes escritos em C ou C++. Estes componentes precisam ser compilados quando o pacote é instalado. Exemplos incluem `numpy`, `scipy`, `pandas`, `lxml` e muitos outros.
   - As Ferramentas de Construção do Microsoft C++ fornecem o compilador e as ferramentas necessárias para essa compilação.

2. **Instalação de Pacotes a partir do Código-fonte:**
   - Quando você instala pacotes Python a partir do código-fonte (por exemplo, usando `pip install` em vez de baixar uma roda precompilada), o processo de instalação pode exigir a compilação do código. Isso é comum em ambientes onde rodas precompiladas não estão disponíveis para a versão do Python ou plataforma específica.

#### Como instalar as Ferramentas de Construção do Microsoft C++?

Você pode instalar as Ferramentas de Construção do Microsoft C++ seguindo estes passos:

1. **Baixe o instalador:**
   - Acesse o [site oficial do Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/) e baixe o instalador das Ferramentas de Construção do Microsoft C++. conforme a imagem abaixo:

   ![Design sem nome](https://github.com/user-attachments/assets/ff4b0a0e-df71-488b-bf26-0ce6a7582293)

2. **Execute o instalador:**
   - Durante a instalação, selecione a opção "Desenvolvimento de desktop com C++" para garantir que você está instalando os componentes necessários. (Veja a imagem abaixo)

![Design sem nome](https://github.com/user-attachments/assets/45fbe88b-223f-450a-a26b-e9cdfb5b685c)

3. **Adicione às variáveis de ambiente (se necessário):**
   - Em algumas situações, você pode precisar adicionar os caminhos das Ferramentas de Construção do Microsoft C++ às variáveis de ambiente do sistema para que possam ser encontradas durante a compilação.



## Instalação do script

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/telegram-channel-downloader.git
   cd telegram-channel-downloader

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash 
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```


3. Instale as dependências:
    ```bash 
    pip install -r requirements.txt
    ```

## Uso

1. Autentique-se no Telegram:

    Na primeira execução, o script solicitará que você insira seu API_ID e API_HASH do Telegram. Esses dados podem ser obtidos em my.telegram.org.


2. Execute o script:

    ```
    python main.py
    ```

3. Digite o ID do canal:

    O script solicitará que você insira o ID ou username do canal. Exemplo:

    ```
    Digite o ID do canal: -1001234567890
    ```

4. Acompanhe o progresso:

    O script criará uma pasta chamada Downloads.
    Dentro dela, será criada uma subpasta com o nome do canal.
    Os vídeos serão baixados em pastas organizadas por módulos, com base no sumário fixado.


5. Estrutura de Pastas

Após a execução do script, a estrutura será algo assim:

```bash 
Downloads/
    Nome_do_Canal/
        Modulo_1/
            video_1.mp4
            video_2.mp4
        Modulo_2/
            video_3.mp4
tasks/
    <channel_id>.json  # Salva o progresso para cada canal
```
## Doações

### Mantenha tudo atualizado e gratuito. Patrocine nossos projetos!!!!
<br/>
<div style="display: inline-block; background-color: white; padding: 10px; border-radius: 5px;">
  <a href="https://www.buymeacoffee.com/vinitemaceta">
    <img align="center" alt="sponsor-badge" src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" />
  </a>
  <a href="https://livepix.gg/vinitemaceta">
    <img align="center" alt="livepix-logo" src="https://static.livepix.gg/images/logo.svg" style="width: 100px; height: auto;" />
  </a>
</div>
<br/>


## Grupo de suporte

caso você tenha dúvidas disponibilizamos um grupo no Telegram [acesse clicando aqui](https://t.me/+cRyaxgNVpgUxNDcx)