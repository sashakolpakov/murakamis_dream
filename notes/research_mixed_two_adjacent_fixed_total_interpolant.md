# A fixed-total holomorphic source reaching the merged-pair saddle

Research deduction, 7 November 2026. A fixed finite sum interpolates
the complete inner source at every physical total index in an
explicit interval. Its holomorphic domain includes the actual
positive-height total critical point. This is an exact domain
statement, not continuation of a packet through an unspecified
small neighborhood of the real interval.

The complete fixed-cutoff contour has two entire endpoint currents.
Their original rate profiles are given below. The principal current
has a nonzero Gaussian on the stated symmetric height corridor;
the endpoint currents are not yet compared to that action.
No numerical evaluation is used.

## 1. A cutoff strictly beyond the actual critical real part

Use the original merged source and \(x_0=\xi+i\upsilon\) from
[the critical-corridor theorem](research_mixed_two_adjacent_critical_corridor.md).
That proof writes
\[
 \Re a_*=\frac12-\frac{B}{2\pi},\qquad
 0<B<\pi/2,\qquad \tan B>3/4.
 \tag{1}
\]
The pentagon identity gives
\[
 \tan^2(\pi/5)=5-2\sqrt5<9/16,
 \tag{2}
\]
since \(\sqrt5>71/32\). Thus \(B>\pi/5\), improving the
upper real bound to
\[
 \frac13<\Re a_*<\frac25,\qquad
 c_*:=2a_*,\qquad
 \frac23<\Re c_*<\frac45,\qquad
                    \frac1{10}<\Im c_*<\frac15.
 \tag{3}
\]
The lower height bound is the original \(h_*>1/20\).
For the upper bound use
\(2\operatorname{atanh}(1/4)/\pi<2(23/90)/3<1/5\).
All these are bounds for the actual original critical point.

Fix
\[
 R=4/5,\qquad M_N=\lfloor NR\rfloor,\qquad
 \alpha_N=-1/(2N),\qquad \beta_N=(M_N+1/2)/N.
 \tag{4}
\]
The cutoff is independent of every free parameter.

## 2. The exact finite interpolant and all physical total indices

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), \(X=e^{-2\pi ix}\), and
\(W=e^{-2\pi iy}\). Use the same original factorial
\(\Pi_N\) and reciprocal continuation \(E_N\). Define
\[
\begin{split}
 T_N(a;c,x,y)={}&e^{2\pi iNa(c-a)}\Pi_N(c)
       \Pi_N(a+x)\Pi_N(c-a+y)\\
 &\hspace{8mm}\cdot E_N(a)^2E_N(c-a)^2E_N(x)E_N(y),\\
 H_N(c;x,y)={}&\sum_{j=0}^{M_N}T_N(j/N;c,x,y).
\end{split}
 \tag{5}
\]
The domain of the finite sum includes the entire complex tube
\[
 \mathcal U=\{2/3<\Re c<4/5,\quad
                9/50<\Re x,\Re y<19/100\},
 \tag{6}
\]
with arbitrary finite imaginary parts. In fact at the physical
summation points \(0\le a\le R\), every numerator argument in
(5) has real part strictly between zero and one. Both free
reciprocal arguments \(a,c-a\) have real part less than one.
The original global reciprocal chart is holomorphic there, including
all its negative-index zeros. These are precisely the domains proved
in [the joint factorial chart](research_mixed_fourier_right_cap_joint_global_chart.md)
and [the reciprocal continuation](research_mixed_fourier_global_factorial_cardinal.md).

For a physical total \(c=m/N\) in (6), every \(j>m\) term
in (5) vanishes through the exact factor
\(E_N((m-j)/N)^2=0\); its other factors are finite.
For \(0\le j\le m\), the factorial recurrence gives
\[
 \boxed{\quad
 H_N(m/N;x,y)
   =P_m\sum_{j=0}^{m}
       \frac{r^{-j(m-j)}p_j(X)p_{m-j}(W)}
                         {P_j^2P_{m-j}^2}.
 \quad}
 \tag{7}
\]
Thus (5) equals the complete original inner sum, including \(P_m\),
not a central subset of it. The equality holds for every free
\(x,y\) in (6), and therefore for all their analytic derivatives.
It holds at every admitted physical total along both parities.
No derivative in the new interpolation variable \(c\) is substituted
for a prescribed ordinary normal adapter.

The full pair is still the sum over all \(0\le m<N\).
Replacing its admitted \(m\)'s by (7) leaves every complementary
total index unchanged. In particular this note does not discard the
interval between \(4/5\) and the previously proved diagonal collar.

## 3. A full fixed-cutoff contour and both infinite tails

For \(N\ge64\), the whole strip
\(\alpha_N\le\Re a\le\beta_N\) has all three numerator
arguments in (5) strictly inside the original strip \((0,1)\),
uniformly on compact parameter subsets of (6). For example
\[
 \Re(a+x)<4/5+1/128+19/100<1,\qquad
 \Re(c-a+y)<4/5+1/128+19/100<1,
\]
while
\[
 \Re(c-a+y)>2/3-4/5-1/128+9/50>0.
 \tag{8}
\]
The reciprocal arguments remain below one. Therefore the row is
holomorphic on every finite-height rectangle with these cuts, at
all parameter heights in (6). This proves contour admissibility at
the height of (3), rather than assuming it by continuity.

Set \(k_N(a)=(1-e^{-2\pi iNa})^{-1}\). Both cuts in (4)
are half-grid cuts. For any real \(h\), put
\[
 w_{N,h}(t)=\frac1{1+e^{2\pi Nt}}-\boldsymbol1_{\{t<h\}}.
 \tag{9}
\]

**Theorem 1.** At every \(N\ge64\), on (6), the complete finite
source has the exact representation
\[
\begin{split}
 H_N(c;x,y)={}&N\int_{\alpha_N+ih}^{\beta_N+ih}
                                      T_N(a;c,x,y)\,da\\
 &+iN\int_{-\infty}^{\infty}w_{N,h}(t)
     \{T_N(\beta_N+it;c,x,y)-T_N(\alpha_N+it;c,x,y)\}\,dt.
\end{split}
 \tag{10}
\]
Both endpoint integrals converge absolutely at fixed level, locally
uniformly in all parameters. The first integral has positive
density \(N\).

*Proof.* The bounded residue identity uses the residue
\(1/(2\pi iN)\) of \(k_N\), hence coefficient \(N\).
The exact upper and lower nonreal factorial formulas from
[factorial alias elimination](research_mixed_fourier_factorial_alias_elimination.md)
give the following leading exponents, with nonzero fixed-level
coefficients independent of \(a\):
\[
 T_N(a)=C_{\pm,N}(c,x,y)e^{\pi i P_\pm(a)}(1+o(1)),
 \tag{11}
\]
where the upper sign refers to \(\Im a\to+\infty\), and
\[
\begin{split}
 P_+(a)={}&N[-a^2+(2c-1-2x)a+x-x^2]+a-x,\\
 P_-(a)={}&N[-a^2+(1+2y)a+c^2-c-2cy+y-y^2]-a+c-y.
\end{split}
 \tag{12}
\]
These follow respectively from the upper pairs
\(\Pi_N(a+x)E_N(a)^2\) and
\(\Pi_N(c-a+y)E_N(c-a)^2\), retaining the chirp in (5).
The remaining variable-dependent factors have their lower constants.
The terms \(a-x\) and \(-a+c-y\) retain the original finite-level
corrections in the marked factorial.

At \(a=u+iT\), the upper alias therefore decays at rate
\[
 \pi\{N(1+2\Re c-2\Re x-2u)+1\}T.
 \tag{13}
\]
At \(a=u-iT\), the lower alias decays at rate
\[
 \pi\{N(1-2\Re y+2u)+1\}T.
 \tag{14}
\]
The minimum rates on the full interval in (4) exceed
\(\pi NT/3\) and \(3\pi NT/5\), respectively. For (13)
use \(2\beta_N\le8/5+1/N\); for (14) use
\(2\alpha_N=-1/N\). All constants and the \(o(1)\)'s
are uniform on bounded real intervals and compact parameter sets.
Thus both complete horizontal aliases disappear at fixed \(N\).
The two vertical tails have the same decay. Moving the unweighted
horizontal integral to height \(h\), with both joining sides kept,
gives precisely (9)--(10). \(\square\)

There is also an elementary uniform bound on the remote tails.
On a fixed compact parameter set and for bounded choices of \(h\),
there are constants \(C_K,H_K,C\) such that either endpoint density
satisfies, for \(|t|\ge H_K\) and all sufficiently large \(N\),
\[
 N|w_{N,h}(t)T_N(\alpha_N+it)|,
 N|w_{N,h}(t)T_N(\beta_N+it)|
       \le C N^{-1/2}
                  e^{N\{C_K-\pi|t|/6\}}.
 \tag{14a}
\]
To see this, the six moving factorial copies in (5) have heights
of magnitude at least \(|t|-K\). The exact remainder formula in
the cited alias-elimination note bounds their combined logarithmic
error by \(C_K N(1+|t|)e^{-2\pi(|t|-K)}\). The three fixed
factorial copies have their usual compact-strip bounds and contribute
only a fixed multiple of \(N\) to the exponent. Their powers,
together with the moving copies, give the row power \(N^{-3/2}\).
Taking \(H_K\) large and retaining the strict slopes in
(13)--(14) proves (14a). This argument uses the exact nonreal
formulas on the entire tails, rather than extrapolating a
compact-height expansion to infinity.
Neither (14a) nor the fixed-level identity alone pays the remaining
bounded-height endpoint profiles at the critical action.

## 4. The complete original endpoint profiles at positive total height

Take a compact subset of (6) with \(v=\Im c>0\), and choose
\(h=v/2\). All formulas below use the original regular-strip
primitive \(g\), with its absolute constant. Write \(c_r=\Re c\).
For the left endpoint define
\[
\begin{split}
 D_L(t)={}&\Re\{g(c)+g(x+it)+g(c+y-it)
                          -2g(c-it)-g(x)-g(y)\}
                              -2\pi c_r t,\\
 \mathcal P_L(t)={}&D_L(t)+2\pi t\boldsymbol1_{\{t<h\}}.
\end{split}
 \tag{15}
\]
Every displayed argument has real part in \((0,1)\).
The exact midpoint identity is
\[
 |E_N(\alpha_N+it)|^2=(1+e^{2\pi Nt})/N.
\]
It cancels the entire denominator in \(|w_{N,h}|\). Consequently
on every bounded height interval the absolute left-current density
is at most
\[
                  C N^{-1/2}e^{N\mathcal P_L(t)}.
 \tag{16}
\]
The half-grid shifts in the other arguments change only the
uniform prefactor. The two one-sided values at \(t=h\) are kept;
the value of the weight at that one point is immaterial.

For the right endpoint, compactness and sufficiently large \(N\)
ensure \(\Re(c-\beta_N)<0\). Use the exact reciprocal period
identity
\[
 E_N(c-\beta_N-it)
  =(1+e^{-2\pi iNc}e^{-2\pi Nt})
                      E_N(c-\beta_N+1-it).
 \tag{17}
\]
The factor in parentheses is retained, including its possible zeros.
No division by it occurs. Put
\[
\begin{split}
 D_R(t)={}&\Re\{g(c)+g(R+x+it)+g(c-R+y-it)\\
 &\hspace{13mm}-2g(R+it)-2g(c-R+1-it)-g(x)-g(y)\}\\
 &-2\pi\{R v+(c_r-2R)t\},\\
 p_h(t)={}&
 \begin{cases}2\pi(-t)_+,&t<h,\\2\pi t_+,&t\ge h,\end{cases}\\
 \mathcal P_R(t)={}&D_R(t)+4\pi(v-t)_+-p_h(t).
\end{split}
 \tag{18}
\]
Again every \(g\) argument is in its original regular strip.
The square of the factor in (17) has the zero-safe upper rate
\(4\pi(v-t)_+\). Therefore the right-current density is bounded
on bounded height intervals by
\[
                  C N^{-1/2}e^{N\mathcal P_R(t)}.
 \tag{19}
\]
The exact nonreal factorial remainders and (13)--(14) also control
the entire tails. In particular a compact-height comparison, if
proved with a strict margin, must be supplemented by their original
uniform tail bounds; no endpoint is silently truncated in (10).

## 5. The principal current at the required positive height

Keep \(x=y=x_0\), and let
\[
 2/3<\Re c<4/5,\qquad 1/10<\Im c<1/5.
 \tag{20}
\]
The principal line in (10) has equal internal heights
\(a=t+ih\), \(s=c-a=c_r-t+ih\), where \(h=v/2>0\).
Its endpoint portions can have a negative real reciprocal argument.
They are covered by the original upper-half-plane factorial
continuation, not by a regular-strip assumption there. Explicitly
the marked primitive on that half-plane is
\[
 g_+(z)=\pi iz(1-z)
       +\frac{i}{2\pi}\{\operatorname{Li}_2(e^{2\pi iz})-\pi^2/6\}.
 \tag{21}
\]
It agrees with the original \(g\) on its upper regular strip;
its constant and symbol are fixed by
[the factorial continuation theorem](research_factorial_uniform_halfplane_continuation.md).

The phase of (5) along this whole line is
\[
\begin{split}
 F_c(a)={}&g_+(c)+g_+(a+x_0)+g_+(c-a+x_0)\\
       &-2g_+(a)-2g_+(c-a)-2g_+(x_0)+2\pi ia(c-a).
\end{split}
 \tag{22}
\]
Its derivative in \(t\) has zero real chirp contribution. Put
\(r_h=e^{2\pi h}\), \(R_h=e^{2\pi(h+\upsilon)}\).
For \(t>c_r/2\), the squared-modulus differences in its numerator
and denominator ratios are, respectively,
\[
\begin{split}
 &4R_h\sin\pi(c_r+2\xi)\sin\pi(2t-c_r)<0,\\
 &4r_h\sin\pi c_r\sin\pi(2t-c_r)>0.
\end{split}
 \tag{23}
\]
On compact subsets of (20) these signs hold on the entire actual
half-grid interval to the right of the center, for sufficiently
large \(N\): \(c_r+2\xi\in(1,2)\) and
\(0<2t-c_r<1\). The reversed signs hold on its left half.
Thus the real phase is strictly increasing up to \(a=c/2\)
and strictly decreasing afterward, including the zero-extended
reciprocal portions. This proof uses the common radii, not global
concavity on the full interval.

The exact derivative vanishes at \(a=c/2\) by symmetry. Its
second derivative there is
\[
 F_c''(c/2)=2\pi\{\cot\pi(c/2+x_0)-2\cot(\pi c/2)-i\},
 \qquad \Re F_c''(c/2)<0.
 \tag{24}
\]
Indeed \(1/3<\Re(c/2)<2/5\), while
\(1/2<\Re(c/2+x_0)<1\). The whole principal current therefore
has a nonzero uniform Gaussian on compact subsets of (20):
\[
 N\int_{\alpha_N+ih}^{\beta_N+ih}T_N(a;c,x_0,x_0)\,da
  =N^{-1}\frac{\sqrt{2\pi}\,b_c(c/2)}
                     {\sqrt{-F_c''(c/2)}}
       e^{NF_c(c/2)}(1+O(N^{-1})).
 \tag{25}
\]
Here the original nonzero symbol is
\[
 b_c(a)=
 \frac{\mathfrak a(c)\mathfrak a(a+x_0)\mathfrak a(c-a+x_0)}
 {\mathfrak a(a)^2\mathfrak a(c-a)^2\mathfrak a(x_0)^2},
\]
with the continued upper-half-plane branches. The row contributes
\(N^{-3/2}\), the lattice density \(N\), and the inner Gaussian
\(N^{-1/2}\). Local odd corrections cancel; the complement has a
strict phase gap by (23). This proves the stated power and error.
At \(c=c_*\), its action is exactly the regular merged-pair action
before the outside \(\pi i(x+y)\) term.

The finite interpolant (5) is holomorphic throughout the explicit
tube, and (10) holds there with both endpoint currents. Equation
(25) estimates only its principal current. A complete complex
inner-source packet requires comparing both profiles (15), (18)
and their entire tails to \(\Re F_c(c/2)\), or proving a coherent
cancellation before taking their moduli. The exact physical-node
identity alone does not supply that comparison. The complementary
physical total indices and the original outer sampling/closing
operation remain unchanged.
