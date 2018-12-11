from pathlib import Path

res_semester  = ["templates"]
res_arcc      = ["templates"]
res_notebooks = ["templates"]

res_semester  = {k: f"{k}/semester/" for k in res_semester}
res_arcc      = {k: f"{k}/arcc/" for k in res_arcc}
res_notebooks = {k: f"{k}/notebooks/" for k in res_notebooks}

res_semester  = {k: Path(f"admin/{v}") for k, v in res_semester.items()}
res_arcc      = {k: Path(f"admin/{v}") for k, v in res_arcc.items()}
res_notebooks = {k: Path(f"admin/{v}") for k, v in res_notebooks.items()}

resources = {
    "sem" : Path("admin/templates/semester/"),
    "arcc": Path("admin/templates/arcc/"),
    "ntbk": Path("admin/templates/notebooks/"),
}


def res_gen(key, pth):
    return resources[key].joinpath(pth)