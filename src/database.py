from supabase import create_client, Client

URL_SUPABASE = "https://nnhfngiyjuyrffnqfxfi.supabase.co/rest/v1/"
CHAVE_SUPABASE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5uaGZuZ2l5anV5cmZmbnFmeGZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0NjU4MzUsImV4cCI6MjA5NzA0MTgzNX0.ZPxcoHHjQrYqfUDObEr5J4qRHceW-6IRPfvXr3G31eE"

def conectar_banco() -> Client:
    try:
        conexao: Client = create_client(URL_SUPABASE, CHAVE_SUPABASE)
        return conexao
    except Exception as e:
        print(f"Erro ao conectar na nuvem: {e}")
        return None

if __name__ == "__main__":
    banco = conectar_banco()
    if banco:
        print("✓ Conexão com o Supabase estabelecida com sucesso!")