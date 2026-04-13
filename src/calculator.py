import sys

def calcular_dosagem(peso: float, concentracao: float, dose_recomendada: float) -> float:
    if peso <= 0 or concentracao <= 0 or dose_recomendada <= 0:
        raise ValueError("Todos os valores devem ser maiores que zero.")
    resultado = (peso * dose_recomendada) / concentracao
    return round(resultado, 2)

def main():
    print("-" * 40)
    print("      SafeDose CLI - Versão 1.0.0")
    print("-" * 40)
    
    try:
        peso = float(input("Digite o peso do paciente (kg): "))
        conc = float(input("Digite a concentração do remédio (mg/ml): "))
        dose = float(input("Digite a dose recomendada (mg/kg): "))
        
        ml = calcular_dosagem(peso, conc, dose)
        
        print("\n" + "=" * 40)
        print(f" RESULTADO: Aplicar {ml} ml")
        print("=" * 40)
        
    except ValueError as e:
        print(f"\n[ERRO]: Entrada inválida. {e}")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()
