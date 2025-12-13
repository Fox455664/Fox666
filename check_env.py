import sys

print("🔹 Python executable:", sys.executable)
print("🔹 Python version:", sys.version)
print("\n🔹 Python library paths:")
for p in sys.path:
    print("  -", p)

try:
    import pytgcalls
    print("\n✅ py_tgcalls is installed and accessible!")
except ModuleNotFoundError:
    print("\n❌ py_tgcalls is NOT accessible in this Python environment!")