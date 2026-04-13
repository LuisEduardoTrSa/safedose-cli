# SafeDose - Calculadora de Dosagem Segura 💊

![CI Pipeline](https://github.com/LuisEduardoTrSa/safedose-cli/blob/main/.github/workflows/ci.yml) 
> Versão Atual: 1.0.0 (SemVer)

## Sobre o Projeto
O **SafeDose** é uma ferramenta de linha de comando (CLI) desenvolvida para resolver uma dor real: a dificuldade de cuidadores, pais e donos de pets em calcular a dosagem exata de medicamentos líquidos (em ml) baseando-se no peso do paciente e na concentração do remédio.

### O Problema
Erros de dosagem são causas comuns de intoxicação ou falta de eficácia no tratamento. A conversão de **mg/kg** para **ml** exige um cálculo que, em momentos de pressa ou estresse, pode levar a erros fatais.

### ✅ A Solução
A aplicação automatiza esse cálculo. O usuário fornece o peso, a dose recomendada e a concentração do frasco, e o sistema entrega o valor exato a ser administrado, com validações de segurança.

---

## Público-Alvo
- Cuidadores domésticos.
- Pais e responsáveis.
- Tutores de animais de estimação.

## Funcionalidades
- Cálculo de dosagem baseado em peso (kg).
- Tratamento de erros para entradas inválidas (letras ou valores negativos).
- Interface amigável via terminal (CLI).

## Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Testes:** Pytest
- **Linting/Qualidade:** Ruff
- **CI/CD:** GitHub Actions

---

## Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Clone este repositório:
```bash
