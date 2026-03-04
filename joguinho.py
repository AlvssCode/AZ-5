#!/usr/bin/env python3
"""Joguinho divertido de terminal: Batalha do Tesouro."""

from __future__ import annotations

import random
import time


def digitar_lento(texto: str, atraso: float = 0.02) -> None:
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(atraso)
    print()


def barra_energia(valor: int, total: int = 10) -> str:
    cheios = "🟩" * max(valor, 0)
    vazios = "⬜" * max(total - valor, 0)
    return cheios + vazios


def duelo() -> bool:
    energia_jogador = 10
    energia_monstro = 10

    digitar_lento("\n⚔️  Um Guardião da Caverna apareceu!", 0.03)

    while energia_jogador > 0 and energia_monstro > 0:
        print("\nSua energia:   ", barra_energia(energia_jogador))
        print("Energia inimigo:", barra_energia(energia_monstro))
        print("\nEscolha seu ataque:")
        print("1) Golpe rápido (dano 1-3)")
        print("2) Golpe pesado (dano 0-5)")
        print("3) Cura mística (+2 de energia)")

        escolha = input("> ").strip()

        if escolha == "1":
            dano = random.randint(1, 3)
            energia_monstro -= dano
            digitar_lento(f"💥 Você acertou {dano} de dano!")
        elif escolha == "2":
            dano = random.randint(0, 5)
            energia_monstro -= dano
            if dano == 0:
                digitar_lento("😵 Você errou o golpe pesado!")
            else:
                digitar_lento(f"🪓 Ataque devastador! {dano} de dano!")
        elif escolha == "3":
            energia_jogador = min(10, energia_jogador + 2)
            digitar_lento("✨ Você recuperou energia!")
        else:
            digitar_lento("Escolha inválida! Você perdeu o turno...", 0.01)

        if energia_monstro <= 0:
            break

        dano_inimigo = random.randint(1, 3)
        energia_jogador -= dano_inimigo
        digitar_lento(f"👾 O guardião te acertou em {dano_inimigo}.")

    venceu = energia_jogador > 0
    if venceu:
        digitar_lento("\n🏆 Você venceu o guardião e pegou o tesouro!")
    else:
        digitar_lento("\n💀 Você foi derrotado... mas pode tentar de novo!")

    return venceu


def menu() -> None:
    while True:
        print("\n" + "=" * 40)
        print("🎮 BATALHA DO TESOURO 🎮")
        print("=" * 40)
        print("1) Jogar")
        print("2) Regras")
        print("3) Créditos")
        print("4) Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            duelo()
        elif opcao == "2":
            print("\n📜 Regras:")
            print("- Derrote o guardião antes de ficar sem energia.")
            print("- Use ataques diferentes e se cure no momento certo.")
            print("- O jogo é aleatório: cada partida é única!")
        elif opcao == "3":
            print("\nFeito por você + GPT-5.2-Codex 😄")
            print("Roda direto no terminal com: python3 joguinho.py")
        elif opcao == "4":
            digitar_lento("Até a próxima, aventureiro(a)! 👋", 0.02)
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    random.seed()
    menu()
