# The actual complete period is a bounded-source first-normal response

Research proof and independent source test, 27 October 2026. The
ordinary-color bound and the normal boundary factor give an exact
first-normal descriptor system for every knot. On a regular companion
chart this becomes a fixed-rank affine transfer, with the same
characteristic curve as the actual normal operator. The forcing is
polynomially bounded; the complete value is its specified normal cut.

This goes beyond regarding the complete value as an unspecified large
entry of a Gram inverse. It does not prove that the response excites the
geometric branch. Section 3 constructs a coherent source-wall change
which preserves any prescribed finite prefix of actual colors, Weyl
symmetry and the ordinary-color bounds, but kills complete growth and
moves the original contribution to arbitrarily high normal order.

## 1. A universal bounded-source normal equation

Use \(q_N=e^{\pi i/N}\), \(Q_N=q_N^2\), the actual reduced root state
\(F_N(Y)\), and the actual generic colors \(C_j(q)\), with
\[
 F_N(Q_N^j)=C_j(q_N)\ (1\le j<N),\qquad
 C_N(q_N)=F_N(1)=K_N.
\]
The independently proved
[positive trace bound](regularized_kashaev_period.md) gives
\[
 |C_j(q_N)|\le D_N=O(N^{b-1}),\qquad 1\le j<N.       \tag{1}
\]

Fix a polynomial presentation of an actual normal operator
\[
 B=\sum_{i=0}^{d}b_i(q,Y)T^i,\qquad TY=q^2YT,\quad d\ge1,
 \qquad B[(Y-1)F_N]=0.                              \tag{2}
\]
Such an operator exists by applying the actual finite-state theorem
to the weighted state; the primitive minimal presentation is available
in [actual Weyl descent](actual_weyl_descent.md). Equivalently
\(B(Y-1)\) is an actual polynomial annihilator of \(F_N\).
The right factor is retained, rather than inverted at the cut.

Define the generic weighted colors
\[
 d_j(q)=(q^{2j}-1)C_j(q),\qquad
 X_j(q)=(d_j(q),\ldots,d_{j+d-1}(q))^t .
                                                               \tag{3}
\]
Cross-level polynomial rigidity gives the exact generic recurrence
\[
 \sum_i b_i(q,q^{2j})d_{j+i}(q)=0.                  \tag{4}
\]
For fixed \(j\), evaluate (2) at all sufficiently large roots with
\(j+d<N\); this gives infinitely many zeros of the fixed Laurent
polynomial on the left of (4), proving (4).

Put \(p_j(q)=b_d(q,q^{2j})\), and let \(\mathcal N_j(q)\) have \(p_j\)
on the superdiagonal and last row
\(-b_0(q,q^{2j}),\ldots,-b_{d-1}(q,q^{2j})\). Then, before any
specialization,
\[
 p_j X_{j+1}=\mathcal N_jX_j.                       \tag{5}
\]
Choose a fixed sufficiently large initial color \(j_0\) as in
[the all-level theorem](all_level_a_period.md), so none of the
generic \(p_j\), \(j\ge j_0\), is identically zero.

At level \(N\), use the scaled color-normal parameter
\[
 q=q_N(1+s/N),\quad
 x_j=X_j(q_N),\quad y_j=[\partial_sX_j(q_N(1+s/N))]_{s=0}.
                                                               \tag{6}
\]
All dots below denote this derivative, including the moving argument
\(Y=q^{2j}\). Exact differentiation of (5) gives
\[
 p_jx_{j+1}=\mathcal N_jx_j,\qquad
 p_jy_{j+1}-\mathcal N_jy_j
       =g_j:=\dot{\mathcal N}_jx_j-\dot p_jx_{j+1},       \tag{7}
\]
where the undotted coefficients in (7) are evaluated at \(q_N\).
No division by \(p_j(q_N)\) has occurred. Thus (7) remains valid at
every singular step.

The complete cut is exactly
\[
 K_N=\frac12 e_d^t y_{N-d+1}.                       \tag{8}
\]
Indeed \(d_N(q_N)=0\), while
\[
 \partial_s[(q_N(1+s/N))^{2N}-1]_{s=0}=2.
\]
The derivative of \(C_N\) is multiplied by the vanishing factor.
Only its value \(K_N\) remains.

The source in (7) is polynomially bounded uniformly in all steps.
Every component of \(x_j\), \(j_0\le j\le N-d+1\), is either an
ordinary weighted color, bounded by \(2D_N\), or the final zero
\(d_N(q_N)\). Also
\[
 \dot b_i(q,q^{2j})
 =\frac1N(q\partial_q+2jY\partial_Y)b_i(q,Y)
       \big|_{q_N,Q_N^j}=O_B(1).                  \tag{9}
\]
This follows monomial by monomial: \(q^aY^c\) contributes the
bounded factor \((a+2jc)/N\). Hence
\[
 \|x_j\|=O_B(D_N)\quad(j_0\le j\le N-d+1),\qquad
 \|g_j\|=O_B(D_N)\quad(j_0\le j\le N-d).          \tag{10}
\]
It also lies in exactly one fixed coordinate:
\[
 g_j=e_d\gamma_j,\qquad
 \gamma_j=-\sum_{i=0}^d
       \dot b_i(q_N,Q_N^j)d_{j+i}(q_N).           \tag{10a}
\]
For each of the first \(d-1\) rows,
\(\dot{\mathcal N}_jx_j=\dot p_j(x_j)_{r+1}\)
and \(\dot p_jx_{j+1}=\dot p_j(x_j)_{r+1}\), so the two
terms cancel. This proves (10a) even when \(p_j=0\). In scalar
form the normal response is simply
\[
 \sum_{i=0}^d b_i(q_N,Q_N^j)y_{j+i}
    =-\sum_{i=0}^d\dot b_i(q_N,Q_N^j)d_{j+i}(q_N),
 \qquad y_N=2K_N,                                \tag{10b}
\]
where \(y_r=\partial_sd_r(q_N(1+s/N))|_{s=0}\).
The forcing is therefore a bounded single-channel source,
not an arbitrary vector in the companion space.

The initial \(x_{j_0},y_{j_0}\) are bounded because they use finitely
many fixed Laurent-polynomial colors.

Equations (7)--(10) prove an actual, universal bounded-source
first-normal response theorem. The normal is along the honest
integral-color family, with its moving meridian. No off-root
horizontal ADO section is assumed.

## 2. Fixed-rank transfer and its precise singular-step qualification

Where \(p_j(q_N)\ne0\), put
\[
 A_j=\mathcal N_j/p_j.
\]
Then (7) becomes the exact rank-\(d\) affine equation
\[
 x_{j+1}=A_jx_j,\qquad
 y_{j+1}=A_jy_j+\dot A_jx_j.                       \tag{11}
\]
Here \(\dot A_jx_j=e_d\gamma_j/p_j\); the divided normal
source retains the same single channel.
Equivalently the doubled column has rank-\(2d\) transport
\[
 \binom{x_{j+1}}{y_{j+1}}
 =\begin{pmatrix}A_j&0\\ \dot A_j&A_j\end{pmatrix}
   \binom{x_j}{y_j}.                              \tag{12}
\]
All its input is fixed small-color pointing.

For \(J=N-d+1\), define
\(\Phi(k,j)=A_{k-1}\cdots A_j\). The exact selected response is
\[
 2K_N=e_d^t\left[
   \Phi(J,j_0)y_{j_0}
   +\sum_{j=j_0}^{J-1}\Phi(J,j+1)\dot A_jx_j
                    \right].                    \tag{13}
\]
This is an explicit source coupling, rather than a choice of a
largest characteristic root. An adjoint row
\(\lambda_j=\lambda_{j+1}A_j,\ \lambda_J=e_d^t\)
gives the equivalent formula
\[
 2K_N=\lambda_{j_0}y_{j_0}
        +\sum_j\lambda_{j+1}\dot A_jx_j.          \tag{14}
\]

If the nonzero \(p_j(q_N)\) have a uniform polynomial lower bound,
then the divided coefficients and the forcing in (11) have
polynomial bounds too. A simple sufficient condition is that
\(b_d(1,Y)\) have no zeros on the unit circle. In that case they
are uniformly bounded apart from the already bounded \(x_j\).
This is a checkable operator condition, not asserted for every
primitive normal operator.

The transfer has no new classical characteristic actions:
\[
 \det\!\left(LI-
   \begin{pmatrix}A_j&0\\\dot A_j&A_j\end{pmatrix}\right)
       =\det(LI-A_j)^2.                           \tag{15}
\]
On a regular limiting chart \(j/N\to u,\ Y=e^{2\pi iu}\), the
off-diagonal block tends to
\(2uY\partial_YA_{\mathrm{cl}}(Y)\). Thus the first-normal extension
doubles the characteristic of the actual operator; it does not
introduce a new regulator action. Identification of a geometric
factor and excitation of its marked branch are further assertions.

At a zero of \(p_j(q_N)\), (13) is understood only through its
whole meromorphic germ and cancellation. The descriptor equation
(7) stays valid, but its first-normal solutions need not have a
unique cut. Higher lifts can select \(y_j\). The existing bounded
jet budget, applied to \(B\), supplies a uniform finite procedure:
to recover this first derivative, retain the total pole budget
plus one input jet. It does not justify deleting singular steps
or replacing their actual lattices by (11) at a zero.

Consequently the unconditional theorem is (7)--(10). A regular
fixed-rank affine transfer is its stated chartwise strengthening.
Bounded forcing alone gives no exponential lower bound for (13);
the source-weighted Green response is the quantity to estimate.

## 3. A coherent source-wall change can hide growth to any normal order

Here is an exact obstruction to deducing the selected growth from
ordinary-color bounds, a geometric localized factor and a finite
prefix of color pointing. It is not a new knot invariant.

Start with the actual family of any knot. Fix positive integers
\(J,m\), and put
\[
 X=Y+Y^{-1},\quad a_r(q)=q^{2r}+q^{-2r},\quad
 t_J(q,X)=\prod_{r=1}^J(X-a_r(q)),
\]
\[
 R_J(q,Y)=\frac{t_J(q,X)}{t_J(q,2)},\qquad
 h_{J,m}(q,Y)=(1-R_J(q,Y))^m .                    \tag{16}
\]
For \(N>J\), define the whole root function and generic colors by
\[
 \widetilde F_N(Y)
   =1+h_{J,m}(q_N,Y)(F_N(Y)-1),
\]
\[
 \widetilde C_j(q)
   =1+h_{J,m}(q,q^{2j})(C_j(q)-1).               \tag{17}
\]
The denominator in (16) is nonzero at every such \(q_N\).

These families have the following exact properties.

1. Their first \(J\) generic colors are literally unchanged, since
   \(R_J(q,q^{2j})=0\) for \(1\le j\le J\).
2. Every \(\widetilde C_j(q)\) is Laurent polynomial and
   \(\widetilde C_j(1)=1\).
3. They satisfy all ordinary-color identities and also complete
   integral-color compatibility:
   \[
    \widetilde F_N(Q_N^j)=\widetilde C_j(q_N),\qquad
    \widetilde C_N(q_N)=\widetilde F_N(1)=1.
   \]
4. Reciprocity is preserved. All ordinary values remain polynomially
   bounded uniformly in \(j<N\).
5. At each level,
   \(\widetilde F_N(Y)-1\) vanishes to order at least \(2m\)
   at \(Y=1\), regardless of how large \(F_N(1)\) is.

For the only nonobvious algebraic claim in item 2, write \(Q=q^2\).
For \(j>J\), direct factorization gives
\[
 R_J(q,q^{2j})
 =(-1)^JQ^{-jJ+J(J+1)/2}
      {j-1\brack J}_Q\,{j+J\brack J}_Q.           \tag{18}
\]
Both Gaussian coefficients are polynomials. Formula (18) follows
from
\[
 a_j-a_r=Q^{-j}(1-Q^{j-r})(1-Q^{j+r}),\quad
 2-a_r=-Q^{-r}(1-Q^r)^2 .
 \]
For \(j\le J\) the numerator is zero. The apparent pole at \(q=1\)
therefore cancels in every fixed color, proving item 2.

For item 4, the numerator of \(R_J(q_N,Y)\) is bounded by \(4^J\)
on the unit circle, whereas its denominator has modulus
\(\prod_{r=1}^J4\sin^2(\pi r/N)\gg_JN^{-2J}\).
Thus
\[
 |\widetilde C_j(q_N)|
       =O_{J,m}(N^{b-1+2Jm}).
 \]
In fact the same reasoning bounds the multiplier by a fixed power
of the quantum dimension \([j]_{q_N}\): use
\(\sin^2(\pi j/N)/\sin^2(\pi r/N)=[j]^2/[r]^2\).
Thus it is not merely a loss of all semisimple-type polynomial
control.

For item 5, \(1-R_J(q,Y)\) vanishes at \(X=2\), and
\[
 X-2=(Y-1)^2/Y.
 \]
The original complete growth has therefore been moved beyond any
prescribed finite number of normal jets, while the new complete
period is identically one. Choosing the actual figure-eight family,
whose positive exponential growth was proved separately, makes this
a concrete growth-changing example.
More precisely, set
\[
 c_{N,J}=\sum_{r=1}^J\frac1{2-a_r(q_N)}
        \asymp_J N^2 .
\]
All summands are positive at these roots. The first possibly
nonzero coefficient is exactly
\[
 [(Y-1)^{2m}](\widetilde F_N(Y)-1)
       =(-c_{N,J})^m(K_N-1).                     \tag{19}
\]
Thus its exponential rate is the original one, with a specified
polynomial multiplier; the contribution has not merely been
discarded from the entire normal tower.

The construction is still uniformly q-holonomic: multiplication by
the fixed rational function \(h_{J,m}(q,Y)\), and addition of the
constant section, give a fixed rational all-level operator. To see
this directly, if \(P F=0\), then \(P(F-1)=-P1\); a first-order
operator annihilates the rational right side. Conjugate the resulting
homogeneous operator by \(h_{J,m}\), and apply the same argument
once more to add one. Clear its fixed denominators afterward.

Away from \(h_{J,m}=0\), its nonconstant component is rationally
gauge equivalent to the original one. Hence its original geometric
localized factor and characteristic action survive; an added
constant component contributes at most an abelian factor. The
comparison fails to be a unit exactly on the complete source wall.
This is the source-lattice defect, not a failure of color coherence.

The example does not preserve the entire actual knot pointing or its
full operator. In particular it does not contradict the exact
all-level reconstruction theorem, which fixes those data together.
It proves that the geometric localized A-factor, ordinary-color
bounds, reciprocity, all-level color compatibility and any preassigned
finite prefix alone do not force complete growth or first-normal
geometric coupling.

## 4. What the simplification supplies

The actual period has the exact bounded-source descriptor (7) and cut
(8). On a regular normal chart, (13) is a fixed-rank scalar response
whose characteristic is the actual A-symbol, doubled by the normal
extension. This isolates the desired norm problem in an actual
source coupling without positive entrywise crossing estimates.

The next substantive assertion would be a geometric, source-preserving
estimate for that coupling, through its singular lattice charts.
Classical etaleness does not establish it: (16)--(18) preserve the
localized characteristic and hide its contribution at the wall.
The required regular pointed comparison must distinguish that change.
