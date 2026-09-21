from pathlib import Path
import pandas as pd
from src.quality.validate import validate
from src.transform.build_gold import build

def test_quality_and_gold_pipeline(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    raw=Path('data/raw'); raw.mkdir(parents=True)
    pd.DataFrame([{'customer_id':100001,'customer_name':'Test User','city':'Vadodara','state':'Gujarat','plan':'Postpaid','join_date':'2026-01-01','status':'Active'}]).to_csv(raw/'customers.csv',index=False)
    pd.DataFrame([{'recharge_id':'R0000001','customer_id':100001,'recharge_date':'2026-02-01','amount':499,'payment_mode':'UPI'}]).to_csv(raw/'recharge.csv',index=False)
    pd.DataFrame([{'usage_id':'U0000001','customer_id':100001,'usage_date':'2026-02-01','data_used_gb':5.0,'call_minutes':100,'sms_count':10}]).to_csv(raw/'usage.csv',index=False)
    pd.DataFrame([{'complaint_id':'C000001','customer_id':100001,'complaint_date':'2026-02-01','issue_type':'Network Issue','status':'Resolved','resolution_days':2}]).to_csv(raw/'complaints.csv',index=False)
    validate(); build()
    gold=pd.read_csv('data/processed/customer_360.csv')
    assert len(gold)==1
    assert gold.loc[0,'total_recharge']==499
    assert gold.loc[0,'total_data_gb']==5.0
