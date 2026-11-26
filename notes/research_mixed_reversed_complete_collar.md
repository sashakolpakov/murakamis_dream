# A complete right collar in the transposed open-source chart

Research deduction, 5 November 2026. Exact transposition transfers the
completed first-collar theorem to a complete right-cap collar, with
ordinary colors and every Fourier alternative retained. The transferred
region belongs to the opposite retained leg chart. An explicit finite
example shows why this does not identify a collar contribution in the
original chart, even though the complete scalar contractions agree.
No numerical computation or new source estimate is used.

## 1. Transposition before either leg family is summed

For a word \(\boldsymbol\epsilon=(\epsilon_1,\ldots,\epsilon_m)\),
let
\[
 Z_{\boldsymbol\epsilon,N}(w_L,w_R)
 =v(w_L)^TA_{3+\epsilon_1}\cdots A_{3+\epsilon_m}v(w_R),
 \qquad \epsilon_j\in\{0,1\}.
 \tag{1}
\]
The vector \(v(w)\) is the original ordinary Newton evaluation vector.
In [exact Fourier contraction](research_mixed_wire_exact_contraction.md),
equations (10)--(14), the actual matrices satisfy
\[
 A_{3+\epsilon}=S^TB_{3+\epsilon}S,\qquad
 B_{3+\epsilon}^T=B_{3+\epsilon},\qquad
 \Gamma=SS^T=\Gamma^T .
 \tag{2}
\]
These are ordinary transposes, without complex conjugation. In
particular no positive metric or asymptotic symmetry is required.
Writing \(\boldsymbol\epsilon^{\rm rev}=(\epsilon_m,\ldots,\epsilon_1)\),
one obtains the exact polynomial identity
\[
 Z_{\boldsymbol\epsilon,N}(w_L,w_R)
 =Z_{\boldsymbol\epsilon^{\rm rev},N}(w_R,w_L).
 \tag{3}
\]
It holds at every integer \(N\ge2\), both parities, and all ordinary
colors. A derivative of order \(p\) in \(w_L\) and \(q\) in \(w_R\)
is the derivative of order \(q\) in the left color and \(p\) in the
right color of the reversed word. No repeated-root normal is deleted.

At complete color the full original action in
[the open Hessian theorem](research_mixed_open_word_hessian.md),
equation (1), is literally invariant under
\[
 s'_j=t_{m+1-j},\quad t'_j=s_{m+1-j},\quad
 u'_L=u_R,\quad u'_R=u_L,\quad
 \epsilon'_j=\epsilon_{m+1-j}.
 \tag{4}
\]
The vertex sums, shared sums, own-type factorial terms, endpoint
actions and each term of the original quadratic mark are permuted.
The logarithmic strips and lifts are unchanged. Original critical
uniqueness therefore identifies the reversed critical point by (4),
and its action is exactly the same \(M_{\rm open}=\Re\mathcal F_*\).
This is not an inference from the equality of scalar asymptotics.

## 2. The exact fully contracted opposite chart

Keep
\[
 W_{\epsilon,N}(X)=
       \{d_N(X)(1+X^{-N})\}^{\epsilon},
 \qquad k_4=\sum_{j=1}^m\epsilon_j.
 \tag{5}
\]
The original contraction which retains the \(t\)-legs is
\[
\begin{split}
 Z_{\boldsymbol\epsilon,N}
 ={}&\kappa_N^{m+k_4}N^{m+k_4-1}
 \operatorname{CT}_{X_1,\ldots,X_{m-1}}
 \left[
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{m-1}C_{\epsilon_j,N}(X_{j-1},X_j)\right.\\
 &\left.\hspace{25mm}\cdot
 V_{\epsilon_m,N}(w_R,X_{m-1})
 \prod_{j=1}^{m-1}W_{\epsilon_j,N}(X_j)
 \right],
 \qquad X_j=e^{-2\pi it_j}.
\end{split}
 \tag{6}
\]
Here and below every constant term is the original counterclockwise
torus integral. The precise scalar, bands and terminal contraction
are Proposition 1 and equation (13) of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md).

Apply (6) to the reversed word in (3), and rename its retained
variables by \(Y_j=e^{-2\pi is_j}\), \(2\le j\le m\).
This gives the second exact formula
\[
\begin{split}
 Z_{\boldsymbol\epsilon,N}
 ={}&\kappa_N^{m+k_4}N^{m+k_4-1}
 \operatorname{CT}_{Y_2,\ldots,Y_m}
 \left[
 V_{\epsilon_1,N}(w_L,Y_2)
 \prod_{j=2}^{m-1}C_{\epsilon_j,N}(Y_{j+1},Y_j)\right.\\
 &\left.\hspace{25mm}\cdot
 U_{\epsilon_m,N}(w_R,Y_m)
 \prod_{j=2}^{m}W_{\epsilon_j,N}(Y_j)
 \right].
\end{split}
 \tag{7}
\]
For \(m=2\) both conditional products are empty. The matrix factors,
the colors, and the reference coordinates are all reversed before
the conditional polynomials are introduced. In particular (7) does
not assert symmetry of \(C_{\epsilon,N}(X,Y)\), or of \(U\) and \(V\).

Every diagonal factor in (7) is still the entire
\(d_N(Y_j)(1+Y_j^{-N})\). Expanding it gives the original choices
\(\sigma_j\in\{0,\epsilon_j\}\) in this chart:
\[
 d_N(Y_j)^{\epsilon_j}Y_j^{-N\sigma_j}.
 \tag{8}
\]
The terminal alternatives at the left have already been summed
inside \(V_{\epsilon_1,N}\). Equation (3) does not separately match
one selected term of (6) with a selected term of (7); the retained
index family, and hence the location of the explicit aliases, changed.

Both formulas permit their own exact periodic hybrid contour. The
row-dependent cutoff, own-coordinate factor and missing-neighbor
cutoff one are invariant under reversal of the path. Their
Jacobians are conjugated by the coordinate permutation, so the
determinant and its fixed bound are preserved. Product integration
and coordinate permutation introduce no additional sign or level
factor.

## 3. Completed right-cap collar theorem in the opposite chart

Let \(\widehat r_j=s_j^*\), \(2\le j\le m\), be the actual retained
references in (7), and set \(d_j=y_j-\Re\widehat r_j\).
For \(m\ge3\), prescribe
\[
\begin{split}
 z_m&=x_m,\qquad 0\le x_m\le\rho,\\
 z_{m-1}&=y_{m-1}+ik,\qquad
 y_{m-1}\in I_{3+\epsilon_{m-1}},\\
 z_j&=y_j+i\Im\widehat r_j,\qquad
 y_j\in P,\quad 2\le j\le m-2,\\
 P&=[.22,.45],\qquad I_3=[.267,.433],\quad I_4=[.24,.363].
\end{split}
 \tag{9}
\]
Here \(k\) lies between the actual reference height and zero when
the neighboring coordinate is unselected; if that type is four
and selected, \(0\le k\le7/500\). Permit both choices at position
\(m\), both physical choices at position \(m-1\) when its type is
four, and require all positions \(2,\ldots,m-2\) to be unselected.
Set \(Y_j=e^{-2\pi iz_j}\).

**Theorem 1.** The literal selected integrand of (7), with the full
left terminal transform, satisfies on (9)
\[
 |\widehat{\mathscr J}_N|
 \le C_\tau N^{A_\tau}
 \exp N\left\{
 M_{\rm open}-\Delta_{\epsilon_m,\epsilon_{m-1}}^{(m)}
 -\kappa\left(d_{m-1}^2+2\sum_{j=2}^{m-2}d_j^2\right)
 +\tau\right\},
 \qquad \kappa=1/2500000.
 \tag{10}
\]
For \(m\ge4\), the four gaps in the order \(00,10,01,11\) are
\((3/100,3/125,4/125,4/125)\). At \(m=3\) they are
\((3/100,3/125,1/20,1/20)\). Thus one total tolerance below
\(1/250\) leaves a common finite loss \(1/50\).

For \(m=2\), the entire \(Y_2\) collar \(0\le y_2\le\rho\),
at its actual zero collar height, has loss \(1/20\), for both
selections at type four. All statements retain ordinary-color disks,
every fixed ordinary derivative, and both level parities.

*Proof.* Rename the independent variables in the
[complete first-collar theorem](research_mixed_first_collar_full_terminal_completion.md)
for the reversed word. Its first coordinate is \(s_m\), its
second is \(s_{m-1}\), and its complete terminal is the original
left factor \(V_{\epsilon_1,N}\). This is exactly the integrand
in (7), with the colors interchanged as in (3). The original
references agree by (4). Its halfweights, tangents and quadratic
multiplicities therefore become exactly (10). This applies to
every fixed word, not only a word equal to its reversal.

For \(m=2\), use the
[two-vertex whole-collar theorem](research_mixed_two_vertex_first_collar.md)
on that same reversed word. Its single retained coordinate is
\(s_2\), and its scalar is the scalar in (7).
Ordinary derivatives interchange their orders according to (3).
The periodic hybrid graph and its bounded measure are preserved by
the reversal permutation, so the same exponential gap holds for
the restricted sector integral in this chart. \(\square\)

This completes a right-cap collar estimate without duplicating any
source bound. It is an exact relabeling of a region in the reversed
word's integral into a region in (7). It is not yet a right-collar
estimate in (6).

## 4. Why localization in the original retained chart does not follow

There is no pointwise change \(X_j=Y_{m+1-j}\) between (6) and (7).
Those variables represent different physical leg families. The
conditional asymmetry example in reversed-cap assembly already
rules out reversing the arguments of each kernel. The following
example shows the failure directly for the fully contracted
ordinary-color source, even with no conditional factors left.

At \(N=2\), \(r=-1,q=i,P_1=2\), and \(e_1(w)=-w/4\).
The original formulas give
\[
 \begin{split}
 H_2(w,Y)&=1-iw(1-Y)/8,\\
 U_{0,2}(w,X)&=(3+X)/2-iw(1+X)/8,\\
 V_{0,2}(w,X)&=(5+X^{-1})/2-iw/4.
 \end{split}
 \tag{11}
\]
For the word \((3,3)\), the two unscaled integrands obtained by
artificially giving the two retained coordinates the same name
differ by
\[
 \begin{split}
 &U_{0,2}(w_L,X)V_{0,2}(w_R,X)
       -V_{0,2}(w_L,X)U_{0,2}(w_R,X)\\
 &\hspace{22mm}=\frac{i(w_R-w_L)}{16}(3X+X^{-1}).
 \end{split}
 \tag{12}
\]
Its complete constant term is zero, as required by transposition.
At \(X=1\), however, it equals \(i(w_R-w_L)/4\).
For distinct arbitrarily close ordinary colors, its integral over
a sufficiently short real collar is nonzero. Differentiating once
in \(w_R\) also makes the same local failure visible at the exact
complete colors \(w_L=w_R=-2\). Multiplication by the common original
scalar changes none of these conclusions.

Thus equality of the full boundary polynomials, including their
ordinary jets, does not identify their localized collar integrals.
A restriction to a real arc is not constant-term extraction: it
retains nonzero Fourier frequencies such as the two in (12).
The complete-period contractions that led to (6)--(7) cancel those
frequencies only after full integration.

Consequently Theorem 1 cannot simply be added to an original-chart
left-collar bound as if the two estimates bounded disjoint pieces
of one partition of (6). To close the corresponding original-chart
right region, one needs a localized transformation identity with
its remaining Fourier terms controlled, or a complete decomposition
carried out in (7). The missing object is the localized source
observation, not the global transposition identity. No whole
ordinary-closure conclusion is asserted here.

## 5. An exact positive cutoff in the original wire coordinates

A localized identity does hold before either leg family is summed.
It uses the original wire coordinate rather than a retained leg.
Put \(D=N-1\) and retain the cardinal functions

\[
 h_j(x)=\frac{\sin\pi N(x-j/N)}{N\sin\pi(x-j/N)},
 \qquad 0\le j<N,\qquad h(x)=(h_j(x))_j.
 \tag{13}
\]

Their singularities are removable. They are real on the real axis,
including at the removable points. Each is in the \(N\)-dimensional
Fourier space with frequencies
\(-D/2,-D/2+1,\ldots,D/2\). At even levels these are
half-integers: \(h_j(x+1)=(-1)^D h_j(x)\), while every
product \(h_jh_k\) is periodic. Thus the cardinal Parseval identity
from [exact wire contraction](research_mixed_wire_exact_contraction.md),
equation (4) and its proof, is a real Hermitian identity as well as
its original bilinear identity:

\[
 N\int_0^1h(x)h(x)^T\,dx=I_N,
 \qquad N\int_0^1|v^Th(x)|^2\,dx=v^*v.
 \tag{14}
\]

For any measurable real cutoff \(0\le\chi\le1\), define

\[
 Q_\chi=N\int_0^1\chi(x)h(x)h(x)^T\,dx,
 \qquad Q_\chi=Q_\chi^T=Q_\chi^*,\qquad 0\le Q_\chi\le I_N.
 \tag{15}
\]

Indeed \(v^*Q_\chi v=N\int\chi|v^Th|^2\), and (14)
proves both inequalities. No choice of a leg-coordinate gauge is
involved. If \(\chi\) is the indicator of an interval of length
strictly between zero and one, both inequalities are strict: a nonzero finite
Fourier function cannot vanish on an interval. Such a cutoff matrix
is consequently not an orthogonal projection.

For cutoffs \(\chi_1,\ldots,\chi_{m-1}\), the original
wire-restricted contraction is exactly

\[
 \begin{split}
 Z_{\boldsymbol\epsilon,N}^{\boldsymbol\chi}(w_L,w_R)
 &:=v(w_L)^T A_{3+\epsilon_1}Q_{\chi_1}
          A_{3+\epsilon_2}\cdots Q_{\chi_{m-1}}
          A_{3+\epsilon_m}v(w_R)\\
 &=Z_{\boldsymbol\epsilon^{\rm rev},N}^%
       {\boldsymbol\chi^{\rm rev}}(w_R,w_L).
 \end{split}
 \tag{16}
\]

To identify its literal integral, insert (15) in the first line.
It is \(N^{m-1}\) times the product-wire integral with factors
\(\chi_j(x_j)\), the two ordinary boundary factors
\(v(w_L)^TA_{3+\epsilon_1}h(x_1)\) and
\(h(x_{m-1})^TA_{3+\epsilon_m}v(w_R)\), and all intervening
original kernels
\(h(x_{j-1})^TA_{3+\epsilon_j}h(x_j)\).
The second line follows by transposition of every factor, since
both the original \(A\)'s and the \(Q\)'s are symmetric.
It holds for arbitrary ordinary colors, their derivatives and both
parities. Taking all cutoffs equal to one recovers (1). More generally,
any finite partition of unity in each real wire gives an exact,
reversal-compatible partition of the complete scalar. These are
real-wire integrals; no nonholomorphic cutoff is moved to a shifted
contour in this statement.

There is a useful upper estimate at any one such insertion. For any
complex column vectors \(l,r\),

\[
 |l^TQ_\chi r|^2
 \le(l^*Q_\chi l)(r^*Q_\chi r)
 \le\|l\|^2\|r\|^2.
 \tag{17}
\]

Apply Hermitian Cauchy--Schwarz to \(\overline l\) and \(r\)
in the positive semidefinite form \(Q_\chi\).
Because \(Q_\chi\) is real symmetric,
\((\overline l)^*Q_\chi\overline l=l^*Q_\chi l\).
This proves the first inequality even when the form is singular;
(15) proves the second. The vectors may contain all the other
vertex and cutoff factors, so (17) applies to an arbitrary length.
It is an upper bound only, not a positivity or noncancellation
claim for the original bilinear boundary coefficient.

In the exact Newton leg basis, the same insertion is

\[
 \Gamma_\chi=S Q_\chi S^T,
 \qquad \Gamma_\chi^T=\Gamma_\chi,
 \qquad \Gamma_1=\Gamma.
 \tag{18}
\]

This follows by substituting \(A_n=S^TB_nS\) in (16).
The transpose in (18) is not an adjoint, so the positive contraction
statement concerns \(Q_\chi\), not \(\Gamma_\chi\) in the
Euclidean leg norm. In particular a wire interval in (16) is not an
indicator of \(t_j\) or \(s_j\), nor a choice of one of their
Fourier alternatives. The completed collar estimates in Sections
2--3 therefore do not yet bound either energy in (17). A use of
(17) for exponential suppression needs upper bounds for those
specific two energies at the original calibrated action, with a
strict loss in at least one of them. No such calibration follows
from \(0\le Q_\chi\le I\) alone. Equations (16)--(18) give
an exact common localization for reversal, while preserving this
remaining distinction from the already estimated retained-leg
regions.
