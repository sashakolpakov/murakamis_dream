# Exact unit-turn identities for a full microscopic endpoint kernel

Private written calculation, 16 November 2026.

The original unit-leaf coupon map has an exact all-degree formula.
For a full endpoint kernel it is a finite root-of-unity hypergeometric
sum, equivalently a canonical multiplication in the endpoint variable.
Its complementary fixed-index limit has a beta-integral expression.
None of these identities supplies a uniform bound through growing
Newton indices. In particular this note does not permit turning a
marked leaf in the adopted full-product forest theorem.

## 1. Original operators and the full triangular formula

Use
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^D,\quad\kappa=q^{D^2/2},
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,\quad
 c_h=2\cos((2h+1)\pi/N),
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 e_j(Z)=S_j^{-2}\prod_{h<j}(c_h-Z),\qquad
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z).
 \tag{1}
\]
All operator equalities below are in the original full algebra
\(\mathcal A_N=\mathbb C[Z]/(P_N)\), with
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\) and \(Te_j=e_{D-j}\).
The ordinary representative of a class is its remainder of degree
at most \(D\), denoted \(\operatorname{can}\).

For \(\sigma=\pm1\), retain the original signed crossing and define
\[
              U_\sigma=\kappa^\sigma T R^{-\sigma}T.
 \tag{2}
\]
The original turn relation gives
\[
                    T(R^\sigma P)=R^{-\sigma}U_\sigma P.
 \tag{3}
\]
For every \(0\le k\le D\), multiplication preserves the terminal
Newton flag \(\operatorname{span}\{e_{D-k},\ldots,e_D\}\), because
\(Ze_j=c_je_j-s_{j+1}^2e_{j+1}\), with its last raised term zero
in the algebra. Thus \(U_\sigma\) preserves degree at most \(k\).
No radical or half-degree restriction is needed for this assertion.

The full multiplication matrix of \(R\) in the original basis is
\[
 M_{ij}=\kappa(-1)^i q^{i(j+1)}
                   \frac{S_i}{S_jS_{i-j}}\quad(i\ge j);
 \tag{4}
\]
the negative crossing has its coefficient-conjugate matrix.
Frobenius self-adjointness gives
\(J M^{-\sigma}J=(M^{-\sigma})^{\mathsf T}\), where \(J\)
reverses the basis. Consequently, for every degree at most \(D\),
\[
 [e_r]U_\sigma\left(\sum_{s=0}^D p_s e_s\right)
 =\sum_{s=r}^D p_s(-1)^s q^{-\sigma s(r+1)}
                              \frac{S_s}{S_rS_{s-r}}.
 \tag{5}
\]
All factorial indices are below \(N\); no singular specialization
has been used. This is the same triangular identity as in the
low-degree leaf source, now applied to its full valid matrix range.

For the full endpoint kernel put
\[
 U_\sigma K_N(w,Z)=\sum_{r=0}^D a_{r,N}^{\sigma}(w)e_r(Z).
 \]
Then exactly
\[
 \boxed{\quad
 a_{r,N}^{\sigma}(w)=
  \sum_{s=r}^{D}(-1)^s q^{-\sigma s(r+1)}
                  \frac{S_s}{S_rS_{s-r}}\,e_s(w).
 \quad}
 \tag{6}
\]
For real \(w\), the two signs are coefficient-conjugate.
The extreme coefficient satisfies
\[
                         a_{D,N}^{\sigma}(w)=e_D(w).
 \tag{7}
\]
Indeed the single term has multiplier
\((-1)^Dq^{-\sigma D(D+1)}=1\).
This does not control the intermediate coefficients.

## 2. Literal finite hypergeometric forms

For a scalar \(v\ne0\) write \(w=v+v^{-1}\) and use
\((z;Q)_s=\prod_{h=0}^{s-1}(1-zQ^h)\). Directly from (1),
\[
 e_s(w)=(-1)^s q^s
               \frac{(qv;Q)_s(q/v;Q)_s}{(Q;Q)_s^2}.
 \tag{8}
\]
The identity follows by multiplying
\((1-q^{2h+1}v)(1-q^{2h+1}/v)=q^{2h+1}(c_h-w)\)
and \(1-Q^h=-iq^h s_h\).

Set
\[
 A_r(v)=\frac{(qv;Q)_r(q/v;Q)_r}{(Q;Q)_r^2},\quad
 M=D-r,\quad a=qvQ^r,\quad b=qv^{-1}Q^r,\quad c=Q^{r+1}.
 \tag{9}
\]
Then (6) becomes the following exact finite sums:
\[
 \boxed{\begin{split}
 a_{r,N}^{+}(w)
  &=q^{-r^2}A_r(v)
       \sum_{\ell=0}^{M}
           \frac{(a;Q)_\ell(b;Q)_\ell}
                {(c;Q)_\ell(Q;Q)_\ell}\,Q^{-r\ell},\\
 a_{r,N}^{-}(w)
  &=q^{r^2+2r}A_r(v)
       \sum_{\ell=0}^{M}
           \frac{(a;Q)_\ell(b;Q)_\ell}
                {(c;Q)_\ell(Q;Q)_\ell}\,Q^\ell .
 \end{split}}
 \tag{10}
\]
To verify the phases, use
\[
 {s\brack r}_{Q}=q^{r(s-r)}\frac{S_s}{S_rS_{s-r}}
 \]
in (6), substitute (8), and set \(s=r+\ell\).
The positive-sign phase is \(q^{-r^2}Q^{-r\ell}\);
the negative-sign phase is \(q^{r^2+2r}Q^\ell\).
Splitting the finite Pochhammer products at \(r\) gives (10).

In the first sum \(c/(ab)=Q^{-r}\), but its upper limit is
literally \(M=N-1-r\). The factor \((c;Q)_\ell\) remains nonzero
through that limit and vanishes at the next index. Similarly
\((Q;Q)_\ell\) is nonzero throughout the displayed range.
There is no convergent infinite series here. In particular an
infinite \(q\)-Gauss identity cannot be substituted for (10).

## 3. An ordinary resolvent and the endpoint-side adapter

The Frobenius representative of ordinary degree-\(D\) evaluation is
\[
 \boxed{\quad
 \delta_w(Z):=(TK_N(w,\cdot))(Z)
       =\frac{P_N(Z)-P_N(w)}{\eta N^2(Z-w)}.
 \quad}
 \tag{11}
\]
The right side is an ordinary polynomial, including at \(Z=w\).
Indeed its leading coefficient is \(1/(\eta N^2)\), so its trace
is one. Multiplication by \(Z-w\) leaves the constant
\(-P_N(w)/(\eta N^2)\) modulo \(P_N\).
For any ordinary polynomial \(f\) of degree at most \(D\), write
\(f(Z)=f(w)+(Z-w)q(Z)\), with \(\deg q<D\). Since
\(\phi_N(q)=0\), this proves
\(\phi_N(\delta_w f)=f(w)\).
The same equality follows from the dual Newton expansion
\(\sum_s e_s(w)e_{D-s}(Z)\), proving (11).

Transposing the multiplication matrix in (4) also gives
\[
 \boxed{\quad
 a_{r,N}^{\sigma}(w)
     =\kappa^\sigma
              [\operatorname{can}(R^{-\sigma}e_r)](w),
 \qquad
 (U_\sigma^{(Z)}K_N)(w,Z)
     =\kappa^\sigma
              [\operatorname{can}_w(R(w)^{-\sigma}K_N(w,Z))].
 \quad}
 \tag{12}
\]
The right side is the specified ordinary polynomial obtained after
the indicated canonical multiplication, then evaluated at the
ordinary endpoint \(w\). It is not the unreduced product
\(\kappa^\sigma R(w)^{-\sigma}K_N(w,Z)\) off the physical spectrum.
Equation (12) is a derived adapter, not permission to quotient an
arbitrary original free boundary factor.

At a physical \(Z=c_j\), this reads
\[
 (U_\sigma K_N(w,\cdot))(c_j)
       =\kappa^\sigma
             [\operatorname{can}(R^{-\sigma}F_{j,N})](w),
 \qquad F_{j,N}(Z)=K_N(c_j,Z).
 \tag{13}
\]
Thus the remaining estimate is an actual oscillatory finite crossing
functional. Bounds for an arbitrary multiplication operator or for
each term of (6) do not estimate it with the needed polynomial cost.

## 4. A complementary fixed-index anchor

Now put \(w=w_N(\alpha)=2\cosh(\alpha/N)\), with real \(\alpha\)
in a fixed compact interval, and write
\[
 E_{i,N}(\alpha)=(-1)^i e_i(w_N(\alpha)),\qquad
 \mathsf E_m(\alpha)=
       \frac{(a_0)_m(b_0)_m}{(m!)^2},\quad
 a_0=\tfrac12+i\alpha/(2\pi),\quad b_0=\overline{a_0}.
 \tag{14}
\]
For a fixed nonnegative integer \(m\), set \(r=D-m\).
Sine reflection in (6) gives exactly, for either sign,
\[
 a_{D-m,N}^{\sigma}(w_N(\alpha))
   =\eta(-1)^m\sum_{\ell=0}^{m}
      (-1)^\ell q^{-\sigma m(\ell+1)}
         \frac{S_m}{S_\ell S_{m-\ell}}\,
                      E_{N-1-\ell,N}(\alpha).
 \tag{15}
\]
For the phase, write \(s=N-1-\ell\) in (6). Since
\((-1)^s e_s(w)=E_s\),
\[
 q^{-\sigma(N-1-\ell)(N-m)}
       =\eta(-1)^{m+\ell}q^{-\sigma m(\ell+1)}.
 \]
The factorial quotient is
\(S_m/(S_\ell S_{m-\ell})\).

The adopted two-ended endpoint calculation gives, for each fixed
\(\ell\),
\[
 E_{N-1-\ell,N}(\alpha)\longrightarrow
 \frac{\cosh^2(\alpha/2)}
      {\pi^2(\ell+1)^2\mathsf E_{\ell+1}(\alpha)}.
 \tag{16}
\]
Its complementary identity retains the entire upper Newton end;
no low-index approximation is used in (16).
As \(N\to\infty\), the finite sum (15) therefore gives
\[
 \boxed{\quad
 \eta(-1)^m a_{D-m,N}^{\sigma}(w_N(\alpha))
   \longrightarrow
 \frac{\cosh^2(\alpha/2)}{\pi^2}
 \int_0^1\!\!\int_0^1
       (1-tu)^m(1-t)^{a_0-1}(1-u)^{b_0-1}\,dt\,du .
 \quad}
 \tag{17}
\]
The convergence is uniform on compact real parameter intervals.
To verify the integral, the beta identity gives exactly
\[
 \frac1{(\ell+1)^2\mathsf E_{\ell+1}(\alpha)}
 =\int_0^1\!\!\int_0^1
             (tu)^\ell(1-t)^{a_0-1}(1-u)^{b_0-1}\,dt\,du .
 \tag{18}
\]
Indeed its two beta factors are
\(\Gamma(\ell+1)\Gamma(a_0)/\Gamma(\ell+1+a_0)\)
and the analogous \(b_0\) factor.
The sine binomial in (15) tends to \(\binom m\ell\);
summing its alternating finite powers gives \((1-tu)^m\).

For real \(\alpha\), the absolute value of the integral in (17)
is at most
\[
 \int_0^1\!\!\int_0^1
             (1-t)^{-1/2}(1-u)^{-1/2}\,dt\,du=4.
 \tag{19}
\]
This bounds the limiting anchor uniformly in \(m\). At
\(\alpha=0\) the integrand is positive. No positivity is asserted
for other real parameters.

The quantifiers remain important: (17) is proved for each fixed
\(m\), followed by \(N\to\infty\). Its bounded limiting expression
does not prove a uniform finite-\(N\) estimate when \(m\) grows,
and does not control the whole Newton reconstruction or its real
spectral norm. Both signs have the same fixed-index limit after
the displayed exact phase is retained.

## 5. Scope and direct sources

The question left open is a polynomial real-interval bound for
the whole \(U_\sigma K_N(w_N(\alpha),Z)\), including all its
physical normals, uniformly in the level. The naive triangular
bound can be exponential at full degree. Equations (10)--(13)
identify the exact finite cancellation that would have to replace
it. Equation (17) supplies only one endpoint anchor.

In particular no marked-leaf operation is added to a reduction
certificate here. No whole-source or filled-action bound follows,
and no infinite root-of-unity hypergeometric summation is used.

The complete direct sources were read at their unchanged pins,
with the used implications and hashes checked:

* [Original unit-leaf operator](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_low_degree_charged_leaf_reduction.md),
  SHA256 80df78ceafaa97182aebc6831651921f7f8040e1356ee07a3d0d3fbadd02846a:
  original crossing matrix, full turn relation, Frobenius transpose,
  and canonical-representative convention.
* [Both endpoint Newton limits](research_endpoint_normal_two_ended_limit.md),
  SHA256 1e72bffbd0718fec2ae61c7a91dbb93bcd1506a8ca3db28f030cc8fcb2400e93:
  exact complementary product identity and locally uniform fixed
  upper-index limit used in (16).

Only written algebra, text reads and hashes were used. No mathematical
program, numerical experiment, test or build was run. Adopted notes
and public manuscripts are unchanged.
