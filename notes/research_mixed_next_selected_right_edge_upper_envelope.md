# A complete upper envelope for the selected right edge

Private finite-source theorem, 9 November 2026. On the enlarged first-angle
family of the selected charged curve, the literal shortened second edge
is bounded by the larger of its original saddle action and its physical
half-endpoint rate. Both physical endpoint groups, both external caps,
and the complete Fourier corrections are retained. No relative packet
or estimate of the remaining inner current follows without a further
action comparison.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original family and statement

Use the actual selected curve and enlarged family of
[the right-edge guard theorem](research_mixed_next_selected_right_edge_cut_guards.md):
\[
 u=u_\delta=\beta-iK,\quad0\le\delta\le1/2,\qquad
 t=a-iH,\quad\pi/2\le a\le2\pi/3,\quad2/3\le H\le1.
\tag{1}
\]
At \(\delta=0\), \(u=0\); otherwise
\(0<K<\beta/2\), \(0<\beta<4/3\), and \(|\cos u|<1\).
In particular \(H>K\). The original horizontal height
\(H=H(u_\delta)\) belongs to (1).

Retain the exact polynomial, both parity cutoffs, and original action:
\[
 \begin{gathered}
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u),\\
 m(t,u)=\Re\psi(t,u),\qquad e(t,u)=\frac{H+K}{2},\qquad
 M(t,u)=\max\{m(t,u),e(t,u)\}.
 \end{gathered}
\tag{2}
\]
Here \(\psi\) is the original zero-charge critical value continued
in the guard theorem, not a new choice of primitive.

**Theorem.** For each fixed \(\tau>0\), there are constants
\(C_\tau,N_\tau\) such that, throughout (1), at both parities,
\[
 \boxed{\quad |K_N^<(t,u)|\le C_\tau
                 \exp N\{M(t,u)+\tau\},\qquad N\ge N_\tau.\quad}
\tag{3}
\]
This is an upper bound for the complete original sum. It does not
assert that its saddle contribution dominates its endpoint terms.

## 2. The canonical source on the enlarged family

Use the unchanged factorial interpolation
\[
 \begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u),\\
 \mathcal V(y)&=\mathfrak b(y,t)+\mathfrak b(y,u).
 \end{split}
\tag{4}
\]
At \(y=j/N\), this is exactly the summand in (2). The real
upper exponent \(\mathfrak b\) uses the original sidewise sine
primitive and both reciprocal-factorial reflection terms.

For \(0<\Re y<1/2\), the shifted real arguments in (4) lie
strictly between \(-1/3\) and \(5/6\). The reciprocal reflection
identity
\[
 \frac1{G_N(Nw-1/2)}
       =\frac{2\cos(\pi Nw)}{N}G_N(-Nw-1/2)
\tag{5}
\]
therefore proves holomorphy across their negative-real parts and
their zeros, exactly as in
[the joined-contour theorem, Section 1](research_mixed_next_shortened_edge_joined_contour.md).
The own factorial has \(0<\Re y<1/2\), so it has no pole there.
Thus \(T_N\) is holomorphic in the whole open half-strip at every
finite height.

The [uniform factorial theorem, (4)--(5)](research_uniform_factorial_and_boundary_decay.md)
applies with a fixed distance from the outer argument values \(\pm1\).
On compact wire rectangles inside this strip, at bounded heights,
\[
                 |T_N(y;t,u)|\le C N^{-2}e^{N\mathcal V(y)}.
\tag{6}
\]
The same exponent controls every real physical index including
\(j/N\to0\) and \(j/N\to1/2\), with a polynomial prefactor:
\[
 |T_N(j/N;t,u)|\le C N^A e^{N\mathcal V(j/N)},
                         \qquad0\le j\le U_N.
\tag{7}
\]
Here is the endpoint justification. Apply the reciprocal bound
to the two shifted factorials, and the midpoint factorial bound
to the own argument \(x+1/(2N)\), \(x=j/N\). On
\(0\le x\le1/2\),
\[
 N\left|J\left(x+\frac1{2N}\right)-J(x)\right|=O(\log N).
\tag{8}
\]
This follows by integrating the logarithmic sine: only its integrable
\(\log x\) behavior at zero is unbounded on this interval. All
other prefactors are powers of \(N\). Equation (8) proves (7)
uniformly at the index endpoints. At an exact numerator zero
the upper bound remains valid, and at \(j=0\) the exact summand
is one. No partial-index or parity interpolation is used here.

The envelope extends continuously to the two real endpoints, with
\[
                     \mathcal V(0)=0,\qquad
                     \mathcal V(1/2)=e.
\tag{9}
\]
These are the original reflection identities, valid for every
angular real part strictly between zero and \(\pi\), with their
zero-angle limits. In particular (9) also holds at \(u=0\).

## 3. The unweighted upper path

Set \(A=\cos^2(t/2)\), \(B=\cos^2(u/2)\),
\(D_0=A+B-AB\), and \(W=AB/D_0\). The guard theorem proves
\(\Re A,\Re B,\Re D_0,\Re(1/W)>0\) and the original
simple critical point
\[
 y_*=\pi^{-1}\arctan\sqrt W,\qquad
 F_y(y_*)=0,\qquad F(y_*)=\psi(t,u).
\tag{10}
\]
Also \(\Im A>0\) and \(\Im B\ge0\), with \(B=1\) when
\(u=0\). Consequently
\(\Im(1/W)=\Im(1/A)+\Im(1/B)<0\). Thus \(W\) is in the
upper right quadrant and \(y_*\) lies in the upper half-strip.
Its distance from the real boundary is positive uniformly on (1).

The envelope \(\mathcal V\) is continuous and subharmonic on
closed upper rectangles. Its normal derivative jumps by \(+2\pi\)
on each original upper cut; the starting-zero flux is
\(O(\epsilon|\log\epsilon|)\). This is the distributional proof
in [upper continuation, Section 2](research_mixed_next_shortened_edge_upper_continuation.md),
which uses only the same reciprocal identity (5). The new guard
theorem bounds the full horizontal force strictly below one on
both cuts, including the incoming part with negative cut coordinate.
Hence no cut point or starting zero is a local minimum. Off the
cuts the envelope is nonconstant harmonic. On the real bottom,
the guard theorem proves one maximum and no interior local minimum.

We record the side traces for the enlarged angles, rather than
importing the old angle restriction. For one leg
\(z=\theta-iA_0\), set
\(r=\theta/(2\pi)\), \(s=A_0/(2\pi)\). Here
\(0\le r\le1/3<1/2\). On the left boundary the exact derivative is
\[
 \partial_v\mathfrak b(iv,z)
 =\pi-\vartheta_r(s+v)-\vartheta_r(s-v),\qquad
 \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)).
\tag{11}
\]
Since \(|\vartheta_r|\le\pi r\), this derivative is positive;
it is at least \(\pi/3\). The left rate starts at zero and
strictly increases. Its strict sublevel at any level is connected
or empty.

For the right side put
\(\theta_r(v)=\Arg\sin\pi(r+iv)\). For \(0<r<1/2\), this
increases from zero and is strictly between zero and \(\pi/2\)
for positive \(v\). The original right-side derivative is
\[
 \partial_v\mathfrak b(1/2+iv,z)=
 \begin{cases}
 \theta_r(s+v)+\theta_r(s-v)-\pi\in(-\pi,0),&0<v<s,\\
 \theta_r(s+v)-\theta_r(v-s)+\pi\ge\pi,&v>s.
 \end{cases}
\tag{12}
\]
The zero-angle limits are those of the original one-leg formula.
Since \(H>K\), the sum of the two legs decreases up to
\(K/(2\pi)\), then increases strictly. This includes all heights
between the two cuts: the crossed leg contributes at least \(\pi\)
and the un-crossed leg contributes more than \(-\pi\).
At \(K=0\) the increasing interval starts at zero. Every strict
right-side sublevel is therefore connected or empty. Its real
endpoint value is \(e\).

At large upper height the exact sine-primitive expansion gives
\[
 \mathcal V(x+iv)=2\pi v-\frac{aH+\beta K}{2\pi}+o(1)
\tag{13}
\]
uniformly on the compact family and \(0\le x\le1/2\).
Choose a finite top above \(m+1\) and above all selected saddles.

Apply the proof of the planar component lemma in upper continuation
at level \(m\), initially allowing either side trace to be empty.
Every nonempty strict-sublevel component has a minimum on its compact
closure, and the preceding no-minimum facts force that minimum onto
a vertical side. Each nonempty side trace lies in only one component,
so there are at most two components. The local descending sectors
of the simple saddle cannot lie in one component: a simple connecting
arc and a descending crosscut form a Jordan loop containing an
ascending germ, contradicting the subharmonic maximum principle.
This is the full finite-crosscut argument of that lemma. There are
therefore exactly two components, each meeting a different side.
In particular both side traces are nonempty, and \(m>0\).

Join the two saddle germs to their respective side traces through
strict sublevels. On the left side, moving to the real endpoint
does not increase the rate above \(m\). On the right side its
decrease-then-increase property shows that the segment from the
chosen side point to the real endpoint has rate at most
\(\max\{m,e\}\). These paths, joined through a small local saddle
arc, give a path from the left endpoint to the right endpoint
with rate at most \(M\), up to an arbitrarily small tolerance.

More precisely, for any fixed \(\varepsilon>0\), choose real cuts
\(0<\alpha<\gamma<1/2\) in sufficiently small uniform endpoint
collars. Push the side paths slightly into the open half-strip
and connect to these cuts. Continuity gives an upper path from
\(\alpha\) to \(\gamma\) on which
\[
                         \mathcal V\le M+\varepsilon.
\tag{14}
\]
All compact strict paths and the local saddle arc persist under small
parameter changes. A finite cover of (1) provides uniformly bounded
lengths and heights; no globally continuous choice of path is needed.
The \(O(N^{-1})\) displacement of either cut to its original
midpoint is covered by short endpoint connectors and the same
tolerance. Only an upper bound is used on this path, including
any factorial cut crossings.

## 4. Both complete aliases and both endpoint groups

For the two penalized rates
\(\mathcal V(x\pm iv)-2\pi v\), retain the original sidewise
formulas of [the mixed-height proof, Section 5](research_mixed_next_shortened_edge_mixed_height_packet.md).
Their derivation uses \(0\le\theta/(2\pi)<1/2\), so applies
to (1). On the left and right boundaries respectively they give
\[
 \begin{split}
 \mathcal V(\pm iv)-2\pi v&\le\frac{aH+\beta K}{2\pi},\\
 \mathcal V(1/2\pm iv)-2\pi v&\le e.
 \end{split}
\tag{15}
\]
At height \(v=1\), the same exact \(J_\pm\) expansions have
polynomial part of absolute value at most
\((aH+\beta K)/(2\pi)\). Each dilogarithm argument has modulus
at most \(e^{1-2\pi}<1/100\). The complete remainder of both
legs is less than \(4/(99\pi)<1/50\), just as in
[lower continuation, (15)--(20)](research_mixed_next_shortened_edge_lower_continuation.md).
No angle-dependent reflection term has been dropped.

The enlarged range still gives a strict reserve for the left and
deep parts:
\[
 \frac{aH+\beta K}{2\pi}
       \le\frac H3+\frac K4\le e-\frac19,
 \qquad
 \mathcal V(x\pm i)-2\pi<e-\frac1{12}.
\tag{16}
\]
Here \(\beta<\pi/2\), \(H\ge2/3\), and
\(1/9-1/50>1/12\). The right bound in (15) need not have a
strict reserve below \(e\); none is required for (3).

Uniform continuity moves (15) to small interior endpoint columns.
Using also (7)--(9), choose \(\alpha,\gamma\) as in Section 3
and a small fixed \(h_c>0\) such that the physical endpoint
groups, their unweighted collars, and both penalized endpoint
columns are bounded at rate \(e+\varepsilon\). The two aliases
may use the complete paths
\[
 \alpha_N\pm ih_c\longrightarrow\alpha_N\pm i
       \longrightarrow\gamma_N\pm i
       \longrightarrow\gamma_N\pm ih_c,
\tag{17}
\]
where
\(\alpha_N=(\lfloor N\alpha\rfloor+1/2)/N\) and
\(\gamma_N=(\lceil N\gamma\rceil-1/2)/N\).
The exact physical endpoint groups are
\[
 E_N^{\rm phys}=
 \sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
 +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
\tag{18}
\]
Equation (7) gives their absolute sum at most
\(C N^{A+1}e^{N(e+\varepsilon)}\), with the true odd last
index unchanged.

## 5. Exact assembly and the upper bound

Put \(\zeta=e^{2\pi iNy}\). The residue calculation in the
joined-contour theorem, with residue \(1/(2\pi iN)\), gives
the exact identity
\[
 \begin{split}
 K_N^<(t,u)={}&N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy
       +N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy
       +C_N+E_N^{\rm phys},\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
                       \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
                       \frac{T_N}{\zeta-1}\,dy.
 \end{split}
\tag{19}
\]
Both paths \(\Gamma_\pm\) are those in (17), oriented left to right. On the midpoint
columns, \(\zeta=-e^{-2\pi Nv}\), so the reciprocal cap
denominator has modulus at most one. The collars therefore pay
both full caps, with the two displayed signs.

Split \((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\) on the upper
path. Move the entire unweighted term to the path (14). The
two exact added endpoint segments are
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy
       +N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.
\tag{20}
\]
They lie in the same paid collars. Both remaining rational
terms use (17). Since their wire heights have modulus at least
\(h_c\), their exact denominators give the complete exponential
penalty \(e^{-2\pi Nv}\) with a bounded factor. Thus (6),
(14)--(18), and (19)--(20) prove
\[
                  |K_N^<(t,u)|\le C_\varepsilon N^A
                                  e^{N(M+\varepsilon)}.
\tag{21}
\]
Take \(\varepsilon<\tau/2\) and absorb the fixed polynomial
factor in the remaining tolerance. This proves (3), with every
original row, cap, orientation, and Fourier correction retained.

## 6. The comparison still needed for the inner current

The first shortened edge has the adopted slit-plane upper rate
\(\Re\psi(t,0)\). Combining it with (3) and the full inner
multiplier on the lower angular contour gives the larger of
the original geometric rate and the endpoint-sector rate
\[
 \Re\psi(t,0)+\frac{H+K}{2}
                         +\frac{3aH}{2\pi}-H.
\tag{22}
\]
The geometric rate has the established phase comparisons.
No sufficient uniform comparison of (22) with the selected
inner action is proved here. Nor does (3) reach the farther
right interval beyond \(2\pi/3\). These remain separate source
requirements; a phase or symbol identity does not remove them.

## Frozen source bindings

- Selected right-edge guards: `8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc`.
- Original mixed-height source and side formulas: `fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07`.
- Original joined representation: `1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d`.
- Upper component/Jordan and subharmonicity proof: `b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542`.
- Original lower continuation: `79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c`.
- Uniform zero-safe factorial source: `4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11`.
