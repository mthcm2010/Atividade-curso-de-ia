# chat_memoria.py — chatbot que lembra a conversa (Groq)
from llm_memoria import perguntar
from prompts import SISTEMA

MAX_MENSAGENS = 20
COMANDOS = "Comandos: ajuda | limpar | sair"


def historico_para_envio(historico: list) -> list:
    if not historico:
        return historico

    if historico[0].get("role") == "system":
        system = historico[0]
        resto = historico[1:]
        return [system] + resto[-MAX_MENSAGENS:]

    return historico[-MAX_MENSAGENS:]


def main() -> None:
    print("Chat com memória (Groq) — digite 'ajuda' para ver os comandos\n")

    historico = [{"role": "system", "content": SISTEMA}]
    total_perguntas = 0

    while True:
        pergunta = input("você> ").strip()
        comando = pergunta.lower()

        if comando == "sair":
            print(f"Até logo! Você fez {total_perguntas} pergunta(s).")
            break

        if comando == "ajuda":
            print(COMANDOS)
            continue

        if comando == "limpar":
            historico = [{"role": "system", "content": SISTEMA}]
            print("(memória da conversa limpa)")
            continue

        if not pergunta:
            continue

        historico.append({"role": "user", "content": pergunta})
        resposta = perguntar(historico_para_envio(historico))
        total_perguntas += 1
        print("ia>", resposta)
        print()
        historico.append({"role": "assistant", "content": resposta})


if __name__ == "__main__":
    main()
