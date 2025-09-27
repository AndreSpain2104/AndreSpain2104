import requests
import random
import re

# obtener un pokemon aleatorio
pokemon_id = random.randint(1, 898)  # primera gen hasta 898
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
data = requests.get(url).json()

name = data["name"].capitalize()
sprite = data["sprites"]["front_default"]

# actualizar README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

new_section = f"![{name}]({sprite})\n\n*" + f"Pokémon del día: **{name}***"

# reemplazar bloque viejo entre <!-- POKEMON --> ... <!-- END POKEMON -->
readme = re.sub(
    r"<!-- POKEMON -->.*?<!-- END POKEMON -->",
    f"<!-- POKEMON -->\n{new_section}\n<!-- END POKEMON -->",
    readme,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
