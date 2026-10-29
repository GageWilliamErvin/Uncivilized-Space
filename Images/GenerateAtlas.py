# sudo apt update && sudo apt install -y python3-full python3-venv
# python3 -m venv venv
# source venv/bin/activate
# python3 GenerateAtlas.py

import os
from PIL import Image

def generate_atlas_from_layer_files(layers_dir=".", atlas_name="AllImages.atlas"):
    atlas_lines = [
        "AllImages.png",
        "size: 2048, 2048",  # Adjust canvas size as needed or compute dynamically
        "format: RGBA8888",
        "filter: Linear, Linear",
        "repeat: none"
    ]
    
    # Track current dummy packing coordinates if creating a packed sheet,
    # or use actual positions if you prefer grid/absolute layout.
    
    print(f"Scanning directory: {layers_dir}...")
    for filename in sorted(os.listdir(layers_dir)):
        if filename.endswith(".png"):
            full_path = os.path.join(layers_dir, filename)
            
            # Remove extension to get full layer name (e.g. "derpy Shielded Missile")
            layer_full_name = os.path.splitext(filename)[0]
            
            # Strip prefix (e.g. 'derpy Shielded Missile' -> 'Shielded Missile')
            parts = layer_full_name.split(' ', 1)
            sprite_name = parts[1].strip() if len(parts) > 1 else layer_full_name.strip()
            
            with Image.open(full_path) as img:
                w, h = img.size
                # If you have fixed coordinates or want to pack them:
                # For now, we can use placeholder or coordinate-based tracking
                x, y = 0, 0 # Update with your layout coordinates if known
                
            atlas_lines.extend([
                sprite_name,
                "  rotate: false",
                f"  xy: {x}, {y}",
                f"  size: {w}, {h}",
                f"  orig: {w}, {h}",
                "  offset: 0, 0",
                "  index: -1"
            ])
            print(f"Added: {sprite_name} ({w}x{h})")
            
    with open(atlas_name, "w", encoding="utf-8") as f:
        f.write("\n".join(atlas_lines) + "\n")
    print(f"\nSuccessfully generated {atlas_name}!")

if __name__ == "__main__":
    generate_atlas_from_layer_files()