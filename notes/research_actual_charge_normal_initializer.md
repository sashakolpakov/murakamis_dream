# A nonzero initializer from the actual charge normal

Research proof, 23 November 2026.

The first charge normal of the original analytic Hermite coupon gives
an explicit nonzero asymptotic at zero charge. This is a derivative of
the actual finite source, obtained directly from its physical nodes.
Its exponential rate is the complete-edge rate, independent of the fixed
signed crossing powers. It is an inserted observation, not the original unit
coupon or a lower bound for the original knot invariant.

## 1. The original finite source and the assertion

Fix an integer \(N\ge2\), put \(d=N-1\), \(q=e^{\pi i/N}\), and

\[
 \eta=(-1)^d,\qquad P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^d]\operatorname{rem}_{P_N}f.
 \tag{1}
\]

Here \(T_N\) is the Chebyshev polynomial of the first kind. Use the full
algebra \(A_N=\mathbb C[z]/P_N\), including its repeated-root normals,
and the original Newton polynomials and edge kernel of [S]:

\[
 S_a=\prod_{j=1}^a2\sin(\pi j/N),\quad S_0=1,\quad
 e_a(z)=S_a^{-2}\prod_{j<a}(2\cos((2j+1)\pi/N)-z),
\]
\[
 K_N(t,u)=\sum_{a=0}^{d}e_a(-2\cos t)e_a(-2\cos u).
 \tag{2}
\]

Let \(\mathcal C_{N,\chi}\) be the actual entire Hermite family of
[D, Section 9]. At a double root \(c_\tau=-2\cos\tau\), \(0<\tau<\pi\),
its complete data are

\[
 \mathcal C_{N,\chi}(c_\tau)=\cos(N(1-\chi)\tau),\qquad
 \mathcal C_{N,\chi}'(c_\tau)
 =-\frac{N(1-\chi)\sin(N(1-\chi)\tau)}{2\sin\tau}.
 \tag{3}
\]

At the odd-level simple root \(-2\), its value is one. Define

\[
             \mathfrak d_N=\left.\partial_\chi
                                      \mathcal C_{N,\chi}\right|_0.
 \tag{4}
\]

This notation does not denote a modified quantum dimension.

Let \(\Gamma=(V,E)\) be a fixed finite undirected graph carrying exactly
the same-index kernels (2). Repeated edges and loops are allowed.
Choose a nonempty set \(I\subseteq V\) of selected vertices, none isolated.
Put \(m=|I|\), \(e=|E|\), and let \(d_v\ge1\) be the original degree of
\(v\in I\), counting a loop twice. Every unselected boundary angle is
fixed at zero. Fix integers \(n_v\), of either sign or zero, before
taking \(N\to\infty\).

Use the original crossing packet
\(R_N=q^{d^2/2}\sum_{a=0}^d(-q)^a e_a\), with the displayed exponential
meaning of its fractional power, and retain all its original phases.
Its nodal value, in the normalization of [S, Sections 3 and 7], is

\[
 R_N(c_t)^{n}=C_{N,n}e^{inNt^2/(4\pi)},\qquad
 C_{N,n}=\exp\!\left(\frac{\pi i n(N-1)^2}{4N}\right).
 \tag{5}
\]

Products and negative powers are taken in the full original algebra.
Define the actual normal source

\[
 Z_N^{\rm nor}=
 \left(\prod_{v\in I}\phi_N^{(v)}\right)
 \left[\prod_{v\in I}R_N(z_v)^{n_v}\mathfrak d_N(z_v)
                  \prod_{vw\in E}K_N(t_v,t_w)\right],
 \qquad z_v=-2\cos t_v.
 \tag{6}
\]

For a loop the factor is \(K_N(t_v,t_v)\). No outside polynomial is
reduced, and no semisimple replacement precedes (6).

**Theorem.** Put

\[
 G_{\rm Cat}=\int_0^{\pi/4}\log(\cot s)\,ds,\qquad
 M_\infty=\frac{4G_{\rm Cat}}\pi,\qquad
 \varepsilon_N=\prod_{v\in I}C_{N,n_v}.
\]

Then, through both level parities,

\[
 \boxed{\quad
 Z_N^{\rm nor}=\varepsilon_N N^{3(m-e)/2}
       (2\pi)^m4^{-e}\prod_{v\in I}(d_v-in_v)^{-3/2}
       e^{NeM_\infty}\bigl(1+O(N^{-1})\bigr).
 \quad}
 \tag{7}
\]

The powers use the branch positive on the positive real axis, continued
in the right half-plane. In particular the leading coefficient is
nonzero. Constants may depend on the fixed graph and power vector.
The exact identities below hold at every level; (7) is a large-level
asymptotic and does not assert nonvanishing at every small level.

## 2. The charge derivative retains exactly the nodal values

At each double root, \(\cos(N\tau)=\eta\) and \(\sin(N\tau)=0\).
Differentiating the actual data (3), rather than a lattice asymptotic,
gives

\[
 \mathfrak d_N(c_\tau)=0,\qquad
 \mathfrak d_N'(c_\tau)=\frac{\eta N^2\tau}{2\sin\tau},\qquad
 P_N''(c_\tau)=\frac{N^2}{2\sin^2\tau}.
 \tag{8}
\]

The normal's value at the odd simple root is zero. Since \(P_N\) is
monic of degree \(N\), the top coefficient of a remainder equals the
sum of the finite residues of \(f/P_N\). For any polynomial \(E\),
put \(f=\mathfrak d_NE\). The
residue at a double root is \(2\mathfrak d_N'(c)E(c)/P_N''(c)\).
Consequently the exact full-algebra identity is

\[
 \phi_N(\mathfrak d_NE)
       =2N^2\sum_{\tau\in\mathcal T_N}\tau\sin\tau\,E(c_\tau),
 \quad
 \mathcal T_N=\left\{\frac{\pi(N-1-2l)}N:
                          0\le l<\lfloor N/2\rfloor\right\}.
 \tag{9}
\]

Thus \(\mathfrak d_N^2=0\) in \(A_N\), while
\(\phi_N(\mathfrak d_N\overline f f)\ge0\); conjugation fixes the real
variable \(z\). These are consequences of the original first normals.
They do not discard those normals from (6).

Enumerate the distinct double nodes as
\(c_l=2\cos((2l+1)\pi/N)\), \(0\le l<r=\lfloor N/2\rfloor\).
They are strictly decreasing. The literal factors in (2) show

\[
 e_a(c_l)>0\ (a\le l),\qquad e_a(c_l)=0\ (a>l),\qquad
 K_N(c_l,c_j)=\sum_{a\le\min(l,j)}e_a(c_l)e_a(c_j)>0.
 \tag{10}
\]

Here the notation \(K_N(c_l,c_j)\) means evaluation in its spectral
arguments. In particular every row \(a\ge r\) vanishes at the retained
nodes. At odd levels this also kills \(a=(N-1)/2\), whose only other
nodal value lies at the simple root. This does not assert that its
double-root normals vanish. Formula (9) now converts (6)
exactly to a finite nodal sum with weights \(2N^2t\sin t\), kernels
(10), and the phases (5).

## 3. A global nodal tail bound

For a physical node \(c_t=-2\cos t\), a nonzero Newton value obeys

\[
 0\le\frac{e_a(c_t)}{e_a(-2)}
   =\prod_{j<a}\left(1-
           \frac{1-\cos t}{1+\cos((2j+1)\pi/N)}\right)
   \le e^{-a(1-\cos t)/2}.
 \tag{11}
\]

If a numerator is zero the same inequality remains true. A zero
denominator can occur only beyond the surviving rows at odd levels;
those values already vanish. At a complete boundary \(t=0\), the
ratio is one wherever defined.

For completeness, the required complete-index estimates are elementary.
Set

\[
 b(x)=2\int_0^x\log(\cot\pi s)\,ds.
 \tag{12}
\]

On compact subintervals of \(0<x<1/2\), midpoint summation in the
cosine numerator and Stirling's formula in the sine denominator give

\[
 e_a(-2)=\frac{e^{Nb(a/N)}}{2N\sin(\pi a/N)}(1+O(N^{-1})).
 \tag{13}
\]

One obtains its uniform logarithmic version down to \(a=0\) by
separating \(\log(2\sin\pi s)=\log s+\log(2\sin\pi s/s)\).
The latter summand is smooth at zero and the former is handled by
Stirling. The cosine summand is smooth on every such lower interval.
The function \(b\) increases to its unique maximum at \(1/4\), then
decreases; \(2b(1/4)=M_\infty\).

Fix, for example, \(\epsilon=1/10\). Equations (12)--(13) imply
\(\sum_{a<\epsilon N}e_a(-2)^2\le CN^A e^{N(M_\infty-\delta)}\)
for some \(\delta>0\). Also [S, (18)] gives
\(K_N(0,0)\le CN^A e^{NM_\infty}\).
Applying (11) to the remaining indices, and using
\((1-\cos t)+(1-\cos u)\le4\), proves for all physical or complete
endpoints

\[
 0\le K_N(t,u)\le CN^A
   e^{N\{M_\infty-c[(1-\cos t)+(1-\cos u)]\}}
 \tag{14}
\]

with some fixed \(c>0\). Thus the whole nodal sum outside any fixed
small angle box is exponentially smaller than \(e^{NeM_\infty}\).
Each selected angle receives its original degree \(d_v\ge1\).
The weights in (9) are polynomial in \(N\), and the nodal crossing
values have modulus one. This also controls every loop and repeated
edge, without dropping a physical row or endpoint current.

## 4. The half-Gaussian coefficient in both parities

The full local kernel theorem imported in [S, (18)] has its original
separately even phase and amplitude. In particular, near zero,

\[
 K_N(t,u)=N^{-3/2}a(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \quad a(0,0)=\tfrac14,\quad
 \psi=M_\infty-\frac{t^2+u^2}{4\pi}+O((t^2+u^2)^2).
 \tag{15}
\]

The amplitude calibration can also be checked directly from (13).
The phase \(2b\) has second derivative \(-8\pi\) at \(1/4\), so real
Laplace summation of \(e_a(-2)^2\) gives
\(K_N(0,0)\sim\tfrac14N^{-3/2}e^{NM_\infty}\).
The exact consecutive-product ratio makes the low sequence unimodal,
so its omitted shoulders have a strict gap. At odd levels the high
values are zero. At even levels, putting \(b=d-a<N/2\), reflection gives
\(e_a(-2)=[N^2e_b(-2)\cos^2(\pi(b+1/2)/N)]^{-1}\le1\)
for \(a\ge N/2\). Thus no additional leading coefficient is hidden in
that calibration.

Put \(x_v=\sqrt N\,t_v\) in the exact nodal sum. The crossing phase
and all incident quadratic terms give
\(\exp[-(d_v-in_v)x_v^2/(4\pi)]\) at vertex \(v\).
Furthermore \(t\sin t=t^2(1+O(t^2))\).

The positive grid has spacing \(2\pi/N\). For even \(N\) it is the
positive midpoint grid; for odd \(N\) it is the positive integer grid,
with its zero point absent and of zero weight. Every factor is
separately even. Reflection therefore converts either grid to half a
full Gaussian lattice. The full-lattice rectangle or midpoint rule has
error \(O(N^{-1})\) at spacing \(2\pi/\sqrt N\): apply the cellwise
second-derivative remainder to a Gaussian times a fixed polynomial.

Taylor's formula in (15), followed by Gaussian moment bounds and
(14), gives the same relative error for the actual kernel product.
For instance first restrict to \(|x_v|\le N^{1/12}\); the error is
bounded by \(N^{-1}\) times a fixed polynomial in the \(x_v\), against
a decaying Gaussian. The remaining scaled angles have exponentially
small Gaussian tails by (14). These arguments apply to complex
Gaussians because \(\Re(d_v-in_v)=d_v>0\).

Each vertex's coefficient is consequently

\[
 2N^2\frac{N}{2\pi}N^{-3/2}
   \int_0^\infty x^2e^{-(d_v-in_v)x^2/(4\pi)}\,dx
       =2\pi N^{3/2}(d_v-in_v)^{-3/2}.
 \tag{16}
\]

Multiplying (16), the edge factors \(4^{-e}N^{-3e/2}\), and the
exact phase \(\varepsilon_N\) proves (7).

## 5. Original-source meaning and continuation limits

If \(Z_N(\boldsymbol\chi)\) denotes (6) with each
\(\mathfrak d_N\) replaced by its actual coupon, finite Hermite
interpolation gives the exact identity

\[
 Z_N^{\rm nor}=
   \left.\left(\prod_{v\in I}\partial_{\chi_v}\right)
                         Z_N(\boldsymbol\chi)\right|_{\boldsymbol0}.
 \tag{17}
\]

No lattice-only charge asymptotic was differentiated. The uniform
zero-face theorem [Z] instead divides a specified principal Fourier
interpolation; it expressly distinguishes that interpolation from
the whole off-lattice coupon source. Formula (7) evaluates the actual
normal observation (17), with arbitrary fixed signed powers.

However \(\mathcal C_{N,0}=\eta\,1\) and
\(\mathcal C_{N,1}=1\). Thus the full source is not divisible by the
charges. Its all-zero value remains \(\eta^m\) times the uninserted
source. Subtraction or antisymmetrization would change the observation;
in particular \(\mathcal C_{N,1}-\mathcal C_{N,-1}=0\).
The positive form in (9) also does not define a quotient preserved by
Newton reversal \(Je_a=e_{d-a}\), the original turn: its null space
contains \(e_d\), while \(Je_d=e_0\) is not null. For example, a reversed
edge \(\sum_a e_a(c_l)e_{d-a}(c_j)\) vanishes at every pair of double
nodes: nonzero factors would require both \(a<r\) and \(d-a<r\), which
is impossible. Such a retained edge is outside theorem (7).

Accordingly (7) supplies a nonzero inserted initializer at the complete
edge rate \(eM_\infty\). For a general graph this has not been identified
with a manifold volume. It gives no source-preserving continuation to
the unit coupon, no control of transported cuts or relative-cycle
coefficients, and no filled-volume or original-knot lower bound.

## Complete proof sources and coverage

Both complete matching proof texts were read:

- [D] [Actual analytic coupon family](research_dominant_saddle_transport.md), 685 lines, SHA-256 `413940497a23e884d726b91f9c0ebc01994fef8216811ed2c6fb0838fc80bb04`.
- [S] [Original finite small-charge source](research_small_charge_path_source.md), 809 lines, SHA-256 `c6d0ce2a4ecf1412aa3752cb8a94c6933bb47acab5d96d879c6f1b17b2db2a90`.

The complete [Z] [zero-charge low-source theorem](research_zero_charge_uniform_low_source.md), 496 lines, SHA-256 `d4412c67ca520894840b80e390058ce2438af906ea13f719abb5def5c252496d`, was read for coverage. It does not assert (17)'s actual normal asymptotic.
Only written mathematics and text/hash operations were used. Earlier
finals, manuscripts and public documents were not edited.
