import random, re

# Genera un número aleatorio de Pokémon (1 - 898)
pokemon_id = random.randint(1, 898)
sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"

# Lee el README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Define marcas
start = "<!--START_SECTION:pokemon-->"
end = "<!--END_SECTION:pokemon-->"
new_content = f"{start}\n![Pokemon]({sprite_url})  \n{end}"

# Reemplaza el bloque existente
updated_readme = re.sub(f"{start}.*?{end}", new_content, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)

print(f"Pokémon actualizado a #{pokemon_id} 🐾")
