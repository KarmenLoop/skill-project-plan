"""Build a dependency-aware plan with measurable acceptance criteria."""
from runtime import *

def process(data):
    rows=records(data,"tasks")
    ids=unique(rows)
    tasks={r["id"]:dict(r) for r in rows}
    for row in rows:
        text(row.get("title"),"title")
        text(row.get("acceptance"),"acceptance")
        number(row.get("duration"),"duration",0.000001)
        deps=strings(row.get("depends_on"),"depends_on")
        if len(set(deps))!=len(deps): raise ValueError("duplicate dependency")
        if set(deps)-ids: raise ValueError("unknown dependency")
    done={}
    ordered=[]
    while len(done)<len(tasks):
        ready=sorted(k for k,t in tasks.items() if k not in done and set(t["depends_on"])<=set(done))
        if not ready: raise ValueError("dependency cycle")
        for ident in ready:
            row=tasks[ident]
            parent=max(row["depends_on"],key=lambda k:done[k]["finish"],default=None)
            start=done[parent]["finish"] if parent else 0
            result=dict(row,earliest_start=start,finish=start+row["duration"])
            done[ident]=result
            ordered.append(result)
    last=max(done,key=lambda k:done[k]["finish"],default=None)
    path=[]
    while last is not None:
        path.append(last)
        last=max(tasks[last]["depends_on"],key=lambda k:done[k]["finish"],default=None)
    return {"ordered_tasks":ordered,"critical_path":path[::-1],"estimated_duration":max((x["finish"] for x in ordered),default=0)}

if __name__ == "__main__":
    sys.exit(main(process, "Build a dependency-aware plan with measurable acceptance criteria."))
