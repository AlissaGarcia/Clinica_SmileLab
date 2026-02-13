# 🦷 SmileLab — Sistema Web para Gestão de Clínica Odontológica

## Descrição Geral do Software

O **SmileLab** é um sistema web desenvolvido para apoiar a gestão de uma clínica odontológica, oferecendo funcionalidades para administração de usuários, pacientes, dentistas e agendamentos. O sistema foi **projetado e implementado exclusivamente sob uma Arquitetura de Software em Camadas**, garantindo separação clara de responsabilidades, organização do código, facilidade de manutenção e possibilidade de evolução futura.

Este projeto foi desenvolvido como atividade acadêmica da disciplina **Arquitetura de Sistemas**, atendendo às exigências de construção de um sistema não monolítico, com front-end, back-end e persistência de dados bem definidos.

---

## Objetivo do Sistema

Desenvolver um sistema web funcional para gestão de clínica odontológica, aplicando corretamente os conceitos de **arquitetura em camadas**, com:

* Camada de apresentação (interface com o usuário);
* Camada de aplicação/negócio (regras, validações e controle do sistema);
* Camada de persistência de dados (armazenamento e manipulação das informações).

---

## Arquitetura de Software

O SmileLab foi projetado em uma **Arquitetura em Camadas**, na qual cada parte do sistema possui responsabilidades bem definidas:

### 1. Camada de Apresentação (Front-end)

Responsável pela interação com o usuário. Implementa as telas, formulários e dashboards do sistema.

Principais responsabilidades:

* Interface gráfica;
* Formulários de cadastro e autenticação;
* Exibição de dados;
* Envio de requisições ao back-end.

Tecnologias:

* HTML5
* CSS3
* JavaScript //em desenvolvimento
* Templates do Django

---

### 2. Camada de Aplicação / Negócio (Back-end)

Responsável pelo processamento das requisições, aplicação das regras de negócio, validações e controle de acesso.

Principais responsabilidades:

* Regras de negócio;
* Autenticação e autorização;
* Controle de usuários e perfis;
* Comunicação entre a interface e a base de dados.

Tecnologia:

* Python
* Django Framework

---

### 3. Camada de Persistência de Dados

Responsável pelo armazenamento, recuperação e integridade das informações do sistema.

Principais responsabilidades:

* Mapeamento das entidades;
* Execução de consultas;
* Gerenciamento do banco de dados.

Tecnologia:

* SQLite (padrão do Django)

---

## Justificativa da Arquitetura em Camadas

A adoção da arquitetura em camadas possibilita:

* Separação clara de responsabilidades;
* Redução de acoplamento entre componentes;
* Maior organização do projeto;
* Facilidade de manutenção;
* Melhor compreensão do sistema;
* Possibilidade de expansão futura (ex: APIs, novos front-ends, troca de banco de dados).

---

## Modelagem do Sistema

O sistema foi modelado considerando as seguintes entidades principais:

* **Usuário** — controle de acesso e perfis (administrador, dentista, secretária);
* **Paciente** — cadastro e gerenciamento dos pacientes;
* **Dentista** — informações profissionais e vínculo com consultas;
* **Consulta / Agendamento** — marcação e controle de atendimentos;
* **Prontuário** — histórico clínico do paciente; //em desenvolvimento
* **Pagamento** — controle financeiro. //em desenvolvimento

Cada entidade possui atributos próprios e relacionamentos definidos no módulo `models.py`, utilizando o ORM do Django.

---

## Funcionalidades Principais

* Autenticação de usuários;
* Controle de acesso por perfil;
* Cadastro de pacientes;
* Cadastro de dentistas;
* Cadastro de secretárias;
* Listagem e gerenciamento de usuários;
* Agendamento de consultas;
* Dashboards específicos por perfil;
* Integração com banco de dados.

---

## Tecnologias Utilizadas

* Python 3
* Django
* HTML5
* CSS3
* JavaScript
* SQLite
* Git e GitHub

---

## Estrutura de Pastas (resumo)

```
Clinica_SmileLab/
│
├── construct_SmileLab/      # Configurações principais do projeto
├── usuarios/               # Aplicação principal do sistema
│   ├── models.py           # Entidades e persistência
│   ├── views.py            # Regras de negócio e controle
│   ├── urls.py             # Rotas do sistema
│   ├── forms.py            # Formulários
│   ├── templates/          # Camada de apresentação
│
├── db.sqlite3               # Banco de dados
├── manage.py                # Gerenciador do projeto
└── README.md
```

---

## Instruções para Execução

1. Clone o repositório:

```
git clone <link-do-repositorio>
```

2. Acesse a pasta do projeto:

```
cd Clinica_SmileLab
```

3. Crie e ative o ambiente virtual:

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências:

```
pip install django
```

5. Execute as migrações:

```
python manage.py migrate
```

6. Crie um superusuário:

```
python manage.py createsuperuser
```

7. Inicie o servidor:

```
python manage.py runserver
```

8. Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## Requisitos Funcionais

* Permitir login de usuários;
* Permitir cadastro de pacientes;
* Permitir cadastro de profissionais;
* Permitir gerenciamento de usuários;
* Permitir agendamento de consultas;
* Permitir visualização de dados por perfil.

---

## Requisitos Não Funcionais

* Utilizar arquitetura em camadas;
* Código organizado e modular;
* Sistema executável localmente;
* Uso de controle de versão;
* Facilidade de manutenção.

---

## Autoria

Projeto desenvolvido por **Alissa Garcia Moreira**

Disciplina: Arquitetura de Sistemas

---

## Observação Acadêmica

Este sistema foi desenvolvido com foco na aplicação prática dos conceitos de **Arquitetura de Software em Camadas**, conforme solicitado na atividade, priorizando organização, separação de responsabilidades e boas práticas de engenharia de software.
