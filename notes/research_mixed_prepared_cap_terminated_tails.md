# Two private tail faces in the terminating prepared-cap chart

Research deduction, 7 November 2026. Inside the original three outer
index intervals, the new terminating chart has only two private
real-face comparisons. Its entire upper-half Newton tail already
has a strict elementary gap below the certified prepared action.
The outer-index complement must be kept coherent in its first cap;
this note makes that separation exact. There is no new numerical
evaluation or proposed parameter cover.

Use the whole finite source and phase \(\widetilde F\) of
[the terminating-chart theorem](research_mixed_prepared_cap_terminated_chart.md).
Let
\[
 C_3=[.22,.5]\times[.2,.42]^2,\qquad
 C_{\rm new}=[.1,.4]\times C_3,\qquad
 M=\Re\Phi_{\rm cap}(x_0,-2).
 \tag{1}
\]
The completed original action record
[research-mixed-prepared-cap-action.json](../repro/results/research-mixed-prepared-cap-action.json),
SHA-256
\(\mathtt{271c82db6397ef6de1749ff05a75faba9b94f318587f2765d0aaf7126a373239}\),
in particular proves \(M>53/25\). We use only that already
certified lower bound.

## 1. Exact order of grouping and the physical rate

First partition the exact finite sum by whether
\((j,k,l)/N\in C_3\). On the complementary part, keep the
entire first cap \(U_{0,N}(w,r^j)\) in the original prepared
three-index formula; do not take absolute values inside its
terminating \(a\)-sum. On the part in \(C_3\), use the
exact terminating identity and partition \(u=a/N\) into
\([0,.1]\), \([.1,.4]\), \([.4,.5]\), and \([.5,1-t]\),
always intersected with its actual physical support.
Overlapping endpoints can be assigned to either neighboring piece.
This is an exact partition of the original finite source.

At complete ordinary color, the zero-safe physical row upper rate
on this latter part is
\[
 \begin{split}
 \widetilde E(u,t,p,q)&=Q(t,u)+R(t,p,q),\\
 Q(t,u)&=\mathcal V(u)+J(u+t)-2J(u)-2J(t),\\
 R(t,p,q)&=V_{\mathbb R}(t,p)+V_{\mathbb R}(p,q)-J(p)
                   -\tfrac12\log\rho+L(q),\\
 V_{\mathbb R}(x,z)&=J(x+z)-J(x)-J(z),\\
 L(q)&=q\log\rho-\int_0^q
                  \log|1-Ke^{-2\pi iv}|\,dv .
 \end{split}
 \tag{2}
\]
Here \(\rho=|K|\in(3/5,5/8)\), and \(\mathcal V\)
is the original complete Newton entropy. All three triangular
supports \(u+t\le1,t+p\le1,p+q\le1\) remain.
Their exact prohibited equality rows are zero.
For \(0<u<1/2\), (2) equals
\(\Re\widetilde F(u,t,p,q;x_0,-2)\).
For \(u\ge1/2\), the zero-safe estimate
\(\mathcal V(u)\le0\) is used instead of analytically continuing
the low-row Newton packet.

The uniform finite factorial and Newton bounds in
[the physical cap theorem](research_mixed_three_first_cap_packet.md)
give (2) with polynomial losses and an arbitrarily small rate
tolerance, including both parities, physical endpoints and fixed
ordinary derivatives. Its whole-color regularization supplies the
same bound on a sufficiently small ordinary-color neighborhood.

## 2. Both private cuts are monotone barriers

**Proposition 1.** For every \(t\in[.22,.5]\), the complete
physical lower tail \(0\le u\le.1\) is bounded by its value at
\(u=.1\). The complete upper tail
\(.4\le u<.5\), when supported, is bounded by its value at
\(u=.4\).

*Proof.* In the low half of the physical support,
\[
 \exp Q_u(t,u)
 =\frac{\cos^2(\pi u)\sin(\pi(u+t))}
        {2\sin^4(\pi u)}.
 \tag{3}
\]
If \(0<u\le.1\), then \(u+t\in[.22,.6]\) and hence
\(\sin\pi(u+t)\ge\sin(\pi/5)\).
The original physical-cap inequality
\(\cos^2(\pi/10)\sin(\pi/5)>2\sin^4(\pi/10)\)
makes (3) greater than one.
If \(.4\le u<.5\) in the support, its numerator is at most
\(\cos^2(2\pi/5)\), and its denominator is at least
\(2\sin^4(2\pi/5)\). The opposite original strict inequality
makes (3) less than one. These are the same bounds used in
[the right extension](research_mixed_physical_three_cap_right_extension.md),
Section 3, and they cover the present full \(t\)-interval.
The comparisons extend to physical support endpoints by continuity
and the zero-safe product bounds. The other term \(R\) is
independent of \(u\). \(\square\)

Thus these two tails have precisely the upper rates
\[
 F_-=\max_{(t,p,q)\in C_3}
               \Re\widetilde F(.1,t,p,q;x_0,-2),\qquad
 F_+=\max_{(t,p,q)\in C_3}
               \Re\widetilde F(.4,t,p,q;x_0,-2).
 \tag{4}
\]
All cut points are supported, since \(u+t\le.9\) there.
Both three-dimensional objectives are strictly concave by the
terminating-chart theorem. No value or sign of (4) is asserted.

## 3. The full upper-half Newton tail is already below the action

**Proposition 2.** On all of the physical region
\((t,p,q)\in C_3\), \(1/2\le u\le1-t\),
\[
       \widetilde E(u,t,p,q)<\frac{3397}{1875}
                                      <M-\frac3{10}.
 \tag{5}
\]

*Proof.* The upper-half Newton estimate and \(J(u)\ge0\)
give \(Q<1/2\), exactly as in the original physical cap proof:
\(J(u+t)<1/6\) and \(-2J(t)<1/3\).
No value at an odd-level Newton zero is divided out.

For every nonnegative supported pair,
\[
 V_{\mathbb R}(x,z)\le2J(5/6)<\frac13,\qquad
 |J(p)|<\frac16 .
 \tag{6}
\]
The elementary ideal-triangle maximum in (6) is proved in
[the original seam majorant](research_mixed_endpoint_seam_majorants.md),
Section 2; its proof retains all boundary pairs.
Also
\[
 L(q)\le q\log\frac{\rho}{1-\rho}
      <q\log\frac53,\qquad
 -\tfrac12\log\rho<\tfrac12\log\frac53,\qquad
 \log\frac53<\frac{13}{25}.
 \tag{7}
\]
The last rational witness is the four-term positive exponential
series recorded in
[the original contracted-tail reduction](research_mixed_contracted_pair_outer_index_elimination.md),
Section 5. Since \(q\le21/50\), equations (6)--(7) give
\[
 R<\frac56+\left(\frac12+\frac{21}{50}\right)\frac{13}{25}
      =\frac{4919}{3750}.
 \tag{8}
\]
Adding \(Q<1/2\) proves the first inequality in (5).
The certified \(M>53/25\) gives
\[
 M-\frac{3397}{1875}>\frac{578}{1875}>\frac3{10}.
 \tag{9}
\]
This proves the strict gap for the entire upper-half region,
including its triangular endpoint and every revived ordinary
derivative. A sufficiently small total finite-source tolerance
preserves any smaller fixed gap. \(\square\)

## 4. Complete physical complement: only the two private faces remain

Section 3 of
[the coherent three-index source theorem](research_mixed_prepared_cap_three_index_sheet.md)
now proves the required outer estimate. It keeps the original
\(t,p,q\) outside marker through all old clipping moves, and
uses only the six successful outer faces of the immutable first
prepared face/alias record. The unsuccessful private \(s=.49\)
face is not used. If \(U_{j,\pm}\) denote those six stored
upper bounds, set
\[
 E_{\rm outer}=\max\{146/75,U_{t,-},U_{t,+},
                         U_{p,-},U_{p,+},U_{q,-},U_{q,+}\}.
\]
The source theorem proves \(E_{\rm outer}<M-1/400\).
It bounds the whole original three-index contribution with
\((t,p,q)\notin\operatorname{int}C_3\), in exactly the
grouping of Section 1.

Consequently the complete physical complement to \(C_{\rm new}\)
has the rigorous upper rate
\[
       \max\left\{E_{\rm outer},F_-,F_+,\frac{3397}{1875}\right\}.
 \tag{10}
\]
This is an exact grouping implication. It does not replace a
coherent outer estimate by an absolute bound for the new Newton
rows. Only the two comparisons \(F_-<M,F_+<M\) remain
for this physical complement. If they hold with gaps
\(\delta_-,\delta_+>0\), its complete raw gap is at least
\(\min(1/400,\delta_-,\delta_+)\). Any fixed smaller gap
survives the total finite-source tolerance, uniformly on sufficiently
small original parameter neighborhoods and for fixed jets.

The two faces in (4) are different source functions from the old
\(s=.27,.49\) faces. Their values may not be transferred from
that chart. Likewise (10) is a physical-tail statement and does
not pay the new zero-mode joining currents or horizontal/vertical
aliases. Those must use the exact interpolated rows and contour
of the terminating-chart theorem, retaining every original
residue coefficient and support boundary.
