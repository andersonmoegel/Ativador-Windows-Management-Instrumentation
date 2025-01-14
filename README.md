# README - Script de Diagnóstico e Reparação do WMI no Windows

## Descrição
Este script foi desenvolvido para verificar, ativar e reparar o serviço WMI (Windows Management Instrumentation) em sistemas Windows. Ele também inclui um sistema de registro de logs para monitoramento das operações realizadas.

---

## Funcionalidades

1. **Verificação de Execução como Administrador**  
   O script verifica se está sendo executado com permissões administrativas, necessárias para manipular serviços do sistema e modificar arquivos em diretórios protegidos.

2. **Logs de Diagnóstico**  
   Cria e grava logs detalhados no arquivo `C:\Windows\Temp\wmi_status.txt` para registrar o status do WMI e qualquer ação corretiva tomada.

3. **Diagnóstico do WMI**  
   Usa a biblioteca `win32com.client` para tentar uma conexão com o serviço WMI e verifica seu status.

4. **Ativação do WMI**  
   Se o serviço WMI estiver parado, o script tenta ativá-lo usando o comando `sc start winmgmt`.

5. **Reparo do WMI**  
   Se a verificação do WMI falhar, o script tenta reparar o repositório WMI com os comandos `winmgmt /verifyrepository` e `winmgmt /salvagerepository`.

---

## Requisitos
- Python instalado no sistema.
- Módulo `pywin32` para interagir com o WMI.  
  Pode ser instalado com:
  ```bash
  pip install pywin32
  ```

---

## Uso
1. Certifique-se de executar o script com permissões de administrador.  
   - Se não for iniciado como administrador, o script tentará se reiniciar com permissões elevadas.
2. O resultado das operações será salvo no log `C:\Windows\Temp\wmi_status.txt`.
3. O script imprime mensagens de status no console para fácil monitoramento durante a execução.

---

## Notas e Considerações
- **Compatibilidade:** Este script é projetado para sistemas Windows.  
- **Riscos Potenciais:** Manipular o WMI pode afetar serviços críticos do sistema. Use com cautela e somente se for necessário.
- **Exclusão de Logs Antigos:** O arquivo de log anterior é excluído antes de criar um novo para manter o relatório atualizado e evitar crescimento excessivo do arquivo.

---

## Limitações
- Se o script não conseguir obter permissões de administrador, ele não poderá executar diagnósticos ou reparos no WMI.
- Depende de comandos internos do Windows (`sc`, `winmgmt`), que podem variar entre diferentes versões do sistema.

---

## Changelog
- Versão 1.0: Primeira versão funcional com diagnóstico, ativação e reparo do WMI.

---

## Contribuições
Sugestões de melhorias e novas funcionalidades são bem-vindas.
