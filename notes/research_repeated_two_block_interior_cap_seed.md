# A stronger actual cap seed for repeated two-crossing Gram blocks

Research deduction, 8 November 2026. No numerical evaluation is used.

One interior coefficient of the actual vector
\(K_{2,N}\mathbf e_0\), where \(K_{2,N}=(M_N^2)^*M_N^2\),
has a nonzero complete finite-sum asymptotic. It gives a strictly
larger second-moment rate than Jensen's bound from the first moment.
Positive moment ratios then improve the lower rate for every longer
original capped word \((2,4,\ldots,2,3)\). No sharp capped rate or
volume identity for these longer knots is asserted.

## 1. A literal coefficient of the full original source

Retain the source, scalar and closing convention of
[repeated reflected block moments](research_repeated_reflected_block_positive_moments.md):
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=q^{D^2/2},\quad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\quad S_0=1,
 \quad K_2=(M^2)^*M^2.
 \tag{1}
\]
Let \(\beta_N=K_2\mathbf e_0\), and write
\(\mu_{m,N}=\mathbf e_0^*K_2^m\mathbf e_0\). Thus
\(\mu_{2,N}=\|\beta_N\|_2^2\), and the literal capped scalar is
\(Z_{2,m,N}=\kappa^{2m-1}\mu_{m,N}\).

The original two-crossing matrix has the exact entries
\[
 (M^2)_{\ell n}
  =\kappa^2 i^{\ell-n}
    q^{\ell(\ell+3)/2+\ell n+n(n+1)/2}
       \frac{S_\ell^2}{S_n^2S_{\ell-n}},
 \qquad 0\le n\le\ell\le D.
 \tag{2}
\]
It is zero outside this triangle. To check (2), substitute
\(i=D-\ell,j=n\) in the exact \(JM^2\) formula of
[two-crossing coefficients](research_degree_two_power_two_formula.md),
use \(S_{D-a}=N/S_a\), and retain
\(\kappa^2(-1)^Dq^D=1\). Its first column is the original
\(\kappa^2i^\ell q^{\ell(\ell+3)/2}S_\ell\).
All these are matrix identities in the full Newton algebra.

Taking the Hermitian product in \(K_2\), then putting
\(j=D-\ell\), proves
\[
 \boxed{\quad
 (\beta_N)_n
 =i^n q^{-n(n+1)/2-nD}\frac{N^2}{S_n^2}
       T_N(n/N),\qquad
 T_N(n/N)=\sum_{j=0}^{D-n}q^{nj}\frac{S_{j+n}}{S_j^3}.
 \quad}
 \tag{3}
\]
In particular \(T_N(0)=\sum_jS_j^{-2}\) and
\((\beta_N)_0=N^2\sum_jS_j^{-2}=\mu_{1,N}\).
The endpoint \(n=D\) is also included in (3). No cap or outgoing
observation has been freely chosen, and no physical row is absent.

## 2. The selected analytic phase and its action increase

Use the original holomorphic primitive
\[
 J(z)=\int_0^z\operatorname{Log}(2\sin\pi w)\,dw
 \tag{4}
\]
continued from \(0<z<1\), and put
\[
 F(x,t)=J(x+t)-3J(x)+i\pi tx,
 \qquad x_0=1/6,\qquad c=-2J(1/6)=2J(5/6).
 \tag{5}
\]
Near \((x_0,0)\), this is holomorphic and
\[
 F_x(x_0,0)=0,\qquad F_{xx}(x_0,0)=-2\pi\sqrt3.
 \tag{6}
\]
The implicit function theorem supplies a unique holomorphic
\(x(t)\) through \(x_0\) with \(F_x(x(t),t)=0\). Set
\[
 \Phi(t)=F(x(t),t),\qquad
 A(t)=\sqrt{\frac\pi2}
       \sqrt{\frac{\sin\pi(x(t)+t)}{\sin^3\pi x(t)}}
       \frac1{\sqrt{-F_{xx}(x(t),t)}}.
 \tag{7}
\]
All square roots continue their positive real choices at zero;
in particular \(A(0)=3^{-1/4}\). Direct differentiation gives
\[
 \begin{gathered}
 x'(0)=\frac12+\frac{i}{2\sqrt3},\qquad
 \Phi(0)=c,\qquad \Phi'(0)=\frac{i\pi}{6},\\
 \Phi''(0)=\frac{4\pi}{\sqrt3}+i\pi.
 \end{gathered}
 \tag{8}
\]
For example \(F_{xt}(x_0,0)=\pi\sqrt3+i\pi\),
\(F_{tt}(x_0,0)=\pi\sqrt3\), and
\(\Phi''=F_{tt}-F_{tx}^2/F_{xx}\), fixing both signs in (8).

For positive real \(t\) close to zero define
\[
 \mathcal S(t)=\Re\Phi(t)-2J(t).
 \tag{9}
\]
Since
\(J(t)=t\log(2\pi t)-t+O(t^3)\), equations (8)--(9) give
\[
 \mathcal S(t)=c+2t[1-\log(2\pi t)]
                     +\frac{2\pi}{\sqrt3}t^2+O(t^3)>c
 \tag{10}
\]
on a sufficiently small fixed interval \(0<t\le\tau\).
The number \(\tau>0\) will also satisfy the source conditions
proved next; it is chosen once, independently of \(N\).

## 3. The complete finite sum has this nonzero leading term

**Theorem 1.** There is \(\tau>0\) such that, uniformly for all
physical \(n\) with \(0\le n/N\le\tau\),
\[
 \boxed{\quad T_N(n/N)
  =N^{-1/2}A(n/N)e^{N\Phi(n/N)}(1+O(N^{-1})).\quad}
 \tag{11}
\]
The estimate is through all integer levels and retains the entire
sum (3), including both physical ends. No continuation of its
moving upper index to noninteger \(n\) is asserted.

*Proof.* Choose fixed \(0<a<x_0<b<1/2\), for example
\(a=1/12,b=1/4\). The real function \(-2J(x)\) on \([0,1]\)
has its unique global maximum \(c\) at \(x_0\): its derivative is
\(-2\log(2\sin\pi x)\), with its only other interior zero
at \(5/6\), a strict minimum. Thus there is \(g>0\) such that
its value outside \((a,b)\) is at most \(c-g\).

The entire closed triangle \(x,t\ge0,x+t\le1\) has the continuous
real profile \(J(x+t)-3J(x)\). Uniform continuity and the
endpoint-uniform factorial estimate therefore give, for sufficiently
small fixed \(\tau\), an absolute upper bound
\[
 \sum_{j/N\notin(a,b),\ 0\le j\le D-n}
        \frac{S_{j+n}}{S_j^3}
   \le C N^C e^{N(c-g/2)}\qquad(0\le n/N\le\tau).
 \tag{12}
\]
Here \(|q^{nj}|=1\), and \(\Re\Phi(t)\) is within \(g/4\) of
\(c\) after a further shrinking. This pays the full omitted real
sum, not merely a rowwise approximation on a compact interior.

For the retained indices use the original canonical sine factorial
\(G_N\) from
[factorial continuation](research_terminal_reflected_factorials.md),
Section 1, and its regular expansion from
the canonical factorial lemma in
[the original factorial source](../papers/conway-asymptotics/factorial.tex).
The endpoint-uniform absolute estimate used in (12) is also recorded in
[uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md).
The exact interpolant is
\[
 f_N(x,t)=e^{i\pi Ntx}
                    \frac{G_N(N(x+t))}{G_N(Nx)^3}.
 \tag{13}
\]
At \(x=j/N,t=n/N\), this is exactly the summand in (3).
On a fixed small complex rectangle around \([a,b]\), with small
complex \(t\), the scaled factorial arguments \(x,x+t\) have real
parts strictly between zero and one. The function is holomorphic there, and its
uniform holomorphic expansion is
\[
 f_N(x,t)=\frac1{2N}
    \sqrt{\frac{\sin\pi(x+t)}{\sin^3\pi x}}
        e^{NF(x,t)}(1+O(N^{-1})).
 \tag{14}
\]
This is the same canonical interpolation used in the complete
two-crossing coefficient source; the factors are not inferred from
values at a few physical nodes.

Here are all the finite contour pieces. Let the retained indices be
\(aN<j<bN\) and put the vertical sides at the immediately adjacent
half-grid points \(a_N,b_N\). Fix a sufficiently small height
\(H>0\), independent of \(N\). On the closed rectangle
\([a_N,b_N]+i[-H,H]\), choose \(H\), then \(\tau\), so that
\[
 \Re F_{xx}<-\gamma<0,\qquad
 |\Im F_x|<\pi/2,\qquad
 a_N<\Re x(t)<b_N,\qquad 0\le\Im x(t)<H/2.
 \tag{15}
\]
These follow from (6), \(F_{xx}(x,0)=-2\pi\cot\pi x<0\) on
\([a,b]\), real \(F_x(x,0)\), and (8). In addition the real
cut profiles stay below \(c-3g/4\), the entire real maximum is
within \(\pi H/4\) of \(c\), and
\(|\Re\Phi(t)-c|<\min(g/4,\pi H/4)\). Take \(H\) small enough
that \(\pi H/2<g/4\). All these are compatible strict conditions
at \(t=0\), and persist after shrinking \(\tau\).

The exact residue formula with \(\pi N\cot(\pi Nx)\), oriented
counterclockwise on this finite rectangle, equals the retained
sum. On its upper and lower halves split the cotangent into its
constant modes \(-i\) and \(+i\), respectively, and the two
remainders. The two constant pieces, including their vertical
portions, give precisely \(+N\int_{a_N}^{b_N}f_N(x,t)\,dx\).
No endpoint contribution has been deleted in this splitting.

On the horizontal sides the remainders have rate \(-2\pi H\).
By (15), the change of \(\Re F\) from the real line is at most
\(\pi H/2\). The real-maximum and critical-action allowances just
specified show a strict gap at least \(\pi H\) below
\(\Re\Phi(t)\). On either half-grid vertical side, at height
\(h\), the corresponding remainder is bounded by a constant
times \(e^{-2\pi N|h|}\), including \(h=0\). Its complete profile
is at most the real-cut value minus \(3\pi|h|/2\). Thus all four
vertical remainder pieces have a fixed gap as well. Polynomial
prefactors in the kernels and (14) do not alter these strict gaps.

Deform the remaining unweighted real integral to the horizontal
line at height \(\Im x(t)\). Its two unweighted vertical joins
stay below \(c-g/2\), by the cut gap and the choice of \(H\).
On the new horizontal segment, (15) gives a unique strict maximum
of \(\Re F\) at \(x(t)\), since \(F_x(x(t),t)=0\). The usual
one-variable analytic Gaussian expansion, with negative real
quadratic part and the positive continued square root, gives
\[
 N\int_{a_N}^{b_N} f_N(x,t)\,dx
  =N^{-1/2}\sqrt{\frac\pi2}
    \sqrt{\frac{\sin\pi(x(t)+t)}{\sin^3\pi x(t)}}
    \frac{e^{N\Phi(t)}}{\sqrt{-F_{xx}(x(t),t)}}
       (1+O(N^{-1})).
 \tag{16}
\]
This includes \(t=0\); its displaced height then equals zero.
The factor \(+N\), the \((2N)^{-1}\) in (14), and the Gaussian
\(\sqrt{2\pi/N}\) give exactly the constant in (16). All bounds
are uniform on the stated closed parameter interval. Equations
(12)--(16) prove (11) for the full original sum. \(\square\)

## 4. Strictly stronger rates for the entire positive capped word

Fix any \(t_0\in(0,\tau)\), and let \(n_N\) be an integer nearest
to \(Nt_0\), with \(t_N=n_N/N\). Theorem 1, (3), and the regular
factorial formula at \(t_0\) prove
\[
 (\beta_N)_{n_N}
 =i^{n_N}q^{-n_N(n_N+1)/2-n_ND}
  N^{1/2}\frac{A(t_N)}{2\sin\pi t_N}
  e^{N[\Phi(t_N)-2J(t_N)]}(1+O(N^{-1})).
 \tag{17}
\]
Its leading coefficient is nonzero; in particular
\[
 \mu_{2,N}\ge C_{t_0}N e^{2N\mathcal S(t_0)},
                   \qquad C_{t_0}>0,
 \tag{18}
\]
for all sufficiently large levels. Rounding changes the real exponent
by a bounded amount, which is included in \(C_{t_0}\).

The first moment has the existing exact asymptotic
\[
 \mu_{1,N}=\sum_{j=0}^{D}S_j^2
    =3^{-1/4}N^{3/2}e^{Nc}(1+O(N^{-1})),
 \tag{19}
\]
as follows by reflection from the reciprocal-factorial Laplace sum
in the [positive-cycle theorem](research_positive_three_crossing_cycle.md),
equations (22)--(24). Positive moment
ratios now give, for every fixed \(m\ge2\),
\[
 \mu_{m,N}\ge\frac{\mu_{2,N}^{m-1}}{\mu_{1,N}^{m-2}}
 \ge C_{m,t_0}N^{2-m/2}
   e^{N[2(m-1)\mathcal S(t_0)-(m-2)c]},
 \qquad C_{m,t_0}>0.
 \tag{20}
\]
Thus the entire original capped scalar satisfies
\[
 \boxed{\quad
 \liminf_N N^{-1}\log|Z_{2,m,N}|
 \ge mc+2(m-1)[\mathcal S(t_0)-c]>mc
                          \qquad(m\ge2).
 \quad}
 \tag{21}
\]
The improvement comes from an actual nonzero interior observation
of the full initialized vector. Positivity is used only after that
coefficient has been estimated, to retain it in the full norm and
to propagate the moment ratios. No arbitrary Gaussian input,
unproved cap overlap, or signed-tail cancellation is assumed.

All original normals and both quantum-level parities are included.
The theorem estimates physical coefficient rows and the capped
moments; it makes no assertion of a uniform interpolated packet in
a continuously varying row parameter outside the retained analytic
chart. The operator-norm upper rate and the cyclic trace result of
the preceding note remain different quantities. Matching the new
lower bound to an upper bound and identifying the longer knot's
geometric volume are still open.
