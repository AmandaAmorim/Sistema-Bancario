
# 💰 Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python com funcionalidades básicas de **depósito**, **saque** e **extrato**.

## 🧠 Funcionalidades

- **Depósito**
  - Aceita apenas valores positivos.
  - Atualiza o saldo e registra no extrato.
- **Saque**
  - Limite de R$ 500 por saque.
  - Máximo de 3 saques diários.
  - Verifica saldo e número de saques antes de permitir a transação.
- **Extrato**
  - Exibe o saldo atual, número de saques e depósitos realizados.
  - Lista todas as transações efetuadas.
- **Sair**
  - Encerra o programa.

## 🖥️ Como usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o script:
   ```bash
   python sistemaBancario.py
   ```
3. Interaja com o menu no terminal:

   ```
   Bem vindo ao Sistema Bancário!
   Digite o número da opção desejada: 
   1. Depositar
   2. Sacar
   3. Extrato 
   4. Sair
   ```

## 🛑 Regras de negócio

- ✅ Depósitos devem ter valor positivo.
- ✅ Saques:
  - Máximo de **3 saques** permitidos.
  - Limite de **R$ 500 por saque**.
  - Saque só é permitido se houver saldo suficiente.
- ✅ O extrato exibe o histórico apenas das transações realizadas.

## 📁 Estrutura do código

- Variáveis principais:
  - `saldo`: armazena o valor disponível.
  - `limite`: valor máximo de cada saque.
  - `extrato`: histórico de transações.
  - `numero_saques`: contador de saques realizados.
  - `LIMITE_SAQUES`: constante que define o máximo de saques diários.
  - `depositos`: contador de depósitos realizados.
- Estrutura de controle principal com `while True` e condicionais (`if`, `elif`, `else`).

## 🚀 Possíveis melhorias futuras

- Armazenamento de dados em arquivo ou banco de dados.
- Cadastro de múltiplos usuários.
- Interface gráfica com Tkinter ou Web com Flask.
- Relatórios financeiros.
