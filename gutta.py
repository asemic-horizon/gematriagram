import pyoeis
import unicodedata
from gematria import gematria, gematrix

oeis = pyoeis.OEISClient()

def oeis_lookup(query):
    res = oeis.lookup_by(prefix="",query=query, max_seqs = 3, list_func = True)
    fmt_examples = lambda xs: ','.join([x.replace(":","\n").replace(";","\n").strip("...").strip("--") for x in xs])
    ans = [f"[{r.id}] {r.name} ({r.author.strip('_')}):\n {fmt_examples(r.examples)}" for r in res]
    if ans == []:
        return f"No results found for {query}"
    else:
        return "\n\n".join(ans)
