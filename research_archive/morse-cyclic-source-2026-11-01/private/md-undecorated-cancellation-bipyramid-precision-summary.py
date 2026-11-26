#!/usr/bin/env python3
"""Summarize finite signed diagnostics and independent precision replays."""
import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args();root=args.directory;mp.mp.dps=240
    prefix='md-undecorated-cancellation-bipyramid-'
    names=['final-results.json','diagnostic-100-all-results.json','final-extended-results.json',
           'diagnostic-odd-extended-results.json','final-220-results.json']
    files={name:json.loads((root/(prefix+name)).read_text()) for name in names}
    def keyed(data):return {(r['N'],r['case']):r for r in data['cases']}
    base=keyed(files[names[0]]);low=keyed(files[names[1]])
    higher={**base,**keyed(files[names[2]]),**keyed(files[names[3]])}
    high=keyed(files[names[4]])
    def compare(a,b):
        checked=0;identical=0;worst=mp.mpf(0);zero=[]
        for key in sorted(a.keys()&b.keys()):
            for field in ('FULL','CROSS','difference'):
                x,y=mp.mpf(a[key][field]['value']),mp.mpf(b[key][field]['value'])
                if not y:
                    zero.append(dict(N=key[0],case=key[1],field=field,lower_value=str(x),higher_value='0'))
                    continue
                err=abs(x-y)/abs(y)
                worst=max(worst,err);checked+=1;identical+=(err==0)
        return dict(nonzero_quantities_compared=checked,
                    identical_at_all_80_stored_significant_digits=identical,
                    worst_relative_discrepancy=str(worst),zeros_reported_separately=zero,
                    qualification='Agreement of stored 80-digit values is a precision diagnostic, not an interval-arithmetic error certificate.')
    combined={**higher,**high}
    endpoint_max=[]
    for N in range(3,13):
        rows=[r for (n,_),r in base.items() if n==N and all(x in ('-2','2') for x in r['spectra'])]
        best=max(rows,key=lambda r:mp.mpf(r['difference']['log_abs_over_N_minus_Phi']) if r['difference']['log_abs_over_N_minus_Phi'] is not None else mp.ninf)
        endpoint_max.append(dict(N=N,case=best['case'],spectra=best['spectra'],
                                 signed_difference=best['difference']['value'],
                                 log_abs_difference_over_N_minus_Phi=best['difference']['log_abs_over_N_minus_Phi']))
    cancellation=[]
    for (N,name),r in combined.items():
        peak=mp.mpf(r['max_intermediate_abs'])
        for field in ('FULL','CROSS','difference'):
            value=mp.mpf(r[field]['value'])
            if value and abs(value)>peak*mp.mpf('1e-120'):
                cancellation.append((max(mp.mpf(0),mp.log10(peak/abs(value))),N,name,field))
    cancellation.sort(reverse=True)
    artifacts=[]
    for name in names:
        path=root/(prefix+name)
        artifacts.append(dict(file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              run_script_sha256=files[name]['script_sha256'],precision=files[name]['precision_digits']))
    script=root/(prefix+'diagnostic.py')
    output=dict(status='finite_precision_comparison_complete',
                Phi=files[names[0]]['Phi'],volume_normalization=files[names[0]]['actual_drilled_volume'],
                primary_tuples=650,primary_endpoint_tuples=640,primary_interior_tuples=10,
                distinct_tuples_including_extensions=len(combined),
                exact_integer_checks_N3=len(files[names[0]]['exact_integer_level_three_checks']),
                independent_homogeneous_coefficient_checks=len(files[names[0]]['independent_multivariate_coefficient_checks']),
                local_resolvent_polynomial_coefficients_checked=sum(x['polynomial_coefficients'] for x in files[names[0]]['local_identity_checks']),
                max_relative_local_resolvent_error=max(float(x['relative_band_identity_error']) for x in files[names[0]]['local_identity_checks']),
                precision_100_vs_160=compare(low,base),precision_160_vs_220=compare(higher,high),
                largest_endpoint_remainder_by_level=endpoint_max,
                largest_peak_to_answer_digit_ratios=[dict(digits=str(t),N=N,case=name,quantity=f) for t,N,name,f in cancellation[:12]],
                cancellation_qualification='Peak means largest stored partial transfer entry, not a sum of absolute paths or a rigorous condition number.',
                sampled_remainder_rates_all_below_Phi=all(mp.mpf(r['difference']['log_abs_over_N_minus_Phi'])<0 for r in combined.values() if r['difference']['log_abs_over_N_minus_Phi'] is not None),
                current_runner_sha256=hashlib.sha256(script.read_bytes()).hexdigest(),artifacts=artifacts,
                limitation='Finite endpoint and selected interior evaluations do not estimate the continuous spectral supremum or prove a uniform exponential gap.')
    dest=root/(prefix+'precision-summary.json');dest.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('artifacts','largest_endpoint_remainder_by_level','largest_peak_to_answer_digit_ratios')},indent=2))


if __name__=='__main__':main()
