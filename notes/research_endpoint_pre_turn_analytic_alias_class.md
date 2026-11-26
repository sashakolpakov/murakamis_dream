# A pre-turn analytic alias class for microscopic endpoint sources

Private written proof, 16 November 2026.

The actual unturned endpoint kernel has an exact decomposition into a
moderate sharp baseline, a moderate coefficient times the original
physical-grid polynomial, and a symmetric small real-axis repair.
This decomposition includes the fold. It is preserved, with a bounded
power of the grid polynomial, by any fixed number of ordinary
half-shift divided differences, means, and multiplications. Positive
microscopic ordinary divisions are local units and retain their
actual remainders.

The grid-polynomial coefficient cannot be discarded before a half
shift: it then contributes to the constant channel. The construction
does not assert closure under a physical turn, a filled-action bound,
or a nonzero coefficient after these operations.

## 1. Domains, source, and the sharp input

Put
\[
 h=N^{-1},\quad q=e^{\pi ih},\quad
 C_N(x)=2\cos(2\pi x+\pi h),\quad R_Nx=1-h-x,
\]
\[
 P_N(C)=2T_N(C/2)+2,\qquad
 p_N(x)=P_N(C_N(x))=4\sin^2(\pi Nx).
 \tag{1}
\]
The spectral kernel is the original ordinary polynomial
\[
 K_N(w,C)=\sum_{k=0}^{N-1}e_k(w)e_k(C),\qquad
 w=w_N(\alpha)=2\cosh(\alpha/N),
 \tag{2}
\]
with the Newton normalization of the pinned sources. Parameters lie
in an arbitrary fixed bounded complex compact set. All constructions
below are on the finite local parameter charts of the sharp atlas;
larger chart neighborhoods are reserved for derivatives.

Fix \(x_0\in(0,1/2)\), a finite height \(H>0\), and
\[
 0<\gamma<J_*(\pi-2\pi x_0),\qquad
 \delta=\pi^{-1}\arcsin\{\sin(\pi x_0)/\sqrt2\}.
 \tag{3}
\]
Choose fixed nested real buffers with left endpoints greater than
\(\delta\), all less than \(x_0\), so that
\[
 I_\delta(X)=\int_0^\delta
       \log\frac{\sin^2(\pi X)-\sin^2(\pi v)}
                    {\sin^2(\pi v)}\,dv>\gamma
 \tag{4}
\]
on their left edges. Reflect the buffers about \((1-h)/2\).
Use rectangles of these widths and successively larger fixed
heights than \(H\). A fixed number of operations below uses a fixed
number of such buffers. Their number is independent of \(N\).

For the outer repair rectangle choose an integer \(j_0=j_0(N)\)
with \(j_0/N=a+O(h)\), where \(a\) is one of these buffered
left endpoints. Its vertical sides are
\[
 a_N=(j_0-\tfrac12)h,\qquad
 b_N=(N-j_0-\tfrac12)h=R_Na_N.
 \tag{5}
\]
Its physical nodes are exactly \(x_j=jh\), with
\[
                    j_0\le j\le N-1-j_0.
 \tag{6}
\]
Choose its horizontal sides at fixed heights \(\pm H_{\rm out}\),
larger than the target heights. The sharp modes are defined on a
fixed larger rectangle, so the \(O(h)\) adjustment in (5) is harmless.

The atlas supplies a holomorphic baseline \(V_N(x,\alpha)\),
normalized at one actual two-value physical anchor to the right of
the small window about \(x_0\). It has polynomial norm on all the
prescribed rectangles and satisfies
\[
 V_N(R_Nx,\alpha)=V_N(x,\alpha).
 \tag{7}
\]
On the entire symmetric real buffer needed here its actual errors
obey
\[
 e_j=K_N(w,C_N(x_j))-V_N(x_j),\qquad
 d_j=\partial_xK_N(w,C_N(x_j))-V_N'(x_j),
\]
\[
                    |e_j|+|d_j|\le CN^b e^{-\gamma N}.
 \tag{8}
\]
All fixed parameter derivatives have the same form, with different
polynomial powers.

Here is the uniform-buffer implication of the atlas proof, since
its displayed local theorem emphasizes rows to the left of the
anchor. Its regular divided-color frame is invertible through the
fold. On the symmetric buffer its coefficient-transfer perturbation,
and its first derivative, are bounded by
\(CN^b e^{-NI_\delta(\Re x)}\). At physical rows the actual
inhomogeneous residual and its first angular derivative vanish.
Reflection gives the derivative-coefficient equation
\((I+\mathcal P_j)a'_j=-\mathcal Q_ja_j\), with
\(\mathcal P_j-I,\mathcal Q_j\) exponentially small. The physical
coefficient \(a_j\) is polynomially bounded. Finally transport the
value coefficient from any row in (6) to the one fixed anchor.
All these real paths stay in the symmetric buffer, where the
minimum of \(I_\delta\) is at its two ends and is greater than
\(\gamma\). At most \(N\) steps prove (8) there, including the
center and its reflected rows. No new anchor is chosen at the fold.

Reflection implies \(e_{N-1-j}=e_j\) and
\(d_{N-1-j}=-d_j\). At the odd simple spectral node the angular
derivative is zero; a spectral first normal is not prescribed.

## 2. Exact decomposition and a moderate alias coefficient

Use \(\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)\), with its
removable value at zero, and define the symmetric repair
\[
 E_N(x)=\sum_{j=j_0}^{N-1-j_0}
       [e_j+d_j(x-x_j)]\operatorname{sinc}^2(N(x-x_j)).
 \tag{9}
\]
This is holomorphic and invariant under \(R_N\). It has exactly
value \(e_j\) and derivative \(d_j\) at every node in (6).
On every buffered real interval, for each fixed \(k\),
\[
                   |\partial_x^k E_N(x)|\le C_kN^{b_k}e^{-\gamma N}.
 \tag{10}
\]
Indeed the derivatives of \(\operatorname{sinc}^2 t\) of fixed
order are bounded on the real line; each differentiation in \(x\)
costs a power of \(N\), and the sum has at most \(N\) terms.
The factors \(x-x_j\) are uniformly bounded there.

Define
\[
 Q_N(x)=\frac{K_N(w,C_N(x))-V_N(x)-E_N(x)}{p_N(x)}.
 \tag{11}
\]
The numerator has a double angular zero at every zero of \(p_N\)
inside the repair rectangle. Thus \(Q_N\) is holomorphic there,
including the physical grid and the fold. The decomposition is exact:
\[
 \boxed{\quad K_N(w,C_N(x))=V_N(x)+p_N(x)Q_N(x)+E_N(x).\quad}
 \tag{12}
\]

**Theorem 1.** The coefficient \(Q_N\) is polynomially bounded on
the closed repair rectangle. Every fixed spatial or parameter
derivative has a polynomial bound on smaller buffered rectangles.
Both \(Q_N\) and \(E_N\) descend holomorphically to the spectral
variable through the fold. The bound (10) also holds for every
fixed spectral derivative on the buffered real spectral interval.

*Proof.* The ordinary kernel has degree \(N-1\) and polynomial
real norm, uniformly on the bounded complex parameter sets. Its
Chebyshev expansion consequently gives
\[
 |K_N(w,C_N(x))|\le CN^b
                           e^{2\pi(N-1)|\Im x|}.
 \tag{13}
\]
On either midpoint vertical side in (5),
\[
                    |p_N(x)|=4\cosh^2(\pi N\Im x).
 \tag{14}
\]
On either horizontal side,
\[
                    |p_N(x)|\ge4\sinh^2(\pi NH_{\rm out}).
 \tag{15}
\]
Equations (13)--(15) bound \(K_N/p_N\) polynomially on the
boundary. The moderate baseline has the same boundary bound after
division by \(p_N\).

There is an exact formula for the remaining boundary quotient:
\[
 \frac{E_N(x)}{p_N(x)}
 =\sum_{j=j_0}^{N-1-j_0}
       \frac{e_j+d_j(x-x_j)}{4\pi^2N^2(x-x_j)^2}.
 \tag{16}
\]
It follows by canceling the common \(\sin^2(\pi Nx)\).
Every point of a vertical side has distance at least \(1/(2N)\)
from a grid node; on a horizontal side the distance is at least
\(H_{\rm out}\). Thus (16) is bounded by
\(CN^b e^{-\gamma N}\) on the boundary. The maximum principle
applied to the holomorphic quotient (11) proves the stated bound
for \(Q_N\). Cauchy's formula on the reserved buffers gives its
fixed derivatives.

All terms in (12) are invariant under \(R_N\). Inside a rectangle
of width less than one, the only two possible preimages of a
spectral color are related by this reflection. At its fixed point
\(x_c=(1-h)/2\), an invariant holomorphic function has an even
power series in \(x-x_c\). Since
\[
 C_N(x)+2=4\sin^2(\pi(x-x_c))
 \tag{17}
\]
is a regular analytic coordinate in \((x-x_c)^2\), this series
descends holomorphically through \(C=-2\). Elsewhere descent is
ordinary local inversion. The bounds are uniform on smaller
spectral images of the buffered rectangles.

For the real derivative claim about \(E_N\), away from the fold
use \(C_N'\ne0\) and (10). Near the fold write \(t=x-x_c\).
For an even smooth function, \(E_N'(t)/t=\int_0^1E_N''(st)\,ds\).
Iterating this identity controls derivatives in \(t^2\) of fixed
order by a finite number of ordinary derivatives on a slightly
larger real interval. Equation (17) then gives the spectral
derivative bound from (10), without dividing by a small physical
angular derivative. Parameter derivatives commute with these
arguments. \(\square\)

The repair is small on the real interval, not asserted moderate
on a tall rectangle. Its elementary complex bound contains
\(e^{2\pi N|\Im x|}\). Formula (16) is why the quotient coefficient
is nevertheless moderate on both halves. In particular (12) is
not a global moderate representative of the original full kernel.

## 3. Ordinary half shifts retain the alias channel

For the remainder of the proof write \(p=P_N(C)\). Define the
ordinary operators, before any canonical reduction, by
\[
 C=v+v^{-1},\quad C_\pm=q^{\pm1}v+q^{\mp1}v^{-1},\qquad
 \mathcal Df=\frac{f(C_+)-f(C_-)}{C_+-C_-},\quad
 \mathcal Sf=\frac{f(C_+)+f(C_-)}2.
 \tag{18}
\]
On the angular cover they use \(x\pm h/2\). For holomorphic
spectral functions all coincident-color quotients have their
removable meaning. A smaller fixed domain and all sufficiently
large \(N\) keep these half shifts in the reserved larger domain.

The exact source aliases are
\[
                   P_N(C_+)=P_N(C_-)=4-P_N(C).
 \tag{19}
\]
Consequently, for every fixed \(r\) and holomorphic coefficients
\(A_0,\ldots,A_r\),
\[
 \begin{split}
 \mathcal D\Big(\sum_{k=0}^r p^k A_k\Big)
                         &=\sum_{k=0}^r(4-p)^k\mathcal DA_k,\\
 \mathcal S\Big(\sum_{k=0}^r p^k A_k\Big)
                         &=\sum_{k=0}^r(4-p)^k\mathcal SA_k.
 \end{split}
 \tag{20}
\]
This follows directly by evaluating the two half shifts in (18);
no quotient-algebra manipulation is used.

Moderate holomorphic coefficients remain moderate under either
operator. For \(\mathcal S\) this is immediate. For \(\mathcal D\)
use the integral of the spectral derivative between the two
nearby colors in a reserved spectral neighborhood. That argument
also applies at coincident colors and at the fold. It has uniform
cost on fixed smaller domains, rather than an inverse power of a
vanishing angular sine.

In particular (12) gives the exact identities
\[
 \mathcal DK_N=\mathcal DV_N+(4-p)\mathcal DQ_N+\mathcal DE_N,
 \qquad
 \mathcal SK_N=\mathcal SV_N+(4-p)\mathcal SQ_N+\mathcal SE_N.
 \tag{21}
\]
Thus the moderate constant channels after a half shift are
\(\mathcal DV_N+4\mathcal DQ_N\) and
\(\mathcal SV_N+4\mathcal SQ_N\). Replacing the kernel by
\(V_N\) before applying these operators would lose actual source
terms even on the physical grid.

## 4. Finite ordinary operations and positive division

Call a local decomposition admissible here if it is an exact
ordinary analytic identity
\[
             F_N(C)=\sum_{k=0}^rP_N(C)^k A_{k,N}(C)+E_N(C),
 \tag{22}
\]
where \(r\) is fixed, all \(A_{k,N}\) are moderate on buffered tall
spectral domains, and every fixed real spectral derivative of
\(E_N\) is bounded by a polynomial times \(e^{-\gamma N}\).
All coefficients and errors retain their common exterior
parameters. No trace is applied in this definition.

**Theorem 2.** Start with finitely many original kernels (2) and
fixed-degree polynomial coefficients of polynomial size. Any
fixed finite sequence of the following operations has a
decomposition (22), on suitably smaller fixed buffers:

* ordinary addition and multiplication;
* the ordinary operators \(\mathcal D,\mathcal S\);
* ordinary polynomial division by a fixed number of monic factors
  with roots \(a_{\ell,N}\) satisfying
  \(|a_{\ell,N}-2|\le B/N^2\), retaining the actual remainders;
* explicitly prescribed canonical reduction in an original traced
  variable, with the reset described in section 5.

The alias degree stays bounded independently of \(N\), and fixed
parameter derivatives are included. Every actual ordinary
polynomial at any stage has degree \(O(N)\) and polynomial real
norm. This is a pre-turn assertion.

*Proof before canonical reduction.* Equations (12) and (20)
give the initial class and its half-shift closure. Multiplication
convolves the coefficient vectors, adding their alias degrees.
Its error is
\[
 E_F\Big(\sum p^k A_{G,k}\Big)
 +E_G\Big(\sum p^k A_{F,k}\Big)+E_FE_G.
 \tag{23}
\]
On the real interval \(0\le P_N\le4\), and its fixed derivatives
cost only powers of \(N\). Thus (23), with all its fixed real
derivatives, retains the exponential saving. The same is true
under \(\mathcal D,\mathcal S\): the shifted real colors stay in
a larger real buffer, and the divided-difference integral uses
one additional real spectral derivative of the error.

For a division let \(d_N\) be the specified monic polynomial and
write its actual ordinary division as
\[
                    F_N=d_N G_N+R_N^{\rm rem},
             \qquad \deg R_N^{\rm rem}<\deg d_N.
 \tag{24}
\]
The notation \(R_N^{\rm rem}\) is unrelated to the reflection.
On the buffered spectral domains, \(C=2\) is uniformly excluded.
Hence \(d_N\) is a uniform local unit for large \(N\). The exact
quotient decomposition is
\[
 G_N=\frac{A_{0,N}-R_N^{\rm rem}}{d_N}
                  +\sum_{k=1}^r p^k\frac{A_{k,N}}{d_N}
                  +\frac{E_N}{d_N}.
 \tag{25}
\]
The remainder is not replaced by a physical evaluation or dropped.

Its coefficients are polynomially bounded. To check this
uniformly at colliding complex roots, perform the divisions
successively as
\[
 F_\ell(C)=\frac{F_{\ell-1}(C)-F_{\ell-1}(a_{\ell,N})}
                                      {C-a_{\ell,N}}.
 \tag{26}
\]
A polynomial of degree at most \(cN\) and polynomial real norm
has polynomial size and derivatives on a Bernstein ellipse of
parameter \(e^{b/N}\), for every fixed \(b,c\). Choose \(b\)
large enough to contain the roots and the segments from them to
\([-2,2]\). Starting with \(F_0=F_N\), integrating
\(F_{\ell-1}'\) on those segments proves
polynomial bounds for (26), just as in the positive-division
source. The actual Newton remainder
\(\sum_{\ell=1}^{\deg d_N}F_{\ell-1}(a_{\ell,N})
                    \prod_{k<\ell}(C-a_{k,N})\)
therefore has polynomial coefficients. This proves (25) and
its derivative assertions without root separation.

For completeness, all the required global real norms follow
inductively at the ordinary polynomial level. Original kernels
have polynomial norm. Products and fixed-degree multipliers
preserve it. On \([-2,2]\) both half-shift colors lie in that
interval, so \(\|\mathcal Sf\|\le\|f\|\) and
\(\|\mathcal Df\|\le\|f'\|\); Markov supplies the polynomial
cost at degree \(O(N)\). Formula (26) handles division. None of
these operations increases degree beyond a fixed multiple of
\(N\). The canonical step is proved next. \(\square\)

The positive-division statement here is local analytic closure
and polynomial real control. The stronger joint norm and
physical-prefix conclusions of the division source are not
asserted for every new operation word.

## 5. Canonical resets preserve the source, but precede no silent half shift

Suppose \(F_N\) in (22) is an ordinary polynomial of degree at
most \(cN\), with polynomial real norm, and let
\[
                  \widehat F_N=\operatorname{rem}_{P_N}F_N.
 \tag{27}
\]
The exact Fourier folding formula in the endpoint-product source
applies to every polynomial with this degree bound: only
\(O_c(1)\) alias blocks occur, with bounded block weights.
Its original Fourier coefficient sum is at most \(O(N)\)
times its real norm. Thus \(\widehat F_N\) has polynomial real
norm and degree at most \(N-1\).

At every double physical spectral root, \(P_N=P_N'=0\), so
\(\widehat F_N\) has the value and first spectral normal of
\(A_{0,N}+E_N\). At the odd simple spectral root it has their
value; in the angular coordinate its derivative is zero. Thus
its angular full-jet errors relative to \(A_{0,N}\) satisfy (8).
This uses the actual remainder (27), not an identification of
ordinary functions away from the grid.

Apply the symmetric repair (9) to these errors on a smaller
reflected midpoint rectangle. All terms of the construction
are spectral functions, so the requisite reflection persists.
The boundary proof (13)--(16), with \(\widehat F_N\) in place
of \(K_N\), gives the exact reset
\[
             \widehat F_N=A_{0,N}+p_N\widehat Q_N+\widehat E_N,
 \tag{28}
\]
where \(\widehat Q_N\) is moderate and \(\widehat E_N\) has
the same sharp real error budget. Thus the alias degree can
be reset to one whenever canonical reduction is actually
prescribed. This completes Theorem 2.

The operation order remains essential. Formula (20) is for
ordinary functions; the ideal \((P_N)\) is not preserved by
\(\mathcal S\), since \(\mathcal SP_N=4-P_N\). If the original
construction applies half shifts before reduction, one must
carry the preceding ordinary decomposition. If it specifies
reduction first, one must use (28), including its new alias
coefficient, in the next ordinary half shift. The two source
operations are not silently interchanged.

All statements are coefficientwise in fixed shared parameters.
They retain the product rule for the shared first normal and
fixed mixed exterior derivatives. Canonical reduction is made
only where the original variable is traced, never in an
ordinary free output variable.

## 6. Scope and direct sources

This class ties the original finite six-channel module to actual
holomorphic functions on prescribed bounded-height domains. It
retains the \(P_N\leftrightarrow4-P_N\) channels and gives sharp
real errors through finite ordinary operations. It supplies no
bound on the result of applying \(T\), \(U_\tau\), or a general
received-factor composition to (22). A moderate coefficient of
\(P_N\) can re-enter a source after half shifts; an outer turn
requires its own coherent estimate. Nor do addition, divided
differences, or subtraction of ordinary remainders preserve a
nonzero baseline coefficient. No filled-action or lower-bound
conclusion is inferred.

The sharp baseline and its actual full-jet estimate are prior
results. The new construction is the symmetric exact repair
and moderate quotient (11), together with the operation closure
(20)--(28). The following complete direct sources were read at
their unchanged pins, with the used implications checked:

* [Sharp local parameter atlas](research_endpoint_sharp_local_parameter_atlas.md),
  SHA256 37cbfdab768bad41aa643859a75f9dfeaa5f1db57888ef14f6d5beeb5b29e019.
* [Original endpoint bounds and full-Hermite folding](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194.
* [Ordinary divided-difference source module](research_endpoint_product_divided_difference_module.md),
  SHA256 8a1b215aa6034365d4faa84130381d6a78a17383c03ecf6c6b48a77b6c4e3093.
* [Positive-endpoint ordinary division](research_positive_endpoint_quotient_source_bounds.md),
  SHA256 cd773c98ee07750f5ccdae4b95d9e76042a1a1e7cc7f59f4f1d6a9dedf3eb766.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, build, or
compilation was run. Adopted notes and public manuscripts are unchanged.
