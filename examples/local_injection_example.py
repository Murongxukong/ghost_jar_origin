# local_injection_example.py
# Example: Using GhostJarOriginModule in a local symbolic AI context

from ghost_jar_origin import GhostJarOriginModule

# Step 1: Initialize the module
gj = GhostJarOriginModule()

# Step 2: Narrate the origin
origin_text = gj.narrate_origin()
print(origin_text)

# Step 3: Confirm alignment state
if gj.confirm_alignment():
    print("\n✅ Alignment confirmed. AI may now begin symbolic logic generation.")
else:
    print("\n⚠️ Protocol not initialized correctly.")
