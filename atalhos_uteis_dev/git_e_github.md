"""
Criação de repositórios no Github:
Nome do projeto: Nome que deseja
Descrição do projeto: Descrição curta sobre o que se trata 
Privacidde: (Público: Todos podem ver / Privado: Apenas o Usuário ou quem ele permitir pode ver) 
Arquivo README: Onde consegue descrever o projeto mais detalhadamente. 
Gitignore: Ignorar arquivos que você não deseja que sejam add 
Licence: Para as pessoas saberem qual a liberdade do repositório tanto pra uso/divulgação.
Tecla "." do teclado, leva para uma espécie de Visual Studio Code online feito para o Github


Atalhos importantes do Git:
mkdir (cria um diretório)
touch (cria um arquivo)
cd (Encontra dentro da pasta outra pasta)
cd .. (Volta uma pasta)
.gitkeep (Arquivo que normalmente é encontrado em pastas para o git status reconhecer a pasta vazia na checagem)
.gitignore (Git irá ignorar o que estiver dentro)
COMANDO: echo PASTA/ > .gitignore (Será enviada a pasta PASTA/ para os ignorados)
COMANDO: echo > .gitignore (Deixa o arquivo vazio)
git init (Inicializa um repositório Git)
git status (Mostra o Status da área de trabalho/index de preparação e o status do arquivo, inclusive se falta adicionar algum arquivo para área de preparação)
P.S.: Área de preparação ou Index de preparação é a área onde estarão os arquivos que vamos fazer comit
git clone URL (URL é o Https ou SSC do github, clona um repositório, se escrever algo após a URL muda o nome da pasta que está sendo clonada no git)
git clone URL --branch NOME DA BRANCH --single-branch (Nesse caso clona apenas a branch)
git remote add origin URL (Adicionou a origem github a um repositório do Git já existente)
touch README.md (Cria um arquivo readme de extensão markdown (ainda não está rastreado e reconhecido pelo git até você add ele com o git add <file>))
clear (Limpa a tela do terminal)

git add ARQUIVO (Adiciona um arquivo a área de preparação, não comitado)
git add . (Adiciona todos os arquivos a área de preparação)
git commit -m"" ("" É a mensagem que será adicionada ao salvar o comit com suas alterações)
git log (Exibe o log do commit feito)
git relog (Exibe o log completo)

Desfazendo erros:
- git init na pasta errada:
rm -rf .git (Remove o repositório git da pasta)
- Salvou errado o arquivo e quer retornar pra última versão:
git restore ARQUIVO (Retorna o ARQUIVO ao original antes do commit)
- Alterar mensagem do último commit:
git commit --amend -m "MENSAGEM" (Altera a mensagem do último commit)
git commit --amend -m (Abre o editor para alterar a mensasgem do último commit)
- Desfazer o último commit, indo para o anterior a ele
git log (Logo em seguida copiar o código após commit)
/Três formas de se fazer agora:/
git reset --soft CÓDIGO (Retorna os último arquivos commitados a área de preparação)
git reset --mixed CÓDIGO OU git reset (Retorna os últimos arquivos para a serem adicinados a área de preparação)
git reset --hard CÓDIGO (Exclui completamente os últimos arquivos, sem recuperação)
git reset PASTA/ARQUIVO.md (Nesse caso ele retira o ARQUIVO.md da área de preparação)
git restore --staged PASTA/ARQUIVO.md (Nesse caso ele retorna o ARQUIVO.md para área de preparação)

Atualizar arquivos do Github (Repositório Remoto) para o Git (Repositórios local) e vice versa:
git push origin main (envia as atualizações do repositório local para o remoto, esse código se encontra no repositório dentro do github)
git pull (Puxa as atualizações do Repositório Remoto)

Definições e atalhos de Branch:
- Branch é uma ramificação do projeto principal (main), uma forma de alterar o arquivo principal sem salvar ele, seja pra teste ou para formar alguma ideia.
- Em projetos maiores as branchs servem pra mais de uma pessoa trabalhar no mesmo arquivo sem atrapalhar o arquivo principal e as outras pessoas
git checkout -b NOMEDABRANCH (Agora qualquer alteração será feita nesse branch e não na original)
git checkout main (Volta para o principal, ignorando as alterações do branch)
git branch -v (Exibe a versão dos branchs comparados ao main)
git merge NOMEDABRANCH (Adiciona as alterações e arquivos do branch selecionado ao main)
git branch -d NOMEDABRANCH (Exclui a branch selecionada)

Comandos úteis de Branch:
git fetch origin main (Baixa os arquivos do repositórios remoto sem alterar o repositório local)
git diff main origin/main (Avalia quais são as diferenças entre o repositório remoto e local)
git merge origin/main (Atualiza o arquivo baixado com o do local)
git clone LINKHTMLDOGITHUB --branch NOMEDABRANCH --single-branch (clona uma branch do github para seu git, singlebranch indica qual branch você deseja clonar, caso não seja indicado clonará apenas a principal)
git stash (Arquiva modificações feitas na branch)
git stash list (Mostra as modificações arquivadas)
git stash pop (Permanece as modificações recentes e exclui as modificações no stash)
git stash apply (Traz as modificações do stash de volta para o branch)


Tentar enviar alterações do repositório local sendo que foram feitas alterações no repositório remoto:
- Assim que tentar enviar o arquivo vai ser rejeitado, teremos que dar um git pull e vai ter um aviso de conflito
- O conteúdo do arquivo em conflito será alterado com as duas informações e cabe a nós decidir quais atualizações permanecem
git add .
git commit -m"MENSAGEM"
git push (Agora será enviado pois já foi feita a correção)


Markdown:
Markdown é uma espécie de linguagem de marcação simples, uma forma mais simples de estar escrevendo um HTML
Site para editar readme no formato markdown (md): read.so/pt/editor

Sites interessantes:
GitHub Desktop: desktop.github.com
My Octocat : myoctocat.com


"""
