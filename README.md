#controle_de_gastos Pessoais (Python)

Sistema simples de controle financeiro pessoal com interface em terminal. Permite registrar receitas e despesas, categorizá-las e gerar relatórios mensais. Ideal como projeto de portfólio para iniciantes que desejam praticar Python com foco em organização, leitura de arquivos, manipulação de dados com pandas e boas práticas de estrutura modular.
---

#funcionalidades
- Registrar **receitas** e **gastos** com data atual automática
- Categorização por tipo (ex: alimentação, transporte, salário, etc.)
- Relatórios mensais com total por tipo e listagem
- Armazenamento em CSV (estrutura tipo banco de dados simplificado)
---

#tecnologias_usadas

- Python 3.10 ou superior
- pandas
- Interface via terminal (CLI)
---

#estrutura_do_projeto

```
controle_de_gastos/
├── main.py                   # Arquivo principal
├── data/
│   └── gastos.csv           # Base de dados dos registros
├── modules/
│   ├── menu.py              # Menu principal
│   ├── registros.py         # Lógica para registrar gastos/receitas
│   ├── relatorios.py        # Geração de relatórios
│   └── util.py              # Funções auxiliares (ex: limpar tela)
└── README.md
```

##dica: certifique-se de que o arquivo `gastos.csv` tem o seguinte cabeçalho:
> `data,tipo,categoria,descricao,valor`
---

#como_rodar_localmente

1. Clone este repositório ou baixe o ZIP:

```bash
git clone https://github.com/seu-usuario/controle_de_gastos.git
```

2. Instale as dependências (usando ambiente virtual ou diretamente):

```bash
pip install -r requirements.txt
```

3. Execute o sistema:

```bash
python main.py
```

---

#requirements.txt

```txt
pandas
```

---

#To-do (ideias para evoluir)

- [ ] Adicionar visualização gráfica com matplotlib
- [ ] Permitir edição e exclusão de lançamentos
- [ ] Interface com Tkinter (GUI opcional)
- [ ] Exportar relatório como PDF ou Excel

---

#aprendizados_e_boas_práticas

- Uso de `pandas` para leitura e escrita de arquivos CSV
- Organização modular com divisão clara entre camadas
- Tratamento de exceções simples para melhorar a UX
- Projeto ideal para demonstrar conhecimento básico de Python e estrutura de projetos
---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se livre para usar, modificar e contribuir.
---

Feito Robson_Guezine.
