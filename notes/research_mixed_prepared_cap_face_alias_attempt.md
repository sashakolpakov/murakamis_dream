# Prepared cap: one genuine physical-face obstruction

Saved-data assessment, 7 November 2026. The prescribed sixteen-case
comparison encloses every case, proves fifteen strict inequalities, and
fails at the upper private-index face. The failure is an actual excess
of the real physical rate at a saved rational point. It is not caused
by interval width or by a loose tangent support. This does not establish
an obstruction to the original signed prepared source.

## 1. Immutable inputs and exact saved arithmetic

The sole comparison record is
[research-mixed-prepared-cap-face-alias-budget.json](../repro/results/research-mixed-prepared-cap-face-alias-budget.json),
SHA-256
`ad1b0c1b0bf81aba86335584c65800c2e891dff84ba0b5f787a63bc4df986545`.
Its writer is
[check_mixed_prepared_cap_face_alias_budget.py](../experiments/check_mixed_prepared_cap_face_alias_budget.py),
SHA-256
`4edd3da78c86d8acc699e6ca73acb54bdca6d37325641a300c9836f9cb829b7e`;
its fixed [protocol](research_mixed_prepared_cap_face_alias_protocol.md)
has SHA-256
`0340e96f1ab5add62dc15358be1804a77f19ed8a1ca9070bfa2c1fbbca6d8720`.

The original critical action comes from
[research-mixed-prepared-cap-action.json](../repro/results/research-mixed-prepared-cap-action.json),
SHA-256
`271c82db6397ef6de1749ff05a75faba9b94f318587f2765d0aaf7126a373239`.
Write its certified real enclosure as \([M_-,M_+]\). Exact rational
comparison of the saved endpoints gives
\[
 2.120165258<M_-\le M:=\Re\Phi_{\rm cap}\le M_+<2.120165259.
 \tag{1}
\]
The original root square, its action uncertainty, and the quadratic
\(60\cdot10^{-32}\) action error are all retained.

The assessment checks all thirty-eight input hashes against the current
files and the unchanged before/after manifest. It checks the ordered
eight-face/eight-alias inventory, original target intervals, heights,
and trial membership. For each case it recombines the four signed
support terms from all sixteen saved rational products, then subtracts
the saved lower alias penalty. All 256 products and all sixteen upper
bounds agree exactly with the record; their recorded gaps are exactly
\(M_- - U\). These checks use rational arithmetic only. No analytic
function, proposal, optimizer, or source evaluation is repeated.

The record has `visited_cases = valid_cases = 16` and
`full_inventory_completed = true`, with no domain failure. Its
`pending_cases` field retains the initial sixteen case descriptions;
that stale metadata field does not describe an unfinished computation.
Completeness here is checked from the actual sixteen-case inventory.
The frozen record is left unchanged.

## 2. A lower witness above the original action

Let
\[
 C=[.27,.49]\times[.22,.5]\times[.2,.42]^2.
\]
Case `face:s:upper` uses the exact real trial
\[
 z_0=(s,t,p,q)=
 \left(\frac{49}{100},\frac{14469681533}{50000000000},
       \frac{282866188799}{10^{12}},
       \frac{122983533}{400000000}\right).
 \tag{2}
\]
All coordinates other than \(s\) are strictly interior to their
target intervals, and
\(s+t<1\), \(t+p<1\), \(p+q<1\). Thus this is a regular,
supported physical point, not a prohibited sum-\(N\) face.

The saved analytic phase interval, **before** adding any tangent
support terms, proves the exact decimal inequalities
\[
 2.136852869<\Re\mathcal F_{\rm cap}(z_0)<2.136852870,
 \qquad
 \operatorname{width}\bigl(\Re\mathcal F_{\rm cap}(z_0)\bigr)
      <10^{-23}.
 \tag{3}
\]
Here (3) means containment of the entire saved outward interval; it is
not a rounded midpoint assertion. Equations (1)--(3) imply
\[
 \Re\mathcal F_{\rm cap}(z_0)-M
 >2.136852869-2.120165259>\frac1{60}.
 \tag{4}
\]
In particular a sharper tangent, a better maximizer, or greater
arithmetic precision cannot prove that this face lies below \(M\).

On the real supported domain the original phase has real part exactly
\(E_\lambda\), equation (3) of
[the coherent physical-tail reduction](research_mixed_prepared_cap_physical_tail_reduction.md).
Continuity and (4) give an open supported region with
\(s>.49\), arbitrarily close to \(z_0\), on which
\(E_\lambda>M+1/100\). The full real-index coefficient theorem
used there has a nonzero leading amplitude on compact middle
intervals. Together with the ordinary factorial and outgoing
Pochhammer asymptotics, it therefore realizes this rate in the modulus
of supported physical rows, up to polynomial factors, along lattice
points approaching that region in both level parities.

Consequently the proposed absolute physical-tail bound below \(M\)
is false for this decomposition. This concerns the modulus of rows
after the already coherent endpoint coefficient, but before summing
the remaining private index. It does **not** give a lower bound on
their signed sum or contradict a full prepared-source asymptotic.

## 3. The fifteen surviving comparisons

The exact recombination gives the following uniform lower margins
relative to \(M_-\), hence also relative to the true action \(M\).

| Compared set | Number | Strict gap | Limiting recorded case |
|---|---:|---:|---|
| Other real faces of \(C\) | 7 | \(>1/400\) | `face:t:lower` |
| Single-coordinate horizontal aliases | 8 | \(>1/20\) | `alias:p:upper` |
| Far physical ceiling \(146/75\) | 1 | \(>17/100\) | fixed ceiling |

For orientation, outward rational decimal ceilings for the two
limiting passing bounds are
\[
 U_{t,\mathrm{lower}}\le2.117306773049,
 \qquad U_{p,\mathrm{upper\ alias}}\le2.067984226018.
 \tag{5}
\]
All other saved positive and negative comparisons remain visible in
the immutable source record. In particular the failed face is not
deleted from the maximum. The full-source criterion in
[the contour reduction](research_mixed_prepared_cap_full_source_criterion.md)
is still not discharged.

## 4. Where cancellation must be retained

The [literal prepared-source identity](research_mixed_prepared_three_four_cap_source.md)
already permits performing the entire first private-index sum before
modulus. In its original notation,
\[
 \begin{split}
 G_{34,N}(y,w)=\kappa_N^3N c_y
 \sum_{\substack{j+k<N\\k+\ell<N}}
 U_{0,N}(w,r^j)
 \frac{Y^\ell Q^{jk}P_{j+k}P_{k+\ell}}
 {P_jP_k^3P_\ell(Y;r)_{\ell+1}}.
 \end{split}
 \tag{6}
\]
This exact finite sum includes the upper-\(s\) physical tail and the
central private-index contribution together. It introduces no
additional Fourier alternative. Accordingly a proof using (6), or an
equivalent staged contour identity which combines its upper private
tail and artificial joining face before modulus, can avoid the
obstruction (4). It must establish its own source continuation,
current bounds, and remainder estimates; the present fifteen passed
inequalities alone do not supply those conclusions.

The outcome is thus a rigorous diagnosis of one failed decomposition,
with fifteen reusable estimates, and no claim of a completed prepared
kernel, arbitrary boundary propagation, or a larger knot class.
