# What remains of the second period after the completed real arc

Private exact reduction, 11 November 2026. Author-frozen after full
proof and direct-source readback. Independent review is required
before adoption.

For an actual word beginning with \(443\), the new first-period
theorem covers the complete second density on the real interval
\([1/2,18/25]\). The closed interval \([7/8,1]\) was already
covered by a different complete-message theorem. The intervening
real interval is still missing. There are also two missing
second-coordinate connections on the left: the available long
left-connection theorems assume \(444\), not \(443\).

This note gives an exact finite decomposition which keeps these
three regions visible. It proves a conditional completion criterion;
it does not assert estimates on the missing regions.

## 1. Both complete Fourier sectors

Fix the original actual word, reference and markings in
[the completed first-period theorem](research_mixed_443_complete_first_period_real_second_arc.md).
In particular the word has length at least four and begins with
\(443\). Put
\[
 \ell=11/50,\quad r=9/20,\quad u=18/25,\quad v=7/8,\quad
 H=1/100,\quad z=b+ic_3,\quad b\in[\ell,r].
 \tag{1}
\]
The actual second height is \(c_2<0\). The third index remains
ordinary, also at length four, with its original following leg.
Write \(Z=e^{-2\pi iz}\).

Keep the complete finite polynomial
\[
 f_N(w,Y)=N\operatorname{CT}_X
       [U_N(w,X)d_N(X)(1+X^{-N})C_{1,N}(X,Y)].
 \tag{2}
\]
Thus \(f_N\) contains both first Fourier coefficients. Its degree
in each of \(w,Y\) is at most \(N-1\), and it is the single original
unnormalized physical first sum.
For the second coordinate set
\[
 \begin{split}
 P_N(w;Y,Z)&=f_N(w,Y)d_N(Y)C_{0,N}(Y,Z),\\
 D_{\mu,N}(w;y,z)&=
       P_N(w;e^{-2\pi iy},Z)e^{2\pi i\mu Ny},\qquad \mu=0,1.
 \end{split}                                                   \tag{3}
\]
There is no outgoing halfweight because the third type is three.
All numerator and denominator factors in \(C_{0,N}\) are the original
ones, and its summation range remains \(0\le j<N\).

The \(Y\)-exponents of \(C_{0,N}(Y,Z)\) lie in \([-N+1,0]\).
Both \(f_N\) and \(d_N\) have degree at most \(N-1\).
Therefore
\[
                  \operatorname{supp}_Y P_N
                             \subset[-N+1,2N-2].
 \tag{4}
\]
If \(\zeta=e^{-2\pi i/N}\) and \(P_k=(\zeta;\zeta)_k\), the
exact second physical contraction is consequently
\[
 \begin{split}
 T_N(w,Z)
   &:=\sum_{k=0}^{N-1}
        \frac{f_N(w,\zeta^k)}{P_k}C_{0,N}(\zeta^k,Z)\\
   &=N\operatorname{CT}_Y[(1+Y^{-N})P_N(w;Y,Z)]\\
   &=N\sum_{\mu=0}^1\int_0^1D_{\mu,N}(w;y,z)\,dy .
 \end{split}                                                   \tag{5}
\]
Only exponents zero and \(N\) can be multiples of \(N\) in (4).
This proves the identity, including its scalar \(N\).
It holds at both parities. It removes neither a physical row
nor a Fourier term.

The first factor \(N\) is already inside (2); the factor \(N\) in
(5) is the second extraction density. Expanding (2) thus restores
the original \(N^2\,da\,dy\) and all four combinations of the two
first and two second sectors.

## 2. An exact decomposition into known and missing paths

For the unselected second sector use the oriented path
\[
 \Gamma_0:\quad
 0\longrightarrow ic_2\longrightarrow\ell+ic_2
 \longrightarrow r+ic_2\longrightarrow1/2+ic_2
 \longrightarrow1/2\longrightarrow u\longrightarrow v
 \longrightarrow1.
 \tag{6}
\]
For the selected sector use
\[
 \Gamma_1:\quad
 0\longrightarrow iH\longrightarrow\ell+iH
 \longrightarrow r+iH\longrightarrow1/2+iH
 \longrightarrow1/2\longrightarrow u\longrightarrow v
 \longrightarrow1.
 \tag{7}
\]
The densities (3) are entire and one-periodic in the additive
variable \(y\), so Cauchy's theorem replaces each real integral
in (5) by its path (6) or (7), exactly at every finite level.

Retain the original unselected plateau contribution
\[
 J_N(w,z)=N\int_{[\ell,r]+ic_2}D_{0,N}(w;y,z)\,dy .
 \tag{8}
\]
It contains the complete first polynomial \(f_N\).
Define the two left contributions and the two middle contributions:
\[
 \begin{split}
 L_{0,N}&=N\int_{\,0\to ic_2\to\ell+ic_2}
                          D_{0,N}(w;y,z)\,dy,\\
 L_{1,N}&=N\int_{\,0\to iH\to\ell+iH}
                          D_{1,N}(w;y,z)\,dy,\\
 M_{\mu,N}&=N\int_u^vD_{\mu,N}(w;q,z)\,dq,\qquad\mu=0,1.
 \end{split}                                                   \tag{9}
\]
Let \(K_N\) be the sum of the integrals on all pieces of (6)--(7)
other than the plateau (8) and the four contributions (9),
each with its stated sector and original density.
Then
\[
 T_N(w,Z)=J_N(w,z)+K_N(w,z)
                +L_{0,N}+L_{1,N}+M_{0,N}+M_{1,N}.             \tag{10}
\]
This is a finite algebraic/contour identity, not an asymptotic
replacement.

On the real middle interval the two densities differ only by
a unit-modulus monomial:
\[
 D_{1,N}(w;q,z)=e^{2\pi iNq}D_{0,N}(w;q,z).
 \tag{11}
\]
Thus a pointwise upper bound for one of them there pays both
middle contributions. This observation does not hold with a
unit-modulus multiplier on the nonreal left connections.

## 3. Every contribution placed in \(K_N\) is already bounded

Let \(\Lambda_{123}(z)\) and
\[
 \delta=\min\{(9/20-\Re r_2)^2/250000000,10^{-6}\}>0
 \tag{12}
\]
retain their values in the completed first-period theorem.
The exact applicable inputs are:

| Second path piece | Sector | Complete-density source |
|---|---|---|
| \([\ell,r]+iH\) | \(1\) | Complete selected plateau, Theorem (11): gap \(1/12800-\tau\), for both \(443\) and \(444\) |
| \([r,1/2]+iH\) | \(1\) | Complete selected \(443\) shoulder, Theorem 1: gap \(1/100000-\tau\) |
| \(1/2+i[0,H]\) | \(1\) | Complete \(443\) half-face theorem, third line of (6): gap \(\delta-\tau\) |
| \([r,1/2]+ic_2\) | \(0\) | The same half-face theorem, first line of (6): gap \(\delta-\tau\) |
| \(1/2+i[c_2,0]\) | \(0\) | The same half-face theorem, second line of (6): gap \(\delta-\tau\) |
| \([1/2,u]\) | \(0,1\) | Completed first period on the real second arc, Theorem (5): gap \(\delta/128\) |
| \([v,1]\), including \(1\) | \(0,1\) | Far real second arc, Theorem 1 (6): gap \(1/500\) |

Each input bounds precisely \(f_Nd_N(Y)Y^{-\mu N}C_{0,N}\),
with the complete \(f_N\). In the final row the source explicitly
allows both \(443\) and \(444\); taking its flag \(\beta=0\)
gives the \(C_{0,N}\) factor and removes its outgoing halfweight.
Its Sections 3--6 first bound the whole first coefficient on
the complete first circle, then attach every row of \(C_{0,N}\)
and the whole second diagonal. It is not merely a bound for
the last real portion of the first contour.

The half-face inputs use their native second sectors only.
Both second sectors are allowed on the real arcs.
Every input retains both first Fourier terms, all finite
conditional indices, the sampling corrections and joins in
its internal contour proof, and both level parities.
Reversing the orientation of the selected vertical does not
change its modulus bound.

Choose the source tolerances to be smaller than half their
displayed gaps, and take a common smaller ordinary-color disk.
Fixed path lengths and the factor \(N\) cost only a polynomial.
Since \(\delta\le10^{-6}\), the safe common conclusion is
\[
 |K_N(w,z)|\le C N^A
              e^{N\{\Lambda_{123}(z)-\delta/256\}}.
 \tag{13}
\]
Fixed ordinary-color derivatives obey the same conclusion on
smaller disks.

## 4. The precise remaining sufficient condition

Suppose there are positive constants
\(\gamma_0,\gamma_1,\gamma_M\), uniform in \(b\in[\ell,r]\),
both parities, and a common fixed ordinary-color disk, such that
\[
 |L_{\mu,N}|\le C N^A
                    e^{N(\Lambda_{123}-\gamma_\mu)},
 \qquad \mu=0,1,
 \tag{14}
\]
and
\[
 |M_{0,N}|+|M_{1,N}|
       \le C N^A e^{N(\Lambda_{123}-\gamma_M)}.
 \tag{15}
\]
Then (10)--(13) prove
\[
 |T_N(w,Z)-J_N(w,z)|
       \le C' N^{A'}e^{N(\Lambda_{123}-\gamma)},\qquad
 \gamma=\min\{\delta/256,\gamma_0,\gamma_1,\gamma_M\}>0.
 \tag{16}
\]
Pointwise complete-density bounds along the three missing
geometric regions in (9) are sufficient for (14)--(15).
They are stronger than necessary: cancellation within the
four displayed integrals could also prove those estimates.
Nothing here assumes such cancellation.

The original unselected plateau theorem separately compares
\(J_N\) with the original two-coordinate plateau contribution.
That comparison can be combined with (16) once (14)--(15)
are proved. Equation (16) alone does not assert a nonzero
coefficient for the next transfer or a new knot family.

## 5. What the existing left-end results actually provide

The complete unselected second-left connection has source
research_mixed_complete44_second_left_connection.md.
Its Section 1 assumes a word beginning with \(444\), attaches
\(C_{1,N}(Y,Z)\), and carries \(|d_N(Z)|^{1/2}\).
The selected-left source
research_mixed_complete44_second_selected_left_connection.md
has the same \(444\) restriction.
Their theorems therefore do not establish either (14) for
the present \(443\) source. Replacing that third factor or
discarding its allocation would change the statement.

Two smaller results do apply to \(443\):

* The complete-message seam theorem bounds both sectors on
  a fixed complex neighborhood of \(Y=1\), equivalently near
  \(y=0\) and \(y=1\).
* The unselected plateau-collar theorem bounds sector zero
  on fixed complex neighborhoods of its two plateau endpoints,
  including \(\ell+ic_2\).

Those results pay short endpoint portions of suitable left
connections. Their widths may depend on the fixed word;
neither claims that its neighborhood reaches the other end.
Thus they can shorten the unknown paths in (9), but they do
not close them. No \(444\) left-connection theorem is used
as a \(443\) estimate in this reduction.

## 6. What contour deformation can and cannot remove

For the paths (6)--(7), the only uncovered right-side real
interval is \([18/25,7/8]\). It may be replaced by a complex
path with the same endpoints, because each density is entire
in \(y\). This changes the location of the required estimate.
The already proved bounds on the two adjacent real intervals
do not by themselves bound that replacement path.

There is also a simple topological constraint. Every continuous
additive path from \(0\) to \(1\) has real part taking every
value in \([0,1]\). Equivalently, its exponential image in
\(\mathbb C^\times\) has winding number minus one and meets
every argument sector. In particular a second coefficient
contour cannot simply omit all arguments corresponding to
\(18/25<\Re y<7/8\) modulo one.
It can cross them at nonzero height, but then the appropriate
complete density, including \(Y^{-\mu N}\), must be estimated
at that height.

Crossing \(Y=0\) is not an unrecorded shortcut: (4) is Laurent,
and the coefficient integrands also contain \(dY/Y\).
Such a change would need its exact residues or another finite
coefficient identity. A separately proved symmetry or algebraic
transformation could supply a different method; no such
identity is assumed here.

The remaining analytic target is therefore explicit: two
complete left connections for \(443\), and one complete middle
real arc (or controlled replacement path) serving both second
sectors. All other terms of (10) already have the bound (13).

## Direct source versions

| Direct source | SHA-256 | Implication used |
|---|---|---|
| research_mixed_443_complete_first_period_real_second_arc.md | d01b6b31e72e0e46d53db8e2ce65755018778b1de884ae5d71d392b19ec78e87 | Complete \(f_N\), original source and action, both-sector real arc through \(18/25\) |
| research_mixed_complete44_second_selected_full_first_period.md | c2556f56a34b9ee09a94b3881b2f3ffce4d182839600f5a9122f9735f0a0bc7b | Whole selected second plateau and degree of the complete \(f_N\) |
| research_mixed_443_complete_second_selected_right_shoulder.md | e001e0681e6e5cc52ff62040201f9bd9db6fa09b2a892a1e05495000287b8277 | Complete selected right shoulder for \(443\) |
| research_mixed_443_complete_second_half_face.md | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b | Unselected shoulder and both native half-face verticals |
| research_mixed_complete44_second_far_real_arc.md | 922a114d355f134aae94065d2c8996ac26d670f6dd5439f20285c7c7b627dd2e | Complete \(f_N\) with the \(C_0\) factor and both sectors on the closed arc \([7/8,1]\) |
| research_mixed_complete44_second_period_seam_collar.md | e203f8041ddcc3c002d09de0a5d94a458f2499a3f55325fce27126c3c7b66a6c | Fixed seam neighborhoods for \(443\), with both sectors |
| research_mixed_complete44_second_unselected_boundary_collars.md | 2543869547dc679c6bfaf311eb09a4286afdd590a055b80033b568d3eafe7e80 | Unselected endpoint collars and the separate plateau-remainder comparison |
| research_mixed_complete44_second_left_connection.md | f997e5d64ffb8d5534eb2ff6151e8f2081348e97e9a677c5592ccebe1effcba1 | Scope check only: its long unselected connection is restricted to \(444\) |
| research_mixed_complete44_second_selected_left_connection.md | 38558b4cea06c14de8a8e229cd95119d1f86c5dcd856bcde1fae837831d93b43 | Scope check only: its long selected connection is restricted to \(444\) |

The entire final proof and all nine directly used source implications
were read, and all nine source hashes match. The last two bindings
are scope checks only. Separate full proof and direct-source review
are required before adoption.
No mathematical numerical evaluation, saved-value arithmetic,
test, import, compilation or frozen-source edit is used.
