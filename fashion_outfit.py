import random

tops = ["neon green crop top", "sequined blazer", "tie-dye hoodie", "leopard print tank top", "polka dot shirt"]
bottoms = ["striped pants", "glittery skirt", "plaid shorts", "floral leggings", "denim overalls"]
shoes = ["rainbow sneakers", "cowboy boots", "platform sandals", "fur-lined slippers", "neon yellow high heels"]
accessories = ["giant sombrero", "inflatable flamingo floatie", "LED sunglasses", "feather boa", "unicorn horn headband"]

def generate_outfit():
    top = random.choice(tops)
    bottom = random.choice(bottoms)
    shoe = random.choice(shoes)
    accessory = random.choice(accessories)
    outfit = f"Top: {top}\nBottom: {bottom}\nShoes: {shoe}\nAccessory: {accessory}"
    return outfit

if __name__ == "__main__":
    print("Your ridiculous fashion outfit is:")
    print(generate_outfit())
