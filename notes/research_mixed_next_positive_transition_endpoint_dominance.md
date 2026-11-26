# Endpoint dominance for the complete attached coefficient envelope

Private written source theorem, 9 November 2026. The maximum of the
positive-transition outgoing envelope plus the selected outer action
occurs at zero cosine frequency. A previously paid physical half-input
row fixes that endpoint strictly below the original geometric rate.
The resulting estimate concerns the complete original attachment.

The separate physical-half-input action-anchor theorem and the whole
finite outer-mode asymptotic have completed their source/proof reviews.
No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original finite source and rates

Retain the full source of
[positive transition, (1), (14), (25)--(29)](research_mixed_next_outgoing_positive_chebyshev_transition.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
q=e^{i\pi/N},\quad r=q^{-2},\quad \kappa_N=q^{D^2/2},\\
C_{b,N}(Z)=\sum_{\ell=0}^{D-b}
 \frac{r^{-b\ell}(r^{b+1};r)_\ell(rZ;r)_\ell}{(r;r)_\ell^2},
\qquad C_{D,N}=1,\\
P_b^{\rm rad}(X)=e_b(X)/e_M(X),\\
F_N^+(X,Z)=\sum_{b=M}^{D}(-q)^bC_{b,N}(Z)P_b^{\rm rad}(X)
         =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2),\\
f_{k,N}(Z)=(-1)^{M+k}
       \sum_{d=k}^{U}q^{M+d}\beta_{d,k,N}C_{M+d,N}(Z),
\qquad \beta_{d,k,N}>0 .
\end{gathered}                                                    \tag{1}
\]
The quotient is an ordinary polynomial. No outgoing row, phase,
literal stopping factor, or top-degree term is removed.

Let \(Z_*\) be the original outgoing value of an actual complete
word in powers three and four beginning \(343\), of length at
least five. Keep
\[
\begin{gathered}
\mathcal E(a,Z_*)=-\int_a^1\log|\mathcal L(v,Z_*)|\,dv,\qquad
E_0=\mathcal E(1/2,Z_*),\\
J(v)=\int_0^v\log(2\sin\pi s)\,ds,\qquad J(0)=J(1/2)=J(1)=0,\\
\mathcal H(x,t)=J(2x)-J(x-t)-J(x+t)-2J(1/2+x),\\
\mathcal D(t,Z_*)=\max_{t\le x\le1/2}
 \{\mathcal E(1/2+x,Z_*)+\mathcal H(x,t)\},\qquad0\le t\le1/2 .
\end{gathered}                                                    \tag{2}
\]
The action has its original terminal normalization
\(\mathcal E(1,Z_*)=0\). The complete transition theorem proves
\[
|f_{k,N}(Z_*)|\le CN^A e^{N\mathcal D(k/N,Z_*)},\qquad0\le k\le U
                                                                  \tag{3}
\]
at both parities, including every endpoint and half-index shift.

For the original selected charged action write
\[
\Gamma(\delta)=\Re\{S(u_\delta)+3iu_\delta^2/(4\pi)-i\delta u_\delta\},
\quad u_\delta=\beta_\delta-iK_\delta,\quad M_3=\Gamma(0).
\]
The [far-node theorem, Lemma 1](research_mixed_next_outer_far_nodes_and_paired_contour.md)
and the adopted depth bound give
\[
\Gamma'(\delta)=-K_\delta,\qquad
0<K_\delta<\min\{2/5,\pi\delta/3\}\quad(0<\delta\le1/2).          \tag{4}
\]
These are the original phases; no coefficient phase is substituted
for the finite sum in (1).

**Theorem 1.** Uniformly on the actual reference family,
\[
\boxed{\quad
\max_{0\le t\le1/2}\{\mathcal D(t,Z_*)+\Gamma(1/2-t)\}
                       =E_0+\Gamma(1/2).
\quad}                                                         \tag{5}
\]
The inequality toward the right is strict at every \(t>0\).
Equality at zero uses \(\mathcal D(0,Z_*)=E_0\).

## 2. A stronger middle action chord

The original
[sharper-tail comparison, (12),(15)](research_mixed_next_outgoing_sharper_tail_and_ellipse.md)
gives
\[
E_0-\mathcal E(1/2+x,Z_*)\ge\tfrac12J(1/2+x)+\gamma_0x,\quad
0\le x\le1/3,\qquad \gamma_0=\log(126/125)>1/126.                \tag{6}
\]
For \(0<z<\pi/2\),
\[
                         \cot z\le z^{-1}-z/3.                 \tag{7}
\]
Indeed \(F(z)=(3-z^2)\sin z-3z\cos z\) has
\(F'(z)=z(\sin z-z\cos z)>0\): the expression in parentheses
vanishes at zero and has derivative \(z\sin z>0\).
Division by \(3z\sin z\) proves (7). Integration yields
\(\log(\sin z/z)\le-z^2/6\). Thus
\[
J(5/6)=-J(1/6)\ge
       \frac16\{1-\log(\pi/3)\}+\frac{\pi^2}{3888}.              \tag{8}
\]
Use \(25/8<\pi<22/7\), as in the original complete-action estimates.
The exact integral expansion of \(\log(1+x)\) gives
\[
\log(\pi/3)<\log(22/21)
 <1/21-1/882+1/27783.
\]
Consequently
\[
\begin{split}
J(5/6)
&>\frac{10}{63}+\frac1{5292}-\frac1{166698}
                  +\frac{625}{248832}\\
&>\frac{10}{63}+\frac1{6000}+\frac1{400}
 =\frac{10}{63}+\frac1{375}>\frac{61}{378}. 
\end{split}                                                     \tag{9}
\]
Here \(166698>30\cdot5292=158760\), so the difference of
the two unit fractions exceeds \(29/158760>1/6000\),
using \(174000>158760\). Also \(250000>248832\) gives
the \(1/400\) comparison, and
\(61/378-10/63=1/378<1/375\).

The integrand of \(J\) decreases on \([1/2,5/6]\).
Its averages therefore give \(J(1/2+x)\ge3xJ(5/6)\)
for \(0\le x\le1/3\). Equations (6),(9) prove
\[
\boxed{\quad
\mathcal A(x):=E_0-\mathcal E(1/2+x,Z_*)>x/4,
\qquad0<x\le1/3 .
\quad}                                                         \tag{10}
\]
The constant is exact:
\((3/2)(61/378)+1/126=1/4\).
No pointwise derivative bound \(1/4\) is asserted.

## 3. A terminal gain from the actual half-line inverse

Retain the principal half-line source of the
[absolute anchor](research_mixed_next_outgoing_absolute_anchor.md)
and [terminal normalization, (12)--(16)](research_mixed_next_outgoing_action_terminal_normalization.md).
For \(5/6\le a\le1\), put
\[
\vartheta=(\pi a-\pi/2)/2,\quad \sigma=2\sin\pi a,\quad
\tau=\sigma^{3/2},\quad
V=3e^{i\vartheta}+2e^{-3i\vartheta}+Z_*e^{5i\vartheta}.
\]
On \(\ell^2(\mathbb Z_{\ge0})\) the frozen operator is
\[
\mathsf H_0=VI+\tau(e^{i\vartheta}S+e^{-i\vartheta}S^*),
\qquad m(a,Z_*)=(\mathsf H_0^{-1})_{00},
\]
where \(S\) is the unilateral shift. Its off-diagonal part is
self-adjoint of norm at most \(2\tau\). The
[full-tail energy, (13)](research_mixed_next_outgoing_full_tail_weighted_energy.md)
gives
\[
\Re V+\Im V-2\tau>8/25.
\]
It follows that
\[
\Re\langle v,(1-i)\mathsf H_0v\rangle\ge(8/25)\|v\|^2,\qquad
\|\mathsf H_0^{-1}\|\le25\sqrt2/8.                              \tag{11}
\]
The inverse already exists by the adopted half-line theorem;
the bound follows directly from the first inequality. It includes
\(a=1\), where \(\tau=0\).

The exact characteristic normalization is
\(|\mathcal L|=\sigma|m|\). Together with the adopted tail
circle, (11) proves
\[
|\mathcal L(a,Z_*)|<
       \min\{4/5,\;32(1-a)\},\qquad5/6\le a<1.                 \tag{12}
\]
For the second inequality use \(\sin\pi a\le\pi(1-a)\) and
\[
25\sqrt2\pi/4<1375/49<32,
\]
which follow from \(\sqrt2<10/7\), \(\pi<22/7\), and
\(1375<1568\). This is an estimate of the already identified
principal ratio, not a new finite contour continuation.

Set \(\epsilon=1/40\), \(e=1/2-x\), and
\[
\mathcal G(e)=
\begin{cases}
\epsilon-e-e\log(\epsilon/e),&0<e\le\epsilon,\\
\epsilon,&e=0,\\
0,&e\ge\epsilon .
\end{cases}                                                     \tag{13}
\]
This function is nonnegative and continuous. Since
\(\log(5/4)>2/9\), (12) gives
\[
-\log|\mathcal L(a,Z_*)|\ge
       \frac29+\max\{0,\log[1/(40(1-a))]\}.
\]
Integrating from \(a=5/6\), and using (10) at \(x=1/3\),
proves
\[
\boxed{\quad
\mathcal A(x)>
 \frac{13}{108}-\frac29e+\mathcal G(e),
\qquad e=1/2-x,\quad1/3\le x\le1/2 .
\quad}                                                         \tag{14}
\]
The extra integral is exactly (13), including its integrable
logarithmic endpoint. All terms retain the same original action.

## 4. Transition entropy pays the full outer-action increase

The exact entropy in (2) satisfies
\[
-\mathcal H(x,t)\ge\pi t^2\cot\pi x
              \ge t^2/x-2t^2,\qquad
-\mathcal H(x,t)\ge\pi^2t^2(1/2-x).                             \tag{15}
\]
These follow by integrating twice
\[
\mathcal H_{tt}(x,t)=
-\frac{2\pi\cot\pi x}{1-\sin^2\pi t/\sin^2\pi x},
\qquad \mathcal H(x,0)=\mathcal H_t(x,0)=0,
\]
using respectively
\(\cot\pi x\ge(1-2x)/(\pi x)\) and
\(\cot\pi x\ge\pi(1/2-x)\).
Continuity supplies \(t=x\) and \(x=1/2\); the point
\(t=x=0\) has its exact zero value.

The other exact derivative is
\[
\mathcal H_x(x,t)=
 \log\frac{\sin^2\pi x}{\sin^2\pi x-\sin^2\pi t}
 \ge-2\log\cos\pi t.
\]
Integration to \(\mathcal H(1/2,t)=0\) gives
\[
-\mathcal H(x,t)\ge[-2\log\cos\pi t](1/2-x),\qquad t<1/2.        \tag{16}
\]
When \(t\ge1/4\), the bracket is at least
\(\log2>56/81\), by the original positive logarithm-series
witness. The point \(t=x=1/2\) is handled directly below.

We claim, for all \(t\le x\le1/2\),
\[
\mathcal A(x)-\mathcal H(x,t)>
\begin{cases}
(2/5)t,&0<t\le1/4,\\
1/8,&1/4\le t\le1/2.
\end{cases}                                                     \tag{17}
\]
For \(x\le1/3\) and \(t\le1/4\), (10),(15) give
\[
\mathcal A(x)-\mathcal H(x,t)>
 x/4+t^2/x-2t^2\ge t-2t^2\ge t/2>(2/5)t .
\]
For \(x\ge1/3\), \(t\le1/6\), monotonicity of \(\mathcal A\)
gives a bound \(1/12>1/15\ge(2/5)t\).
For \(x\ge1/3\), \(1/6\le t\le1/4\), use
\(\pi^2t^2\ge1/4\) in (14),(15):
\[
\mathcal A(x)-\mathcal H(x,t)>
 13/108+e/36+\mathcal G(e)\ge13/108>1/10\ge(2/5)t .
\]
This proves the first case of (17).

If \(t\ge1/4\), \(x\le1/3\), then
\(\pi^2t^2\ge9/16>1/4\), and (10),(15) give a bound
\(x/4+(1/4)(1/2-x)=1/8\).
For \(t\ge1/4\), \(x\ge1/3\), equations (14),(16) give
\[
\mathcal A(x)-\mathcal H(x,t)>
           13/108+(38/81)e+\mathcal G(e).                       \tag{18}
\]
Put \(q_0=38/81\). On \(0\le e\le\epsilon\), differentiation
shows that the minimum of \(q_0e+\mathcal G(e)\) is
\(\epsilon(1-e^{-q_0})\). On \(e\ge\epsilon\) the value
is at least \(q_0\epsilon\). Since \(e^{q_0}\ge1+q_0\),
both intervals give
\[
q_0e+\mathcal G(e)\ge
 \epsilon\frac{q_0}{1+q_0}=\frac{19}{2380}>\frac1{216},
\]
where the last comparison is \(4104>2380\).
Thus (18) exceeds \(13/108+1/216=1/8\).
At \(t=x=1/2\), the same estimate follows directly from
(14), since \(\mathcal H(1/2,1/2)=0\).
This proves all of (17).

Meanwhile, (4) implies
\[
\Gamma(1/2-t)-\Gamma(1/2)
  =\int_{1/2-t}^{1/2}K_s\,ds<(2/5)t\qquad(t>0),                \tag{19}
\]
and
\[
\int_0^{1/2}K_s\,ds
 <\int_0^{1/2}\min\{2/5,\pi s/3\}\,ds
 =\frac15-\frac6{25\pi}<\frac{34}{275}<\frac18.                 \tag{20}
\]
The break point is \(6/(5\pi)<1/2\). The penultimate
inequality uses \(\pi<22/7\); the last is \(272<275\).
Combining (17)--(20), for every \(t>0\) and \(x\ge t\),
\[
\mathcal E(1/2+x,Z_*)+\mathcal H(x,t)+\Gamma(1/2-t)
                       <E_0+\Gamma(1/2).
\]
Compact attainment in (2), and the exact value at \(t=0\),
prove Theorem 1.

## 5. The actual endpoint and complete finite attachment

The separate
[physical-half-input action-anchor theorem](research_mixed_next_physical_half_input_action_anchor.md)
proves
\[
E_0+\Gamma(1/2)\le\Lambda-g_0,\qquad
                         g_0=\frac1{2\cdot10^{13}}.            \tag{21}
\]
It retains the unfiltered physical row \(b=M\), the exact
identity \(\ell_M(-2)=\mathcal O_{N,0}\), the nonzero full
constant-mode asymptotic, the complete two-sided outgoing anchor,
both parity endpoints, and the original scalar
\(1/(\kappa_N^2N)\).

Thus (5),(21) give
\[
\sup_{0\le t\le1/2}\{\mathcal D(t,Z_*)+\Gamma(1/2-t)\}
                                      \le\Lambda-g_0.          \tag{22}
\]
This does not require the stronger sufficient excess comparison
\(M_3+E_0-\Lambda<5\pi/226\) from the earlier combined-envelope
note.

Retain the exact whole observation
\[
\mathcal O_{N,k}=\mathcal L_N(T_k(-X/2)),\qquad
\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F].
\]
The adopted
[whole outer asymptotic](research_mixed_next_whole_outer_fourier_asymptotic.md)
gives
\[
|\mathcal O_{N,k}|\le CN^A e^{N\Gamma(1/2-k/N)}
       \qquad0\le k<\lceil15N/32\rceil,                        \tag{23}
\]
by taking its fixed \(\delta_1=1/32\). Every such integer has
\(k/N<15/32\), hence \(\delta>1/32\).
The bound includes \(k=0\), with its exact reflected factor two.
Equations (3),(22),(23), summed over at most \(N\) terms, imply
\[
\sum_{0\le k<\lceil15N/32\rceil}
 |f_{k,N}(Z_*)\mathcal O_{N,k}|
                   \le CN^A e^{N(\Lambda-g_0)}.                \tag{24}
\]
The complementary modes through the literal top degree \(U\)
are already paid by
[terminal-mode payment, (29)--(30)](research_mixed_next_combined_action_terminal_mode_payment.md):
\[
\sum_{\lceil15N/32\rceil\le k\le U}
 |f_{k,N}(Z_*)\mathcal O_{N,k}|
                 \le CN^A e^{N(\Lambda-1/500)}.                \tag{25}
\]
Index ranges are also restricted to \(0\le k\le U\), and empty
ranges contribute zero. Consequently
\[
\boxed{\quad
\left|\frac1{\kappa_N^2N}\mathcal L_N(F_N^+(\,\cdot\,,Z_*))\right|
 \le C\exp\!\left\{N\left(\Lambda-\frac1{4\cdot10^{13}}\right)\right\}
\quad}                                                         \tag{26}
\]
for all sufficiently large \(N\), uniformly on the actual reference
family at both parities. The polynomial factors in (24),(25)
are absorbed into \(g_0/2\), and \(|\kappa_N|=1\).
The proof in fact bounds the sum of the absolute values of
these complete Fourier-mode contributions.

No normal derivative or odd simple-node value is deleted from
\(Q_N^{\rm full}\). The positive transition weights are used
only in their eligible modulus ceiling; no complex outgoing
phase is replaced. Equation (26) concerns this exact reference
attachment. The separate full-transfer assembly and boundary
extension are still required before asserting a new knot theorem
or stability under arbitrary fixed short fillings.

## Source bindings

- Exact positive transition and coefficient envelope:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Complete outgoing middle inequalities and tail circle:
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Actual half-line root and terminal action normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Full-tail rotated energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Complete outgoing absolute anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Selected depth/action upper comparisons:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.
- Original complete-action rational conventions:
  7ef8adaa33c1fed792379d4ead3aef70cb4e704816b6979fb1f156fe16b07a9d.
- Physical-half-input action anchor:
  3ba93da54e86226990fe844cd245b8a973650ca84c0ca0088e9cdc579594d967.
- Whole finite outer Fourier asymptotic:
  8c0f4853c05443eb76d821bca6d7248f6c00e19177a796e530e4b4cd24d93ac6.
- Complete finite terminal-mode payment:
  7a0a060b8313d250d7b0e49d181f5242f4a47b0a3d56d19d542f60497f323587.

