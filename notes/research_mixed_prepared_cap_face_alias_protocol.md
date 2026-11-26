# Fixed face and alias bounds for the prepared three-four cap

Unexecuted protocol and source formulas, 7 November 2026. The
[completed critical-existence theorem](research_mixed_fourier_boundary_critical_existence.md)
identifies the original prepared root. The
[full-source criterion](research_mixed_prepared_cap_full_source_criterion.md)
leaves eight real faces and eight single-height aliases, all strictly
concave in their free real coordinates. This protocol bounds those
sixteen complete domains by supporting planes. A trial need not be
stationary, and no further root-existence assertion is used for it.
No proposal, analytic function, optimizer or gain has been evaluated.

The action comparison will use a separate certified interval for the
original prepared action. The paired-kernel action is not an input.
The protocol and all literal input hashes must be frozen and fully
reviewed before any execution. There is one prescribed pass, with
no fallback, precision change, refinement or retry.

## 1. Exact collapsed phase and its endpoint branch

Keep the coordinate order \((s,t,p,q)\), real box and heights
\[
\begin{split}
 C&=[27/100,49/100]\times[11/50,1/2]\times[1/5,21/50]^2,\\
 h_-&=(-11/200,-9/125,-51/500,-51/500),\\
 h_+&=(1/25,21/1000,3/200,3/200).
\end{split}
\tag{1}
\]
The exact row interpolation, strict Hessian, gradient strips and all
source branches hold on the product of these intervals by
[the typed-height theorem](research_mixed_prepared_cap_typed_height_rectangle.md).
Its endpoint coordinate is the original holomorphic function
\[
\begin{split}
 d(s)&=1-2e^{2\pi is},&
 \omega(s)&=\frac{i+\sqrt{d(s)}}2,\\
 u_c(s)&=
 \frac{\operatorname{Log}(1+i\omega(s))
              -\operatorname{Log}(1-i\omega(s))}{2\pi i}.
\end{split}
\tag{2}
\]
These are the continued branches of the
[endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md).
On its whole rectangle, \(\Re d>1\), the square root has positive
real part, both logarithm arguments have positive real part, and
\[
 0<\Re u_c(s)<\Re s<1/2,\qquad \Im u_c(s)>0.
\tag{3}
\]
For the positive-real-part assertion in (2), write
\(\sqrt d=a+ib\). The argument \(2\pi\Re s\) lies in
\((\pi/2,\pi)\), so \(b<0\). Also
\(|\Im d|<3\): here \(e^{-2\pi\Im s}\le e^{.11\pi}<3/2\).
Thus \(b^2<|\Im d|/2<3/2\), hence \(-2<b<0\).
Consequently
\(\Re(1+i\omega)=(1-b)/2>0\) and
\(\Re(1-i\omega)=(3+b)/2>0\).
For example \(e^{.11\pi}<3/2\) follows from
\(.11\pi<.35\) and the positive-series estimate
\(e^x\le1+x+x^2/[2(1-x/3)]\) at \(x=.35\).
No unrelated arctangent branch is selected.

The original primitive is
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad g'(z)=\operatorname{Log}(1-e^{-2\pi iz}),
 \qquad g''(z)=\frac{2\pi i e^{-2\pi iz}}{1-e^{-2\pi iz}},
\tag{4}
\]
on \(0<\Re z<1\). Its normalization agrees with
\(g=J+\pi i(z-z^2)/2\) and \(g(0)=0\).
The principal dilogarithm formula is used only on this original
regular strip.

Put \(u=u_c(s)\), \(K=e^{2\pi ix_0}\), \(Q=e^{-2\pi iq}\).
The collapsed original prepared phase is exactly
\[
\begin{split}
 F={}&-2g(1/2-u)-3g(u)-g(s-u)
       +g(s+t)+g(t+p)+g(p+q)\\
    &-2g(t)-3g(p)-g(q)
       +\pi i(1/4+u-3u^2+2su+2tp)\\
    &+(q-1/2)\operatorname{Log}K
       -\frac{\operatorname{Li}_2(KQ)-\operatorname{Li}_2(K)}
                    {2\pi i}.
\end{split}
\tag{5}
\]
In particular the constant \(i\pi/4\) is retained. To check (5),
replace every \(J(z)\) in the original endpoint action
\[
 -2J(1/2-u)-3J(u)-J(s-u)+\pi isu
                  -\frac{\pi i}{2}(s-s^2)
\]
by \(g(z)-\pi i(z-z^2)/2\). The remaining polynomial is
\(\pi i(1/4+u-3u^2+2su)\). The incidence in the last line of
(5) is exactly \(\ell_q(x_0)\), since the original branch has
\(\operatorname{Log}K=2\pi ix_0\). This proves the complete
phase identity, including its additive constant.

Endpoint stationarity is used only to differentiate this explicitly
collapsed phase. The four derivatives are
\[
\begin{split}
 F_s&=g'(s+t)-g'(s-u)+2\pi iu,\\
 F_t&=g'(s+t)+g'(t+p)-2g'(t)+2\pi ip,\\
 F_p&=g'(t+p)+g'(p+q)-3g'(p)+2\pi it,\\
 F_q&=g'(p+q)-g'(q)+\operatorname{Log}K-\operatorname{Log}(1-KQ).
\end{split}
\tag{6}
\]
They hold at every trial in (1), not only at the prepared critical
point. They are the original derivatives in
[the critical-curve theorem](research_mixed_prepared_three_four_cap_critical_curve.md).

For the untrusted proposal calculation only, the full holomorphic
Hessian is explicit. Write
\[
\begin{split}
 B_{uu}&=-2g''(1/2-u)-3g''(u)-g''(s-u)-6\pi i,\\
 B_{su}&=g''(s-u)+2\pi i.
\end{split}
\]
Its diagonal entries are
\[
\begin{split}
 F_{ss}&=g''(s+t)-g''(s-u)-B_{su}^2/B_{uu},\\
 F_{tt}&=g''(s+t)+g''(t+p)-2g''(t),\\
 F_{pp}&=g''(t+p)+g''(p+q)-3g''(p),\\
 F_{qq}&=g''(p+q)-g''(q)-2\pi iKQ/(1-KQ).
\end{split}
\tag{7}
\]
The only off-diagonal entries are the symmetric adjacent ones
\[
 F_{st}=g''(s+t),\qquad
 F_{tp}=g''(t+p)+2\pi i,\qquad
 F_{pq}=g''(p+q).
\tag{8}
\]
The endpoint Schur complement in (7) follows from
\(u_c'=-B_{us}/B_{uu}\); the original endpoint theorem makes
\(B_{uu}\ne0\). The rigorous certificate below does not need a
new interval Hessian bound: it uses the already proved concavity.

## 2. Exactly sixteen whole domains

First list the eight faces of \(C\), in coordinate order
\(s,t,p,q\), lower then upper face. Their height vector is zero.
The fixed face coordinate is exactly its rational endpoint; the
other three coordinates range independently over their whole intervals
in (1).

Next list the eight aliases in the same coordinate/sign order.
For the alias indexed by \((j,\pm)\), all four real coordinates
range over \(C\), and its fixed height vector is
\(h_{j,\pm}e_j\). Its rate has the original debit
\(2\pi|h_{j,\pm}|\). No other height, target restriction or
source profile is introduced.

Each function in this list is strictly concave in its free real
coordinates. There are no omitted faces, aliases, support corners
or boundary maximizers. The source criterion separately pays all
common-height joins and all vertical currents. Its far physical
ceiling remains exactly \(146/75\).

## 3. Fixed untrusted proposals

Use CPython's binary64 float and complex arithmetic and its standard
math/cmath elementary functions for every untrusted proposal. Require
the binary64 format explicitly, and record the Python version and
platform. These arithmetic choices have no proof role; every final
rational trial is independently evaluated by Arb/Acb as specified
below.

For each domain, start at the midpoint of every free real interval.
Keep its prescribed fixed coordinate, if any, and fixed heights
unchanged. Perform exactly 32 floating-point Newton proposals using
the real parts of (6)--(8), restricted to the three or four free
coordinates. Each step solves
\[
       (\Re F'')_{\mathrm{free,free}}\,\Delta
                              =(\Re F')_{\mathrm{free}},
\]
then replaces the free vector by its current value minus
\(\alpha\Delta\), with \(\alpha=1/2\) for the first eight
steps and \(\alpha=1\) for the last 24. Clamp each free coordinate
to its interval inset by \(10^{-8}\). Use deterministic partial
pivoting, with the first row winning a tie. There is no convergence
test, line search, alternative starting point or changed damping.

The proposal uses only the center of the old interface-root square
to form a floating approximation of \(K\). This is explicitly
untrusted; the rigorous evaluation uses the entire square.
After the last step, round each free coordinate to the nearest
multiple of \(10^{-12}\), with a fixed ties-to-even rule applied
to the exact rational value of the binary64 number. Implement this
by converting the float with Fraction.from_float before multiplying
by \(10^{12}\); do not first round a floating scaling product.
Keep every fixed face coordinate exactly rational. Verify that the
result is in its complete domain. Record all 32 steps, including
gradients, restricted Hessians, solves, clamping and the final
rational point. A failure is recorded; it supplies no alternative
proposal.

The maximum proposal inventory is 16 cases times 32 derivative
evaluations, or 512. These evaluations use (2), (4), (6)--(8),
with the nine primitive exponentials reused inside each evaluation.
They require at most 5,120 floating exponentials, 512 floating
square roots and 5,120 floating logarithms, plus one cached
floating logarithm of the proposed \(K\). There are no proposal
dilogarithms or phase-value searches.

## 4. One rigorous value and gradient per domain

Use Arb/Acb at exactly 256 bits. The original interface record is
[research-three-four-source-interface.json](../repro/results/research-three-four-source-interface.json),
with its original writer. Retain the complete rational root square
and form \(K=(1+2a-4a^2)^{-1}\) outward, as in the successful
boundary-update test. Never replace its certified radius by zero.
Compute one enclosure each of \(\pi\), \(\operatorname{Log}K\)
and \(\operatorname{Li}_2(K)\).

At each exact rational proposal, evaluate (2), then (5)--(6).
Construct every rational input outward and save its endpoint
containment. Before each square root or logarithm require its
stated branch guard on the complete containing rectangle.
In particular check \(\Re d>1\), the positive real part of its
principal square root and both endpoint logarithm arguments, and
the endpoint chamber (3). Require all nine primitive arguments
\[
        1/2-u,\ u,\ s-u,\ s+t,\ t+p,\ p+q,\ t,\ p,\ q
\tag{9}
\]
to remain in their original strips, with their exponential images
off the principal dilogarithm cut and their \(g'\) logarithm
arguments on the original branch. Require the full containing
root and outgoing products to satisfy \(|K|<1\) and
\(|KQ|<7/10\), using outward or exact rational squared-modulus
bounds. There is no clipping of a failed rectangle.

Each case uses nine primitive exponentials and dilogarithms,
seven \(g'\) logarithms, one endpoint exponential, one endpoint
square root, two endpoint logarithms, and the outgoing dilogarithm
and logarithm. The outgoing \(Q\) is the already evaluated
exponential for \(g(q)\). The exact maximum rigorous analytic
inventory is therefore
\[
 \begin{array}{c|r}
 \pi&1\\
 \text{complex exponentials}&160\\
 \text{principal square roots}&16\\
 \text{principal logarithms}&161\\
 \text{principal dilogarithms}&161
 \end{array}
\tag{10}
\]
or 499 calls. A domain failure can prevent later calls on that
case; attempted and completed counts must be retained. All sixteen
original cases are still visited once. No interval root solve,
gain evaluation or new Hessian certification is performed.

Let \(y\) denote the exact rational real proposal and \(h\) its
prescribed height. Suppose the saved intervals give
\[
 \Re F(y+ih)\le f_+,\qquad
       \Re F_j(y+ih)\in[g_{j,-},g_{j,+}].
\]
For the complete target interval \([L_j,R_j]\), including a
singleton in a fixed face coordinate, set
\[
 S_j=\max\{g_{j,-}(L_j-y_j),g_{j,-}(R_j-y_j),
           g_{j,+}(L_j-y_j),g_{j,+}(R_j-y_j)\}.
\tag{11}
\]
All these are exact rational operations on saved interval endpoints.
The certified upper for this entire domain is
\[
          U=f_++\sum_{j=1}^4S_j
                       -2\pi_-\sum_{j=1}^4|h_j|,
\tag{12}
\]
where \(\pi_-\) is the saved lower endpoint. Physical faces have
\(h=0\). Retain all four support terms, even when a fixed face
term is exactly zero. Strong concavity proves the supporting-plane
bound at the actual original \(K\). The larger root square is
used only to enclose its value and derivatives; no new reference
family is asserted by evaluating that square.

## 5. Prepared action input and complete outcome

The separate input will be
[research-mixed-prepared-cap-action.json](../repro/results/research-mixed-prepared-cap-action.json),
from the independently reviewed original residual/action proof.
It must have successful status and current before/after source
bindings. Its full interface root and original \(K\) association
must agree with those used above. The planned exact fields are
\[
 \text{action\_enclosure.real}=[M_-,M_+],\qquad
                  \text{M\_lower\_rational}=M_-.
\]
The consumer must verify their equality and the recorded enlargement
of the proposal action by \(60r^2\), with the same certified radius
\(r\). This is an inherited action proof, not a reevaluation or a
new root selection. The input's writer, proof, successful record and
all inherited bindings will be pinned before this protocol is frozen
for execution.

Let \(U_{\mathrm{face}}\) and \(U_{\mathrm{alias}}\) be the two
maxima of the eight exact uppers (12). Save every individual upper,
including any positive or failed comparison, and form
\[
 U_{\mathrm{all}}=\max\{146/75,U_{\mathrm{face}},U_{\mathrm{alias}}\},
                  \qquad \delta=M_--U_{\mathrm{all}}.
\tag{13}
\]
The complete sign test succeeds exactly when all sixteen certificates
are valid and \(\delta>0\). Save \(\delta\) as an exact rational,
without replacing it by a threshold selected after evaluation.
Failure of this sufficient comparison is inconclusive for the
actual source; it is not a counterexample to its asymptotic.

The future evaluator is
[check_mixed_prepared_cap_face_alias_budget.py](../experiments/check_mixed_prepared_cap_face_alias_budget.py);
its sole prescribed output is
[research-mixed-prepared-cap-face-alias-budget.json](../repro/results/research-mixed-prepared-cap-face-alias-budget.json).
Neither file has been executed or any output generated by this note.
The output must be absent and opened exclusively. Bind this protocol,
the source/branch/typed-height/full-source proofs, the original root
record and writer, and the prepared-action proof, writer and record,
before any proposal or analytic call. Bind the evaluator itself and
recheck every input afterward.

Save all cases and iteration histories, exact domains, rational input
conversions, analytic argument and branch witnesses, value/gradient
enclosures, all signed products in (11), the separate debit, all
maxima and action comparisons, attempted/completed inventories and
every stage-specific failure. A provenance or arithmetic error
invalidates the complete conclusion. A failed comparison never
causes a replacement trial, dropped case or second run.

If the single fixed test succeeds, it discharges the two remaining
inequalities of the full-source criterion for this prepared cap.
The common-height joins, all 624 split lattice corrections and the
true physical endpoints are already covered by that criterion.
The resulting theorem is local in the outgoing Fourier variable;
no whole-period envelope, arbitrary-message propagation or
knot-family conclusion follows from these sixteen comparisons.
