from pathlib import Path
from compiler.compiler import compile_metadex

def test_compile_smoke(tmp_path):
    src = Path("source_yaml")
    out = tmp_path / "metadex.json"
    compile_metadex(str(src), str(out))
    assert out.exists()
