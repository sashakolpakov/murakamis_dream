# The endpoint-conditioned score at a protected singleton

This note concerns the actual four-incidence coefficient flow of a
marked simple-sphere Morse source. It proves that the published
fifty-four-region example also obstructs the combined local score
formed from endpoint entropy and sharp relative spectral energy.
The proof transforms the same rational witness; it does not optimize
new numerical examples or estimate the signed shared coefficient.

The source and topology are those of
[the singleton-sector theorem](/private/tmp/murakamis_dream-publication/notes/actual_singleton_sector_envelope_obstruction.md).
The local coefficient theorems used below hold before any global
contraction, so their applicability does not require a flat-plat
presentation. The global positive-endpoint volume and uniqueness
theorems in
[the endpoint-conditioned criterion](/private/tmp/murakamis_dream-publication/notes/general_endpoint_conditioned_source_energy.md)
retain their stated original flat-plat hypotheses. No extension of
those theorems is assumed here.

## 1. The common flow and its three local scores

At a crossing region with ordered source variables \((x,b,c,y)\),
write
\[
 q=(q_x,q_b,q_c,q_y),\qquad q_i\ge0,\qquad
 q_x+q_b+q_c+q_y=1.                                      \tag{1}
\]
These are the limits of the four exponents divided by \(d=N-1\).
All incidences of one ordinary face have total load one. The two
protected faces have total load zero, and hence every incidence of
either protected face has load zero. These are the original face
constraints; no independent local maximization may change them.

For \(0\le a\le1/2\), define
\[
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \qquad
 \Lambda(t)=-\int_0^t\log|2\sin v|\,dv,\qquad
 C(a_1,a_2,a_3)=\sum_i f(a_i),\quad \sum_i a_i=\frac12.
                                                               \tag{2}
\]
In particular \(f(0)=f(1/2)=0\) and
\(f(1/2-a)=f(a)\). The normalization is the original triangle
coefficient normalization.

When \(q_b,q_c\le1/2\), the complete central coefficient entropy is
\[
 \begin{split}
 h_C(q)=\max_{s\in I(q)}
 \bigl[
  C(s,q_b,\tfrac12-q_b-s)
  +C(q_x-s,q_c,\tfrac12-q_c-q_x+s)
 \bigr],\\
 I(q)=
 \left[\max(0,q_x+q_c-\tfrac12),
       \min(q_x,\tfrac12-q_b)\right].
 \end{split}                                                   \tag{3}
\]
Thus a particular admissible split gives a lower bound for \(h_C\).
It does not give a separate maximization at each shared face.

Let \(h(q)\) denote the full positive endpoint-reference entropy,
using \(-V_N(-2)\) at even levels and the stated first-normal
regularization at odd levels. The one-sided energy theorem gives
the continuous bound
\[
 g(q)=C(q_x,q_y,\tfrac12-q_x-q_y)
 \quad\text{on LEFT or RIGHT support}.                         \tag{4}
\]
On the central region, both \(h\) and \(g\) equal \(h_C\).
The earlier LEFT weighted-envelope coefficient rate is
\[
 h_{\mathrm{env}}(q)=t\,C(q_x/t,q_b/t,q_y/t),\qquad
 t=2(1-q_c)>0,                                                \tag{5}
\]
with value zero at \(q_c=1\). The combined score under discussion is
\[
 h_{\mathrm{sharp}}(q)=
 \begin{cases}
 h_C(q),&q_b,q_c\le1/2,\\
 \min\{h_{\mathrm{env}}(q),(h(q)+g(q))/2\},&q_c\ge1/2,
 \end{cases}                                                  \tag{6}
\]
and the reflected formula on RIGHT. Its seams agree.
The claimed universal criterion would require the maximum of
\(\sum_e h_{\mathrm{sharp}}(q_e)\) over the original noncentral feasible
flows to be strictly below
\(\Phi=\operatorname{Vol}(Y)/(2\pi)\).

## 2. Structural equality on a protected singleton

Suppose that \(b,y\) are precisely the two protected variables in
this quartet, while \(x,c\) are ordinary. Every LEFT load has the form
\[
              q(u)=(u,0,1-u,0),\qquad 0\le u\le\frac12.        \tag{7}
\]
The protected-outer coefficient theorem gives, uniformly through
both parity limits,
\[
 h(q(u))=-2f(u),\qquad g(q(u))=2f(u).                          \tag{8}
\]
Indeed its path endpoints are \(\mu=0,\nu=u\); its exact limiting
spectral coefficient maximum is
\(f(\mu)+f(\nu-\mu)-f(\nu)=0\), whereas its reference entropy is
\(2(f(\mu)-f(\nu))=-2f(u)\).
These statements use the full unused-row products, including the
omitted half, rather than a quotient evaluated at a spectral zero.
They are precisely
[the protected-outer theorem, equations (4)–(5)](/private/tmp/murakamis_dream-publication/notes/actual_protected_outer_spectral_energy.md).

For \(u>0\), equation (5) has \(t=2u\), so its triangle is
\((1/2,0,0)\), of entropy zero. At \(u=0\) the continuous
endpoint value is also zero. Hence
\[
                 h_{\mathrm{sharp}}(q(u))=0
                 \quad(0\le u\le1/2).                         \tag{9}
\]
Thus the relative-energy improvement is exactly equal to the old
coefficient envelope throughout this entire protected face.
This is not an inequality that could become strict after a better
choice of shared radii.

There is a corresponding exact global variational identity.
Fix this protected singleton at one region and require every other
region to be central. For each of those other regions retain two
triangle rows \(a_{e,0},a_{e,1}\), each of total load \(1/2\).
At the chosen region retain only the two loads \(u\) at \(x\) and
\(1-u\) at \(c\), with \(0\le u\le1/2\). Impose all original
ordinary and protected face totals. Call the resulting compact
polytope \(\mathcal A\), and put
\[
                 E(a)=\sum_{e\ne e_0}
                       \bigl(C(a_{e,0})+C(a_{e,1})\bigr).      \tag{10}
\]
Then
\[
 \max_{\text{this original closed sector}}
           \sum_eh_{\mathrm{sharp}}(q_e)
       =\max_{a\in\mathcal A}E(a)
       =\inf_{\ell\in\mathbb R^{F_{\mathrm{ord}}}}
          \left[
          \sum_{e\ne e_0}X_e(e^\ell)
          +\max\{\ell_c,(\ell_x+\ell_c)/2\}
          -\sum_f\ell_f
          \right].                                          \tag{11}
\]
Empty feasible sets have value \(-\infty\).

For the first equality, a triangle assignment aggregates to
\[
 q_x=a_{0,x}+a_{1,x},\quad q_b=a_{0,b},\quad
 q_c=a_{1,c},\quad q_y=a_{0,y}+a_{1,y}.                         \tag{12}
\]
This is central and supplies one admissible split in (3).
Conversely, at any central four-load choose a maximizing split in
(3). This changes no four-load and therefore no shared face total.
The selected region contributes zero by (9). Compactness then
proves both inequalities in the first equality.

For the second equality, each central triangle has the original
Legendre formula \(Q(e^\ell)=\max_a(C(a)+a\cdot\ell)\).
The selected interval has support function
\[
 \max_{0\le u\le1/2}\{u\ell_x+(1-u)\ell_c\}
        =\max\{\ell_c,(\ell_x+\ell_c)/2\}.                    \tag{13}
\]
Weak duality follows on summing and using the face totals.
For the reverse inequality, maximize the continuous concave
function (10) on the product of the compact row simplexes and
the interval for \(u\), at any prescribed vector of face totals.
The hypograph of this maximum is closed and convex. Separating
a point strictly above it at the original feasible target vector
gives a finite affine majorant. Its vertical coefficient is
positive, since a feasible point with the same face totals
excludes coefficient zero. Normalize that coefficient to one;
the remaining coefficients are the shared \(\ell_f\).
Let the separation height approach the maximum.
If the target is infeasible, separation from the compact incidence
image sends the dual cost to \(-\infty\).
No minimizing positive radius vector is required.

The right side of (11) is exactly the genuine singleton's
previous weighted-envelope capacity. Thus on this entire class
of sectors, endpoint conditioning with the stated sharp local
energy does not improve that capacity.

## 3. The original fifty-four-region witness

Use the oriented sphere, perfect matching, and nonmatching mark
of the published singleton example. Its protected faces are
\(29,50\), its selected LEFT region is \(32\), and its quartet is
\((x,b,c,y)=(0,50,16,29)\). Its rational value is
\[
 \lambda=\frac{548219162717}{10^{12}},\qquad
 u=\frac{\lambda}{2}
   =\frac{548219162717}{2\cdot10^{12}}.                        \tag{14}
\]
At region \(32\) take \(q=(u,0,1-u,0)\). At each other region
aggregate its two certified rational triangle rows by (12).

Every spectator triangle row has total \(1/2\), nonnegative
entries, and zero on each protected corner. Therefore
\(q_b,q_c\le1/2\) at every spectator. If
\(s=a_{0,x}\), its row equations give exactly
\[
 \begin{gathered}
 a_0=(s,q_b,\tfrac12-q_b-s),\\
 a_1=(q_x-s,q_c,\tfrac12-q_c-q_x+s),\\
 \max(0,q_x+q_c-\tfrac12)\le s
           \le\min(q_x,\tfrac12-q_b).
 \end{gathered}                                              \tag{15}
\]
All fifty-four ordinary face totals are exactly one, by the
published rational certificate, and both protected totals are zero.
At the selected region \(q_c=1-u>1/2\), so this is genuinely
inside the limiting LEFT region rather than only a central seam.

Equations (3), (9), and (15) imply
\[
 \sum_{e=0}^{53}h_{\mathrm{sharp}}(q_e)
       \ge E_{\mathrm{dual}}>\Phi+\frac15.                         \tag{16}
\]
Here \(E_{\mathrm{dual}}\) is exactly the sum of the same 106
spectator triangle entropies in the published certificate.
The strict numerical constant in (16) is not a floating-point
optimization: the public rational interval verifier proves
\[
 E_{\mathrm{dual}}-P(L^{\mathrm{up}})>0.2055724276,\qquad
                         \Phi\le P(L^{\mathrm{up}}),               \tag{17}
\]
at its stated positive rational upper witness. The new argument
needs no further transcendental evaluation.

The accompanying exact script
\(\texttt{md-endpoint-conditioned-singleton-flow-check.py}\)
reads that original certificate, constructs all four-loads,
checks every interval in (15), and verifies all original targets.
Its JSON output retains the resulting rational four-loads.
The published topology and support checks supply a literal
knot-producing Morse source and nonzero shared sector at all
sufficiently large even levels. The continuous-score obstruction
(16) already follows from the exact feasible flow; a signed
coefficient lower bound is not used.

This disproves universal validity of the combined score criterion
for the class of all original matched simple-sphere Morse sources.
It does not identify this example with a certified original
flat-plat presentation. It does not contradict the conditional
criterion: that criterion proves a consequence only when its
strict inequality holds.

## 4. What the witness means geometrically

The witness is a feasible flow for the comparison problem (10),
not a positive angle structure for the original full triangulation.
This can be seen before any stationarity or representation theory.

At the selected region, its input triangle has only the ordinary
face \(0\), since \(50,29\) are protected. In an original complete
triangle assignment it must therefore have load \(1/2\) at \(0\).
The output triangle has ordinary corners \(0,16\), so write its
loads as \(r,1/2-r\), with \(0\le r\le1/2\). The spectators in
the witness already contribute totals \(1-u\) at \(0\) and \(u\)
at \(16\). Restoring both positive original triangle rows produces
the total loads
\[
 \begin{split}
 A_0&=1-u+\tfrac12+r=1+(\tfrac12-u+r),\\
 A_{16}&=u+\tfrac12-r=1-(\tfrac12-u+r).
 \end{split}                                                \tag{18}
\]
The mismatch cannot vanish because
\[
                 \tfrac12-u
                    =\frac{451780837283}{2\cdot10^{12}}>0.    \tag{19}
\]
All other ordinary totals remain one. In angular units the two
star sums differ from \(2\pi\) by opposite amounts
\(\pm2\pi(1/2-u+r)\).

These are explicit formal angular defects. They do not by
themselves construct a hyperbolic cone manifold, even though that
language might suggest an interpretation: the witness has not
supplied globally compatible edge lengths, developed face maps,
or the original peripheral holonomies. Moreover it is a rational
feasible lower witness, not an established critical point of even
the modified comparison problem. The signed reference action
\(h(q(u))=-2f(u)\) and the energy compensation \(g(q(u))=2f(u)\)
are distinct terms; replacing their average by zero does not
give a regulator chain for the original exterior.

Consequently volume rigidity of representations cannot be
applied directly to the comparison score. Equation (18) identifies
the exact complete-angle equation lost at the protected region.
It does not force a quantitative cancellation in the actual
period. Such cancellation must be established using its coherent
shared coefficients, spectral phases and primitive filling
functional.

## 5. Current consequence

On these protected-singleton sectors, the full combined
endpoint/energy score equals the old envelope capacity as a
global constrained variational problem, not merely at an isolated
test point. The original R54 certificate therefore gives an
explicit failure of a universal gap for that score.

What remains open is a bound on the signed shared remainder, or
on its filled period. The example does not rule out estimates
that retain the common face phases or otherwise use information
lost by independent local coefficient absolute values.
