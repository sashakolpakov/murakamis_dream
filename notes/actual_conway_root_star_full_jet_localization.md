# Full-Hermite localization for an actual Conway root star

31 October 2026. This proves an absolute
whole-source upper bound and strict child-alias/child-color gaps for
the literal scalar

\[
Z_N(j_0,\ldots,j_s)=
\phi\!\left(h_{j_0}^{\varepsilon_0}
 \mathsf T\!\left(\prod_{i=1}^s h_{j_i}^{\varepsilon_i}\right)\right).
\]

Here \(h_j^\varepsilon=\mathsf T(R^\varepsilon L_j)\), \(\varepsilon_i\in\{0,1,-1\}\), and \(s\ge1\) is fixed.
It preserves every repeated Casimir root and its first normal.
It does NOT prove the remaining root-only far-color gap, a full filling
asymptotic, or a norm estimate preserving the optimized action of an
arbitrary turned child.

The inputs are the [exact color source algebra](actual_pure_conway_auxiliary_color_leaf.md), the [full Newton half-twist transport](actual_odd_conway_newton_transport.md), and the [uniform coherent-core recurrence bound](actual_pretzel_global_core_spectral_gap.md). The [root-character Fourier contraction](actual_conway_root_character_fourier_contraction.md) uses the angular estimate below to control root aliases and root-only far colors. The [general all-core packet theorem](actual_conway_general_core_packet_and_gap.md) supplies the complementary original wire-window statement. Neither companion is needed to infer the estimates proved here.

## 1. The actual full-jet norm and the marked scalar

Put \(d=N-1\) and \(\theta=\pi/N\).

\[
\begin{gathered}
P_N(z)=2T_N(z/2)+2,\qquad c_k=2\cos((2k+1)\theta),\quad0\le k<N,\\
B_r(z)=\prod_{a=0}^{r-1}(c_a-z),\qquad
\widehat B_r=B_r/s_r^2,\qquad
s_r=\prod_{a=1}^r2\sin(a\theta).
\end{gathered}
\]

The original algebra is \(\mathbb C[z]/(P_N)\). Each distinct interior node is
double; at odd \(N\) there is also the simple node \(-2\). On this full algebra
define

\[
\|F\|_{\mathcal J}=
\max\left\{\max_{\text{double }c}(|F(c)|+|F'(c)|),
 \ |F(-2)|\ \text{if }N\text{ is odd}\right\}.
\tag{1}
\]

The derivative at the odd simple node is not a quotient invariant and
is deliberately absent. This is a genuine norm, and the ordinary product
rule proves exactly

\[
\|FG\|_{\mathcal J}\le\|F\|_{\mathcal J}\|G\|_{\mathcal J}.
\tag{2}
\]

The original marked functional is
\(\phi(F)=(-1)^dN^2[z^d]\operatorname{rem}_{P_N}F\). Equivalently it is the sum of the
finite residues of \((-1)^dN^2F/P_N\). At a double node \(c=2\cos t\),

\[
\frac{P_N''(c)}2=\frac{N^2}{4\sin^2t},\qquad
\frac{P_N'''(c)}6=\frac{N^2\cos t}{8\sin^4t}.
\]

These follow by differentiating
\((4-z^2)P_N''-zP_N'+N^2(P_N-2)=0\). Therefore

\[
\begin{aligned}
\phi(F)&=(-1)^d\sum_{\text{double }c}
 [(4-c^2)F'(c)-cF(c)]+\mathbf1_{N\text{ odd}}F(-2),\\
|\phi(F)|&\le3N\|F\|_{\mathcal J}.
\end{aligned}\tag{3}
\]

In particular the norm does not replace \(\phi\) by its semisimple trace.

The unturned physical root coupon has only polynomial cost:

\[
\|R^\varepsilon L_j\|_{\mathcal J}\le CN^3,\qquad
1\le j\le N,\quad\varepsilon\in\{0,1,-1\}.
\tag{4}
\]

Indeed \(|L_j(z)|=|U_{j-1}(z/2)|\le j\) on \([-2,2]\); Markov's inequality
gives \(|L_j'|\le j(j-1)^2/2\) there. The original Hermite crossing has
unit-modulus node values and

\[
\frac{R'(c_k)}{R(c_k)}
 =-\frac{d-2k}{4i\sin((2k+1)\theta)}.
\]

at the double nodes, of modulus at most \(N^2/8\). The inverse has the
negative logarithmic derivative and the same modulus. The original
Cartan scalar is a unit phase.

By the full Frobenius turn identity, with no tangle isotopy asserted,

\[
Z_N=\phi(R^{\varepsilon_0}L_{j_0}E_N),\qquad
E_N=\prod_{i=1}^s h_{j_i}^{\varepsilon_i}.
\tag{5}
\]

Combining (2)--(5) gives the general algebraic criterion

\[
|Z_N|\le CN^4\|E_N\|_{\mathcal J}.\tag{6}
\]

Thus any actual child estimate in this norm passes through every
physical root color and both half-twist signs at polynomial cost.
The question is the size of the CHILD norm, not the root character.

## 2. High Newton coordinates have only polynomial normal size

Let \(\lceil N/2\rceil\le r\le d\) and \(\ell=N-r\le\lfloor N/2\rfloor\).
Reflection \(c_{d-a}=c_a\) gives the exact polynomial identity

\[
B_r(z)B_\ell(z)=(-1)^NP_N(z).\tag{7}
\]

\(\widehat B_r\) vanishes at all the actual nodes. Its derivative at a double
node \(c_k\), indexed uniquely by \(0\le k<\lfloor N/2\rfloor\), is also zero unless \(k<\ell\).
When \(k<\ell\) both factors in (7) have a simple zero. Since

\[
|B_\ell'(c_k)|
=\frac{s_{\ell+k}s_{\ell-1-k}}{2\sin((2k+1)\theta)},
\qquad s_rs_{\ell-1}=N.
\]

the quadratic term of (7) gives

\[
|\widehat B_r'(c_k)|
=\frac{s_{\ell-1}^2}
 {2\sin((2k+1)\theta)s_{\ell+k}s_{\ell-1-k}}.
\tag{8}
\]

This includes \(\ell=1\) and both endpoint parities. To bound it, put

\[
D_k=\frac{s_{\ell+k}s_{\ell-1-k}}{s_{\ell-1}^2}.
\]

One has \(D_0=2\sin(\ell\theta)\), while

\[
\frac{D_{k+1}}{D_k}
=\frac{\sin((\ell+k+1)\theta)}{\sin((\ell-1-k)\theta)}
\ge1.
\]

The two positive angles sum to \(2\ell\theta\le\pi\), and the first is
the larger. Thus

\[
\|\widehat B_r\|_{\mathcal J}
\le\max_{0\le k<\ell}
\frac1{4\sin((2k+1)\theta)\sin(\ell\theta)}
\le\frac{N^2}{16}.
\tag{9}
\]

All high-coordinate first normals are retained in this estimate.
At odd \(N\) the simple-node value is zero, as required by (1).
The exact constant is not needed later; polynomial growth is.

## 3. Low-degree interpolation costs only a polynomial

Let \(M=\lfloor(N-1)/2\rfloor\). For every polynomial \(F\) of degree at most \(M\),

\[
\|F\|_{\mathcal J}\le CN^5\max_{\text{distinct }c}|F(c)|.
\tag{10}
\]

Here is an elementary interpolation proof covering both parities.
At even \(N=2m\) the distinct nodes are the zeros of
\(Q_N(z)=2T_m(z/2)\). At odd \(N=2m+1\) they are the zeros of

\[
Q_N(z)=(z+2)\bigl[U_m(z/2)-U_{m-1}(z/2)\bigr].
\]

The number of nodes is \(M+1\). In the even case \(\|Q_N\|_{[-2,2]}\le2\) and
\(|Q_N'(c)|\ge m\). In the odd case \(\|Q_N\|_{[-2,2]}\le4N\). At an interior
node \(c=2\cos t\), the identity

\[
U_m(\cos t)-U_{m-1}(\cos t)=\frac{\cos(Nt/2)}{\cos(t/2)}.
\]

gives \(|Q_N'(c)|=N/[2\sin(t/2)]\ge N/2\); at \(-2\) its magnitude is \(N\).
Markov's inequality bounds \(\|Q_N'\|\) by \(CN^3\) in both cases.
The real mean-value theorem therefore bounds each Lagrange cardinal
\(Q_N(z)/[(z-c)Q_N'(c)]\) by \(CN^2\) on \([-2,2]\). Summing at most \(N\) cardinals
gives \(\|F\|_{[-2,2]}\le CN^3\max_c|F(c)|\). A final Markov inequality
gives (10), including all the double-node derivatives.

For \(r\le M\), index the distinct nodes by \(0\le k\le M\).
The actual nodal values \(\widehat B_r(c_k)\) are nonnegative:
they vanish if \(k<r\) and every factor is positive otherwise. Moreover

\[
\max_c\widehat B_r(c)\le\widehat B_r(-2).
\]

Thus for any coefficients \(a_r\),

\[
\left\|\sum_{r=0}^M a_r\widehat B_r\right\|_{\mathcal J}
\le CN^5\sum_{r=0}^M|a_r|\widehat B_r(-2).
\tag{11}
\]

The positive expression on the right is only an upper bound. No
positivity of a signed source polynomial on an interval is assumed.

Uniform sine-factorial summation, including the integrable endpoint
at \(r/N=1/2\), yields

\[
\begin{gathered}
\log\widehat B_r(-2)=Ng(r/N)+O(\log N),\qquad0\le r\le M,\\
g(x)=J(2x)-4J(x),\qquad
J(x)=\int_0^x\log(2\sin\pi t)\,dt.
\end{gathered}\tag{12}
\]

Indeed the logarithmic rate is
\(2\int_0^x\log\cot(\pi t)\,dt\). It vanishes at \(x=0\) and has the same
derivative as \(g\). The midpoint cosine product and ordinary sine
factorials each have uniform \(O(\log N)\) errors on this closed range.

## 4. Actual leaf core and alias bounds in the full-jet norm

Let

\[
\begin{gathered}
G_0=g(1/4)=\frac{2\,\mathrm{Catalan}}{\pi},\qquad
K_0=\max_{0\le u\le1}k(u)=\frac{v_3}{\pi},\\
k(u)=-2J(u/2),\qquad\Delta=G_0-K_0>0.
\end{gathered}\tag{13}
\]

The maximum of \(k\) is at \(u=1/3\); the duplication identity for \(J\) gives
its value \(v_3/\pi\). Positivity of \(\Delta\) is elementary. For instance
\(\mathrm{Catalan}>8/9\) and

\[
v_3=\frac{3\sqrt3}{4}\sum_{n\ge0}
\left[(3n+1)^{-2}-(3n+2)^{-2}\right]<\frac{301}{256}.
\]

follow by keeping the first term, bounding the remaining positive
series by \(1/16+\int_1^\infty(3x+1)^{-2}\,dx=7/48\), and using \(\sqrt3<7/4\).
Hence \(\Delta>1387/(2304\pi)>0\).

Write the exact physical leaf as \(C_j^\varepsilon+A_j^\varepsilon\). The proved coherent
core coefficients have the UNIFORM exponential upper rate
\(\widetilde g(u)=g(\max(u,1/4))\); pure coefficients satisfy the stronger \(g\).
Equations (10)--(12) give

\[
\max_{j,\varepsilon}\|C_j^\varepsilon\|_{\mathcal J}
\le\exp\{N(2G_0+o(1))\}.
\tag{14}
\]

The \(o(1)\) is uniform over the original physical colors and indices.
Its proof is the actual complete-diagonal recurrence with its terminal
source, not an assumed coefficientwise contraction under a half twist.
The key maximization is

\[
\max_{0\le u\le1/2}\{\widetilde g(u)+g(u)\}=2G_0.
\]

and this maximum is unique at \(u=1/4\). Thus the Newton evaluation weight
removes the flat plateau of \(\widetilde g\) which obstructs the bare coefficient
argument at quarter leaves.

For an alias, split its actual polynomial into indices \(\le M\) and \(>M\).
The low part is bounded by (11), the high part by (9). The full
triangular transport theorem gives coefficient rate at most \(k(u)\) on
ALL \(0\le u\le1\), with only a polynomial prefactor. Therefore

\[
\max_{j,\varepsilon}\|A_j^\varepsilon\|_{\mathcal J}
\le\exp\{N(G_0+K_0+o(1))\}
=\exp\{N(2G_0-\Delta+o(1))\}.
\tag{15}
\]

For the low part use \(g\le G_0\) and \(k\le K_0\). For the high part
\(\max_{u\ge1/2}k(u)=k(1/2)=G_0/2\), which is smaller still.
This is not an alias value-only bound: (9) is precisely the estimate
of the normals invisible at all nodes.

There is also a strict child-color gap. For every fixed \(\delta>0\) there
is \(\gamma_\delta>0\) such that

\[
\max_{\substack{N-j\ge\delta N\\\varepsilon}}
\|h_j^\varepsilon\|_{\mathcal J}
\le\exp\{N(2G_0-\gamma_\delta+o(1))\}.
\tag{16}
\]

If \(j\le\lfloor N/2\rfloor\), the core is absent and (15) applies. Otherwise
\(h=N-j\le M\). Fix \(\beta\in(1/4,1/2)\). For \(r\le\beta N\), the exact global
far-color recurrence subtracts a positive constant from \(\widetilde g\)
uniformly when \(h\ge\delta N\). For \(r>\beta N\), \(g+\widetilde g=2g\) has a
fixed gap below \(2G_0\). Equations (10)--(12) prove the claimed bound
for the signed cores; for the pure core the original ratio
\(J(x-t)+J(x+t)-2J(x)\) supplies the same strict loss near quarter.
Adding the alias bound proves (16).

## 5. The original product star and its exact exponential reference

For each fixed \(s\), (2), (6), and (14)--(16) imply

\[
\sup_{\text{physical }j_i,\varepsilon_i}
|Z_N(j_0,\ldots,j_s)|\le\exp\{N(2sG_0+o(1))\}.
\tag{17}
\]

with both parities and every original normal term retained.
Every nonempty CHILD alias sector has rate at most \(2sG_0-\Delta\),
and whenever at least one CHILD color satisfies \(N-j_i\ge\delta N\),
the whole source has a uniform strict gap below \(2sG_0\).
The root color \(j_0\) and sign \(\varepsilon_0\) are unrestricted in these statements.

The reference \(2sG_0\) is exactly the actual pure complete action, rather
than a convenient larger norm. At all complete pure colors,

\[
Z_N(N,\ldots,N)=\phi(L_Nh_N^s)
=N\sum_{k=0}^{N-1}h_N(c_k)^s>0.
\tag{18}
\]

The complete \(h_N\) has positive Newton coefficients
\(a_{N,r}=N^2s_{2r}/s_r^4\) of rate \(g(r/N)\). From (12), its maximum
nodal value has upper rate \(2G_0\). Conversely choose \(r=\lfloor N/4\rfloor\)
and the smallest node \(c_M\). For odd \(N\) this is \(-2\). For even \(N\),
\(c_M+2=O(N^{-2})\); on the chosen \(r\) range every \(c_a+2\) is bounded
away from zero, so replacing \(-2\) by \(c_M\) changes the logarithm of
this single positive term by \(O(N^{-1})\). That term has rate \(2G_0\).
Thus

\[
\lim_{N\to\infty}\frac1N\log\max_kh_N(c_k)=2G_0,\qquad
\lim_{N\to\infty}\frac1N\log Z_N(N,\ldots,N)=2sG_0.
\tag{19}
\]

In particular (17) does not pay a spurious root-leaf alias action.
For the critical family \(\mathsf C(h\,\mathsf T(h^s))\), its geometric value, when that
geometry is invoked, is the same original complete action (19).
No topological re-rooting or identification with a different source
has been used.

## 6. Boundary of the full-jet estimate

The estimates prove a useful root-independent contraction criterion:
if an arbitrary actual child \(E_N\) has a full-jet rate at most \(F_E\), then all
the literal root-color contractions (5) have rate at most \(F_E\), with the
same strict losses whenever present in the child norm. They do not
prove that \(F_E\) equals the optimized closed action for every child.

In particular the turn is not polynomially bounded in this fixed
norm: \(L_N\) has polynomial jets but \(\mathsf T L_N=h_N\) has rate \(2G_0\).
An arbitrary turned child's internal action cannot be preserved by
simply declaring this Hilbert or trace norm invariant.

For the product star, the ONLY color case not given a strict loss
by (16) is one in which all children remain in the complete corridor
but the root color is macroscopic. Formula (4) estimates that root
character in absolute value and cannot produce its oscillatory
loss. The exact Fourier/Hermite contraction is still required for that case; it is supplied
by the [independently proved root-character theorem](actual_conway_root_character_fourier_contraction.md). In particular this note alone does not restore the full
filling period at its action below the complete value, and asserts
no new long-twist volume equality.

## 7. A global angular Gaussian envelope for the whole child polynomial

The norm estimate has a useful stronger form on a fixed complex angular
strip. Write \(\vartheta\) for its angular coordinate, distinct from
\(\theta=\pi/N\). There are constants \(c,C,y_0>0\) and a uniform \(e_N\to0\) such that
every physical leaf, at all colors and signs, obeys

\[
|h_j^\varepsilon(2\cos(\vartheta+iy))|
\le\exp\{N[2G_0-c(\vartheta-\pi)^2+Cy^2+e_N]\},
\quad0\le\vartheta\le2\pi,\quad |y|\le y_0.
\tag{20}
\]

In particular the positive-axis endpoints have a fixed exponential
gap. The same estimate, with a polynomial multiplier and slightly
smaller \(c\) and \(y_0\), holds for any fixed number of angular derivatives.
Consequently \(E_N\), a product of \(s\) such actual leaves, has the same
type of estimate with complete rate \(2sG_0\). Constants may depend on
the fixed \(s\), not on any physical colors.

Here are the two required arguments, including the normal coordinates.
First, full Hermite interpolation is polynomially conditioned:

\[
\|\operatorname{rem}_{P_N}F\|_{[-2,2]}
\le CN^C\|F\|_{\mathcal J}.
\tag{21}
\]

To see this, first replace \(F\) by its representative of degree below \(N\).
Interpolate the values by a polynomial \(I\) of degree at most \(M\),
using the distinct-node polynomial \(Q_N\) in section 3. Its norm and
derivative norm have polynomial bounds by the proof of (10).
The difference \(F-I\) is divisible by \(Q_N\). Write \(F-I=Q_NG\).
At each double node \(G(c)=(F'(c)-I'(c))/Q_N'(c)\).
For even \(N\) there are \(m\) such nodes and \(\deg G\le m-1\), so the same
Chebyshev interpolation applies. For odd \(N\) there are \(m\) double nodes
and \(\deg G\le m-1\); interpolate at the roots of
\(K_m(z)=U_m(z/2)-U_{m-1}(z/2)\). One has \(\|K_m\|\le N\) and
\(|K_m'(c)|=N/[8\sin(t/2)\cos^2(t/2)]\ge N/8\).
The same mean-value/Markov cardinal argument is polynomial.
Multiplying by \(Q_N\) proves (21).
Expanding that representative of degree below \(N\) in Chebyshev
polynomials, each coefficient has modulus at most twice its interval
supremum. Thus (21) also gives the explicit strip consequence

\[
|F(2\cos(\vartheta+iy))|
\le CN^Ce^{N|y|}\|F\|_{\mathcal J}.
\tag{22}
\]

Apply this to the alias and use (15). For \(y_0<\Delta/4\) its entire
complex-strip rate is at most \(2G_0-3\Delta/4\). This includes precisely
the high-index normals which nodal evaluation alone would miss.

For a core, all Newton indices are at most \(M\). Its termwise upper action is

\[
\begin{aligned}
\mathcal A(u,\vartheta,y)&=\widetilde g(u)+b(u,\vartheta,y),\\
b(u,\vartheta,y)&=\int_0^u
\log|2\cos(2\pi v)-2\cos(\vartheta+iy)|\,dv-2J(u).
\end{aligned}\tag{23}
\]

The corresponding finite products have this UNIFORM limsup majorant
on the compact set \(0\le u\le1/2,\ 0\le\vartheta\le2\pi,\ |y|\le y_0\).
For completeness, truncate each logarithm below by \(\log\epsilon\).
The truncated factors are continuous, so their midpoint Riemann sums
converge uniformly. The untruncated sum is bounded above by that sum.
The two circular-distance factors in
\(2\cos(2\pi v)-2\cos(\vartheta+iy)\) have uniformly integrable negative
logarithmic tails. Their integral truncation error tends uniformly
to zero, including coalescing zeros and moving integration endpoints.
The endpoint factorial errors are \(O(\log N)\). Taking N first and then
\(\epsilon\) down to zero proves the required uniform upper bound.

At \(y=0\), the circular-arc rearrangement gives

\[
b(u,\vartheta,0)\le b(u,\pi,0)=g(u).
\tag{24}
\]

strictly when \(0<u<1/2\) and \(\vartheta\ne\pi\bmod2\pi\).
Indeed the numerator integral is \(1/(2\pi)\) times the integral of
\(\log|1-e^{it}|\) on the arc of length \(4\pi u\) centered at \(\vartheta\).
That even circular function is strictly increasing in distance from
zero on \((0,\pi)\); the arc integral is uniquely largest when centered
at \(\pi\), unless the arc is empty or the entire circle.
It follows from (24) and section 4 that \(\mathcal A\) has the unique maximum
\(2G_0\) at \((u,\vartheta)=(1/4,\pi)\).

Near that point none of the numerator factors vanishes. Put
\(w=\vartheta-\pi+iy\). The holomorphic action there is

\[
\begin{gathered}
B(u,w)=-J\!\left(\frac12-u+\frac{w}{2\pi}\right)
-J\!\left(\frac12-u-\frac{w}{2\pi}\right)-2J(u),\\
B(u,0)=g(u),\qquad
B_{ww}(u,0)=-\frac{\tan(\pi u)}{2\pi}.
\end{gathered}\tag{25}
\]

The real part of \(B\) equals \(b\). Its even Taylor expansion in \(w\),
together with the quadratic strict maximum of \(\widetilde g+g\) at \(1/4\),
gives constants \(c_1,c_2,C>0\) such that

\[
\mathcal A(u,\vartheta,y)
\le2G_0-c_1(u-1/4)^2-c_2(\vartheta-\pi)^2+Cy^2.
\]

on a fixed neighborhood. The one-sided second derivatives of
\(\widetilde g\) at \(1/4\) are sufficient: the added \(g\) has strictly negative
second derivative on BOTH sides.
On the complementary compact set at \(y=0\), (24) gives a fixed
strict gap. Continuity of the integral in (23) preserves half that
gap for a sufficiently small fixed \(y_0\). Reducing \(c_2\), if necessary,
puts this whole complement under the right side of (20).
Sum the at most \(N\) core terms and absorb the uniform recurrence error.
The aliases from (22) also fit the same estimate after reducing \(c\).
This proves (20) for the actual whole polynomial.

To obtain derivatives apply Cauchy's estimate on angular disks
of radius \(1/N\) inside a smaller strip. The exponent in (20) changes
by only \(O(1)\), so each fixed derivative costs a power of \(N\).
No arbitrary off-grid continuation of the physical color is used.

## 8. A joint spectral/color packet at the negative endpoint

The [quarter-index source theorem](actual_conway_quarter_index_color_packet.md) gives a nonzero local analytic packet compatible with (20), including all original phases. The canonical factorial continuation is the one in the [exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md).

Choose a fixed small index window \(I\) about \(x_0=1/4\). The selected
normalized local coefficient \(\ell_N^\varepsilon\) has an exponentially accurate
holomorphic interpolant

\[
I_N^\varepsilon(x,t)
=N^{1/2}b_\varepsilon(x,t)e^{Nf_\varepsilon(x,t)}
[1+O(N^{-1})].
\]

Here \(t\) is the actual scaled child deficit, the window is fixed before
\(N\), and the original unnormalized coefficient is
\(e^{i\varepsilon\pi d/4}\ell_N^\varepsilon\). The approximate equality on the physical
index grid is relative exponential, as proved by the source theorem;
we do not use the displayed \(O(N^{-1})\) in place of that fact.

For integer \(r=Nx\), the exact Newton polynomial at \(z=-2\cos w\) has the
canonical interpolation

\[
\mathcal B_N(x,w)=
\frac{\prod_{\pm}G_N(N/2-1/2\pm Nw/(2\pi))}
 {G_N(Nx)^2\prod_{\pm}G_N(N/2-Nx-1/2\pm Nw/(2\pi))}.
\tag{26}
\]

This follows directly by multiplying
\(4\cos(\pi(a+1/2)/N+w/2)\cos(\pi(a+1/2)/N-w/2)\).
All Gamma arguments are in fixed regular strips near the chosen
index window. The canonical factorial expansion gives

\[
\mathcal B_N(x,w)
=\frac{e^{NB(x,w)}}{2N\sin(\pi x)}[1+O(N^{-1})].
\tag{27}
\]

uniformly holomorphically. The half-integer shifts in (26) cancel
the four numerator/denominator sine prefactors; omitting them would
give a wrong amplitude.

Define the exact finite analytic window

\[
W_N^\varepsilon(t,w)=
\sum_{r/N\in I}\ell_N^\varepsilon(r,t)\widehat B_r(-2\cos w).
\]

The factorial source continuation is taken only on this regular
window; there is no proposed continuation of a moving low-index
cutoff. Let

\[
F_\varepsilon(x,t,w)=f_\varepsilon(x,t)+B(x,w).
\]

At \((x,t,w)=(1/4,0,0)\), its data are

\[
\begin{gathered}
F=2G_0,\qquad F_x=0,\qquad F_{xx}=-8\pi,\\
F_{tt}=-\frac{2\pi}{1-\varepsilon i},\qquad
F_{ww}=-\frac1{2\pi},\qquad
F_{xt}=F_{xw}=F_{tw}=0.
\end{gathered}\tag{28}
\]

Thus a unique nearby critical \(x_\varepsilon(t,w)\) is holomorphic and even
separately in \(t,w\). The same finite cotangent-rectangle proof used
for the original wire packet, now in one index, applies to this
fixed window: exponential grid error first, then the nonconstant
cotangent modes and endpoint connectors, then the translated
complex Gaussian. It gives

\[
\begin{aligned}
W_N^\varepsilon(t,w)&=
a_\varepsilon(t,w)e^{N\Phi_\varepsilon(t,w)}[1+O(N^{-1})],\\
\Phi_\varepsilon(t,w)&=F_\varepsilon(x_\varepsilon(t,w),t,w),\\
a_\varepsilon(t,w)&=
\sqrt{\frac{2\pi}{-F_{\varepsilon,xx}(x_\varepsilon(t,w),t,w)}}
\frac{b_\varepsilon(x_\varepsilon(t,w),t)}
 {2\sin(\pi x_\varepsilon(t,w))}\ne0.
\end{aligned}\tag{29}
\]

The power of \(N\) is zero: the coefficient contributes \(N^{1/2}\),
the Newton factor \(N^{-1}\), the primitive one-index sum \(N\), and the
Gaussian \(N^{-1/2}\). Square roots continue their positive complete
Gaussian marks. In particular

\[
a_0(0,0)=\frac14,\qquad
a_\varepsilon(0,0)=\frac14\,2^{-1/4}e^{-i\varepsilon\pi/8},
\quad\varepsilon\in\{-1,1\}.
\tag{30}
\]

These are amplitudes for \(W\), before restoring \(e^{i\varepsilon\pi d/4}\).

For physical \(|h|\le\delta N\), the actual whole leaf satisfies

\[
h_{N-h}^\varepsilon(-2\cos w)=
e^{i\varepsilon\pi d/4}W_N^\varepsilon(h/N,w)
+O\!\left(e^{N(2G_0-\gamma)}\right).
\tag{31}
\]

uniformly for \(w\) in a fixed small complex disk. To prove this, use
the unique index maximum in section 7 to bound the omitted core
indices, and use (15),(22) for the alias. Shrink the \(t,w\) domains
so these fixed residual levels stay below \(\operatorname{Re}\Phi_\varepsilon\). This proves
(31) without analytically extending the full alias in color.

For the product of \(s\) physical children, multiply (29)--(31),
retaining the product of the original unit phases. Its joint
spectral/color packet has phase \(\sum_i\Phi_{\varepsilon_i}(t_i,w)\) and nonzero
amplitude \(\prod_i a_{\varepsilon_i}\). At complete colors its \(w\)-Hessian is
\(-s/(2\pi)\). The exact unturned root chirp discussed in the separate
Fourier contraction calculation adds \(i\varepsilon_0w^2/(4\pi)\), giving

\[
-\frac{s-i\varepsilon_0}{2\pi}.
\tag{32}
\]

Consequently a subsequent local Fourier stationary calculation
has the root color Hessian \(-2\pi/(s-i\varepsilon_0)\), agreeing with the
literal complete root port cotangent \(1/s\). Equation (32) is a
compatibility check and local input; the global root-character
Fourier identity and its endpoint currents remain the separate
contraction proof.


The theorem localizes the stated root-star source. It does not assert a general turned-child bound or a filled-volume theorem.