# Root evaluations of the frozen compatibility and the outgoing action

Private exact-source deduction, 9 November 2026. The frozen
codimension-one compatibility is a divided difference of the Fourier
generating polynomial. Repeated characteristic roots require ordinary
derivatives, not a distinct-root approximation. For the complete
outgoing source, the artificial constant Fourier weight cancels
exactly against the radial rescaling of these roots.

The resulting action bound has no exponential cost near the first
crossing. A block starting at a positive macroscopic frequency has
a corresponding proved action saving. The full block still has the
ceiling \(E_Z(0)\); no saving below that ceiling or actual cancellation
budget is established. Boundary corrections and the orientation of
the frozen half-line remain explicit. No mathematical numerical
evaluation or frozen-source edit is used.

## 1. The exact functional, including repeated roots

Fix a shifted full symbol in the first-crossing chamber of
[the oriented range theorem](research_mixed_next_outer_oriented_factor_range_conditions.md).
Thus, for a fixed frequency \(\tau<1/2\) sufficiently close to \(1/2\),
\[
 P_\lambda(z)=p(e^\lambda z,\tau),\qquad
 h_1(\tau)<\lambda<h_2(\tau),
 \tag{1}
\]
has winding one and no unit-circle zero. Its canonical factorization
is
\[
 P_\lambda(z)=d\,p_-(z)\,z\,p_+(z),\qquad
 p_-(z)=\prod_{j=1}^{m}(1-\rho_j/z),\qquad m=12.
 \tag{2}
\]
The roots \(\rho_j\) are all the inside roots, repeated with
multiplicity. They are nonzero and have modulus less than one.
The pole order of the full symbol is eleven, so its winding-one
inside count is twelve. The analogous statement for the crossed
degree-eleven factor has \(m=6\).

Keep the source's Toeplitz convention
\((T(b)f)_n=\sum_{k\ge0}b_{n-k}f_k\). For a finite sequence
\(f=(f_0,\ldots,f_K,0,\ldots)\), define its generating polynomial
\[
 \mathcal F(z)=\sum_{n=0}^{K}f_nz^n,\qquad
 H_\rho(s)=\prod_{j=1}^{m}(1-\rho_js)^{-1}
              =\sum_{n\ge0}\mathfrak h_n(\rho)s^n.
 \tag{3}
\]
Then the exact compatibility of the full frozen model is
\[
 \ell_\rho(f):=[T(p_-^{-1})f]_0
       =\sum_{n=0}^{K}\mathfrak h_n(\rho)f_n.
 \tag{4}
\]
Indeed \(p_-^{-1}(z)=\sum_{n\ge0}\mathfrak h_n(\rho)z^{-n}\);
the zeroth Toeplitz row is precisely (4).

Let \(Q_\rho(z)=\prod_{j=1}^{m}(z-\rho_j)\). A positively oriented
contour enclosing all these roots gives the equivalent exact formula
\[
 \boxed{\quad
 \ell_\rho(f)=\frac{1}{2\pi i}
       \oint\frac{z^{m-1}\mathcal F(z)}{Q_\rho(z)}\,dz .
 \quad}
 \tag{5}
\]
One may initially take a circle of radius greater than
\(\max|\rho_j|\). Expand
\(z^{m-1}/Q_\rho(z)=z^{-1}\sum_{n\ge0}\mathfrak h_n(\rho)z^{-n}\)
and integrate term by term; the finite polynomial \(\mathcal F\)
proves (5). Contour deformation then gives any enclosing contour.

If the roots are distinct, (5) is the explicit evaluation formula
\[
 \ell_\rho(f)=
  \sum_{j=1}^{m}
       \frac{\rho_j^{\,m-1}\mathcal F(\rho_j)}
                       {\prod_{k\ne j}(\rho_j-\rho_k)}.
 \tag{6}
\]
For distinct root values \(\xi_a\) of multiplicities \(m_a\),
put \(Q_a(z)=\prod_{b\ne a}(z-\xi_b)^{m_b}\).
The exact repeated-root version is
\[
 \boxed{\quad
 \ell_\rho(f)=
 \sum_a\frac1{(m_a-1)!}
  \left[
   \frac{d^{m_a-1}}{dz^{m_a-1}}
       \left\{\frac{z^{m-1}\mathcal F(z)}{Q_a(z)}\right\}
  \right]_{z=\xi_a}.
 \quad}
 \tag{7}
\]
This is the Hermite divided difference of
\(z^{m-1}\mathcal F(z)\) at the full root multiset. Formulas
(4)--(5), unlike separated terms in (6), remain uniformly
meaningful when roots coalesce.

Equivalently, the partial fraction decomposition
\[
 H_\rho(s)=\sum_a\sum_{\ell=1}^{m_a}
                 \frac{A_{a,\ell}}{(1-\xi_as)^\ell}
 \tag{8}
\]
gives
\[
 \ell_\rho(f)=
 \sum_a\sum_{\ell=1}^{m_a}
   \frac{A_{a,\ell}}{(\ell-1)!}
   \left[
    \frac{d^{\ell-1}}{dz^{\ell-1}}
                  \{z^{\ell-1}\mathcal F(z)\}
   \right]_{z=\xi_a}.
 \tag{9}
\]
The binomial series for each denominator proves (9).
There is no polynomial part in (8), since its numerator is
constant and its denominator has positive degree.

## 2. Radial scaling cancels the constant source weight

Let \(\sigma_1,\ldots,\sigma_m\) be the corresponding roots of
the unshifted symbol \(p(z,\tau)\). In the chamber (1) this is
one fixed multiset: all eleven original inside roots and the
single newly crossed outer root. Then
\[
 \rho_j=e^{-\lambda}\sigma_j,\qquad
 \mathfrak h_n(\rho)=e^{-\lambda n}\mathfrak h_n(\sigma).
 \tag{10}
\]
Consequently, for every finite sequence \(g\),
\[
 \boxed{\quad
 \ell_\rho((e^{\lambda n}g_n)_n)
          =\sum_n\mathfrak h_n(\sigma)g_n .
 \quad}
 \tag{11}
\]
The right side is independent of \(\lambda\) throughout that
crossing chamber. In the evaluation formulas it is obtained by
replacing \(\rho\) by \(\sigma\) and using the unweighted
generating polynomial. No singularity of that polynomial is
crossed, since it is entire.

There is a root-separation-free bound for this expression.
For any multiset with \(\max_j|\sigma_j|\le R\), its complete
homogeneous coefficients satisfy
\[
 |\mathfrak h_n(\sigma)|
       \le {n+m-1\choose m-1}R^n.
 \tag{12}
\]
To prove it, expand the product of the \(m\) geometric series
in (3). There are \({n+m-1\choose m-1}\) monomials of total
degree \(n\), each of modulus at most \(R^n\).
The same proof includes repeated roots.

In the first-crossing chamber, specifically,
\[
                 \max_j|\sigma_j|=e^{h_1(\tau)}.
 \tag{13}
\]
All eleven original inside roots have smaller modulus than one.
Thus the newly crossed root determines (13), even though
every root remains in the exact sum (11).

## 3. Substitute the complete outgoing polynomial

Use the literal attached source from
[the action-weighted Green theorem, Section 4](research_mixed_next_outgoing_action_weighted_green_ellipse.md):
\[
 F_N^+(X,Z)=\sum_{b=M}^{D}(-q)^b C_{b,N}(Z)P_b^{\rm rad}(X),
 \qquad D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M.
 \tag{14}
\]
All complete rows through \(b=D\), their phases and the original
radical quotients are retained. The
[finite span theorem, Section 5](research_mixed_next_outer_oriented_factor_range_conditions.md)
records their exact root-of-unity stops and denominators.

Write its exact Chebyshev expansion as
\[
 F_N^+(X,Z)=\sum_{k=0}^{U}\widehat F_{k,N}(Z)T_k(X/2).
 \tag{15}
\]
For the original angular convention \(X=-2\cos u\), define
the positive Fourier coefficients
\[
 d_{0,N}=\widehat F_{0,N},\qquad
 d_{k,N}=\tfrac12(-1)^k\widehat F_{k,N}\quad(k\ge1).
 \tag{16}
\]
Then
\[
 F_N^+(-2\cos u,Z)
      =d_{0,N}+\sum_{k=1}^{U}d_{k,N}(e^{iku}+e^{-iku}).
 \tag{17}
\]
This fixes both the sign and the factor two before a one-sided
generating polynomial is formed. An orthonormal cosine convention
is related by the fixed diagonal normalization; it is not
silently substituted for (16).

The adopted actual source bound is
\[
 |d_{k,N}(Z)|\le CN^A e^{NE_Z(k/N)},\qquad
 E_Z(s)=\mathcal E(1/2+s,Z),\qquad0\le k\le U.
 \tag{18}
\]
It is uniform on the stated actual output family and at both
parities. The [sharper outgoing theorem, Section 2](research_mixed_next_outgoing_sharper_tail_and_ellipse.md)
proves the original action loss
\[
 E_Z(s)\le E_Z(0)-c_0s,\qquad
 c_0=\frac{205}{1134},\qquad0\le s\le1/2.
 \tag{19}
\]
Neither statement is a coefficientwise relative asymptotic.

Fix integers \(0\le L\le K\le U\), and form the actual forward
coefficient block
\[
 \mathcal G_{L,K,N}(z,Z)=
               \sum_{j=0}^{K-L}d_{L+j,N}(Z)z^j.
 \tag{20}
\]
In the frozen half-line functional apply the constant weight to
this block, \(f_j=e^{\lambda j}d_{L+j,N}(Z)\).
Equations (5)--(11) give its exact bad-component value
\[
 \begin{split}
 \mathfrak D_{L,K,N}(\tau,Z)
  &:=\ell_\rho(f)
    =\sum_{j=0}^{K-L}\mathfrak h_j(\sigma)d_{L+j,N}(Z)\\
  &=\frac1{2\pi i}\oint
       \frac{z^{m-1}\mathcal G_{L,K,N}(z,Z)}
                         {\prod_{j=1}^{m}(z-\sigma_j)}\,dz .
 \end{split}
 \tag{21}
\]
The derivative formulas (6)--(9) apply to this complete
generating polynomial. Equation (21) is the direct full-symbol
functional; it does not first discard one oriented factor.

Put \(\beta_N=L/N\), \(\alpha_N=K/N\), and
\(\kappa_\tau=h_1(\tau)\). The exact action ceiling is
\[
 \boxed{\quad
 |\mathfrak D_{L,K,N}|
 \le CN^{A'}
 \exp\!\left[
 N\max_{\beta_N\le s\le\alpha_N}
        \{E_Z(s)+\kappa_\tau(s-\beta_N)\}\right].
 \quad}
 \tag{22}
\]
Indeed (12), (13), and (18) bound every term of (21);
there are at most \(N\) terms, and \(m=12\) is fixed.
The estimate is uniform through coalescence of roots, since
no inverse root separation appears in its proof.

The endpoint root theorem gives
\(\kappa_\tau=(4\pi/37)(1/2-\tau)+O((1/2-\tau)^3)\).
Hence on a fixed, possibly smaller left neighborhood of
\(\tau=1/2\), one has \(\kappa_\tau<c_0\).
In that neighborhood, (19) reduces (22) to
\[
 \boxed{\quad
 |\mathfrak D_{L,K,N}|
       \le CN^{A'}e^{N\{E_Z(0)-c_0\beta_N\}} .
 \quad}
 \tag{23}
\]
This is an actual action saving for a block whose first index
is at least a fixed positive multiple of \(N\). For the full
block \(L=0\), (22) has maximum exactly \(E_Z(0)\):
the endpoint \(s=0\) attains that value and (19) bounds the
other candidates above by it. This says the present absolute
source ceiling supplies no further saving; it is not a lower
bound for \(\mathfrak D_{0,K,N}\).

## 4. Variable weights, orientation and boundary corrections

For a proposed variable Fourier weight \(W\), the same
substitution is exact, but (11) does not remove its nonlinear
variation. If
\[
 f_j=e^{N\{W((L+j)/N)-W(L/N)\}}d_{L+j,N},
 \tag{24}
\]
the rate in (22) is replaced by
\[
 \max_{\beta_N\le s\le\alpha_N}
 \left\{
 E_Z(s)+W(s)-W(\beta_N)
             +(\kappa_\tau-\lambda)(s-\beta_N)
 \right\}.
 \tag{25}
\]
This follows directly from (10),(12), without replacing the
actual weight by its tangent on a block of length comparable
with \(N\). The linear choice \(W(s)=\lambda s\) recovers
(22). On a smaller coefficient window one may use its actual
finite polynomial in (5); no frequency orientation has to be
guessed.

In particular, at the actual positive hard Fourier endpoint
\(k=K\), inward indexing \(j=K-k\) reverses the frozen
Laurent symbol. The winding-one forward symbol of Section 1
then becomes the reverse half-line symbol, whose defect is
a one-dimensional kernel rather than a range condition.
Applying (21) to a chosen forward block does not identify it
as an already-established condition of that reversed finite
boundary. The original even reflection and the other boundary
must still be assembled by an exact operator argument.

The factor route also retains its literal boundary correction.
With \(A,B,K\) from the
[range theorem, (18)--(21)](research_mixed_next_outer_oriented_factor_range_conditions.md),
\[
 T(P_\lambda)=T(A)T(B)+K,\qquad
 K_{n,k}=0\ (n>4\text{ or }k>4),\qquad K_{4,4}=1.
 \tag{26}
\]
Let \(\ell_B\) be the inside-root functional of the crossed
factor \(B\). The equation \(T(P_\lambda)v=f\) requires
\[
 \boxed{\quad
 \ell_B(T(A)^{-1}f)
      =\sum_{k=0}^{4}v_k\,\ell_B(T(A)^{-1}Ke_k).
 \quad}
 \tag{27}
\]
Both sides are exact. The generating functions of
\(T(A)^{-1}f\) and \(T(A)^{-1}Ke_k\) are holomorphic in
the unit disk, since these sequences are in \(\ell^2\).
Choose a contour of radius strictly between the inside-root
radius of \(B\) and one. Equations (5)--(9) then give their
evaluation/derivative formulas as well. The needed Taylor
series converge uniformly on that contour.
No term on the right of (27) has been set to zero, and
(22) does not purport to estimate this preprocessed functional
by simply dropping \(T(A)^{-1}\) or \(K\).

The complete source still obeys the original full Hermite
forcing identity and retains its eleven generated output
modes in a finite compression. The formulas here neither
replace that identity by a frozen compatibility nor prove
a factorization of the finite grouped operator. They supply
an exact form and an original-action ceiling for a proposed
bad component. A sufficient global budget, or control of
the correlated finite boundary responses after such a
projection, remains to be proved.

## Frozen source versions

- Full-symbol and oriented-factor half-line ranges, boundary defect,
  and literal outgoing span:
  6f6a411d7788f2727e3261195bb2a8e46871c631d6f86fab5b2cbb26ed2507a5.
- Original complete attached source and action coefficient bound:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Original sharper outgoing action loss:
  fab5571d039f9fa4e36c0b6ca981f4ebbd2e7384923249882cf22e58eccc8ba3.
- Exact endpoint roots and first simple crossing:
  aa0a17aec890cfe3951feaafd14a0c35b0d809a348181009e497cdc02dcdee90.
