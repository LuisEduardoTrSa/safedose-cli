import sys
import requests

def consultar_medicamento_fda(nome_remedio: str) -> dict:
    busca = nome_remedio.strip().lower().replace(" ", "+")
    url = f'https://api.fda.gov/drug/label.json?search=openfda.generic_name:"{busca}"&limit=1'
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            dados = response.json()
            if "results" in dados and len(dados["results"]) > 0:
                resultado = dados["results"][0]
                openfda_data = resultado.get("openfda", {})
                
                # Extrai os dados se existirem
                generico = openfda_data.get("generic_name", ["Não identificado"])[0]
                marca = openfda_data.get("brand_name", ["Não identificada"])[0]
                return {"generico": generico.title(), "marca": marca.title()}
        return None
    except requests.exceptions.RequestException as e:
        return None

def calcular_dosagem(peso: float, concentracao: float, dose_recomendada: float) -> float:
    if peso <= 0 or concentracao <= 0 or dose_recomendada <= 0:
        raise ValueError("Todos os valores devem ser maiores que zero.")
    resultado = (peso * dose_recomendada) / concentracao
    return round(resultado, 2)

def main():
    print("-" * 50)
    print("           SafeDose CLI - Versão 1.1.0")
    print("      Integração Internacional OpenFDA Ativa")
    print("-" * 50)
    
    try:
        # Etapa 1: Consumo da API
        print("\n[1] VALIDAÇÃO DO MEDICAMENTO")
        # Dica: Como a API é americana, princípios ativos internacionais funcionam melhor
        remedio = input("Digite o princípio ativo (ex: Ibuprofen, Amoxicillin, Paracetamol): ")
        
        print("Consultando base de dados da FDA...")
        dados_remedio = consultar_medicamento_fda(remedio)
        
        nome_exibicao = remedio.title()
        if dados_remedio:
            print(f"✓ Medicamento validado!")
            print(f"  Nome Genérico: {dados_remedio['generico']}")
            print(f"  Marca de Referência: {dados_remedio['marca']}")
            nome_exibicao = dados_remedio['generico']
        else:
            print("⚠ Medicamento não encontrado na base ou erro de conexão.")
            print("  Prosseguindo com o nome digitado sob responsabilidade do usuário.")

        # Etapa 2: Calculadora Original
        print("\n[2] PARÂMETROS DE DOSAGEM")
        peso = float(input("Digite o peso do paciente (kg): "))
        conc = float(input(f"Digite a concentração de {nome_exibicao} (mg/ml): "))
        dose = float(input("Digite a dose recomendada (mg/kg): "))
        
        ml = calcular_dosagem(peso, conc, dose)
        
        print("\n" + "=" * 50)
        print("                 PRESCRIÇÃO SEGURA")
        print("=" * 50)
        print(f" Medicamento: {nome_exibicao}")
        print(f" Paciente: {peso} kg")
        print("-" * 50)
        print(f" RESULTADO: Administrar {ml} ml")
        print("=" * 50)
        
    except ValueError as e:
        print(f"\n[ERRO]: Entrada inválida. {e}")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()
